# LaTeX-Vorlage — DHBW Bachelor-Thesis (Studiengang Unternehmertum)

Eine kompilierbare LaTeX-Vorlage für Bachelor-Thesen an der DHBW, abgestimmt auf den Studiengang Unternehmertum. Enthält:

- **Layout** nach DHBW-Vorgabe (Helvetica 11pt, A4, 2 cm Ränder, 3 cm rechter Korrekturrand, 1,5-zeilig).
- **Bibliographie** mit `biblatex` + `biber` (Stil `authoryear`).
- **Glossar und Abkürzungsverzeichnis** mit `glossaries`.
- **Deckblatt** und **Selbstständigkeitserklärung** als Platzhalter.
- **Drei Beispielkapitel** (Einleitung, Hauptteil, Fazit), die direkt kompilieren.
- **KI-Setup- und Build-Integration:** `KI-SETUP.md`, `CLAUDE.md`, `.claude/skills/latex-build/SKILL.md` und `AGENTS.md`, damit du nach dem Klonen nur „Ja, bitte einrichten" und später „Kompiliere die Thesis" sagen musst.

## KI-Schnellstart

Das funktioniert mit Claude Code, OpenAI Codex oder einem GPT-/Claude-Agenten mit lokalem Datei- und Terminalzugriff. Ein reiner Browser-Chat ohne Dateizugriff kann die Schritte nur erklären, nicht selbst ausführen.

Wenn du die Vorlage von einer KI klonen und einrichten lassen willst, gib ihr zuerst diesen Prompt:

```text
Klone dieses Repo in einen neuen Ordner `meine-thesis`:
https://github.com/SingularityWeft/LaTeX-Vorlage-DHBW-UN-Bachelor-Thesis

Wechsle danach in den Ordner und lies `README.md`, `KI-SETUP.md` und die passende Agenten-Datei:
- `AGENTS.md` für Codex/GPT-basierte Coding-Agenten
- `CLAUDE.md` für Claude Code

Warte danach auf mein Startsignal.
```

Wenn die KI im Ordner steht, reicht:

```text
Ja, bitte einrichten.
```

Die KI richtet dann das LaTeX-Projekt arbeitsfertig ein: sie schützt das öffentliche Vorlagen-Remote vor versehentlichen Pushes, legt eine `ki-erklaerung.md` an, prüft die LaTeX-Toolchain, baut eine erste `main.pdf` und listet die offenen Platzhalter für Deckblatt und Metadaten.

## Vortragsmaterial

Zum DHBW-Abendvortrag gibt es die Folien im Ordner [`vortrag/`](vortrag/):

- [`dhbw-abendvortrag-slides.pdf`](vortrag/dhbw-abendvortrag-slides.pdf) — PDF-Fassung zum schnellen Teilen.
- [`slides.html`](vortrag/slides.html) — interaktive HTML-Fassung inklusive benötigter Assets.
- [`anleitungen/`](vortrag/anleitungen/) — drei Markdown-Sheets für das Setup von SecondBrain bis LaTeX-Template.

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

Die KI liest entweder `CLAUDE.md` plus `.claude/skills/latex-build/SKILL.md` (Claude Code) oder `AGENTS.md` (Codex/GPT-Agenten) und führt die richtige Kompilier-Sequenz aus, prüft die Logs und meldet Fehler.

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
├── KI-SETUP.md                            # Ablauf für "Ja, bitte einrichten"
├── CLAUDE.md                              # Projektanweisungen für Claude Code
├── AGENTS.md                              # Projektanweisungen für OpenAI Codex / GPT-Agenten
├── main.tex                               # Hauptdokument (Präambel + Kapitel)
├── literatur.bib                          # Bibliographie (BibTeX-Format)
├── .gitignore                             # ignoriert LaTeX-Build-Artefakte
├── .claude/
│   └── skills/
│       └── latex-build/
│           └── SKILL.md                   # Claude-Code-Skill für den Build
└── vortrag/
    └── anleitungen/                       # Setup-Sheets aus dem DHBW-Abendvortrag
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

`CLAUDE.md`, der Claude-Code-Skill und `AGENTS.md` enthalten Regeln, die die KI dazu bringen, am Sessionende ungefragt einen Eintrag anzuhängen — du musst sie nur einmal anlegen.

## Lizenz

MIT-Lizenz, freie Weiterverwendung. Anpassungen an die DHBW-Standortvorgaben sind vermutlich nötig (Deckblatt-Wording, Selbstständigkeitserklärung).

## Fragen / Issues

Issues und Pull Requests willkommen unter <https://github.com/SingularityWeft/LaTeX-Vorlage-DHBW-UN-Bachelor-Thesis>.
