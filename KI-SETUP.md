# KI-Setup: "Ja, bitte einrichten"

Diese Datei beschreibt den Zielzustand, wenn ein lokaler KI-Agent dieses Repo geklont hat und der User danach sagt:

```text
Ja, bitte einrichten.
```

Gilt auch für ähnliche Formulierungen wie "richte die Vorlage ein", "mach das arbeitsfertig" oder "setup bitte".

Diese Datei ist für persönliche Arbeitskopien gedacht. Wenn du gerade das öffentliche Vorlagen-Repo selbst wartest, gelten die normalen Maintainer-Git-Regeln des Projekts.

## Scope

Dieses Setup macht das LaTeX-Thesis-Projekt arbeitsfertig. Es richtet keinen kompletten Obsidian-Vault ein. Für das vollständige SecondBrain-System zuerst `vortrag/anleitungen/01-start-ki-einrichten.md` und `vortrag/anleitungen/02-prompts.md` lesen.

Ein reines Chatmodell ohne lokalen Datei- und Terminalzugriff kann diese Schritte nur erklären, nicht ausführen. Dann den User darauf hinweisen.

## Ablauf für den KI-Agenten

1. **Orientieren**
   - Lies `README.md`.
   - Lies die passende Agenten-Datei: `AGENTS.md` für Codex/GPT-basierte Coding-Agenten, `CLAUDE.md` für Claude Code.
   - Prüfe mit `git status -sb`, ob der Arbeitsbaum sauber ist.

2. **Template-Remote absichern**
   - Prüfe `git remote -v`.
   - Wenn `origin` auf `https://github.com/SingularityWeft/LaTeX-Vorlage-DHBW-UN-Bachelor-Thesis.git` zeigt: nicht dorthin pushen.
   - Benenne dieses Remote in `vorlage` um:
     ```bash
     git remote rename origin vorlage
     ```
   - Erkläre dem User danach kurz, dass ein eigenes privates GitHub-/GitLab-Remote später separat hinzugefügt werden kann.
   - Lösche `.git` nicht automatisch. Ein kompletter History-Reset braucht eine explizite Zusatzfreigabe.

3. **KI-Erklaerung anlegen**
   - Wenn `ki-erklaerung.md` noch fehlt, lege sie nach der Vorlage aus `README.md` an.
   - Füge einen ersten Eintrag für die heutige Einrichtung hinzu.

4. **Personalisierung vorbereiten**
   - Suche die offenen Platzhalter:
     ```bash
     rg -n "%% PLACEHOLDER|PLACEHOLDER" main.tex README.md
     ```
   - Erfinde keine persönlichen Daten. Wenn Titel, Name, Matrikelnummer, Kurs, Betreuer oder Abgabedatum fehlen, lass die Platzhalter stehen und liste sie im Abschlussbericht.

5. **LaTeX-Toolchain prüfen**
   - Prüfe:
     ```bash
     pdflatex --version
     biber --version
     makeglossaries --version
     ```
   - Wenn ein Tool fehlt: nicht builden. Verweise auf MacTeX bzw. TeX Live und sage, welcher Befehl fehlt.

6. **Ersten Build ausführen**
   - Wenn alle Tools vorhanden sind, führe die volle Build-Sequenz aus:
     ```bash
     pdflatex main.tex
     biber main
     makeglossaries main
     pdflatex main.tex
     pdflatex main.tex
     ```
   - Prüfe danach, dass `main.pdf` existiert und größer als 0 Byte ist.
   - Prüfe `main.log` auf echte Fehlerzeilen (`Error`, `!`). Underfull/Overfull-Hinweise nur kurz als Layout-Warnungen einordnen.

7. **Lokales Git sichern**
   - Wenn Dateien geändert wurden, mache ein lokales Commit:
     ```bash
     git add -A
     git commit -m "chore: initialise personal thesis workspace"
     ```
   - Nur pushen, wenn ein eigenes Remote konfiguriert ist. Nie in das öffentliche Vorlagen-Repo pushen.

8. **Abschlussbericht**
   - Melde knapp:
     - ob `main.pdf` gebaut wurde,
     - ob `ki-erklaerung.md` angelegt wurde,
     - welches Remote aktiv ist,
     - welche Platzhalter noch vom User auszufüllen sind,
     - welcher nächste sinnvolle Prompt ist, z. B. "Passe Deckblatt und Metadaten mit meinen Daten an."
