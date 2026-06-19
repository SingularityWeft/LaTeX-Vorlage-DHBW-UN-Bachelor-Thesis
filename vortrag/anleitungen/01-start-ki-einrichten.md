---
date: 2026-05-16
tags:
  - vortrag
  - info-sheet
  - ki
---

# Sheet 01 — Start hier: KI einrichten und Vault vorbereiten

Hallo,

das hier ist der **Einstieg** — danach bist du sofort einsatzbereit. Die Idee dieses Setups: Statt dass du Ordner und Vorlagen mühsam per Hand anlegst, übernimmt die KI das. Du selbst machst nur vier Schritte, danach copy+paste aus [`02-prompts.md`](02-prompts.md) Anweisungen in dein KI-Fenster und sie macht den Rest.

Wenn du verstehen möchtest, **was** die KI in den Prompts überhaupt tut (Vault-Logik, Wikilink-Konventionen, LaTeX-Pakete im Detail), liegt das Hintergrundmaterial in [`03-system-erklaerung.md`](03-system-erklaerung.md). Für das reine Aufsetzen brauchst du das nicht.

Die Anleitung zeigt beide Werkzeuge, die ich im Vortrag erwähnt habe — **Claude Code** (Anthropic) und **OpenAI Codex** (CLI + Desktop) — parallel und gleich tief.

> **Kurz zu „CLI":** Steht für *Command Line Interface*. Heißt einfach: ihr bedient das Programm nicht per Klick, sondern indem ihr im Terminal-Fenster Befehle eintippt. Das ist beim ersten Mal ungewohnt, aber für KI-Tools dieser Art ist das Terminal die schnellste Schnittstelle — Mausklicks würden nur bremsen.

Beide Tools funktionieren konzeptionell identisch: sie greifen auf einen Ordner zu (euren Vault), lesen darin automatisch die Konventionen-Datei (`CLAUDE.md` für Claude, `AGENTS.md` für Codex) und reden dann mit euch über eure Notizen.

> **Desktop-App oder CLI?** Beide Anbieter bieten zwei Wege:
> - **Desktop-App** (klickbar, mit Fenster): einfacher Einstieg, keine Terminal-Berührung nötig. Geeignet, wenn ihr „nur mal probieren" wollt.
> - **CLI im Terminal:** mächtiger, schneller, besser scriptbar — und das eigentliche „native" Format dieser Tools. Geeignet, wenn ihr regelmäßig damit arbeiten wollt.
>
> In dieser Anleitung zeige ich für jedes Tool **beide Wege** — ihr könnt euch entscheiden oder beide installieren (sie stören sich nicht). Die Konventionen aus [Teil C](#teil-c--provenance-ki-inhalt-vs-eigener-inhalt) gelten in beiden Varianten gleich.

---

## Schnellstart — alle Download-Links auf einen Blick

Wer erst loslegen und später lesen will: hier sind alle Quellen. Erklärungen, Setup-Reihenfolge und Konventionen kommen weiter unten.

| Was                                                            | Link                                                                                  |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **OpenAI Codex Desktop App** (Mac/Windows, seit März 2026)     | <https://developers.openai.com/codex/app>                                             |
| **OpenAI Codex** — GitHub (CLI + alternative Wege)             | <https://github.com/openai/codex>                                                     |
| **Claude Desktop Quickstart** (mit integrierter Code-Funktion) | <https://code.claude.com/docs/en/desktop-quickstart>                                  |
| **Claude Apps** (Desktop für Mac/Windows + Mobile)             | <https://claude.com/download>                                                         |
| **Claude Code** — nativer CLI-Installer (ohne Node.js)         | `curl -fsSL https://claude.ai/install.sh \| bash`                                     |
| **Claude Code** — GitHub & vollständige Setup-Doku             | <https://github.com/anthropics/claude-code> · <https://code.claude.com/docs/en/setup> |
| **Remote für Multi-Device-Sync** — GitHub-Konto (kostenlos, privates Repo)  | <https://github.com/signup> · neues privates Repo: <https://github.com/new> |
| **Remote für Multi-Device-Sync** — GitLab-Alternative (kostenlos, EU-Hosting möglich) | <https://gitlab.com/users/sign_up> · neues privates Repo: <https://gitlab.com/projects/new> |
| **LaTeX-Thesis-Vorlage** (DHBW Unternehmertum, fertig zum Klonen, mit KI-Build-Skill) | <https://github.com/SingularityWeft/LaTeX-Vorlage-DHBW-UN-Bachelor-Thesis> |

> **Multi-Device-Sync:** Wenn du am Laptop **und** Desktop arbeiten willst (oder als Backup in der Cloud), brauchst du ein GitHub- oder GitLab-Konto (beide kostenlos). Während die Downloads laufen, kannst du dich schon mal anmelden — die Anbindung passiert dann via Prompt 4 in [`02-prompts.md`](02-prompts.md). GitLab ist eine sinnvolle Alternative, wenn dir EU-Datenhosting wichtig ist.

**Wichtigster Mehrwert dieses Sheets:** [Teil C](#teil-c--provenance-ki-inhalt-vs-eigener-inhalt) zeigt, wie ihr KI-geschriebene Inhalte sauber von euren eigenen unterscheidet. Ohne diese Disziplin verliert ihr nach einigen Wochen den Überblick, was ihr selbst gedacht und was die KI vorgeschlagen hat.

---

## Was ihr am Ende habt

1. Claude Code **und/oder** OpenAI Codex lokal installiert und eingerichtet (Desktop-App oder CLI).
2. Eine erste KI-Session in eurem Vault — die KI kennt eure Templates und Konventionen.
3. Ein **Provenance-System**, mit dem ihr jederzeit nachvollziehen könnt, welcher Text von euch und welcher von der KI stammt.

Dauer: ca. 30–60 Minuten beim ersten Mal.

---

# Die 4 Schritte zum laufenden System

Das ist der Mindest-Workflow. Mehr brauchst du für den Start nicht — die Tool-Vergleichs- und Detail-Abschnitte weiter unten sind nur, wenn du tiefer verstehen willst.

## Schritt 1 — Obsidian installieren und leeren Vault anlegen

1. Obsidian herunterladen: <https://obsidian.md/download>
2. Doppelklick auf das `.dmg`, App in den Ordner `Programme` ziehen.
3. Obsidian öffnen → „Create new vault".
4. Name: `SecondBrain` (oder wie du willst). Ort: dein Benutzerordner, ich empfehle `~/Obsidian/SecondBrain/`.
5. „Create" klicken.

Du hast jetzt einen leeren Vault — das ist die Spielwiese, in der gleich alles passiert.

## Schritt 2 — KI installieren (Claude Code oder OpenAI Codex)

**Schnellster Weg für Anfänger (klickbar, kein Terminal):** Eine der beiden Desktop-Apps:

- **Claude Desktop:** <https://claude.com/download> — mit integrierter Code-Funktion [Quickstart](https://code.claude.com/docs/en/desktop-quickstart)
- **OpenAI Codex Desktop:** <https://developers.openai.com/codex/app>

Installieren, einloggen mit deinem Anthropic- bzw. OpenAI-Account, fertig.

> Wenn du lieber die CLI-Variante (Terminal) willst, findest du alle drei Installationswege weiter unten in [Teil A](#teil-a--claude-code-einrichten-desktop-oder-cli) (Claude) bzw. [Teil B](#teil-b--codex-einrichten-desktop-oder-cli) (Codex).

## Schritt 3 — `CLAUDE.md` (CODEX: `AGENTS.md`) in den Vault legen

Das ist die zentrale Konventionsdatei: die KI liest sie automatisch, wenn sie im Vault arbeitet, und hält sich an die darin beschriebenen Regeln.

Erstelle im Vault-Root (also direkt in `~/Obsidian/SecondBrain/`) eine Datei namens `CLAUDE.md` — am einfachsten in Obsidian: Rechtsklick auf den Vault → „New note" → Dateiname `CLAUDE` eingeben. Kopiere folgenden Inhalt hinein:

````markdown
# SecondBrain — Konventionen

Dies ist ein Obsidian-Vault + Git-Repo. Halte dich an die unten beschriebenen Regeln, wenn du in diesem Verzeichnis arbeitest.

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

## Session Log

Datei: `journal/YYYY-MM-DD-Session Log.md`
Template: `templates/daily-note.md`

Inhalt: Ziel heute · Was passiert ist · Entscheidungen (Tabelle) · Nächste Session.
Immer bidirektional verlinken: Session Log ↔ besprochene doing/-Items.

## TODO

Datei: `inbox/YYYY-MM-DD-titel.md`
Template: `templates/todo.md`
Pflichtfelder: Status, Deadline, Consequence Scan, Next Action (1 Satz).

## Entscheidung

Datei: `doing/decision-titel.md`
Template: `templates/decision.md`
Pflichtfelder: Deadline + Default-Option falls Deadline verstreicht.

Nach getroffener Entscheidung — Pflicht-Konsequenz-Extraktion vor dem Move:
1. Kurzfristige Folge-TODOs als `inbox/YYYY-MM-DD-titel.md` anlegen und in der Decision-Note verlinken.
2. Not-TODOs inline dokumentieren (verworfene Optionen + 1-Satz-Begründung).
3. Session Log verlinken.
4. Datei nach `decisions/YYYY-MM-DD-titel.md` verschieben (NICHT nach `done/`).

## Vernetzung (keine Orphans!)

Jede Note muss mindestens einen ein- UND ausgehenden Wikilink haben.
Pflicht bei neuen Notes: `## Vernetzung`-Abschnitt am Ende.

## Status-Tags

`#todo` · `#done` · `#decision` · `#priority-1`

## Ordnerstruktur doing/

Alles flach in `doing/` — keine Unterordner. Sortierung via Tags.

---

## Git — Versionierung am Sessionende (Pflicht)

Damit nichts verloren geht und jede Änderung nachvollziehbar bleibt: Wenn das aktuelle Verzeichnis ein Git-Repository ist (`.git/`-Ordner vorhanden), gilt:

1. **Am Sessionende** prüfe `git status`. Falls uncommitted Änderungen existieren:
   - `git add -A`
   - `git commit -m "<aussagekräftige Nachricht: was hat sich konkret geändert>"` — eine Zeile, nicht generisch („update files"), sondern spezifisch („todo: Q3-Recherche-Plan in inbox angelegt").
   ```
   docs(inbox): TODO für Q3-Recherche angelegt
   ```
3. **Push, wenn ein Remote konfiguriert ist** und der aktuelle Branch Tracking-Info hat: `git push`. Wenn der Push scheitert (z. B. Auth-Problem), **nicht raten** — stop, dem User die Fehlermeldung melden.
4. **Niemals destruktive Git-Befehle** ohne explizite Zustimmung des Users: kein `git reset --hard`, kein `git push --force`, kein `git branch -D`, kein `git clean -f`.
5. **Diese Regel gilt für jedes Repo**, in dem du arbeitest — Vault, Thesis-Projekt, Code-Repo. Nicht nur für den Vault.

---

## Provenance — Autorenschaft kennzeichnen (Pflicht)

Damit klar bleibt, was ich (Mensch) und was du (KI) geschrieben hast:

1. **Neue Note komplett von dir angelegt:** Frontmatter-Feld `author: claude` (bzw. `author: codex`) setzen.
2. **Bestehende Note: du ergänzt einen Abschnitt:** den ergänzten Inhalt in einen Obsidian-Callout packen:
   ```
   > [!ai] Vorschlag (YYYY-MM-DD)
   > <dein vorgeschlagener Text>
   > Status: ungeprüft.
   ```
3. **Bestehende Note: du änderst nur einzelne Wörter/Sätze:** im Commit explizit ausweisen, plus im Session Log 1-Zeiler unter „Was passiert ist".
4. **Am Sessionende (wenn `ki-erklaerung.md` im Working Directory existiert):** ungefragt einen Eintrag anhängen, der dokumentiert: (a) was du in dieser Session selbst beigetragen hast, (b) welche von außen importierten KI-Inhalte (Gemini, GPT, andere) ich dir in die Hand gegeben habe — mit der Quellenangabe, die ich mitgegeben habe.

**Niemals:** das `author:`-Feld einer bestehenden Note ohne explizite Ansage des Users ändern. Wenn der User einen Vorschlag übernimmt, entfernt **er** die Callout-Wrapper — nicht du.
````

Wenn du Codex statt Claude nutzt: gleiche Datei, anderer Name. Lege sie als `AGENTS.md` an (gleicher Inhalt). Falls du beide parallel testen willst, ist es am einfachsten, eine Datei zu pflegen und die andere als Verweis darauf anzulegen — siehe [B.3](#b3-vault-als-working-directory).

## Schritt 4 — KI im Vault starten

**Wenn du die Desktop-App nutzt (klickbar):**

### Claude Desktop (</> Code), Empfehlung: Anfänger erstmal nur Codex s.u.
1. App öffnen (Claude Desktop).
2. Im Menü oben Code auswählen, dann im rechten Menü neben "Lokal" das Arbeitsverzeichnis "SecondBrain" auswählen. Bei Claude Desktop führt das in den Code-Modus (siehe [Quickstart-Anleitung von Anthropic](https://code.claude.com/docs/en/desktop-quickstart) mit Screenshots).
3. Die App zeigt jetzt einen Chat (oder etwas, was wie ein Chat aussieht). Du kannst tippen.

Damit ist die KI „in deinem Vault" und kann darin arbeiten (lesen und schreiben) — sie liest die `CLAUDE.md` automatisch und kennt deine Vorgaben.

### Codex Desktop
1. App öffnen (Codex Desktop).
2. Im Menü links "Projekte" suchen, rechts davon das kleine Ordner Icon anklicken: "Vorhandenen Ordner verwenden"  das öffnet eure Dateiordnerübersicht, dort den SecondBrain-Ordner anklicken. 
	- *Falls ihr Claude Desktop bereits angelegt habt, kann Codex dessen CLAUDE.md einfach übernehmen ("Zu importierende Einstellungen auswählen: Codex hat nützliche Einstellungen aus einer anderen Agent-App gefunden").*
3. Die App hat einen Chat (oder etwas, was wie ein Chat aussieht). Du kannst tippen.


**Wenn du die CLI-Variante nutzt (Terminal):**

Terminal öffnen, dann diesen Block kopieren und einfügen:

```bash
cd ~/Obsidian/SecondBrain
claude       # für Claude Code
# ODER:
codex        # für OpenAI Codex 
```

Das `cd ~/Obsidian/SecondBrain` wechselt in deinen Vault. Danach startet `claude` (bzw. `codex`) die KI **in genau diesem Ordner** — sie liest automatisch die `CLAUDE.md`/`AGENTS.md` darin.

Probier zum Test diesen Prompt:

```
Lies CLAUDE.md (bzw. AGENTS.md) und fass mir in 3 Sätzen zusammen, was die wichtigsten Konventionen sind.
```

Wenn die Antwort auf Workflow (inbox→doing→done), Wikilinks und Provenance eingeht: alles sitzt.

---

# Weiter mit `02-prompts.md`

Damit ist das Setup fertig. Den Rest — Ordnerstruktur, Templates, git-Versionierung, optionale LaTeX-Vorlage — erledigt die KI für dich. Öffne jetzt [`02-prompts.md`](02-prompts.md) und arbeite die Prompts 1 bis 7 nacheinander ab.

Wenn etwas hakt: dieses Sheet hier nochmal aufschlagen — die Detail-Doku unten erklärt alles, was du fürs produktive Arbeiten mit KI zu wissen brauchst.

---

# Detail-Doku — wenn du tiefer einsteigen willst

Alles ab hier ist optional. Wenn du jetzt einfach loslegen willst, scroll hoch zu [`02-prompts.md`](02-prompts.md). Die folgenden Abschnitte erklären Tool-Unterschiede, Installationsvarianten, Kontext-Design und das Provenance-System im Detail.

---

## Welches Tool? Kurzer Vergleich

|                                 | **Claude Code** (Anthropic)                                                                                   | **OpenAI Codex** (CLI + Desktop)                                                                 |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Modellstärke aktuell (Mai 2026) | Opus (stärkstes Modell für komplexe technische Aufgaben), Sonnet (Standardmodell für Code & Text), Haiku (schnell & günstig für leichtere Tasks) | GPT-5.x (starke Modelle für Planung, Tools & Code), Codex-CLI/Desktop als spezialisierte Coding-Umgebung |
| Konventionsdatei                | `CLAUDE.md` (Vault-Root)                                                                                        | `AGENTS.md` (Vault-Root)                                                                         |
| Authentifizierung               | Anthropic-Account (Abo) oder API-Key                                                                            | OpenAI-Account (Abo) oder API-Key                                                                |
| Stärken                         | Sehr lange Kontexte, gute Arbeit mit vielen Dateien, gutes Verständnis projektweiter Konventionen              | Gutes Kontextmanagement, schnelle Ausführung, starke Code-Generierung, multimodal                |
| Kosten                          | Pro-/Max-Abo (typisch deutlich günstiger als reine API-Nutzung bei intensiven Sessions) oder API pay-as-you-go | ChatGPT Plus/Pro (Abo) oder API pay-as-you-go                                                    |
| Für wen am besten geeignet      | Fortgeschrittene Nutzer:innen, die Kontext-Design verstehen und ihre Prompts und Projektstruktur bewusst steuern wollen | Einsteiger:innen und Praktiker, die sich wenig mit Kontext-Management beschäftigen möchten und von automatischer Kontextverwaltung profitieren |

> **Kurz erklärt:**
> - Bei intensiver, täglicher Nutzung sind Abo-Modelle (Claude Pro/Max, ChatGPT Plus/Pro) in der Regel deutlich günstiger als reine API-Nutzung, weil sie hohe oder praktisch unbegrenzte Kontingente für interaktive Sessions bieten.
> - Die **API** (*Application Programming Interface* — die Schnittstelle, über die euer Tool mit dem Anbieter spricht) eignet sich vor allem für Automationen, Integrationen und Workflows, bei denen ihr den Tokenverbrauch genau steuern und skaliert abrechnen möchtet. Der **API-Key** ist dabei der lange Zeichen-Schlüssel, mit dem ihr euch ausweist — findet ihr im Entwickler-Bereich des jeweiligen Anbieters.
> - **Claude Code** punktet vor allem bei sehr langen Kontexten und projektweiter Konsistenz, wenn ihr bereit seid, euer Kontext-Design aktiv zu steuern (Struktur, Dateien, Prompts).
> - **OpenAI Codex** übernimmt einen großen Teil des Kontext-Managements automatisch: Es speichert Sessions, lädt relevante Dateien und Historien wieder ein und komprimiert ältere Teile der Unterhaltung, sodass ihr euch weniger um das Kontextfenster kümmern müsst — ideal, wenn ihr „einfach losarbeiten" wollt, ohne tief in Prompt- und Kontext-Strategien einzusteigen.

### Was ist Kontext-Design?

Kontext-Design bezeichnet die bewusste Gestaltung dessen, was euer Modell zu einem Zeitpunkt „weiß" — also welche Informationen, Dateien und Anweisungen im **Kontextfenster** (dem aktuell sichtbaren Arbeitsspeicher des Modells) landen und wie sie strukturiert sind.

Wichtige Elemente von Kontext-Design:

- **Strukturierte Anweisungen.** Ihr definiert explizit, wie das Modell arbeiten soll: Konventionsdateien (`CLAUDE.md`, `AGENTS.md`), Rollenbeschreibungen, Projektregeln, Coding-Guidelines. Diese liegen stabil im Kontext und geben den „Rahmen" vor — sollten **knapp formuliert** sein, da bei jeder Interaktion dafür Tokens verbraucht werden.

- **Kuratierter Input.** Ihr entscheidet, welche Dateien, Texte, Mails oder Anforderungen relevant sind und wie sie ins Prompt integriert werden — z. B. nur relevante Ausschnitte, klare Markierungen wie „Context:", „Task:".

- **Kontext-Hierarchie.** Ihr trennt zwischen langfristigem Kontext (Projektregeln, Architektur), mittelfristigem Kontext (aktueller Branch, Feature, Ticket) und kurzfristigem Kontext (konkrete Funktion, Diff, Fehlermeldung) und haltet diese Ebenen sauber getrennt.

- **Lebenszyklus des Kontexts.** Ihr plant, wann welche Informationen hinzugefügt, aktualisiert oder entfernt werden — z. B. ältere Chat-Teile zusammenfassen, neue Anforderungen hinzufügen, alte Logs durch Summaries ersetzen — damit das Kontextfenster nicht „zumüllt".

- **Wiederverwendbarkeit.** Ihr gestaltet euer Kontext-Design so, dass ihr es in verschiedenen Sessions, Projekten und Tools wiederverwenden könnt (Standardprompts, Templates, Projektkonventionen), statt jedes Mal bei Null anzufangen.

**Kurz gesagt:** Kontext-Design ist die Fähigkeit, euer LLM als „System" zu denken — ihr baut euch eine Art Informationsarchitektur für eure KI-Sessions. Codex nimmt euch einen Teil davon durch automatische Kontextverwaltung ab, während Claude euch mehr Kontrolle (und Verantwortung) über die bewusste Gestaltung des Kontexts lässt.

**Meine Empfehlung:** Probiert das, womit ihr ohnehin schon ein Abo habt. Konzeptionell sind beide austauschbar — die Konventionen aus [Teil C](#teil-c--provenance-ki-inhalt-vs-eigener-inhalt) funktionieren in beiden Tools identisch, ihr müsst nur die Konventionsdatei einmal pflegen (oder beide spiegelnd, falls ihr parallel testet).

---

## Voraussetzungen (für beide Tools)

**Immer nötig:**

- macOS aus Sheet 1
- Ein Account beim jeweiligen Anbieter (Anthropic bzw. OpenAI). Pro-Abo oder API-Zugang reicht.

**Nur nötig, falls ihr die `npm`-CLI-Variante installieren wollt:**

- **Node.js** installiert. Im Terminal prüfen: `node --version` → erwartet `v20.x` oder höher. Falls fehlt: <https://nodejs.org/> → LTS-Installer laden.

> **Kurz erklärt:**
> - **Node.js:** eine Programmlaufzeit-Umgebung — vereinfacht gesagt: das, worauf manche CLI-Tools überhaupt laufen können. Vergleichbar damit, dass Word den Microsoft-Office-Unterbau braucht.
> - **LTS:** *Long Term Support* — die stabile, langfristig gepflegte Version. Bei Node.js gibt es immer eine LTS- und eine experimentelle Version. Nehmt **immer LTS**, außer ihr wisst genau, warum nicht.
> - **Wenn ihr die Desktop-App oder den nativen CLI-Installer von Claude wählt, braucht ihr Node.js nicht** — die bringen alles mit.

---

# Teil A — Claude Code einrichten (Desktop oder CLI)

## A.1 Installation — drei Wege

Wählt **einen** der folgenden Wege. Mein Vorschlag: **Weg 1**, wenn ihr klicken statt tippen wollt, sonst **Weg 2**.

### Weg 1 — Claude Desktop App (klickbar, kein Terminal nötig)

Download für macOS und Windows: <https://claude.com/download>

Die Desktop-App bringt **Claude Code als integrierte Funktion** mit — ihr könnt im Fenster eine „Coding"-Session starten, einen Vault-Ordner auswählen und dann mit Claude über eure Notizen reden, ohne je das Terminal anzufassen.

Quickstart-Anleitung von Anthropic für genau diese Funktion: <https://code.claude.com/docs/en/desktop-quickstart>

### Weg 2 — Nativer CLI-Installer (Terminal, ohne Node.js)

Empfohlen, wenn ihr im Terminal arbeiten wollt und kein Node.js installiert habt. Ein einziger Befehl, läuft danach von überall:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Aktualisiert sich künftig selbst, ohne dass ihr etwas tun müsst.

### Weg 3 — `npm`-Installation (falls ihr Node.js eh nutzt)

```bash
npm install -g @anthropic-ai/claude-code
```

> **`npm`** ist der „Paket-Manager" von Node.js — eine Art App-Store fürs Terminal, der Programme aus dem Internet lädt und einrichtet. Das `-g` bedeutet „global installieren", damit ihr `claude` aus jedem Ordner heraus aufrufen könnt.

### Installation prüfen

Nach Weg 2 oder 3 im Terminal:

```bash
claude --version
```

Eine Versionsnummer muss erscheinen. Bei Weg 1 (Desktop-App) prüft die App-Version stattdessen über „Claude → Über Claude" im Menü.

Offizielle Setup-Doku mit allen Optionen: <https://code.claude.com/docs/en/setup>
GitHub-Repository: <https://github.com/anthropics/claude-code>

## A.2 Authentifizierung

Beim ersten Aufruf führt Claude Code euch durch den Login. Im Vault-Ordner starten:

```bash
cd ~/Obsidian/SecondBrain
claude
```

Es öffnet ein Browserfenster zum Anmelden bei eurem Anthropic-Account. Nach erfolgreichem Login: zurück ins Terminal, das ist eure erste Session.

## A.3 Vault als Working Directory

> **„Working Directory"** ist einfach das Verzeichnis (= der Ordner), in dem ihr ein Programm gestartet habt. Wenn ihr im Terminal mit `cd ~/Obsidian/SecondBrain` in den Vault wechselt und dort `claude` aufruft, ist der Vault das Working Directory dieser Session.

**Faustregel:** Claude Code **immer im Vault-Ordner starten**. Es liest beim Start automatisch die `CLAUDE.md` im aktuellen Verzeichnis und kennt dadurch eure Konventionen (Wikilink-Format, inbox→doing→done, Pflichtfelder etc.).

Wenn ihr Claude in einem anderen Ordner startet — z. B. im LaTeX-Thesis-Projekt — legt dort eine **eigene** `CLAUDE.md` an, die nur für diesen Ordner gilt.

## A.4 Erste Test-Session

Im Vault gestartet, probiert:

```
Lies CLAUDE.md und beschreib mir in 3 Sätzen, was die wichtigsten Konventionen sind.
```

Wenn die Antwort auf eure Regeln eingeht (inbox→doing→done, Wikilinks etc.), sitzt das Setup.

## A.5 Permissions

Claude Code fragt vor jedem Schreibvorgang nach. Beim ersten Mal nervig, langfristig sehr beruhigend.

Sicherheit ohne Compromise: Lest jede Permission-Anfrage einmal bewusst, bevor ihr „immer erlauben" wählt. Vor allem bei Befehlen, die löschen oder verschieben können.

---

# Teil B — Codex einrichten (Desktop oder CLI)

## B.1 Installation — zwei Wege

### Weg 1 — Codex Desktop-App (klickbar, kein Terminal nötig)

Download für macOS und Windows: <https://developers.openai.com/codex/app>

Die Codex Desktop-App ist seit März 2026 verfügbar und bringt ähnliche Funktionen wie die Claude Desktop-App mit: ihr arbeitet in einem Fenster, könnt Ordner auswählen, mit der KI über euren Vault reden und Änderungen anstoßen — alles per Klick statt per Befehl.

Im Microsoft Store für Windows ebenfalls erhältlich.

### Weg 2 — Codex CLI (Terminal)

```bash
npm install -g @openai/codex
```

Prüfen:

```bash
codex --version
```

GitHub-Repository und alternative Installationswege: <https://github.com/openai/codex>
Offizielle Codex-Produktseite: <https://openai.com/codex/>

> **Stand Mai 2026:** Die OpenAI-Codex-Werkzeuge entwickeln sich schnell. Wenn unten ein Befehl nicht funktioniert, prüft die offizielle Anleitung: <https://platform.openai.com/docs/codex-cli>

## B.2 Authentifizierung

Im Vault-Ordner starten:

```bash
cd ~/Obsidian/SecondBrain
codex
```

Beim ersten Aufruf führt Codex durch den Login (entweder via ChatGPT-Account oder API-Key). Folgt den Hinweisen im Terminal.

## B.3 Vault als Working Directory

Identisch zu Claude: **immer im Vault-Ordner starten**. Codex liest automatisch die Datei `AGENTS.md` im aktuellen Verzeichnis (analog zu `CLAUDE.md`).

Wenn ihr im selben Vault Claude **und** Codex nutzen wollt, könnt ihr `AGENTS.md` einfach als **symbolischen Link** auf `CLAUDE.md` anlegen — dann pflegt ihr eure Konventionen nur einmal:

```bash
cd ~/Obsidian/SecondBrain
ln -s CLAUDE.md AGENTS.md
```

> **Symbolischer Link** (kurz „Symlink"): eine Datei, die nicht selbst Inhalt hat, sondern auf eine andere Datei verweist. Wenn Codex `AGENTS.md` öffnet, liest es in Wahrheit den Inhalt von `CLAUDE.md`. Vorteil: ihr ändert nur eine Datei, beide Tools sehen die Änderung sofort.

## B.4 Erste Test-Session

```
Lies AGENTS.md und beschreib mir in 3 Sätzen, was die wichtigsten Konventionen sind.
```

## B.5 Permissions

Wie bei Claude: Codex fragt vor schreibenden Aktionen nach. Auch hier: bewusst lesen, was ihr freigebt.

---

# Teil C — Provenance: KI-Inhalt vs. eigener Inhalt

Das ist der Teil, an dem viele scheitern. Wenn ihr nach drei Wochen nicht mehr wisst, welcher Absatz in eurer Doing-Note von euch und welcher von der KI stammt, ist euer SecondBrain kaputt — ihr glaubt euren eigenen Notizen nicht mehr.

Es gibt drei Mechanismen, die zusammen funktionieren. Keiner allein reicht.

## C.1 Frontmatter-Feld `author` (für ganze Notes)

Jede Note, die die KI **komplett** anlegt, bekommt ein `author:`-Feld:

```yaml
---
date: 2026-05-16
author: claude       # mögliche Werte: estelle, claude, codex, estelle+claude
tags: [todo]
---
```

Vorteile:

- Per Obsidian-Search filterbar (`author: claude`).
- Mit dem Dataview-Plugin sogar als Tabelle: „alle KI-Notes, die ich noch nicht gegengelesen habe".
- Beim Promotion-Move (z. B. `inbox/` → `doing/`) zwingt euch das Feld zur bewussten Entscheidung: bleibt `author: claude` stehen, oder ändert ihr auf `author: estelle`, weil ihr die Inhalte übernommen habt?

## C.2 Obsidian-Callout für KI-Abschnitte in gemischten Notes

Wenn die KI nur **einen Teil** einer bestehenden Note ergänzt, packt sie ihn in einen Callout:

```markdown
> [!ai] Claude-Vorschlag (2026-05-16)
> Hier kommt der vorgeschlagene Text.
> Status: ungeprüft.
```

Optisch sofort erkennbar in der Preview (eigene Box mit Icon). Beim Übernehmen löscht ihr einfach die `> [!ai]`-Wrapper-Zeilen — der Inhalt wird zu eurem Text.

**Diese „Promotion" ist das eigentliche Signal:** „Ich habe das gelesen und stimme zu." Solange ein Abschnitt im Callout steht, ist er Vorschlag — nicht eure Aussage.

## C.3 Konventionen in `CLAUDE.md` / `AGENTS.md` festschreiben

Damit sich die KI auch wirklich an [C.1](#c1-frontmatter-feld-author-für-ganze-notes) und [C.2](#c2-obsidian-callout-für-ki-abschnitte-in-gemischten-notes) hält, **müsst ihr es in der Konventionsdatei stehen haben**. Sonst tut sie's mal, mal nicht.

Fügt in eurer `CLAUDE.md` (im Vault-Root) folgenden Block hinzu — analog kopiert in `AGENTS.md`, falls ihr Codex nutzt:

````markdown
## Provenance — Autorenschaft kennzeichnen

**Pflicht bei jeder von dir geschriebenen oder geänderten Note:**

1. **Neue Note komplett von dir angelegt:** Frontmatter-Feld `author: claude` (bzw. `author: codex`) setzen.
2. **Bestehende Note: du ergänzt einen Abschnitt:** den ergänzten Inhalt in einen Obsidian-Callout packen:
   ```
   > [!ai] Vorschlag (YYYY-MM-DD)
   > <dein vorgeschlagener Text>
   > Status: ungeprüft.
   ```
3. **Bestehende Note: du änderst nur einzelne Wörter/Sätze:** im Commit explizit ausweisen, plus im Session Log ein 1-Zeiler unter „Was passiert ist".
4. **Am Sessionende (wenn `ki-erklaerung.md` im Working Directory existiert):** ungefragt einen Eintrag anhängen, der dokumentiert: (a) was du in dieser Session selbst beigetragen hast, (b) welche von außen importierten KI-Inhalte (Gemini, GPT, andere) der User dir in die Hand gegeben hat — mit der Quellenangabe, die der User mitgegeben hat.

**Niemals:** das `author:`-Feld einer bestehenden Note ohne explizite Ansage des Users ändern. Wenn der User einen Vorschlag übernimmt, entfernt **er** die Callout-Wrapper — nicht du.
````

Sobald dieser Block in eurer Konventionsdatei steht, halten sich beide Tools daran (mit gelegentlicher Erinnerung — die KI ist nicht perfekt, aber die Regel macht Korrekturen einfach: „Du hast das `author:`-Feld vergessen.").

## C.4 Akademische KI-Erklärung — für Thesis, Hausarbeit, Veröffentlichung

[C.1](#c1-frontmatter-feld-author-für-ganze-notes)–[C.3](#c3-konventionen-in-claudemd--agentsmd-festschreiben) lösen die Frage „Was habe ich vs. was die KI in **diesem Vault** gemacht?". C.4 löst die Frage „Was muss ich **abgeben** als KI-Erklärung?" — bei Thesis, Seminararbeit oder Paper.

Die meisten Hochschulen (auch DHBW) verlangen mittlerweile ein eigenes Dokument oder einen Appendix-Abschnitt, der **transparent ausweist**: welches KI-Tool wofür, in welchem Umfang, an welchen Stellen. Das ist nicht nur Pflicht — es ist auch die einzige Chance, dass ihr **selbst** in sechs Monaten noch wisst, woher welcher Gedanke kam.

### Praxis-Workflow

**1. Eigene Datei im Projekt anlegen:** in eurem Thesis-/Projektordner (nicht im Obsidian-Vault, sondern dort, wo die Arbeit entsteht — z. B. `~/thesis/ki-erklaerung.md`):

````markdown
# KI-Erklärung — [Titel der Arbeit]

Diese Datei dokumentiert kontinuierlich die Nutzung von KI-Werkzeugen im Verlauf der Arbeit. Format pro Eintrag: Datum · Tool · Aufgabe · Umfang · Quelle (bei importierten Inhalten).

## Einträge

### 2026-05-16 · Claude Code (Opus 4.7)
- **Aufgabe:** Kapitel 3.2 Argumentationsstruktur überprüft, drei Gegenargumente vorgeschlagen.
- **Umfang:** Inhaltliche Diskussion im Chat; finale Formulierungen von mir.
- **Übernommenes:** zwei der drei Gegenargumente, sinngemäß umformuliert (Abschnitt 3.2.2).

### 2026-05-16 · Gemini (importierter Inhalt)
- **Aufgabe:** TikZ-Code für Abbildung 4.1 (Prozessdiagramm).
- **Umfang:** Vollständiger Codeblock von Gemini, nach Textvorgabe von mir.
- **Quelle:** Gemini-Session vom 14.05.2026, Prompt-Zusammenfassung in `references/gemini-2026-05-14-tikz.md`.
````

**2. Eingangsdisziplin bei Importen aus anderen KIs:** Wenn ihr aus Gemini/GPT/anderen Tools Inhalte (Texte, Grafiken z.B. als TikZ-Code, Tabellen) in euren Vault oder in die Thesis übernehmt, **kennzeichnet sie sofort** — bevor sie vergessen sind. Drei Möglichkeiten:

- Direkter Kommentar im Text/Code: `% TikZ-Code: Gemini, 2026-05-14, von mir angepasst`
- Eigene Notiz unter `references/`: `references/gemini-2026-05-14-tikz.md` mit Prompt + Roh-Output + was übernommen wurde.
- Frontmatter-Feld: `imported_from: gemini-2026-05-14`.

**3. Sessionende-Ritual:** Am Ende jeder Claude-Code- (oder Codex-)Session sagt ihr explizit:

> „Häng bitte einen Eintrag in `ki-erklaerung.md` an: was hast du in dieser Session beigetragen, und welche importierten KI-Inhalte (Gemini etc.) habe ich dir heute in die Hand gegeben? Datum, Tool, Aufgabe, Umfang."

Wenn die Konventionsdatei (siehe [C.3](#c3-konventionen-in-claudemd--agentsmd-festschreiben), Punkt 4) den Eintrag fordert, tut die KI das auch ohne explizite Aufforderung — aber das Ritual stellt sicher, dass ihr **bewusst** unterschreibt: „Ja, so war's heute."

### Warum sich der Aufwand lohnt

- **Eure eigene Klarheit:** Nach drei Wochen wisst ihr ohne dieses Logbuch nicht mehr, ob die elegante Formulierung in Kapitel 5 von euch, von Claude oder paraphrasiert aus einem GPT-Vorschlag stammt. Mit dem Logbuch: nachschlagen, fertig.
- **Prüfsicherheit:** Bei Nachfragen könnt ihr beantworten, woher welcher Teil stammt.
- **Konsistenz mit den Hochschulvorgaben:** DHBW (und die meisten anderen) verlangen die Erklärung ohnehin — wenn ihr sie kontinuierlich pflegt, ist sie am Abgabetag fertig, statt am Vorabend rekonstruiert.

---

# Erste produktive Session — Vorschläge zum Ausprobieren

Wenn alles steht, probiert in eurer ersten richtigen Session eines davon:

1. **TODO aus Brain-Dump destillieren:**
   > „Ich habe gerade auf dem Flur folgende Gedanken gehabt: [Gedanken]. Leg mir daraus einen TODO in inbox/ an, nach dem Template todo.md."

2. **Weekly Review vorbereiten:**
   > „Schau dir die Session Logs der letzten 7 Tage in journal/ an. Erstell mir einen Entwurf für ein Weekly Review nach Template weekly-review.md im journal/-Ordner — als Vorschlag, ich übernehme dann manuell."

3. **Inbox-Triage:**
   > „Welche Notes in inbox/ sind älter als 7 Tage? Schlag pro Note eine Aktion vor: weiter ins doing/, in trashed/, oder zusammenführen mit existierender Note."

---

# Datenschutz und Kosten — kurz und ehrlich

**Datenschutz:**

- Beide Tools senden eure Anfragen + die zur Beantwortung gelesenen Dateien an die jeweiligen Anbieter (Anthropic bzw. OpenAI, Google, Perplexity etc.).
- Anthropic und OpenAI verpflichten sich (Stand Mai 2026), API-Inhalte nicht standardmäßig fürs Modelltraining zu verwenden — das ist bei den **CLI-Tools mit API-Auth** der Normalfall. Bei ChatGPT-Plus-Auth (Codex) genau prüfen: dort gelten teils andere Regeln.
- **Faustregel:** Wenn ihr es nicht an einen externen Dienstleister mailen würdet (Steuerdaten, Kundendaten, Gesundheitsdaten), packt es nicht in den Vault, **während** ihr KI-Sessions laufen lasst. Oder legt einen separaten weiteren Obsidian-Vault für Sensitives an, in den die KI nie reinguckt.

**Kosten:**

- Pro-Abos: ~20 €/Monat bei beiden Anbietern, mit großzügigen Limits für persönliche Nutzung. Wer regelmäßig das Kontingent ausschöpft, kann auf ~100 € / 200 €/Monat upgraden.
- API-Pay-as-you-go: variabel nach Modell (Claude Opus 4.7 ist im Mai 2026 das teuerste Modell am Markt und nicht für alles das beste). Für tägliche Notizarbeit in Obsidian unter 10€ im Monat realistisch, für Thesis-Schreibarbeiten können leicht 70 € oder deutlich mehr Kosten entstehen.

---

# Wenn etwas hakt

| Problem                                                                                | Lösung                                                                                                                                                                                                                               |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Claude/Codex ignoriert offensichtlich die Konventionen                                 | Im Vault-Ordner gestartet? Mit `pwd` (steht für *print working directory* — zeigt den aktuellen Ordner an) im Tool prüfen. Falls falsch: `exit`, im richtigen Ordner neu starten.                                                    |
| KI vergisst `author:`-Feld                                                             | In der ersten Antwort der Session daran erinnern: „Lies CLAUDE.md und merk dir das persistent / halte die Provenance-Regeln aus Abschnitt X ein." Beim nächsten Mal sitzt es meistens.                                               |
| `AGENTS.md` und `CLAUDE.md` sollen identisch sein, ich will aber nicht doppelt pflegen | Symlink: `ln -s CLAUDE.md AGENTS.md` (siehe [B.3](#b3-vault-als-working-directory)).                                                                                                                                                 |
| Permission-Anfragen nerven                                                             | Im jeweiligen Settings-File (`.claude/settings.json` bzw. Codex-Pendant) **wenige, sehr spezifische** Allow-Rules eintragen. Nie pauschal alles erlauben — der Punkt der Permissions ist, dass ihr Lösch-/Move-Befehle bewusst seht. |
| `claude: command not found` nach Installation                                          | Terminal neu öffnen (`npm`-PATH wird erst dann aktualisiert). Falls weiter nichts: `which npm` prüfen, ggf. Node neu installieren.                                                                                                   |

---

# Was als Nächstes kommt

Wenn ihr beide Sheets durch habt, läuft ein eigenständiges System: ihr schreibt in Obsidian, eine KI hilft im Vault-Kontext, **die KI committet und pusht automatisch am Sessionende** (gemäß `CLAUDE.md`-Regel oben — gilt für Vault *und* Thesis-Repo), und **die KI kompiliert auf Zuruf eure Thesis zur PDF** („Kompiliere die Thesis" — der `latex-build`-Skill aus Prompt 5 macht den Rest, niemand muss `pdflatex` und `biber` selbst tippen) — und ihr wisst jederzeit, was eure eigenen Gedanken sind und was Vorschläge waren.

Mögliche Folge-Themen (sagt Bescheid, wenn euch eines davon brennt):

- **Dataview-Plugin in Obsidian:** Live-Abfragen über euer Vault („zeig alle offenen TODOs sortiert nach Deadline", „alle KI-Notes ohne Promotion").
- **Multi-Device-Sync:** Vault parallel auf Laptop + Desktop via GitHub oder GitLab.
- **Spezielle Workflows:** Forschungs-Pipeline, Entscheidungs-ADRs mit KI-Unterstützung.

Bei Fragen schreibt mir.

Viele Grüße
Estelle

---

## Vernetzung

- Begleit-Sheets: [[02-prompts]] · [[03-system-erklaerung]]
- Begleitende Teilnehmer-Mail: [[mail-entwurf]]
- Vortrags-Termin: [[2026-05-15-dhbw-alumni-vortrag]]
