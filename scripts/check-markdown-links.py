#!/usr/bin/env python3
"""Prüft relative Inline-Links in versionierten Markdown-Dateien."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(
    r"!?\[[^\]]*\]\((?P<target><[^>]+>|[^)\s]+)(?:\s+['\"][^)]*['\"])?\)"
)
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data"}


def repository_markdown_files(root: Path) -> list[Path]:
    try:
        output = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z", "--", "*.md"],
            check=True,
            capture_output=True,
        ).stdout
        paths = [root / item.decode("utf-8") for item in output.split(b"\0") if item]
    except (FileNotFoundError, subprocess.CalledProcessError):
        paths = list(root.rglob("*.md"))
    return sorted(path for path in paths if ".git" not in path.parts and path.is_file())


def relative_targets(source: Path) -> list[tuple[int, str]]:
    targets: list[tuple[int, str]] = []
    for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        for match in LINK_PATTERN.finditer(line):
            raw_target = match.group("target").strip("<>")
            parsed = urlsplit(raw_target)
            if parsed.scheme.casefold() in EXTERNAL_SCHEMES or raw_target.startswith("#"):
                continue
            if parsed.scheme or parsed.netloc:
                continue
            target_path = unquote(parsed.path)
            if target_path:
                targets.append((line_number, target_path))
    return targets


def main() -> int:
    failures: list[str] = []
    checked = 0
    for source in repository_markdown_files(ROOT):
        for line_number, target in relative_targets(source):
            checked += 1
            resolved = (source.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                failures.append(
                    f"{source.relative_to(ROOT)}:{line_number}: relatives Ziel verlässt das Repository: {target}"
                )
                continue
            if not resolved.exists():
                failures.append(
                    f"{source.relative_to(ROOT)}:{line_number}: relatives Ziel fehlt: {target}"
                )

    if failures:
        print("Markdown-Linkprüfung fehlgeschlagen:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Markdown-Linkprüfung: PASS ({checked} relative Ziele)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
