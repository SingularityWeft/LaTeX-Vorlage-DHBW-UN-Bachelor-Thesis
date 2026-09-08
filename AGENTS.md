# LaTeX-Thesis-Projekt — Konventionen für KI-Tools (Codex / Claude)

Dies ist ein LaTeX-Schreibprojekt im DHBW-Layout (Studiengang Unternehmertum). Halte dich an die folgenden Regeln, wenn du in diesem Verzeichnis arbeitest.

## Setup-Trigger

Wenn der User „Ja, bitte einrichten", „richte die Vorlage ein", „mach das arbeitsfertig" oder ähnlich sagt:

1. Lies `KI-SETUP.md`.
2. Übernimm Profil und Schutzbedarf aus dem Prompt, falls genannt. Frage sonst ausschließlich nach den noch fehlenden Angaben: Profil (`DHBW-Thesis`, `Unternehmensprojekt`, `Informatikprojekt`) und Schutzbedarf (`öffentlich`, `intern`, `vertraulich/Geschäftsgeheimnis`).
3. Führe erst danach den dort beschriebenen profilbewussten Ablauf aus. Bis zum Data/Ethics Gate nur abstrakte oder synthetische Angaben verwenden.
4. `Assist` ist der Safe Default; eine uneindeutige Methode bleibt offen. Kein `Bounded autonomous` ohne den Vertrag aus `AGENTIC-RESEARCH.md` und ein bestätigtes Research Program.
5. Bestehende Dateien und Git-Zustände nicht verändern oder übernehmen. Kein Commit ohne sichtbare Allowlist und Human Gate; niemals automatisch pushen und nie in das öffentliche Vorlagen-Repo `SingularityWeft/LaTeX-Vorlage-DHBW-UN-Bachelor-Thesis` pushen.

Wenn der User das vollständige SecondBrain-System aus dem Vortrag einrichten will, lies zusätzlich `vortrag/anleitungen/README.md` und arbeite die dort verlinkten Sheets in Reihenfolge ab.

## Agentic-Research-Trigger

Wenn der User „Agentic Research“, „Bounded autonomous“, „Experimentierloop“, „Versuchsserie“ oder einen autonomen Research-Lauf anfordert:

1. Lies `AGENTIC-RESEARCH.md`, das freigegebene `research/research-program.md` und die referenzierten Eval Cases vollständig.
2. Ohne freigegebenes Research Program, versionierten Eval Case, bestätigte Daten-/Methoden-Gates und endliche Budgets startet kein Lauf; bleibe in `Assist`.
3. Arbeite nur auf `experiment/<series-id>` und nur in exakt allowlisteten Schreibpfaden. Ein Scope-Verstoß oder versuchter Zugriff auf gesperrte Bestätigungs-Evals stoppt mit `human-review`.
4. Committe jeden Versuch. Ein `discard` wird mit normalem Revert-Commit rückgängig gemacht; kein Reset, Force Push oder Löschen negativer Evidenz.
5. Schreibe für jeden Repeat einen Run Record, auch bei `crash` oder `inconclusive`. Änderungen an Daten, Prompt, Harness oder Eval beginnen eine neue Serien-ID.
6. Die getrennte Evaluator-Rolle führt Bestätigungs-Evals einmal nach Plan aus. Nur ein menschliches Promotion-Gate darf `promoted` setzen; kein automatischer Claim und kein Push.

## Kompilieren

Wenn der User „kompiliere", „build", „render" oder „PDF erstellen" sagt, führe genau diese Sequenz aus:

```bash
pdflatex main.tex
biber main
makeglossaries main
pdflatex main.tex
pdflatex main.tex
```

**Light Variant** (nur reine Textänderung, keine neuen Zitate / kein neues Glossar):

```bash
pdflatex main.tex
```

Nach jedem Build:
- bestätige, dass `main.pdf` existiert und Dateigröße > 0 hat,
- prüfe `main.log` auf neue `Error` / `!`-Zeilen und melde sie,
- ignoriere "Underfull/Overfull hbox" (Layout-Warnungen).

Bei fehlendem `pdflatex` oder `biber`: User auf MacTeX-Installation hinweisen (<https://www.tug.org/mactex/>), nicht weitermachen.

## Git

1. Vor und nach Änderungen `git status --short --branch` prüfen. Bereits geänderte, unversionierte oder gestagte fremde Dateien getrennt dokumentieren und unangetastet lassen.
2. Remotes nur lesen. Zeigt eines auf das öffentliche Vorlagen-Repo, ist jeder Push dorthin verboten; Umbenennen oder Ergänzen eines Remotes braucht eine separate Freigabe.
3. Nur explizit eigene, zuvor aufgelistete Pfade stagen. Pauschales Staging mit `git add -A` oder `git add .` ist verboten.
4. Beim Setup nach `KI-SETUP.md` zuerst die exakte Staging-Allowlist zeigen und die Freigabe abwarten. Danach den gestagten Diff zeigen und für den Commit ein separates Human Gate einholen.
5. Nie automatisch pushen. Ein Push braucht eine ausdrückliche Anweisung und darf niemals in das öffentliche Vorlagen-Repo gehen.

Keine destruktiven Git-Befehle (`reset --hard`, `push --force`, `branch -D`, `clean -f`) ohne explizite Zustimmung.

## Provenance (Akademische KI-Erklärung)

Wenn im Working Directory eine unveränderte Datei `ki-erklaerung.md` existiert: am Sessionende ungefragt einen Eintrag anhängen. War sie bereits vor der Session geändert, bleibt sie ohne Human Gate unangetastet. Format pro Eintrag: Datum · Tool · Aufgabe · Umfang · ggf. importierte externe KI-Quellen (Gemini, GPT etc.) mit Quellenangabe.

Wenn die Datei noch nicht existiert: dem User vorschlagen, sie anzulegen (Vorlage siehe README.md).

## Inhaltliche Eingriffe in .tex-Dateien

- Vor Änderungen die betroffene Datei lesen, nie blind überschreiben.
- Wenn du in einer bestehenden `.tex`-Datei einen ganzen Abschnitt neu schreibst: am Anfang des Abschnitts einen LaTeX-Kommentar einfügen, z. B. `% [KI-Vorschlag YYYY-MM-DD — bitte prüfen]`, damit der User KI-generierte Passagen findet.
- Bei Importen aus anderen KIs (TikZ-Code aus Gemini, Texte aus GPT etc.): direkt im Code/Text einen Kommentar mit Quelle + Datum.

## Stil

- Deutsche Sprache, deutsche Anführungszeichen („..." statt "...").
- Konsistente Verwendung der bereits definierten Glossar-Einträge (`\gls{}`) und Akronyme (`\gls{abk}`).
- Bei Unsicherheit, ob ein Begriff ins Glossar gehört: User fragen.
