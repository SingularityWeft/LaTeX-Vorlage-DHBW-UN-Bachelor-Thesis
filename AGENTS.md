# LaTeX-Thesis-Projekt — Konventionen für KI-Tools (Codex / Claude)

Dies ist ein LaTeX-Schreibprojekt im DHBW-Layout (Studiengang Unternehmertum). Halte dich an die folgenden Regeln, wenn du in diesem Verzeichnis arbeitest.

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

Versioniere am Sessionende automatisch:
1. `git status` prüfen.
2. Bei uncommitted Änderungen: `git add -A` + `git commit -m "<aussagekräftige Nachricht>"` mit `Co-Authored-By:`-Trailer.
3. Falls Remote konfiguriert: `git push`. Bei Auth-Fehler: stoppen und User informieren.

Keine destruktiven Git-Befehle (`reset --hard`, `push --force`, `branch -D`, `clean -f`) ohne explizite Zustimmung.

## Provenance (Akademische KI-Erklärung)

Wenn im Working Directory eine Datei `ki-erklaerung.md` existiert: am Sessionende ungefragt einen Eintrag anhängen. Format pro Eintrag: Datum · Tool · Aufgabe · Umfang · ggf. importierte externe KI-Quellen (Gemini, GPT etc.) mit Quellenangabe.

Wenn die Datei noch nicht existiert: dem User vorschlagen, sie anzulegen (Vorlage siehe README.md).

## Inhaltliche Eingriffe in .tex-Dateien

- Vor Änderungen die betroffene Datei lesen, nie blind überschreiben.
- Wenn du in einer bestehenden `.tex`-Datei einen ganzen Abschnitt neu schreibst: am Anfang des Abschnitts einen LaTeX-Kommentar einfügen, z. B. `% [KI-Vorschlag YYYY-MM-DD — bitte prüfen]`, damit der User KI-generierte Passagen findet.
- Bei Importen aus anderen KIs (TikZ-Code aus Gemini, Texte aus GPT etc.): direkt im Code/Text einen Kommentar mit Quelle + Datum.

## Stil

- Deutsche Sprache, deutsche Anführungszeichen („..." statt "...").
- Konsistente Verwendung der bereits definierten Glossar-Einträge (`\gls{}`) und Akronyme (`\gls{abk}`).
- Bei Unsicherheit, ob ein Begriff ins Glossar gehört: User fragen.
