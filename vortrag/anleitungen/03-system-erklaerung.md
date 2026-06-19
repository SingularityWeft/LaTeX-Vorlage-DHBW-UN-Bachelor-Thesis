---
date: 2026-05-16
tags:
  - vortrag
  - info-sheet
---

# Sheet 03 — System-Erklärung: Was die KI eigentlich tut

> **Dies ist Referenzmaterial.** Für das reine Aufsetzen brauchst du es **nicht**. Wenn du nur das System bauen willst, geh zurück zu [`01-start-ki-einrichten.md`](01-start-ki-einrichten.md) und [`02-prompts.md`](02-prompts.md).
>
> Dieses Sheet erklärt, **was** beim Abarbeiten der Prompts passiert: warum die Ordner so heißen, was Wikilinks sind, wie Git eigentlich funktioniert, welche LaTeX-Pakete in der Vorlage drinstecken und warum. Wenn du dein System tiefer verstehen willst — oder wenn ein Prompt schiefläuft und du Fehler suchen musst — findest du hier alles.

Die Erklärung führt durch dasselbe System, das die KI in den Prompts aufsetzt:

- **Teil A — SecondBrain** mit Obsidian (Vault, Workflow, Templates) — entspricht Prompt 1 + 2 in `02-prompts.md`
- **Teil B — Git-Versionierung** (Repo, Commits, GitHub-Remote) — entspricht Prompt 3 + 4
- **Teil C — Thesis-LaTeX-Vorlage** (DHBW-Layout, biblatex/biber, Glossar) — entspricht Prompt 5

**Zielgruppe:** Du, wenn du verstehen willst, was im Maschinenraum passiert. Anfänger-Niveau, jeder Begriff erklärt.

---

## Was ihr am Ende habt

1. Einen Obsidian-Vault mit klarer Ordnerstruktur und 5 Templates für Daily Notes, TODOs, Entscheidungen, Weekly Reviews und Fristen.
2. Diesen Vault unter Git-Versionierung — jede Änderung nachvollziehbar, nichts geht verloren.
3. Eine LaTeX-Schreibvorlage im DHBW-Layout (Helvetica 11pt, 2cm Ränder, biblatex/biber, Glossar).

Dauer: ca. 60–90 Minuten beim ersten Mal.

---

## Voraussetzungen

- **macOS** (für Windows/Linux funktioniert das meiste analog, aber die Befehle weichen ab)
- Ein bisschen Geduld — beim ersten Mal hakt immer irgendwas

Folgendes installiert ihr im Verlauf:

- Obsidian (Teil A)
- Git und Xcode Command Line Tools (Teil B)
- MacTeX (Teil C — groß, ca. 5 GB)

---

# Teil A — SecondBrain mit Obsidian

## A.1 Obsidian installieren und Vault anlegen

1. Ladet Obsidian herunter: <https://obsidian.md/download>
2. Doppelklick auf das .dmg, App in den Ordner `Programme` ziehen.
3. Obsidian öffnen → „Create new vault".
4. Name: `SecondBrain` (oder wie ihr wollt). Ort: euer Benutzerordner, ich empfehle `~/Obsidian/SecondBrain/`.
5. „Create" klicken.

Das war's. Ihr habt jetzt einen leeren Vault.

## A.2 Vault-Struktur

Wir legen die folgenden Ordner an. Öffnet dazu Terminal.app (Spotlight: Cmd+Space, „Terminal" tippen, Enter) und kopiert diesen Block hinein:

```bash
cd ~/Obsidian/SecondBrain
mkdir -p inbox doing done decisions trashed journal projects references templates termine
```

> **Was ihr da gerade getippt habt:**
> - **`cd`** = *change directory*: wechselt in einen Ordner. `~` ist die Kurzform für euren Benutzerordner (`/Users/euer-name/`).
> - **`mkdir`** = *make directory*: legt einen oder mehrere Ordner an. `-p` heißt: leg auch fehlende Zwischenordner mit an und meckere nicht, wenn etwas schon existiert.
> - **Terminal** ist ein Textfenster, in dem ihr dem Mac direkt Befehle gebt, statt zu klicken. Anfangs ungewohnt, aber für Setup-Schritte wie diesen viel schneller als der Finder.

Die Bedeutung der Ordner:

| Ordner        | Wofür                                                                                                                                                                                                                                                      |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `inbox/`      | Rohe Ideen, neue TODOs. Max. 7 Tage liegen lassen, dann weiterverarbeiten oder nach `trashed/`.                                                                                                                                                            |
| `doing/`      | Aktive TODOs und offene Entscheidungen mit Deadline.                                                                                                                                                                                                       |
| `done/`       | Erledigte Items.                                                                                                                                                                                                                                           |
| `decisions/`  | Getroffene Entscheidungen — schriftlich festgehalten mit Begründung und Folgen (in der Software-Welt nennt man dieses Muster *ADR*: „Architecture Decision Record"; für euch reicht: jede wichtige Entscheidung ist eine eigene Datei, kein loser Zettel). |
| `trashed/`    | Nicht gelöscht, nur aus dem Weg. Statt zu löschen, hierhin verschieben.                                                                                                                                                                                    |
| `journal/`    | Daily Notes (`YYYY-MM-DD-Session Log.md`) + Weekly Reviews.                                                                                                                                                                                                |
| `projects/`   | Eure Projekte (z. B. `bachelorarbeit`, `nebenprojekt-xy`).                                                                                                                                                                                                 |
| `references/` | Transkripte, externe Quellen, PDFs, Notizen zu Büchern.                                                                                                                                                                                                    |
| `templates/`  | Die Vorlagen aus [A.3](#a3-templates-anlegen).                                                                                                                                                                                                             |
| `termine/`    | Deadlines/Fristen.                                                                                                                                                                                                                                         |

## A.3 Templates anlegen

Erstellt im Ordner `templates/` fünf Dateien. Am einfachsten in Obsidian: Rechtsklick auf `templates` → „New note" → Dateiname eingeben → Inhalt aus den Blöcken unten reinkopieren.

> **Zwei Begriffe, die euch unten begegnen:**
> - **Frontmatter:** der kleine Block ganz oben in jeder Note, eingeschlossen von `---`-Zeilen. Dort stehen Metadaten zur Datei (Datum, Tags, später z. B. `author:`). Obsidian — und KI-Tools — können diese Felder auslesen und damit Notes filtern oder sortieren.
> - **Wikilinks:** Verweise von einer Note zur anderen, geschrieben als `[[dateiname]]` (in doppelten eckigen Klammern, **ohne** Ordnerpfad, **ohne** `.md`-Endung). Beim Klick springt Obsidian zur verlinkten Datei. Wenn die Datei noch nicht existiert, legt der Klick sie an.

> **Hinweis zu `{{date}}` und `{{title}}`:** Das sind Platzhalter des Obsidian-Templates-Plugins (Settings → Core Plugins → Templates aktivieren, dann unter „Template folder location" `templates` eintragen). Ohne Plugin könnt ihr die Platzhalter beim Anlegen einer neuen Note manuell ersetzen.

### templates/daily-note.md

````markdown
---
date: {{date:YYYY-MM-DD}}
tags:
  - journal
  - session-log
---

# {{date:YYYY-MM-DD}} — Session Log

→ Vortag: [[{{date-1d:YYYY-MM-DD}}-Session Log#Nächste Session]]
→ Aktuelles Weekly Review: [[ ]]

## Ziel heute

*(Was soll am Ende dieser Session erledigt oder entschieden sein?)*

## Offen aus letzter Session

- [ ]

## Was passiert ist

*(Kompakt — was wurde tatsächlich getan, entschieden, verschoben?)*

## Entscheidungen

| Entscheidung | Begründung | Auswirkung |
|---|---|---|
| | | |

## Nächste Session

- [ ]

## Vernetzung

- [[{{date-1d:YYYY-MM-DD}}-Session Log]]
````

### templates/todo.md

````markdown
---
date: {{date:YYYY-MM-DD}}
tags:
  - todo
---

# {{title}}

**Status:** #todo
**Deadline:** {{date}}
**Blocked by:** —
**Time estimate:** X h (alles unter 15 min direkt erledigen)

## Ziel (Definition of Done)


## Consequence Scan (5 min)

- [ ] Was passiert wenn ich das NICHT mache?
- [ ] Was ist das kleinstmögliche shippable Ergebnis?
- [ ] Welche Entscheidung muss VORHER getroffen werden?
- [ ] Brauche ich jemanden/etwas dafür? (Tool, Input, Feedback)
- [ ] Ist das in 1 Session machbar oder muss ich splitten?

## Next Action

> Konkreter erster Schritt (1 Satz, ausführbar in <10 min)

## Kontext


## Vernetzung

-

## Done?

- [ ]
- [ ] Ergebnis liegt vor → nach `done/` verschieben
````

### templates/decision.md

````markdown
---
date: {{date:YYYY-MM-DD}}
tags:
  - decision
---

# {{title}}

**Status:** #decision
**Deadline:** {{date}}
**Decide by:** Wenn keine Entscheidung bis Deadline → Default-Option gilt.

## Die Frage

> (1 Satz)

## Optionen

| Option | Pro | Con |
|--------|-----|-----|
| A: | | |
| B: | | |

## Default-Option (gilt bei Nicht-Entscheidung)

> **Option:** —
> **Begründung:** Warum ist das der sichere Fallback?

## Consequence Scan

- Was passiert wenn ich NICHT entscheide?
- Was ist die billigste reversible Option?
- Kann ich in 2 Wochen korrigieren wenn falsch?

## Entschieden

> **Datum:** —
> **Gewählte Option:** —
> **Begründung (1 Satz):** —

## Folgen — TODOs (kurzfristig)

- [[YYYY-MM-DD-todo-titel]] — 1-Satz-Beschreibung

## Not-TODOs (bewusst verworfen)

> Verhindert Re-Litigation. Format: Option/Pfad — 1-Satz-Begründung.

- Option B: Begründung

## Abschluss-Checkliste

- [ ] TODOs als inbox/-Notes angelegt und hier verlinkt
- [ ] Not-TODOs dokumentiert
- [ ] Session Log verlinkt
- [ ] Status `#decision` → `#done` ergänzt
- [ ] Datei nach `decisions/YYYY-MM-DD-titel.md` verschoben

## Vernetzung

- Session Log: [[YYYY-MM-DD-Session Log]]
````

### templates/weekly-review.md

````markdown
---
date: {{date:YYYY-MM-DD}}
tags:
  - journal
  - weekly-review
---

# Weekly Review — {{date:YYYY-MM-DD}}

## TL;DR

-
-
-

---

## Session Logs diese Woche

- [[ ]]

## Shipped (done/ diese Woche)

- ✅ [[ ]]

## Inbox Cleanup (> 7 Tage)

- 📥 [[ ]] — verarbeiten oder → trashed/

## doing/ ohne Next Action

- ⚠️ [[ ]]

---

## Was habe ich vermieden?

*(ehrlich sein — was wurde aufgeschoben, umgangen, nicht angefasst?)*

## Erkenntnis oder Entscheidung der Woche

*(eine zentrale Einsicht, getroffene Entscheidung oder gelernte Wahrheit)*

## Fokus nächste Woche (Top 3)

1.
2.
3.

---

## Vernetzung

- Vorwoche: [[ ]]
````

### templates/frist.md

````markdown
---
date: {{date:YYYY-MM-DD}}
tags:
  - frist
---

# {{titel}}

**Status:** #todo
**Deadline:** {{YYYY-MM-DD}}
**Typ:** <!-- z. B. Steuer, Handelsrecht, Behörde, Vertraglich, Förderung -->
**Zuständig:** <!-- Name(n) oder Rolle -->
**Konsequenz bei Versäumnis:** {{was passiert konkret}}

---

## Was ist zu tun?

- [ ] Schritt 1
- [ ] Schritt 2

## Voraussetzungen / Blocked by

-

## Vernetzung

- [[]]
````

## A.4 CLAUDE.md im Vault-Root

Diese Datei dokumentiert die Regeln eures Systems — sie ist gleichzeitig die Anleitung für euch selbst (und falls ihr später eine KI dranhängen wollt, liest sie diese Datei automatisch).

Legt im Vault-Root (also direkt in `~/Obsidian/SecondBrain/`) eine Datei `CLAUDE.md` an mit folgendem Inhalt:

````markdown
# SecondBrain — Konventionen

Dies ist ein Obsidian-Vault + Git-Repo.

## Kernregeln

1. **Vor jeder Änderung lesen** — Datei immer erst lesen, nie blind überschreiben.
2. **Nie löschen** — stattdessen nach `trashed/` verschieben.
3. **Wikilinks immer** als `[[dateiname]]` — kein Ordnerpfad, keine `.md`-Extension.

## Workflow

```
inbox/ → doing/ → done/
                → decisions/   (für #decision-Notes nach Konsequenz-Extraktion)
                → trashed/
```

## Session Log schreiben

Datei: `journal/YYYY-MM-DD-Session Log.md`
Template: `templates/daily-note.md`

Inhalt:
- Ziel heute
- Was passiert ist
- Entscheidungen (Tabelle: Entscheidung | Begründung | Auswirkung)
- Nächste Session

Immer bidirektional verlinken: Session Log ↔ besprochene doing/-Items.

## TODO anlegen

Datei: `inbox/YYYY-MM-DD-titel.md`
Template: `templates/todo.md`
Pflichtfelder: Status, Deadline, Consequence Scan, Next Action (1 Satz).

## Entscheidung anlegen

Datei: `doing/decision-titel.md`
Template: `templates/decision.md`
Pflichtfelder: Deadline + Default-Option falls Deadline verstreicht.

Nach getroffener Entscheidung — Pflicht-Konsequenz-Extraktion:
1. Kurzfristige Folge-TODOs als `inbox/YYYY-MM-DD-titel.md` anlegen und in der Decision-Note verlinken.
2. Not-TODOs inline dokumentieren (verworfene Optionen + 1-Satz-Begründung) — verhindert Re-Litigation.
3. Session Log verlinken.
4. Erst dann: nach `decisions/YYYY-MM-DD-titel.md` verschieben.

## Vernetzung (keine Orphans!)

Jede Note muss mindestens einen ein- UND ausgehenden Wikilink haben.

Pflicht bei neuen Notes: `## Vernetzung`-Abschnitt am Ende.

## Status-Tags

`#todo` · `#done` · `#decision` · `#priority-1`

## Ordnerstruktur doing/

Alles flach in `doing/` — keine Unterordner. Sortierung via Tags:
- `#priority-1` statt Unterordner
- `#decision` statt Unterordner
- `#todo` für Aufgaben
````

## A.5 Konventionen-Kurzfassung

Die wichtigsten Regeln, damit das System auch in 6 Monaten noch funktioniert:

- **Pro Arbeitstag genau ein Session Log** in `journal/`. Am Anfang der Session anlegen, am Ende aktualisieren.
- **Neue Ideen wandern in `inbox/`**, nicht direkt in `doing/`. Spätestens nach 7 Tagen entscheiden: Wird draus was, oder weg damit?
- **`doing/` enthält nur, woran ihr wirklich arbeitet.** Wenn dort 30 Items liegen, ist es kein Doing-Ordner mehr — dann gnadenlos triagieren.
- **Entscheidungen wandern nach `decisions/`, nicht nach `done/`.** Eine Entscheidung ist Referenzmaterial mit Langzeitwert.
- **Niemals löschen** — alles nach `trashed/`. Speicher ist billig, vergessene Begründungen sind teuer.

---

# Teil B — Versionierung mit Git

Git ist eine Versionskontrolle. Stellt euch vor: Time Machine, aber präzise und für jeden Schreibvorgang nachvollziehbar.

> **Drei Begriffe, die euch in diesem Teil ständig begegnen:**
> - **Repository** (kurz „Repo"): so heißt ein Ordner, der unter Git-Versionierung steht. Euer Vault wird mit `git init` zu einem Repo.
> - **Commit:** ein gespeicherter Schnappschuss eures Repos zu einem bestimmten Zeitpunkt, immer mit einer kurzen Beschreibung („was hat sich geändert"). Ihr könnt jederzeit zu jedem alten Commit zurückspringen.
> - **`.gitignore`:** eine Liste von Datei-Mustern, die Git **nicht** versionieren soll — z. B. temporäre Dateien oder Sachen, die nur auf eurem Rechner Sinn ergeben.

## B.1 Git installieren

Öffnet Terminal.app und tippt:

```bash
git --version
```

Wenn ihr eine Versionsnummer seht (z. B. `git version 2.39.0`), seid ihr fertig. Falls macOS euch fragt, ob ihr die „Command Line Tools" installieren wollt — auf „Installieren" klicken und ~5 Minuten warten.

Einmalige Konfiguration (ersetzt Name und Mail durch eure Daten):

```bash
git config --global user.name "Vorname Nachname"
git config --global user.email "ihr@beispiel.de"
git config --global init.defaultBranch main
```

## B.2 Vault unter Versionierung stellen

```bash
cd ~/Obsidian/SecondBrain
git init
```

## B.3 .gitignore anlegen

Manche Dateien sollen **nicht** versioniert werden — z. B. Obsidians UI-State, der sich ständig ändert.

Legt im Vault-Root eine Datei `.gitignore` an mit diesem Inhalt:

```gitignore
# macOS
.DS_Store
**/.DS_Store

# Obsidian UI state — maschinenspezifisch, nicht versioniert
.obsidian/workspace.json

# Obsidian Community Plugins — Binaries, nicht versionieren
.obsidian/plugins/*/main.js
.obsidian/plugins/*/styles.css
```

## B.4 Erstes Commit + Alltags-Workflow

Erstes Commit:

```bash
cd ~/Obsidian/SecondBrain
git add -A
git commit -m "init: vault initial setup"
```

Im Alltag (nach jeder größeren Schreibsession, mindestens 1× pro Tag):

```bash
cd ~/Obsidian/SecondBrain
git add -A
git commit -m "notiz: kurze beschreibung was sich geändert hat"
```

Das war's. Ihr habt jetzt eine vollständige Historie eures Vaults.

## B.5 Optional: GitHub-Remote (Backup in der Cloud)

Wenn ihr euren Vault zusätzlich in der Cloud sichern wollt (privates Repo, nur ihr seht es):

1. GitHub-Konto anlegen: <https://github.com/signup>
2. Neues **privates** Repo erstellen: <https://github.com/new> — Name z. B. `secondbrain`, „Private" anklicken, **keine** README/`.gitignore` mitanlegen.
3. GitHub zeigt euch danach Befehle an. Die Variante „push an existing repository" kopieren und im Terminal im Vault-Verzeichnis ausführen.
4. Künftig nach jedem Commit: `git push`.

Hinweis: Sicherer ist Authentifizierung über SSH oder ein Personal Access Token statt Passwort. Wenn ihr da hängenbleibt — fragt mich, das sprengt dieses Sheet.

---

# Teil C — DHBW-Thesis-LaTeX-Vorlage

LaTeX ist ein Satzsystem. Statt im Word zu klicken, schreibt ihr Text + Befehle und kompiliert daraus eine PDF. Anfangs ungewohnt, später unschlagbar bei langen Dokumenten mit Zitaten, Tabellen, Bibliographie.

## C.1 LaTeX installieren

Ladet **MacTeX** herunter: <https://www.tug.org/mactex/>

Das ist groß (~5 GB) und braucht 10–30 Minuten Installation. Während es lädt, könnt ihr mit [C.2](#c2-was-die-vorlage-kann) weitermachen (lesen).

MacTeX bringt **TeXShop** als Editor gleich mit — ihr findet ihn nach der Installation unter `/Applications/TeX/TeXShop.app`. Wer kein Terminal mag, schreibt und kompiliert ab jetzt komplett in TeXShop (Details in [C.5](#c5-kompilieren)).

Nach Installation im Terminal prüfen:

```bash
pdflatex --version
biber --version
```

Beide Befehle müssen Versionsnummern ausgeben.

## C.2 Was die Vorlage kann

- **DHBW-Layout:** A4, 2cm linker/oberer/unterer Rand, 3cm rechter Rand (Korrekturrand), Helvetica 11pt, 1,5-zeilig.
- **Bibliographie** mit `biblatex` + `biber`, Stil `authoryear` (Autor-Jahr-Zitation), nummeriert + alphabetisch im Literaturverzeichnis.
- **Glossar und Abkürzungsverzeichnis** mit `glossaries`.
- **Fußnoten** in 9pt, Sans-Serif, durchgehend nummeriert (nicht je Kapitel neu).
- **DHBW-Farben** (Blau RGB 0,59,122 + Grau) als `\definecolor` verfügbar.
- **TikZ** für eigene Diagramme.
- **Hyperref** für klickbare Links/Verweise in der PDF.

> **LaTeX-Begriffe in einem Satz:**
> - **biblatex / biber:** das Paar, das aus eurer Quellen-Sammlung (`.bib`-Datei) das fertige Literaturverzeichnis erzeugt und im Text die Zitate einsetzt. `biblatex` ist das LaTeX-Paket, `biber` ist das Hintergrund-Programm, das es ausführt.
> - **BibTeX-Datei (`.bib`):** eine Klartext-Datei mit euren Literaturquellen in einem standardisierten Format. Eine Quelle = ein Block (siehe [Beispiel-Block in C.3](#c3-vorlage-übernehmen) unten).
> - **TikZ:** ein LaTeX-Werkzeug, mit dem ihr Diagramme direkt im Code zeichnen könnt, statt sie in einem Grafikprogramm zu erstellen.
> - **Hyperref / Glossaries:** Pakete für klickbare PDF-Links bzw. ein automatisches Glossar/Abkürzungsverzeichnis.

## C.3 Vorlage übernehmen

Legt euch einen neuen Projektordner an und darin die Datei `main.tex` mit der folgenden Präambel. Den Inhalt eurer Arbeit ergänzt ihr in den `\chapter{…}`-Blöcken.

> **Hinweis:** Das ist ein **Skelett** — Titel, Autor, Glossar-Einträge sind Platzhalter. Wenn ihr die komplette, befüllte Vorlage wollt (inkl. Deckblatt, Selbstständigkeitserklärung, Kapitelstruktur), meldet euch — ich schicke euch dann ein Template-Repo zum Klonen.

````latex
\documentclass[11pt,a4paper,oneside]{book}
\PassOptionsToPackage{multiple}{footmisc}

% ============================================================================
% PAKETE
% ============================================================================

\usepackage[utf8]{inputenc}
\usepackage[ngerman]{babel}
\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}

% Layout (DHBW: 2cm links/oben/unten, 3cm rechts)
\usepackage{geometry}
\geometry{a4paper, left=2cm, right=3cm, top=2cm, bottom=2cm}
\usepackage{setspace}
\onehalfspacing
\setlength{\parskip}{6pt}

% Grafiken und Tabellen
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{multirow}
\usepackage{array}
\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}
\usepackage{float}

% DHBW-Farben
\usepackage{xcolor}
\definecolor{dhbwblue}{RGB}{0,59,122}
\definecolor{dhbwgray}{RGB}{128,128,128}

% Hyperlinks
\usepackage[hidelinks]{hyperref}
\hypersetup{
    colorlinks=false,
    linkcolor=black,
    citecolor=black,
    urlcolor=black,
    pdftitle={Titel der Arbeit},
    pdfauthor={Vorname Nachname},
    pdfsubject={Bachelor-Thesis DHBW, Studiengang XY},
    pdfkeywords={Stichwort1, Stichwort2}
}

% Kopf- und Fußzeilen
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[R]{\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyfoot[R]{\thepage}%
  \renewcommand{\headrulewidth}{0pt}%
  \renewcommand{\footrulewidth}{0pt}%
}

% Bibliographie
\usepackage[backend=biber,style=authoryear,sorting=nyt,maxnames=2,uniquename=init]{biblatex}
\addbibresource{literatur.bib}

% Glossar + Abkürzungen
\usepackage[acronym,toc,numberedsection=autolabel]{glossaries}
\makeglossaries

% Zitate
\usepackage{csquotes}

% Mathematik
\usepackage{amsmath}
\usepackage{amssymb}

% Listen
\usepackage{enumitem}

% Verzeichnisse ins Inhaltsverzeichnis
\usepackage[nottoc]{tocbibind}

% Fußnoten-Formatierung (DHBW: 9pt, Sans-Serif, durchgehend nummeriert)
\usepackage[bottom,hang,flushmargin]{footmisc}
\renewcommand{\footnotelayout}{\sffamily\fontsize{9}{10.8}\selectfont}
\setlength{\footnotesep}{0.5cm}
\setlength{\skip\footins}{12pt}
\counterwithout{footnote}{chapter}

% TikZ für eigene Diagramme
\usepackage{tikz}
\usetikzlibrary{positioning, shapes.geometric, arrows, arrows.meta, decorations.pathreplacing, shadows, calc}

% Mikrotypografie
\usepackage{microtype}

% Querformat für breite Tabellen
\usepackage{pdflscape}

% Caption-Formatierung
\usepackage{caption}
\captionsetup[longtable]{justification=raggedright,singlelinecheck=false}

% Titel-Formatierung
\usepackage{titlesec}
\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries}{\chaptertitlename\ \thechapter}{20pt}{\Huge}
\titlespacing*{\chapter}{0pt}{-20pt}{40pt}

% ============================================================================
% GLOSSAR-EINTRÄGE (Beispiele — anpassen)
% ============================================================================

\newglossaryentry{beispiel}{
    name={Beispielbegriff},
    description={Beschreibung des Begriffs}
}

\newacronym{abk}{ABK}{Ausgeschriebene Abkürzung}

% ============================================================================
% DOKUMENT
% ============================================================================

\begin{document}

\frontmatter
% Hier: Titelblatt, Erklärung, Inhaltsverzeichnis, Abkürzungsverzeichnis
\tableofcontents
\printglossary[type=\acronymtype, title={Abkürzungsverzeichnis}]

\mainmatter

\chapter{Einleitung}
Hier beginnt euer Text.

\chapter{Hauptteil}
% Weitere Kapitel ...

\chapter{Fazit}

\backmatter
\printbibliography[title={Literaturverzeichnis}]

\end{document}
````

Zusätzlich braucht ihr im selben Ordner eine Datei `literatur.bib` für eure Quellen (BibTeX-Format). Eine einzelne Quelle sieht z. B. so aus:

```bibtex
@book{mustermann2024,
  author    = {Max Mustermann},
  title     = {Titel des Buches},
  year      = {2024},
  publisher = {Verlagsname},
  address   = {Ort}
}
```

## C.4 Anpassen

Im Skelett ändert ihr mindestens:

- `pdftitle`, `pdfauthor`, `pdfsubject`, `pdfkeywords` (Zeile mit `\hypersetup`)
- `\addbibresource{literatur.bib}` — falls eure BibTeX-Datei anders heißt
- Glossar-Einträge und Acronyme nach Bedarf
- Inhalt in `\chapter{…}`

## C.5 Kompilieren

LaTeX braucht mehrere Durchläufe, damit Inhaltsverzeichnis, Glossar und Bibliographie konsistent sind. Im Terminal im Projektordner:

```bash
cd ~/euer-projektordner
pdflatex main.tex
biber main
makeglossaries main
pdflatex main.tex
pdflatex main.tex
```

Das ergibt eine `main.pdf` neben der `main.tex`. Beim ersten Lauf gibt es viele Warnungen — die meisten verschwinden ab dem zweiten Durchlauf.

Wenn ihr nur Text geändert habt (keine neuen Quellen, kein neues Glossar), reicht ein einfaches `pdflatex main.tex`.

### Alternative ohne Terminal: TeXShop

TeXShop ist der Editor, der MacTeX beiliegt. Damit könnt ihr Kompilieren per Tastenkürzel statt Terminal:

1. `main.tex` in TeXShop öffnen (Doppelklick auf die Datei, falls TeXShop als Standard registriert ist).
2. **Cmd+T** drückt „Typeset" — entspricht einem `pdflatex`-Lauf. Die PDF erscheint im Vorschau-Fenster daneben.
3. Für die volle Bibliographie- und Glossar-Pipeline (wie in der Terminal-Reihenfolge oben):
   - Oben links in der Toolbar von **„LaTeX"** auf **„BibTeX"** umschalten → **Cmd+T** (verarbeitet die Quellen).
   - Zurück auf **„LaTeX"** → **Cmd+T** → **Cmd+T** (zwei Durchläufe für konsistente Verzeichnisse).
4. Für das Glossar gibt es in TeXShop standardmäßig keinen Button — falls ihr Glossar/Abkürzungsverzeichnis braucht, einmalig im Terminal `makeglossaries main` im Projektordner laufen lassen und danach in TeXShop wieder Cmd+T. Oder das Glossar-Feature im LaTeX-Skelett auskommentieren, wenn ihr es nicht braucht.

Tipp: In TeXShop unter **Einstellungen → Quelle → Encoding** auf **UTF-8 Unicode** stellen, dann gibt es keine Umlautprobleme.

---

# Wie das alles zusammenspielt

In Obsidian schreibt ihr eure täglichen Notizen, Entscheidungen und TODOs. Git versioniert das im Hintergrund — ihr könnt jederzeit nachschauen, was ihr vor drei Wochen entschieden habt und warum. Größere Texte (Thesis, Berichte, Essays) entstehen in LaTeX in einem **eigenen Projektordner** (nicht im Obsidian-Vault), aber die Recherche und Argumentationsstränge sammelt ihr vorher in Obsidian unter `references/` und `projects/`.

---

# Wenn etwas hakt

| Problem | Lösung |
|---|---|
| Obsidian zeigt Wikilinks rot („file not found") | Datei existiert noch nicht — auf den Link klicken legt sie an. Oder Tippfehler im Dateinamen? |
| `git: command not found` | Xcode Command Line Tools nachinstallieren: `xcode-select --install` |
| `pdflatex: command not found` nach MacTeX-Installation | Terminal komplett schließen und neu öffnen — PATH wird erst dann aktualisiert. |
| LaTeX-Fehler „File `literatur.bib' not found" | `\addbibresource{…}` zeigt auf eine Datei, die nicht im selben Ordner liegt. Pfad prüfen. |
| `??` statt Quellen in der PDF | Ihr habt `biber` vergessen oder die Reihenfolge `pdflatex → biber → pdflatex → pdflatex` nicht eingehalten. |
| Umlaute werden komisch dargestellt | Im LaTeX-Editor Encoding auf UTF-8 stellen. |

---


Bei Fragen einfach melden.

Viele Grüße
Estelle

## Verwandte Notizen
- Teil der Vortragsreihe: [[01-start-ki-einrichten|Vortrag: KI einrichten]]
