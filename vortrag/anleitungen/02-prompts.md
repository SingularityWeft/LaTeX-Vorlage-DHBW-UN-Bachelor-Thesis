---
date: 2026-05-16
tags:
  - vortrag
  - info-sheet
  - prompts
---

# Prompts — Schritt für Schritt zum vollständigen System

Voraussetzung: Du hast [`01-start-ki-einrichten.md`](01-start-ki-einrichten.md) durchgearbeitet, hast einen leeren Vault-Ordner (z. B. unter `~/Obsidian/SecondBrain/`), eine `CLAUDE.md` (für Claude) oder `AGENTS.md` (für Codex) im Vault-Root, und die KI läuft im Vault.

> **Wie das hier funktioniert:** Jeder Prompt ist ein Copy-Paste-Block in einem grauen Code-Kasten. Du markierst den Block, kopierst (Cmd+C), wechselst in dein KI-Fenster (Claude Code / Codex), paste­rst (Cmd+V), drückst Enter. Die KI führt aus, fragt zwischendurch nach Permission (immer einmal lesen, bevor du „ja" drückst), und meldet sich, wenn sie fertig ist. Dann der nächste Prompt.

**Reihenfolge:** 1 → 7 strikt nacheinander. Spring nicht.

Wenn ein Prompt schiefläuft: dem AI sagen, was nicht stimmt („Stop, das ist nicht der richtige Ordner — wir sind in X" o. ä.), nicht weiter machen. Lieber einmal mehr fragen als einmal zu wenig.

---

## Prompt 1 — Vault-Ordnerstruktur anlegen

Was passiert: Die KI legt die Standardordner an. Wenn welche schon da sind, lässt sie sie unverändert.

```
Lies CLAUDE.md (bzw. AGENTS.md) im aktuellen Verzeichnis und halte dich an die dort beschriebenen Konventionen.

Lege auf dieser Basis die folgende Ordnerstruktur direkt im aktuellen Verzeichnis an, falls sie noch nicht existiert:

- inbox/
- doing/
- done/
- decisions/
- trashed/
- journal/
- projects/
- references/
- templates/
- termine/

Berichte am Ende kurz, welche Ordner du neu angelegt hast und welche bereits existiert haben. Lege keine Beispiel-Dateien an — die Ordner sollen leer sein.
```

---

## Prompt 2 — Templates erstellen

Was passiert: Die KI legt fünf Vorlagen-Dateien im Ordner `templates/` an. Du nutzt sie später beim Anlegen neuer Notes.

```
Lege im Ordner templates/ folgende fünf Dateien mit exakt dem unten gezeigten Inhalt an. Wenn eine Datei schon existiert, frage mich vor dem Überschreiben.

Datei 1: templates/daily-note.md
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

## Offen aus letzter Session

- [ ]

## Was passiert ist

## Entscheidungen

| Entscheidung | Begründung | Auswirkung |
|---|---|---|
| | | |

## Nächste Session

- [ ]

## Vernetzung

- [[{{date-1d:YYYY-MM-DD}}-Session Log]]


Datei 2: templates/todo.md
---
date: {{date:YYYY-MM-DD}}
tags:
  - todo
---

# {{title}}

**Status:** #todo
**Deadline:** {{date}}
**Blocked by:** —

## Ziel (Definition of Done)


## Consequence Scan

- [ ] Was passiert wenn ich das NICHT mache?
- [ ] Was ist das kleinstmögliche shippable Ergebnis?
- [ ] Welche Entscheidung muss VORHER getroffen werden?

## Next Action

> Konkreter erster Schritt (1 Satz, ausführbar in <10 min)

## Vernetzung

-

## Done?

- [ ]
- [ ] Ergebnis liegt vor → nach `done/` verschieben


Datei 3: templates/decision.md
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

## Entschieden

> **Datum:** —
> **Gewählte Option:** —
> **Begründung (1 Satz):** —

## Folgen — TODOs (kurzfristig)

- [[YYYY-MM-DD-todo-titel]] — 1-Satz-Beschreibung

## Not-TODOs (bewusst verworfen)

- Option B: Begründung

## Vernetzung

- Session Log: [[YYYY-MM-DD-Session Log]]


Datei 4: templates/weekly-review.md
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

## Shipped (done/ diese Woche)

- ✅ [[ ]]

## Inbox Cleanup (> 7 Tage)

- 📥 [[ ]] — verarbeiten oder → trashed/

## Was habe ich vermieden?

## Erkenntnis oder Entscheidung der Woche

## Fokus nächste Woche (Top 3)

1.
2.
3.

## Vernetzung

- Vorwoche: [[ ]]


Datei 5: templates/frist.md
---
date: {{date:YYYY-MM-DD}}
tags:
  - frist
---

# {{titel}}

**Status:** #todo
**Deadline:** {{YYYY-MM-DD}}
**Typ:** <!-- z. B. Steuer, Behörde, Vertraglich, Förderung -->
**Konsequenz bei Versäumnis:** {{was passiert konkret}}

## Was ist zu tun?

- [ ] Schritt 1
- [ ] Schritt 2

## Vernetzung

- [[]]


Wenn alle Dateien geschrieben sind: bestätige kurz, welche fünf du angelegt hast, und ob alle Frontmatter-Blöcke (--- ... ---) korrekt eingeschlossen sind.
```

---

## Prompt 3 — Git initialisieren + erstes Commit

Was passiert: Die KI macht den Vault zu einem Git-Repository, legt eine sinnvolle `.gitignore` an und macht das erste Commit. Ab jetzt ist jede Änderung versioniert.

```
Initialisiere im aktuellen Verzeichnis ein neues Git-Repository. Setze, falls noch nicht global konfiguriert, die globalen Git-Einstellungen — frag mich vorher nach Name und E-Mail, falls nötig.

Lege eine .gitignore-Datei mit folgendem Inhalt an:

# macOS
.DS_Store
**/.DS_Store

# Obsidian UI state — maschinenspezifisch, nicht versioniert
.obsidian/workspace.json

# Obsidian Community Plugins — Binaries, nicht versionieren
.obsidian/plugins/*/main.js
.obsidian/plugins/*/styles.css

# KI-Tool Worktrees (falls Claude Code agenten-features nutzt)
.claude/

Stage anschließend alles und mache ein erstes Commit mit der Nachricht „init: vault initial setup". Hänge an die Commit-Message wie in CLAUDE.md beschrieben einen Co-Authored-By-Trailer für dich an.

Berichte am Ende: Git-Repo erfolgreich angelegt? Welche Dateien sind im Commit? Wie viele insgesamt?
```

---

## Prompt 4 (optional, aber für Multi-Device-Sync nötig) — Remote anlegen (GitHub oder GitLab)

Was passiert: Dein Vault landet zusätzlich als privates Backup in der Cloud — und du kannst auf einem zweiten Gerät den Vault per `git clone` herunterladen und synchron halten.

**Vorbereitung als Mensch — wähle einen der beiden Anbieter:**

**Variante A: GitHub** (am verbreitetsten, Standard)
1. Konto anlegen unter <https://github.com/signup>, falls noch nicht vorhanden.
2. Neues **privates** Repo erstellen unter <https://github.com/new>. Name z. B. `secondbrain`. „Private" anklicken. **Keine** README, keine `.gitignore` mitanlegen (haben wir schon).
3. Kopiere von der gerade angezeigten Seite die Remote-URL (sieht aus wie `git@github.com:DEINNAME/secondbrain.git` oder `https://github.com/DEINNAME/secondbrain.git`).

**Variante B: GitLab** (Alternative — gut, wenn du EU-Hosting bevorzugst)
1. Konto anlegen unter <https://gitlab.com/users/sign_up>.
2. Neues **privates** Projekt erstellen unter <https://gitlab.com/projects/new> → „Create blank project". Name z. B. `secondbrain`. **„Project visibility" auf „Private"** stellen. **Kein** README initialisieren.
3. Kopiere die Remote-URL aus dem „Clone"-Menü (z. B. `git@gitlab.com:DEINNAME/secondbrain.git`).

Dann diesen Prompt mit der gewählten Remote-URL eingesetzt:

```
Füge dem aktuellen Repo das folgende Remote als "origin" hinzu: <HIER DIE REMOTE-URL EINSETZEN>

Setze den Branch auf "main" (falls noch nicht aktiv) und pushe das aktuelle Commit nach origin/main. Wenn dabei eine Authentifizierungsfrage kommt: stoppe und sag mir genau, was der Anbieter will (Token, SSH-Key etc.) — wir lösen das gemeinsam.
```

**Zweites Gerät anbinden (später, optional):** Auf dem zweiten Gerät einfach denselben Vault klonen:

```bash
cd ~/Obsidian/          # oder wo immer du den Vault haben willst
git clone <DIE REMOTE-URL VON OBEN>
```

Künftig vor Sessionstart `git pull` (oder die KI bitten: „Pull den Vault, bevor wir anfangen"), und nach jeder Session pusht die KI automatisch (siehe Git-Regel in CLAUDE.md).

---

## Prompt 5 — LaTeX-Thesis-Vorlage klonen

Was passiert: Du klonst die fertige DHBW-Bachelor-Thesis-Vorlage aus einem öffentlichen Repo, statt sie von der KI neu generieren zu lassen. Vorteile: sie ist getestet, kompiliert sofort, enthält bereits das `latex-build`-Skill (für Claude Code) und eine `AGENTS.md` (für Codex), Deckblatt-Platzhalter, Ehrenwörtliche Erklärung und Vorlage für die KI-Erklärung. Erst hier, nicht im Vault — LaTeX und Notizen trennen.

**Vorbereitung als Mensch:**

1. Stelle sicher, dass MacTeX installiert ist (~5 GB Download von <https://www.tug.org/mactex/>). Prüfe im Terminal: `pdflatex --version` und `biber --version` müssen beide Versionsnummern zeigen.
2. Klone die Vorlage in einen Projektordner deiner Wahl:
   ```bash
   cd ~/Developer/         # oder wo du deine Projekte sammelst
   git clone https://github.com/SingularityWeft/LaTeX-Vorlage-DHBW-UN-Bachelor-Thesis.git meine-thesis
   cd meine-thesis
   ```
3. Starte die KI **in diesem neuen Ordner** (nicht mehr im Vault).

Dann diesen Prompt:

```
Lies README.md und schau dir die Struktur dieses Projektes an. Erkläre mir kurz:

1. Welche Dateien gibt es und was machen sie?
2. Welche Stellen in main.tex sind als %% PLACEHOLDER markiert und müssen ich anpassen, bevor ich abgebe?
3. Wie löse ich künftig einen Build aus — gibt es einen Skill bzw. eine AGENTS.md, die du nutzen kannst?

Initialisiere danach ein frisches Git-Repo in diesem Ordner (lösche dafür den geerbten .git-Ordner und mach ein neues `git init` + erstes Commit „init: thesis aus vorlage übernommen") — damit das hier ab jetzt MEIN Repo ist, nicht ein Klon-Repo der Vorlage.
```

**Wichtig:** Das Repo auf GitHub wird beim Klonen mitgezogen — ohne das `git init`-Reset bist du an die Vorlage gebunden. Der Prompt oben sagt der KI, das `.git`-Verzeichnis zu erneuern, damit du dein eigenes Repo bekommst (und ggf. in Prompt 4 analog dein eigenes GitHub/GitLab-Remote anbinden kannst).

---

## Prompt 5b (optional) — Erste Test-Kompilierung

Was passiert: Du prüfst, ob das LaTeX-Setup funktioniert, indem die KI den Skill direkt anwendet. Voraussetzung: MacTeX installiert.

```
Kompiliere die Thesis. Verwende den latex-build-Skill (bzw. die AGENTS.md-Anweisung).
```

Wenn am Ende eine `main.pdf` im Thesis-Ordner liegt: Setup funktioniert. Wenn nicht: KI meldet die Fehlerzeilen aus `main.log` — gemeinsam debuggen.

---

## Prompt 6 (optional) — `ki-erklaerung.md` für Thesis anlegen

Was passiert: Eine eigene Datei im Thesis-Projekt, die kontinuierlich dokumentiert, was die KI beigetragen hat und was du aus anderen KIs (Gemini, GPT etc.) importiert hast. Wird am Abgabetag zur akademischen KI-Erklärung. Siehe [`01-start-ki-einrichten.md`, Abschnitt C.5](01-start-ki-einrichten.md#c5-akademische-ki-erklärung--für-thesis-hausarbeit-veröffentlichung).

**Vorbereitung:** wechsle in den Thesis-Ordner (`cd ~/Developer/thesis/`) oder starte dort eine neue KI-Session.

```
Lege im aktuellen Verzeichnis eine Datei ki-erklaerung.md mit folgender Struktur an:

# KI-Erklärung — [Titel der Arbeit]

Diese Datei dokumentiert kontinuierlich die Nutzung von KI-Werkzeugen im Verlauf der Arbeit. Format pro Eintrag: Datum · Tool · Aufgabe · Umfang · Quelle (bei importierten Inhalten).

## Einträge

### YYYY-MM-DD · Tool-Name
- **Aufgabe:**
- **Umfang:**
- **Übernommenes:**

(weiter unten neue Einträge anhängen)

Hänge dann einen ersten Eintrag für unsere heutige Session an: was du heute beim Anlegen des LaTeX-Skeletts beigetragen hast (Vollständige Generierung der main.tex und literatur.bib). Datum: heute. Tool: dein Modellname.

Ab jetzt: bei jedem Sessionende in diesem Verzeichnis ungefragt einen neuen Eintrag anhängen, der dokumentiert, was du in der Session beigetragen hast und welche extern (Gemini, GPT etc.) importierten Inhalte ich dir in die Hand gegeben habe.
```

---

## Prompt 7 — Erste produktive Note anlegen (Test)

Was passiert: Du legst gemeinsam mit der KI deine erste echte Note an — am besten ein heutiges Session Log. Damit prüfst du, ob die Templates funktionieren und die Konventionen sitzen.

> **Wechsle wieder in den Vault-Ordner für diesen Prompt** (falls du für Prompt 5–6 in den Thesis-Ordner gewechselt bist).

```
Lege in journal/ ein heutiges Session Log nach Template templates/daily-note.md an. Dateiname: YYYY-MM-DD-Session Log.md mit dem heutigen Datum.

Trage als „Ziel heute" ein: „SecondBrain-System eingerichtet (Sheet 01 + 02 durchgearbeitet)".

Trage unter „Was passiert ist" eine kurze Liste ein, was wir heute zusammen gemacht haben (Vault-Struktur, Templates, git init, optional GitHub-Remote, optional LaTeX-Skelett).

Setze die Vernetzung am Ende sinnvoll und das author:-Feld im Frontmatter auf den passenden Wert für eine gemeinsam erstellte Note. Halte dich an die Konventionen aus CLAUDE.md.

Bestätige am Ende: Datei angelegt? Welcher Pfad? Wie heißt das author:-Feld?
```

---

# Fertig — was du jetzt hast

Wenn alle 7 Prompts durch sind:

- ✅ Vault mit Ordnerstruktur und 5 Templates
- ✅ Git-Versionierung (lokal + optional GitHub-Backup)
- ✅ LaTeX-Schreibprojekt im DHBW-Layout + `latex-build`-Skill (sofern Prompt 5 gemacht) — Kompilier-Kommandos kennst du nie selbst, die KI macht sie auf Zuruf
- ✅ KI-Erklärung-Datei für deine Thesis (sofern Prompt 6 gemacht)
- ✅ Erstes Session Log, KI hat ihre eigene Autorenschaft korrekt markiert

**Im Alltag ab jetzt:**

1. Sessionstart: KI im Vault starten („Lies meine letzten 3 Session Logs und CLAUDE.md, fass den Stand zusammen").
2. Arbeiten: TODOs/Decisions/Notes mit der KI anlegen, immer die Konventionen beachten.
3. **Thesis-Arbeit:** KI im Thesis-Ordner starten (NICHT im Vault), schreiben/redigieren, am Ende: „Kompiliere die Thesis" — die KI nutzt den `latex-build`-Skill und meldet, ob die PDF fehlerfrei gebaut wurde.
4. Sessionende: „Schreib unser Session Log fertig und committe." (Funktioniert auch im Thesis-Ordner: „Committe die Thesis-Änderungen.")
5. Wöchentlich: „Erstell mir einen Weekly-Review-Entwurf nach Template — auf Basis der Session Logs dieser Woche."

Wenn du verstehen willst, **warum** die Struktur so ist (Ordnerlogik, Wikilink-Konventionen, LaTeX-Pakete im Detail), lies [`03-system-erklaerung.md`](03-system-erklaerung.md) — das ist das Hintergrundmaterial zu dem, was die KI in den Prompts oben gemacht hat.

---

# Wenn ein Prompt schiefläuft

| Problem | Lösung |
|---|---|
| KI ignoriert die Konventionen aus CLAUDE.md | „Lies CLAUDE.md nochmal und korrigiere dich entsprechend." |
| KI legt Dateien im falschen Ordner an | Stop sagen, `pwd` im KI-Fenster ausführen lassen, KI ggf. neu starten im richtigen Ordner. |
| KI schlägt vor, etwas zu löschen | Nein. „Bitte nach trashed/ verschieben statt löschen — das ist Konvention." |
| Git-Push scheitert mit Authentifizierungs-Fehler | Stop. Mir Bescheid sagen mit der genauen Fehlermeldung — wir lösen das gemeinsam. |
| Template-Datei sieht nach dem Anlegen kaputt aus (z. B. Frontmatter zerschossen) | „Vergleich Datei X mit dem Original-Block aus Prompt 2 und stell sie wieder her." |
| Ich habe einen Prompt aus Versehen zweimal abgesendet | Meist harmlos — die KI sieht „existiert schon" und tut nichts. Falls doch etwas überschrieben wurde: git status / git diff prüfen, und ggf. `git checkout -- <datei>` zum Zurücksetzen. |

---

## Verwandte Notizen
- Teil der Vortragsreihe: [[01-start-ki-einrichten|Vortrag: KI einrichten]]
