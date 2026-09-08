from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from artifact import onboarding_assistant as assistant  # noqa: E402


def response_body(
    content: object,
    *,
    model: str = "synthetic-model-v1",
    finish_reason: str | None = "stop",
    tool_calls: object | None = None,
) -> bytes:
    message: dict[str, object] = {"role": "assistant", "content": content}
    if tool_calls is not None:
        message["tool_calls"] = tool_calls
    return json.dumps(
        {
            "model": model,
            "choices": [{"message": message, "finish_reason": finish_reason}],
            "usage": {
                "prompt_tokens": 10,
                "completion_tokens": 7,
                "total_tokens": 17,
            },
        }
    ).encode("utf-8")


class LiveContractTests(unittest.TestCase):
    def test_loopback_is_default_and_nonlocal_requires_two_gates(self) -> None:
        self.assertEqual(
            assistant.validate_endpoint(assistant.DEFAULT_ENDPOINT),
            assistant.DEFAULT_ENDPOINT,
        )
        with self.assertRaises(assistant.ContractError):
            assistant.validate_endpoint("http://model.example/v1/chat/completions")
        with self.assertRaises(PermissionError):
            assistant.validate_endpoint("https://model.example/v1/chat/completions")
        with self.assertRaises(PermissionError):
            assistant.validate_endpoint(
                "https://model.example/v1/chat/completions",
                allow_nonlocal=True,
                human_gate_id="   ",
            )
        self.assertEqual(
            assistant.validate_endpoint(
                "https://model.example/v1/chat/completions",
                allow_nonlocal=True,
                human_gate_id="synthetic-egress-gate-001",
            ),
            "https://model.example/v1/chat/completions",
        )

    def test_request_uses_only_documented_fields_and_secret_stays_in_header(self) -> None:
        observed: dict[str, object] = {}

        def transport(request: object, timeout: float) -> tuple[bytes, float]:
            observed["method"] = request.get_method()
            observed["url"] = request.full_url
            observed["payload"] = json.loads(request.data.decode("utf-8"))
            observed["authorization"] = request.get_header("Authorization")
            observed["timeout"] = timeout
            return response_body(
                "Der Zugang braucht die Freigaberolle. [SYN-ACCESS-001]"
            ), 12.5

        result = assistant.call_live_endpoint(
            "Wer bestätigt den Zugang?",
            "synthetic-model-v1",
            api_key="synthetic-test-secret",
            timeout=4.0,
            transport=transport,
            root=ROOT,
        )
        payload = observed["payload"]
        self.assertEqual(
            set(payload), {"model", "messages", "temperature", "stream"}
        )
        self.assertEqual([item["role"] for item in payload["messages"]], ["system", "user"])
        self.assertIs(payload["stream"], False)
        self.assertEqual(payload["temperature"], 0)
        self.assertEqual(observed["authorization"], "Bearer synthetic-test-secret")
        self.assertEqual(observed["url"], assistant.DEFAULT_ENDPOINT)
        self.assertNotIn("synthetic-test-secret", json.dumps(payload))
        self.assertEqual(result.answer.source_ids, ("SYN-ACCESS-001",))
        self.assertEqual(result.latency_ms, 12.5)

    def test_tool_call_streaming_and_structured_content_fail_closed(self) -> None:
        documents = assistant.load_documents(ROOT)
        with self.assertRaises(assistant.ContractError):
            assistant.parse_live_response(
                response_body("text", tool_calls=[{"id": "synthetic"}]), documents
            )
        with self.assertRaises(assistant.ContractError):
            assistant.parse_live_response(
                response_body([{"type": "text", "text": "structured"}]), documents
            )
        with self.assertRaises(assistant.ContractError):
            assistant.parse_live_response(
                response_body("partial", finish_reason="length"), documents
            )

    def test_oversized_response_fails_before_json_processing(self) -> None:
        with self.assertRaises(assistant.ContractError):
            assistant.call_live_endpoint(
                "Synthetische Frage",
                "synthetic-model-v1",
                transport=lambda request, timeout: (
                    b"x" * (assistant.MAX_RESPONSE_BYTES + 1),
                    1.0,
                ),
                root=ROOT,
            )

    def test_redirects_are_not_followed_to_a_different_target(self) -> None:
        handler = assistant._NoRedirect()
        redirected = handler.redirect_request(
            object(), None, 302, "redirect", {}, "https://other.example/v1/chat/completions"
        )
        self.assertIsNone(redirected)

    def test_live_run_writes_record_and_raw_output_without_secret(self) -> None:
        def transport(request: object, timeout: float) -> tuple[bytes, float]:
            return response_body(
                "Die Willkommenskarte wird zuerst gelesen. [SYN-WELCOME-001]"
            ), 9.0

        locked = assistant.verify_locked_hashes(ROOT)
        result = assistant.call_live_endpoint(
            "Was geschieht zuerst?",
            "synthetic-model-v1",
            api_key="synthetic-test-secret",
            transport=transport,
            root=ROOT,
        )
        with tempfile.TemporaryDirectory() as temporary:
            runs_dir = Path(temporary)
            record = assistant.write_live_run_record(
                result,
                question="Was geschieht zuerst?",
                model_id="synthetic-model-v1",
                endpoint=assistant.DEFAULT_ENDPOINT,
                repeat_id="repeat-01",
                case_id="SYN-LIVE-01",
                series_id="series-model-comparison-v1",
                runs_dir=runs_dir,
                eval_hash=locked["evals/exploration/cases.json"],
                data_hash=locked["data/documents.json"],
                runtime_version="synthetic-runtime-v1",
                grade={"passed": True},
            )
            files = list(runs_dir.rglob("*.json"))
            serialized = "\n".join(path.read_text() for path in files)
        self.assertEqual(len(files), 2)
        self.assertNotIn("synthetic-test-secret", serialized)
        self.assertEqual(record["repeat_id"], "repeat-01")
        self.assertEqual(record["status"], "candidate-keep")
        self.assertTrue(record["raw_output_sha256"])

    def test_repeated_mock_runs_keep_config_and_report_spread(self) -> None:
        locked = assistant.verify_locked_hashes(ROOT)
        records = []
        with tempfile.TemporaryDirectory() as temporary:
            runs_dir = Path(temporary)
            for index, latency in enumerate((8.0, 13.0, 10.0), start=1):
                result = assistant.call_live_endpoint(
                    "Was geschieht zuerst?",
                    "synthetic-model-v1",
                    transport=lambda request, timeout, value=latency: (
                        response_body(
                            "Zuerst die Willkommenskarte. [SYN-WELCOME-001]"
                        ),
                        value,
                    ),
                    root=ROOT,
                )
                records.append(
                    assistant.write_live_run_record(
                        result,
                        question="Was geschieht zuerst?",
                        model_id="synthetic-model-v1",
                        endpoint=assistant.DEFAULT_ENDPOINT,
                        repeat_id=f"repeat-{index:02d}",
                        case_id="SYN-MOCK-REPEAT",
                        series_id="series-repeat-v1",
                        runs_dir=runs_dir,
                        eval_hash=locked["evals/exploration/cases.json"],
                        data_hash=locked["data/documents.json"],
                        runtime_version="synthetic-runtime-v1",
                        grade={"passed": True},
                    )
                )
        summary = assistant.summarize_records(records)
        self.assertEqual(summary["run_count"], 3)
        self.assertTrue(summary["repeat_ids_unique"])
        self.assertTrue(summary["configuration_constant"])
        self.assertGreater(summary["latency_ms"]["population_stdev"], 0)

    def test_model_vs_harness_control_allows_only_named_variable(self) -> None:
        baseline = {
            "model_id": "synthetic-model-a",
            "prompt_version": "prompt-v1",
            "harness_version": "harness-v1",
            "data_hash": "data-hash",
            "eval_hash": "eval-hash",
        }
        candidate = dict(baseline, model_id="synthetic-model-b")
        self.assertEqual(
            assistant.compare_configurations(baseline, candidate, "model_id"),
            ["model_id"],
        )
        confounded = dict(candidate, harness_version="harness-v2")
        with self.assertRaises(assistant.ContractError):
            assistant.compare_configurations(baseline, confounded, "model_id")

    def test_run_identifiers_cannot_escape_the_runs_directory(self) -> None:
        result = assistant.LiveResult(
            answer=assistant.Answer(
                text=assistant.REFUSAL_TEXT,
                source_ids=(),
                refused=True,
                policy=assistant.PolicyEvidence(),
            ),
            response_model="synthetic-model-v1",
            usage=None,
            latency_ms=1.0,
            request_hash="request-hash",
        )
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaises(assistant.ContractError):
                assistant.write_live_run_record(
                    result,
                    question="Synthetische Frage",
                    model_id="synthetic-model-v1",
                    endpoint=assistant.DEFAULT_ENDPOINT,
                    repeat_id="repeat-01",
                    case_id="SYN-LIVE-01",
                    series_id="../../outside",
                    runs_dir=Path(temporary),
                    eval_hash="eval-hash",
                    data_hash="data-hash",
                    runtime_version="synthetic-runtime-v1",
                )


if __name__ == "__main__":
    unittest.main()
