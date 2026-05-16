# LaTeX-Vorlage — DHBW Bachelor-Thesis (Studiengang Unternehmertum)

Eine kompilierbare LaTeX-Vorlage für Bachelor-Thesen an der DHBW, abgestimmt auf den Studiengang Unternehmertum. Enthält:

- **Layout** nach DHBW-Vorgabe (Helvetica 11pt, A4, 2 cm Ränder, 3 cm rechter Korrekturrand, 1,5-zeilig).
- **Bibliographie** mit `biblatex` + `biber` (Stil `authoryear`).
- **Glossar und Abkürzungsverzeichnis** mit `glossaries`.
- **Deckblatt** und **Selbstständigkeitserklärung** als Platzhalter.
- **Drei Beispielkapitel** (Einleitung, Hauptteil, Fazit), die direkt kompilieren.
- **KI-Build-Integration:** `.claude/skills/latex-build/SKILL.md` (für Claude Code) und `AGENTS.md` (für OpenAI Codex), damit du im Alltag nur „Kompiliere die Thesis" sagen musst — die KI macht den Rest.

## Voraussetzungen

- **MacTeX** (auf macOS): <https://www.tug.org/mactex/> — Achtung, ~5 GB Download.
- Für Windows/Linux: TeX Live (<https://www.tug.org/texlive/>) oder MiKTeX (<https://miktex.org/>).

Im Terminal prüfen:

```bash
pdflatex --version
biber --version
```

Beide Befehle müssen Versionsnummern ausgeben.

## Installation und erstes Kompilieren

```bash
git clone https://github.com/SingularityWeft/LaTeX-Vorlage-DHBW-UN-Bachelor-Thesis.git meine-thesis
cd meine-thesis
```

Dann eines von beidem:

### Variante 1: Per KI (empfohlen, wenn Claude Code oder OpenAI Codex installiert)

Im Thesis-Ordner Claude Code oder Codex starten und sagen:

```
Kompiliere die Thesis.
```

Die KI liest entweder die `.claude/skills/latex-build/SKILL.md` (Claude Code) oder die `AGENTS.md` (Codex) und führt die richtige Kompilier-Sequenz aus, prüft die Logs und meldet Fehler.

### Variante 2: Per Hand im Terminal

```bash
pdflatex main.tex
biber main
makeglossaries main
pdflatex main.tex
pdflatex main.tex
```

Drei Pässe sind nötig, weil Inhaltsverzeichnis, Bibliographie und Glossar Querverweise erst nach mehreren Durchläufen konsistent auflösen. Ergebnis: `main.pdf` im selben Ordner.

**Light Variant** (nur Textänderung in `.tex`, keine neuen Zitate / keine neuen Glossar-Einträge):

```bash
pdflatex main.tex
```

### Variante 3: Per TeXShop (klickbar, ohne Terminal)

TeXShop liegt MacTeX bei (unter `/Applications/TeX/TeXShop.app`).

1. `main.tex` in TeXShop öffnen.
2. **Cmd+T** drücken (entspricht einem `pdflatex`-Lauf).
3. Oben in der Toolbar von „LaTeX" auf „BibTeX" wechseln → **Cmd+T** (verarbeitet die Quellen).
4. Zurück auf „LaTeX" → **Cmd+T** → **Cmd+T** (zwei finale Pässe für konsistente Verzeichnisse).
5. Für das Glossar: einmal manuell im Terminal `makeglossaries main` im Projektordner laufen lassen, dann in TeXShop nochmal Cmd+T.

## Was du anpassen musst

Suche im Code nach `%% PLACEHOLDER` — alle Stellen, die personalisiert werden müssen:

- `main.tex`: `\hypersetup{...}` (PDF-Metadaten), Deckblatt (Titel, Name, Matrikelnummer, Kurs, Betreuer, Abgabedatum), Selbstständigkeitserklärung (Titel der Arbeit).
- `literatur.bib`: Beispiel-Einträge durch deine echten Quellen ersetzen.
- Glossar-Einträge in `main.tex` (Bereich „GLOSSAR-EINTRÄGE") nach Bedarf erweitern oder ersetzen.
- Optional: DHBW-Logo als `dhbw-logo.png` ergänzen und im Deckblatt einkommentieren. (Aus rechtlichen Gründen ist das Logo hier nicht beigelegt — frag bei deiner DHBW nach der offiziellen Datei.)

## Verzeichnisstruktur

```
.
├── README.md                              # diese Datei
├── main.tex                               # Hauptdokument (Präambel + Kapitel)
├── literatur.bib                          # Bibliographie (BibTeX-Format)
├── .gitignore                             # ignoriert LaTeX-Build-Artefakte
├── .claude/
│   └── skills/
│       └── latex-build/
│           └── SKILL.md                   # Claude-Code-Skill für den Build
└── AGENTS.md                              # Konventionen für OpenAI Codex
```

## KI-Erklärung (akademisch)

Wenn du diese Vorlage mit KI-Unterstützung verwendest, empfiehlt es sich, eine Datei `ki-erklaerung.md` im Projekt-Root anzulegen, die kontinuierlich dokumentiert, was die KI beigetragen hat. Vorlage:

```markdown
# KI-Erklärung — [Titel der Arbeit]

Diese Datei dokumentiert kontinuierlich die Nutzung von KI-Werkzeugen
im Verlauf der Arbeit.

## Einträge

### YYYY-MM-DD · Tool-Name (Modellbezeichnung)
- **Aufgabe:** ...
- **Umfang:** ...
- **Übernommenes:** ...
- **Quelle (bei Import aus anderen KIs):** ...
```

Sowohl der Claude-Code-Skill als auch die `AGENTS.md` enthalten Regeln, die die KI dazu bringen, am Sessionende ungefragt einen Eintrag anzuhängen — du musst sie nur einmal anlegen.

## Lizenz

MIT-Lizenz, freie Weiterverwendung. Anpassungen an die DHBW-Standortvorgaben sind vermutlich nötig (Deckblatt-Wording, Selbstständigkeitserklärung).

## Fragen / Issues

Issues und Pull Requests willkommen unter <https://github.com/SingularityWeft/LaTeX-Vorlage-DHBW-UN-Bachelor-Thesis>.
