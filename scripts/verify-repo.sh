#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
require_latex=false

case "${1:-}" in
  "") ;;
  --require-latex) require_latex=true ;;
  *)
    echo "Unbekannte Option: $1" >&2
    echo "Verwendung: bash scripts/verify-repo.sh [--require-latex]" >&2
    exit 2
    ;;
esac

cd "$repo_root"

# Unter Windows ist sonst die ANSI-Codepage der Standard beim Lesen von Dateien.
export PYTHONUTF8=1

# Unter Windows fehlt python3 oft, oder es ist nur der Microsoft-Store-Platzhalter,
# der keinen Interpreter startet. Deshalb muss jeder Kandidat tatsächlich Python 3 ausführen.
python_cmd=()
for candidate in "python3" "python" "py -3"; do
  read -r -a parts <<< "$candidate"
  if ! command -v "${parts[0]}" >/dev/null 2>&1; then
    continue
  fi
  version="$("${parts[@]}" -c 'import sys; print("%d.%d.%d" % sys.version_info[:3])' 2>/dev/null)" || continue
  version="${version%$'\r'}"
  if [[ "$version" =~ ^3\.[0-9]+\.[0-9]+$ ]]; then
    python_cmd=("${parts[@]}")
    echo "Python: ${candidate} (${version})"
    break
  fi
done

if (( ${#python_cmd[@]} == 0 )); then
  echo "Kein lauffähiges Python 3 gefunden (geprüft: python3, python, py -3)." >&2
  echo "Unter Windows: Python 3 von python.org installieren und den Store-Platzhalter" >&2
  echo "unter Einstellungen > Apps > App-Ausführungsaliase für python/python3 abschalten." >&2
  exit 1
fi

echo "[1/5] Relative Markdown-Links"
"${python_cmd[@]}" scripts/check-markdown-links.py

echo "[2/5] Repository-, Research- und Sicherheitsvertrag"
"${python_cmd[@]}" scripts/check-repository.py

echo "[3/5] Synthetische Offline- und Vertrags-Tests"
"${python_cmd[@]}" -m unittest discover -s examples/onboarding-assistant/tests -v

echo "[4/5] Vorhandene PDF"
if [[ ! -s main.pdf ]]; then
  echo "main.pdf fehlt oder ist leer." >&2
  exit 1
fi
echo "main.pdf: PASS ($(wc -c < main.pdf | tr -d ' ') Bytes)"

echo "[5/5] Vollständiger LaTeX-Build"
missing_tools=()
for tool in pdflatex biber makeglossaries; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    missing_tools+=("$tool")
  fi
done

if (( ${#missing_tools[@]} > 0 )); then
  if [[ "$require_latex" == true ]]; then
    echo "LaTeX ist erforderlich; fehlende Werkzeuge: ${missing_tools[*]}" >&2
    exit 1
  fi
  echo "LaTeX: SKIP (fehlende Werkzeuge: ${missing_tools[*]}; mit --require-latex wäre dies ein Fehler)"
else
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  biber main
  makeglossaries main
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  if [[ ! -s main.pdf ]]; then
    echo "LaTeX-Build erzeugte keine nichtleere main.pdf." >&2
    exit 1
  fi
  if grep -Eq '^!|LaTeX Error|Undefined control sequence|There were undefined references|Please \(re\)run Biber' main.log; then
    echo "main.log enthält Fehler oder ungelöste Referenzen/Zitate." >&2
    exit 1
  fi
  echo "LaTeX: PASS ($(wc -c < main.pdf | tr -d ' ') Bytes)"
fi

echo "Repository-Verifikation: PASS"
