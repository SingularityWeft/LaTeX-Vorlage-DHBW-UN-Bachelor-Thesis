---
name: latex-build
description: Compile a LaTeX document with bibliography and glossary (DHBW-Layout). Use when the user asks to "kompiliere", "build", "render" or "PDF erstellen" in a directory with .tex files.
---

# LaTeX Build (DHBW-Layout)

## Procedure

Strenge Reihenfolge, weil biblatex / glossaries / Inhaltsverzeichnis mehrere Pässe brauchen, um konsistente Querverweise aufzulösen:

```bash
pdflatex main.tex      # 1. Pass — generiert .aux für biber/glossaries
biber main             # verarbeitet .bib Bibliographie
makeglossaries main    # verarbeitet Glossar / Acronyme
pdflatex main.tex      # 2. Pass — löst Bibliographie-Referenzen auf
pdflatex main.tex      # 3. Pass — finalisiert Inhaltsverzeichnis
```

## Nach dem Build

- Bestätige: `main.pdf` existiert, Dateigröße > 0.
- Prüfe `main.log` auf neue `Error` / `!` Zeilen und melde sie dem User.
- "Underfull/Overfull hbox" sind Layout-Warnungen und normalerweise ignorierbar.
- Wenn nicht-aufgelöste Referenzen (`??` im PDF) auftauchen: weitere `pdflatex`-Pässe nötig.

## Wann NICHT kompilieren

- Nur README/Notes geändert (keine `.tex` / `.bib` / `.glo` Edits) — sag das, kein Recompile nötig.
- `pdflatex` / `biber` nicht gefunden — User auf MacTeX-Installation hinweisen (<https://www.tug.org/mactex/>).

## Light Variant (nur Textänderung)

Wenn nur Text in `.tex` geändert wurde (keine neuen Zitate, kein neues Glossar):

```bash
pdflatex main.tex
```

reicht. Für schnelle Iterationen beim Schreiben.

## Häufige Fehlerquellen

| Symptom | Wahrscheinliche Ursache | Lösung |
|---|---|---|
| `?? `-Zeichen statt Zitat im PDF | `biber` vergessen oder Reihenfolge falsch | Volle Sequenz oben durchlaufen |
| `File 'literatur.bib' not found` | `\addbibresource{}` zeigt ins Leere | Pfad in `main.tex` prüfen |
| Glossar leer | `makeglossaries` vergessen | Sequenz mit `makeglossaries` durchlaufen |
| `Package not found` | LaTeX-Paket fehlt | `tlmgr install <paketname>` (MacTeX) |
| `sh: makeindex: command not found` beim `makeglossaries`-Aufruf | MacTeX nicht im `PATH` der aktuellen Shell | Vor dem Build setzen: `export PATH="/Library/TeX/texbin:$PATH"` (oder dauerhaft in `~/.zshrc` / `~/.bash_profile`) |
| Umlaute kaputt | Encoding-Mismatch | Editor auf UTF-8 stellen, `\usepackage[utf8]{inputenc}` prüfen |
