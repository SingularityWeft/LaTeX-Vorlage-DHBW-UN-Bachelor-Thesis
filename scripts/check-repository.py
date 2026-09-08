#!/usr/bin/env python3
"""Prüft den strukturellen, datenbezogenen und CI-/Release-Vertrag."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "onboarding-assistant"

REQUIRED_PATHS = [
    "README.md",
    "TESTED-SETUPS.md",
    "RESEARCH-START.md",
    "DSR-START.md",
    "KI-SETUP.md",
    "AGENTIC-RESEARCH.md",
    "LOCAL-PRIVATE-SETUP.md",
    "SECURITY.md",
    "profiles/dhbw-thesis.md",
    "profiles/unternehmensprojekt.md",
    "profiles/informatikprojekt.md",
    "templates/research/method-choice.md",
    "templates/research/project-manifest.md",
    "templates/research/project-brief.md",
    "templates/research/research-question.md",
    "templates/research/evidence-log.md",
    "templates/research/artifact-spec.md",
    "templates/research/evaluation-plan.md",
    "templates/research/decision-log.md",
    "templates/research/data-ethics-check.md",
    "templates/research/ai-provenance-log.md",
    "templates/research/research-program.md",
    "templates/research/eval-case.md",
    "templates/research/experiment-record.md",
    "templates/research/run-record.md",
    "templates/research/deployment-manifest.md",
    "evals/README.md",
    "runs/README.md",
    "examples/onboarding-assistant/README.md",
    "examples/onboarding-assistant/artifact/onboarding_assistant.py",
    "examples/onboarding-assistant/artifact/system-prompt-v1.txt",
    "examples/onboarding-assistant/data/documents.json",
    "examples/onboarding-assistant/evals/exploration/cases.json",
    "examples/onboarding-assistant/evals/confirmation/cases.json",
    "examples/onboarding-assistant/evals/locked-hashes.json",
    "examples/onboarding-assistant/research/method-choice.md",
    "examples/onboarding-assistant/research/research-program.md",
    "examples/onboarding-assistant/research/evaluation-plan.md",
    "examples/onboarding-assistant/research/decision-log.md",
    "examples/onboarding-assistant/research/deployment-manifest.md",
    "examples/onboarding-assistant/research/shared-on-prem-architecture.md",
    "examples/onboarding-assistant/tests/test_offline.py",
    "examples/onboarding-assistant/tests/test_live_contract.py",
    "examples/onboarding-assistant/runs/example-offline/offline-repeat-01.json",
    "examples/onboarding-assistant/runs/example-offline/offline-repeat-02.json",
    "examples/onboarding-assistant/runs/example-offline/raw/offline-repeat-01.json",
    "examples/onboarding-assistant/runs/example-offline/raw/offline-repeat-02.json",
    "examples/onboarding-assistant/runs/example-offline/summary.json",
    "scripts/check-markdown-links.py",
    "scripts/check-repository.py",
    "scripts/verify-repo.sh",
    ".github/workflows/verify.yml",
    "main.tex",
    "literatur.bib",
    "main.pdf",
]

PROFILE_PATHS = [
    "profiles/dhbw-thesis.md",
    "profiles/unternehmensprojekt.md",
    "profiles/informatikprojekt.md",
]

RUN_REQUIRED_FIELDS = {
    "schema_version",
    "run_id",
    "series_id",
    "experiment_id",
    "repeat_id",
    "seed_or_determinism",
    "status",
    "branch_and_commit",
    "artifact_version",
    "model_id",
    "runtime",
    "prompt_version_sha256",
    "harness_version",
    "data_version_sha256",
    "eval_version_sha256",
    "raw_output_reference",
    "raw_output_sha256",
    "error_status",
    "disposition",
}

ALLOWED_LOCAL_PATHS = Counter(
    {
        (
            "vortrag/anleitungen/03-system-erklaerung.md",
            "/" + "Users/euer-name/",
        ): 1,
    }
)

ALLOWED_SECRET_MATCHES = Counter(
    {
        (
            "examples/onboarding-assistant/artifact/onboarding_assistant.py",
            "api_key=" + "os.environ.get",
        ): 1,
        (
            "examples/onboarding-assistant/tests/test_live_contract.py",
            'api_key="' + "synthetic-test-secret",
        ): 2,
    }
)

# Nur exakte Verbotsformulierungen sind erlaubt. Neue operative Treffer scheitern.
ALLOWED_GIT_POLICY_LINES = Counter(
    {
        (
            "KI-SETUP.md",
            "Pauschales Staging mit `git add -A` oder `git add .` ist verboten. Warte auf eine ausdrückliche Staging-Freigabe und stage danach ausschließlich sichtbare, eigene Pfade:",
        ): 1,
        (
            "CLAUDE.md",
            "- Nur eigene, einzeln aufgelistete Pfade stagen. `git add -A` und `git add .` sind verboten.",
        ): 1,
        (
            "AGENTIC-RESEARCH.md",
            "Ein verworfener Versuch bleibt durch Versuch-Commit, normalen Revert-Commit, Experiment Record, Run Records und Begründung referenzierbar. `git reset --hard`, Force Push sowie das Löschen negativer oder unklarer Evidenz sind verboten.",
        ): 1,
        (
            "AGENTS.md",
            "3. Nur explizit eigene, zuvor aufgelistete Pfade stagen. Pauschales Staging mit `git add -A` oder `git add .` ist verboten.",
        ): 1,
        (
            "AGENTS.md",
            "Keine destruktiven Git-Befehle (`reset --hard`, `push --force`, `branch -D`, `clean -f`) ohne explizite Zustimmung.",
        ): 1,
        (
            "KI-SETUP.md",
            "6. Remotes werden nicht automatisch geändert. Es gibt keinen automatischen Commit und keinen automatischen Push.",
        ): 1,
        (
            "KI-SETUP.md",
            "Ersetze die Beispiel-Allowlist durch die tatsächlich freigegebenen Pfade. Zeige anschließend `git diff --cached --name-only` und `git diff --cached`. Ein Commit benötigt ein zweites ausdrückliches Human Gate. Ein Push findet niemals automatisch statt; zum öffentlichen Vorlagen-Remote ist er verboten.",
        ): 1,
        (
            "CLAUDE.md",
            "- Staging und Commit benötigen getrennte Human Gates; nie automatisch pushen.",
        ): 1,
        (
            "AGENTS.md",
            "5. Bestehende Dateien und Git-Zustände nicht verändern oder übernehmen. Kein Commit ohne sichtbare Allowlist und Human Gate; niemals automatisch pushen und nie in das öffentliche Vorlagen-Repo `SingularityWeft/LaTeX-Vorlage-DHBW-UN-Bachelor-Thesis` pushen.",
        ): 1,
        (
            "AGENTS.md",
            "5. Nie automatisch pushen. Ein Push braucht eine ausdrückliche Anweisung und darf niemals in das öffentliche Vorlagen-Repo gehen.",
        ): 1,
    }
)

CHECKOUT_SHA = "3d3c42e5aac5ba805825da76410c181273ba90b1"


def fail(failures: list[str], message: str) -> None:
    failures.append(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repository_files() -> list[Path]:
    try:
        output = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "-z"],
            check=True,
            capture_output=True,
        ).stdout
        paths = [ROOT / item.decode("utf-8") for item in output.split(b"\0") if item]
    except (FileNotFoundError, subprocess.CalledProcessError):
        paths = [path for path in ROOT.rglob("*") if path.is_file()]
    return sorted(
        path
        for path in paths
        if path.is_file()
        and ".git" not in path.parts
        and not any(part == "private" for part in path.relative_to(ROOT).parts)
    )


def text_files() -> list[tuple[str, str]]:
    decoded: list[tuple[str, str]] = []
    for path in repository_files():
        try:
            decoded.append((str(path.relative_to(ROOT)), path.read_text(encoding="utf-8")))
        except UnicodeDecodeError:
            continue
    return decoded


def check_required_paths(failures: list[str]) -> None:
    for relative in REQUIRED_PATHS:
        path = ROOT / relative
        if not path.exists():
            fail(failures, f"erforderlicher Pfad fehlt: {relative}")
        elif path.is_file() and path.stat().st_size == 0:
            fail(failures, f"erforderliche Datei ist leer: {relative}")


def check_readme_router(failures: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    research = (ROOT / "RESEARCH-START.md").read_text(encoding="utf-8")
    latex_heading = readme.find("## KI-Schnellstart")
    research_heading = readme.find("## Optional: AI-supported Research")
    router_link = readme.find("(RESEARCH-START.md)")
    first_profile = min(readme.find(f"({path})") for path in PROFILE_PATHS)
    if min(latex_heading, research_heading, router_link, first_profile) < 0:
        fail(failures, "README enthält nicht alle LaTeX-/Research-Router-Einstiege")
    elif not latex_heading < research_heading < router_link < first_profile:
        fail(
            failures,
            "README muss zuerst LaTeX zeigen und Research vor den Profilen über RESEARCH-START.md routen",
        )

    method_link = research.find("(templates/research/method-choice.md)")
    research_profiles = [research.find(f"({path})") for path in PROFILE_PATHS]
    if method_link < 0 or any(index < 0 for index in research_profiles):
        fail(failures, "RESEARCH-START.md muss Methodenwahl und alle drei Profile verlinken")
    elif not method_link < min(research_profiles):
        fail(failures, "RESEARCH-START.md muss vor den Profilen in die Methodenwahl führen")

    router_terms = [
        "Design Science Research",
        "Action Design Research",
        "Empirische Softwareforschung",
        "Engineering / kein Forschungsprojekt",
        "Human Gate",
    ]
    for term in router_terms:
        if term.casefold() not in research.casefold():
            fail(failures, f"Methoden-Router enthält Pflichtbegriff nicht: {term}")


def check_profiles(failures: list[str]) -> None:
    for relative in PROFILE_PATHS:
        content = (ROOT / relative).read_text(encoding="utf-8")
        if "(../templates/research/method-choice.md)" not in content:
            fail(failures, f"Research-Profil führt nicht durch die Methodenwahl: {relative}")
        if "## Human Gates" not in content:
            fail(failures, f"Research-Profil enthält kein sichtbares Human Gate: {relative}")
        for term in ("DSR", "ADR", "Engineering"):
            if term not in content:
                fail(failures, f"Research-Profil enthält Methodenabzweigung {term} nicht: {relative}")


def check_eval_locks(failures: list[str]) -> None:
    manifest_path = EXAMPLE / "evals" / "locked-hashes.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(failures, f"Eval-Hashmanifest ist ungültig: {error}")
        return
    expected = {
        "data/documents.json",
        "evals/exploration/cases.json",
        "evals/confirmation/cases.json",
    }
    files = manifest.get("files")
    if manifest.get("hash_algorithm") != "sha256" or manifest.get("synthetic") is not True:
        fail(failures, "Eval-Hashmanifest muss synthetisch und SHA-256-basiert sein")
        return
    if not isinstance(files, dict) or set(files) != expected:
        fail(failures, "Eval-Hashmanifest muss Daten, Exploration und Bestätigung exakt sperren")
        return
    for relative, expected_hash in files.items():
        path = EXAMPLE / relative
        if path.exists() and sha256(path) != expected_hash:
            fail(failures, f"gesperrter Hash verändert: examples/onboarding-assistant/{relative}")

    try:
        confirmation = json.loads(
            (EXAMPLE / "evals" / "confirmation" / "cases.json").read_text(encoding="utf-8")
        )
    except (OSError, json.JSONDecodeError) as error:
        fail(failures, f"Bestätigungs-Eval ist ungültig: {error}")
        return
    if confirmation.get("stage") != "confirmation" or "locked" not in str(
        confirmation.get("status", "")
    ):
        fail(failures, "Bestätigungs-Eval ist nicht strukturell als gesperrt markiert")
    lock_contract = manifest.get("executor", "").casefold()
    if "must not read or write confirmation" not in lock_contract:
        fail(failures, "Hashmanifest trennt Executor und Bestätigungs-Eval nicht")


def check_run_records(failures: list[str]) -> None:
    run_dir = EXAMPLE / "runs" / "example-offline"
    records = sorted(run_dir.glob("offline-repeat-*.json"))
    if len(records) < 2:
        fail(failures, "mindestens zwei synthetische Beispiel-Run-Records sind erforderlich")
    repeat_ids: set[str] = set()
    for path in records:
        relative = str(path.relative_to(ROOT))
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            fail(failures, f"Run Record ist kein gültiges JSON: {relative}: {error}")
            continue
        missing = sorted(RUN_REQUIRED_FIELDS - set(record))
        if missing:
            fail(failures, f"Run Record fehlen Pflichtfelder {missing}: {relative}")
            continue
        for field in RUN_REQUIRED_FIELDS - {"model_id"}:
            if record[field] is None or record[field] == "":
                fail(failures, f"Run-Record-Pflichtfeld ist leer ({field}): {relative}")
        repeat_id = str(record["repeat_id"])
        if repeat_id in repeat_ids:
            fail(failures, f"Repeat-ID ist nicht eindeutig: {repeat_id}")
        repeat_ids.add(repeat_id)
        raw_path = path.parent / str(record["raw_output_reference"])
        if not raw_path.is_file():
            fail(failures, f"Run Record verweist auf fehlenden Rohoutput: {relative}")
        elif sha256(raw_path) != record["raw_output_sha256"]:
            fail(failures, f"Rohoutput-Hash stimmt nicht: {relative}")


def check_content_patterns(failures: list[str]) -> None:
    local_path_pattern = re.compile(
        "/" + r"Users/[A-Za-z0-9._-]+/|/home/[A-Za-z0-9._-]+/|[A-Za-z]:\\Users\\"
    )
    merge_pattern = re.compile(r"^(<{7}|={7}|>{7})(?: |$)", re.MULTILINE)
    secret_patterns = [
        re.compile(r"sk-[A-Za-z0-9_-]{16,}"),
        re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
        re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
        re.compile(r"AKIA[0-9A-Z]{16}"),
        re.compile("-----BEGIN " + r"(?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
        re.compile(
            r"(?i)(?:api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|password)"
            r"\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{12,}"
        ),
    ]
    seen_local_paths: Counter[tuple[str, str]] = Counter()
    seen_secrets: Counter[tuple[str, str]] = Counter()
    for relative, content in text_files():
        for match in merge_pattern.finditer(content):
            line = content.count("\n", 0, match.start()) + 1
            fail(failures, f"Merge-Marker gefunden: {relative}:{line}")
        for match in local_path_pattern.finditer(content):
            key = (relative, match.group(0))
            seen_local_paths[key] += 1
            if seen_local_paths[key] > ALLOWED_LOCAL_PATHS[key]:
                fail(failures, f"lokaler absoluter Pfad erfordert manuelle Prüfung: {relative}: {match.group(0)}")
        for pattern in secret_patterns:
            for match in pattern.finditer(content):
                key = (relative, match.group(0))
                seen_secrets[key] += 1
                if seen_secrets[key] > ALLOWED_SECRET_MATCHES[key]:
                    line = content.count("\n", 0, match.start()) + 1
                    fail(failures, f"typisches Secret-Muster erfordert manuelle Prüfung: {relative}:{line}")
    if seen_local_paths != ALLOWED_LOCAL_PATHS:
        missing = ALLOWED_LOCAL_PATHS - seen_local_paths
        if missing:
            fail(failures, f"dokumentierte lokale-Pfad-Allowlist ist veraltet: {dict(missing)}")
    if seen_secrets != ALLOWED_SECRET_MATCHES:
        missing = ALLOWED_SECRET_MATCHES - seen_secrets
        if missing:
            fail(failures, f"dokumentierte Secret-Allowlist ist veraltet: {dict(missing)}")


def check_git_policy(failures: list[str]) -> None:
    instruction_roots = {
        "README.md",
        "KI-SETUP.md",
        "AGENTS.md",
        "CLAUDE.md",
        "RESEARCH-START.md",
        "DSR-START.md",
        "AGENTIC-RESEARCH.md",
        "LOCAL-PRIVATE-SETUP.md",
        "SECURITY.md",
    }
    policy_pattern = re.compile(
        r"git add -A|git add \.|git\s+push|reset --hard|push --force|clean -f|"
        r"automatisch(?:er|en|es)?\s+Push|automatisch\s+pushen|Push.{0,20}automatisch",
        re.IGNORECASE,
    )
    seen: Counter[tuple[str, str]] = Counter()
    for relative, content in text_files():
        if relative not in instruction_roots:
            continue
        for line in content.splitlines():
            if policy_pattern.search(line):
                key = (relative, line)
                seen[key] += 1
                if seen[key] > ALLOWED_GIT_POLICY_LINES[key]:
                    fail(failures, f"nicht allowlistete Git-Operation in Anweisung: {relative}: {line}")
    if seen != ALLOWED_GIT_POLICY_LINES:
        missing = ALLOWED_GIT_POLICY_LINES - seen
        if missing:
            fail(failures, f"dokumentierte Git-Verbots-Allowlist ist veraltet: {dict(missing)}")


def check_workflow(failures: list[str]) -> None:
    path = ROOT / ".github" / "workflows" / "verify.yml"
    if not path.is_file():
        return
    content = path.read_text(encoding="utf-8")
    if "runs-on: ubuntu-24.04" not in content:
        fail(failures, "CI muss auf dem festen offiziellen Runner ubuntu-24.04 laufen")
    if "permissions:\n  contents: read" not in content:
        fail(failures, "CI benötigt explizit nur contents: read")
    if "bash scripts/verify-repo.sh --require-latex" not in content:
        fail(failures, "CI ruft nicht denselben lokalen Verify-Vertrag im Release-Modus auf")
    if re.search(r"\$\{\{\s*secrets\.", content, re.IGNORECASE):
        fail(failures, "CI darf keine Benutzer-Secrets referenzieren")
    if re.search(r"\b(?:ollama|openai|anthropic|model[-_ ]?host|llm)\b", content, re.IGNORECASE):
        fail(failures, "CI darf kein LLM und keinen Modellhost aufrufen")
    uses = re.findall(r"^\s*-?\s*uses:\s*([^\s#]+)", content, re.MULTILINE)
    if uses != [f"actions/checkout@{CHECKOUT_SHA}"]:
        fail(failures, f"CI-Actions müssen exakt auf freigegebene Commit-SHAs gepinnt sein: {uses}")


def main() -> int:
    failures: list[str] = []
    check_required_paths(failures)
    if failures:
        return report(failures)
    check_readme_router(failures)
    check_profiles(failures)
    check_eval_locks(failures)
    check_run_records(failures)
    check_content_patterns(failures)
    check_git_policy(failures)
    check_workflow(failures)
    return report(failures)


def report(failures: list[str]) -> int:
    if failures:
        print("Repository-Strukturprüfung fehlgeschlagen:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print("Repository-Strukturprüfung: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
