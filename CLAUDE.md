# Claude-Code-Anweisungen für dieses Projekt

Dies ist ein LaTeX-Schreibprojekt im DHBW-Layout. Für Claude Code gelten dieselben Projektregeln wie in `AGENTS.md`.

## Setup-Trigger

Wenn der User "Ja, bitte einrichten", "richte die Vorlage ein", "mach das arbeitsfertig" oder ähnlich sagt:

1. Lies `KI-SETUP.md`.
2. Führe den dort beschriebenen Ablauf aus.
3. Bei einer persönlichen Einrichtung: push nie in das öffentliche Vorlagen-Repo `SingularityWeft/LaTeX-Vorlage-DHBW-UN-Bachelor-Thesis`.

## Build-Trigger

Wenn der User "kompiliere", "build", "render" oder "PDF erstellen" sagt, verwende den Skill `.claude/skills/latex-build/SKILL.md`.

## Git und Provenance

- Keine destruktiven Git-Befehle ohne explizite Zustimmung.
- Wenn `ki-erklaerung.md` existiert, am Sessionende einen knappen Eintrag anhängen.
- Bei KI-generierten Textpassagen in `.tex`-Dateien einen Kommentar setzen, damit der User sie später prüfen kann.
