#!/usr/bin/env python3
"""Erzeugt aus den KI-Angaben der Commits einen Entwurf der KI-Erklärung.

Liest `KI-System`, `KI-Arbeitsschritt` und `KI-Beitrag` aus den Commit-Nachrichten
(siehe THESIS-ARBEITSMODUS.md) und schreibt eine Markdown-Übersicht. Der Entwurf
wird von der Autorin oder dem Autor geprüft, bevor er in die Arbeit übernommen wird.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = Path("thesis") / "ki-erklaerung-entwurf.md"
STAND_PATH = "thesis/STAND.md"

ARBEITSSCHRITTE = [
    "Ideen und Konzeption",
    "Literatursuche und -analyse",
    "Literaturverwaltung",
    "Methoden und Modelle",
    "Code, Formeln und Berechnungen",
    "Tabellen und Übersichten",
    "Visualisierungen",
    "Struktur und Formulierung",
    "Prüfung und Korrektur",
    "Projektorganisation",
]

TRAILER_KEYS = {
    "ki-system": "systems",
    "ki-arbeitsschritt": "steps",
    "ki-beitrag": "contributions",
}

NO_STEP = "(ohne Arbeitsschritt)"

FIELD_SEP = "\x1f"
RECORD_SEP = "\x1e"
LOG_FORMAT = f"%H{FIELD_SEP}%ad{FIELD_SEP}%s{FIELD_SEP}%B{RECORD_SEP}"


@dataclass
class Commit:
    sha: str
    date: str
    subject: str
    systems: list[str] = field(default_factory=list)
    steps: list[str] = field(default_factory=list)
    contributions: list[str] = field(default_factory=list)

    @property
    def has_ki(self) -> bool:
        return bool(self.systems or self.steps or self.contributions)


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return result.stdout


def parse_log(raw: str) -> list[Commit]:
    commits: list[Commit] = []
    for record in raw.split(RECORD_SEP):
        if not record.strip():
            continue
        parts = record.strip("\r\n").split(FIELD_SEP, 3)
        while len(parts) < 4:
            parts.append("")
        sha, day, subject, body = parts
        commit = Commit(sha=sha.strip()[:7], date=day.strip(), subject=subject.strip())
        for line in body.splitlines():
            key, sep, value = line.partition(":")
            attribute = TRAILER_KEYS.get(key.strip().casefold())
            if sep and attribute and value.strip():
                getattr(commit, attribute).append(value.strip())
        commits.append(commit)
    return commits


def start_commit(root: Path) -> str | None:
    """Commit, der thesis/STAND.md angelegt hat, also die Einrichtung des Arbeitsmodus."""
    try:
        added = git(root, "log", "--format=%H", "--diff-filter=A", "--", STAND_PATH).split()
    except subprocess.CalledProcessError:
        return None
    return added[-1] if added else None


def read_commits(root: Path, since: str | None, all_history: bool) -> tuple[list[Commit], str]:
    base = None if all_history else (since or start_commit(root))
    if base is None:
        raw = git(root, "log", "--reverse", "--no-merges", "--date=short", f"--format={LOG_FORMAT}")
        return parse_log(raw), "gesamte Historie"
    first = git(root, "log", "-1", "--date=short", f"--format={LOG_FORMAT}", base)
    rest = git(
        root, "log", "--reverse", "--no-merges", "--date=short", f"--format={LOG_FORMAT}", f"{base}..HEAD"
    )
    return parse_log(first) + parse_log(rest), f"ab Commit {base[:7]}"


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def render(commits: list[Commit], scope: str, today: str) -> str:
    ki_commits = [commit for commit in commits if commit.has_ki]
    by_step: dict[str, list[Commit]] = {}
    for commit in ki_commits:
        for step in commit.steps or [NO_STEP]:
            by_step.setdefault(step, []).append(commit)
    ordered = [step for step in ARBEITSSCHRITTE if step in by_step]
    ordered += sorted(step for step in by_step if step not in ARBEITSSCHRITTE)

    lines = [
        "# KI-Erklärung – Entwurf aus der Git-Historie",
        "",
        f"> Automatisch erzeugt am {today} mit `scripts/ki-erklaerung.py` ({scope}, "
        f"{len(commits)} Commits, davon {len(ki_commits)} mit KI-Angaben). "
        "Entwurf: Zuordnung und Formulierung prüft die Autorin oder der Autor, "
        "bevor der Text in die Erklärung zur Verwendung von KI-Systemen übernommen wird.",
        "",
        "## Übersicht nach Arbeitsschritt",
        "",
    ]
    if not ordered:
        lines += ["Keine Commits mit KI-Angaben gefunden.", ""]
    else:
        lines += ["| Arbeitsschritt | KI-System(e) | Commits |", "|---|---|---|"]
        for step in ordered:
            systems: list[str] = []
            for commit in by_step[step]:
                for system in commit.systems or ["(ohne KI-System)"]:
                    if system not in systems:
                        systems.append(system)
            lines.append(f"| {cell(step)} | {cell(', '.join(systems))} | {len(by_step[step])} |")
        lines.append("")
        lines += ["## Beiträge je Arbeitsschritt", ""]
        for step in ordered:
            lines += [f"### {step}", ""]
            for commit in by_step[step]:
                systems = ", ".join(commit.systems) or "(ohne KI-System)"
                contribution = "; ".join(commit.contributions) or commit.subject
                lines.append(f"- {commit.date} · `{commit.sha}` · {systems}: {contribution}")
            lines.append("")

    unknown = [step for step in ordered if step not in ARBEITSSCHRITTE and step != NO_STEP]
    without_step = [commit for commit in ki_commits if not commit.steps]
    without_system = [commit for commit in ki_commits if not commit.systems]
    lines += ["## Hinweise", ""]
    lines.append(f"- Commits ohne KI-Angaben (eigene Arbeit oder nicht gekennzeichnet): {len(commits) - len(ki_commits)}")
    if unknown:
        lines.append(f"- Arbeitsschritte außerhalb der Liste in THESIS-ARBEITSMODUS.md: {', '.join(unknown)}")
    for label, missing in (("Arbeitsschritt", without_step), ("KI-System", without_system)):
        if missing:
            shas = ", ".join(f"`{commit.sha}`" for commit in missing)
            lines.append(f"- KI-Angaben ohne {label}: {shas}")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="Zieldatei relativ zum Projekt-Root")
    parser.add_argument("--seit", help="Commit, ab dem ausgewertet wird (Standard: Einrichtung des Arbeitsmodus)")
    parser.add_argument("--alle", action="store_true", help="gesamte Git-Historie auswerten")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    parser.add_argument("--heute", default=date.today().isoformat(), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    try:
        commits, scope = read_commits(args.root, args.seit, args.alle)
    except (FileNotFoundError, subprocess.CalledProcessError) as error:
        print(f"Git-Historie nicht lesbar: {error}", file=sys.stderr)
        return 1
    out = args.out if args.out.is_absolute() else args.root / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(commits, scope, args.heute), encoding="utf-8")
    print(f"KI-Erklärung (Entwurf) geschrieben: {out.relative_to(args.root).as_posix() if out.is_relative_to(args.root) else out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
