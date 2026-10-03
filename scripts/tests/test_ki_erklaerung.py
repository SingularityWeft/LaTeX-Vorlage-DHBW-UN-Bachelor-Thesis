"""Tests für scripts/ki-erklaerung.py mit einem synthetischen Git-Repository."""

from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "ki-erklaerung.py"
spec = importlib.util.spec_from_file_location("ki_erklaerung", SCRIPT)
ki = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules["ki_erklaerung"] = ki  # dataclasses braucht das Modul in sys.modules
spec.loader.exec_module(ki)

GIT_ENV = {
    **os.environ,
    "GIT_AUTHOR_NAME": "Synthetische Person",
    "GIT_AUTHOR_EMAIL": "synthetisch@example.invalid",
    "GIT_COMMITTER_NAME": "Synthetische Person",
    "GIT_COMMITTER_EMAIL": "synthetisch@example.invalid",
    "GIT_AUTHOR_DATE": "2026-10-05T10:00:00+02:00",
    "GIT_COMMITTER_DATE": "2026-10-05T10:00:00+02:00",
}


class KiErklaerungTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.run_git("init", "-q")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_git(self, *args: str) -> None:
        subprocess.run(["git", *args], cwd=self.root, env=GIT_ENV, check=True, capture_output=True)

    def commit(self, path: str, message: str) -> None:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("a", encoding="utf-8") as handle:
            handle.write(f"{message}\n")
        self.run_git("add", "--", path)
        self.run_git("commit", "-q", "-m", message)

    def generate(self, *extra: str) -> str:
        out = self.root / "thesis" / "ki-erklaerung-entwurf.md"
        exit_code = ki.main(["--root", str(self.root), "--heute", "2026-10-05", *extra])
        self.assertEqual(exit_code, 0)
        return out.read_text(encoding="utf-8")

    def test_only_commits_since_setup_and_grouped_by_step(self) -> None:
        self.commit("README.md", "Vorlage: Grundgerüst")
        self.commit(
            "thesis/STAND.md",
            "Arbeitsmodus einrichten\n\nKI-System: Claude Code (Anthropic)\n"
            "KI-Arbeitsschritt: Projektorganisation\nKI-Beitrag: Stand und Gliederung angelegt.",
        )
        self.commit(
            "kapitel/02-hauptteil.tex",
            "Kapitel 2.1: Entwurf\n\nKI-System: Codex (OpenAI)\n"
            "KI-Arbeitsschritt: Struktur und Formulierung\nKI-Beitrag: Entwurf aus Stichpunkten.",
        )
        self.commit("kapitel/02-hauptteil.tex", "Tippfehler korrigiert")
        text = self.generate()

        self.assertNotIn("Grundgerüst", text)
        self.assertIn("3 Commits, davon 2 mit KI-Angaben", text)
        self.assertIn("| Projektorganisation | Claude Code (Anthropic) | 1 |", text)
        self.assertIn("| Struktur und Formulierung | Codex (OpenAI) | 1 |", text)
        self.assertLess(text.index("| Struktur und Formulierung"), text.index("| Projektorganisation"))
        self.assertIn("Codex (OpenAI): Entwurf aus Stichpunkten.", text)
        self.assertIn("Commits ohne KI-Angaben (eigene Arbeit oder nicht gekennzeichnet): 1", text)

    def test_incomplete_and_unknown_entries_are_reported(self) -> None:
        self.commit("thesis/STAND.md", "Start\n\nKI-System: Gemini CLI (Google)\nKI-Beitrag: Stand angelegt.")
        self.commit(
            "literatur.bib",
            "Quelle\n\nKI-Arbeitsschritt: Recherche\nKI-Beitrag: Eintrag ergänzt | ungeprüft.",
        )
        text = self.generate()

        self.assertIn("| (ohne Arbeitsschritt) | Gemini CLI (Google) | 1 |", text)
        self.assertIn("| Recherche | (ohne KI-System) | 1 |", text)
        self.assertIn("Arbeitsschritte außerhalb der Liste in THESIS-ARBEITSMODUS.md: Recherche", text)
        self.assertIn("KI-Angaben ohne Arbeitsschritt:", text)
        self.assertIn("KI-Angaben ohne KI-System:", text)

    def test_without_setup_commit_whole_history_is_used(self) -> None:
        self.commit("README.md", "Erster Commit\n\nKI-System: Claude Code (Anthropic)\nKI-Arbeitsschritt: Ideen und Konzeption")
        text = self.generate()

        self.assertIn("gesamte Historie", text)
        self.assertIn("| Ideen und Konzeption | Claude Code (Anthropic) | 1 |", text)


if __name__ == "__main__":
    unittest.main()
