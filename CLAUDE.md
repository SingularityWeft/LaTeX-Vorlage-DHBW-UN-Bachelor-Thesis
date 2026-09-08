# Claude-Code-Anweisungen für dieses Projekt

Dies ist ein LaTeX-Schreibprojekt im DHBW-Layout. Für Claude Code gelten dieselben Projektregeln wie in `AGENTS.md`.

## Setup-Trigger

Wenn der User "Ja, bitte einrichten", "richte die Vorlage ein", "mach das arbeitsfertig" oder ähnlich sagt:

1. Lies `KI-SETUP.md`.
2. Übernimm ein genanntes Profil und einen genannten Schutzbedarf. Frage nur nach fehlenden Angaben: Profil (`DHBW-Thesis`, `Unternehmensprojekt`, `Informatikprojekt`) und Schutzbedarf (`öffentlich`, `intern`, `vertraulich/Geschäftsgeheimnis`).
3. Führe dann den profilbewussten Ablauf aus. Nutze bis zum Data/Ethics Gate nur abstrakte oder synthetische Angaben; `Assist` ist der Safe Default und eine uneindeutige Methode bleibt offen.
4. Verändere keine bestehenden Dateien oder Git-Zustände. Kein Commit ohne sichtbare Allowlist und Human Gate; nie automatisch und nie in das öffentliche Vorlagen-Repo pushen.

## Build-Trigger

Wenn der User "kompiliere", "build", "render" oder "PDF erstellen" sagt, verwende den Skill `.claude/skills/latex-build/SKILL.md`.

## Git und Provenance

- Keine destruktiven Git-Befehle ohne explizite Zustimmung.
- Remotes beim Setup nur lesen; das öffentliche Vorlagen-Remote bleibt push-gesperrt.
- Nur eigene, einzeln aufgelistete Pfade stagen. `git add -A` und `git add .` sind verboten.
- Staging und Commit benötigen getrennte Human Gates; nie automatisch pushen.
- Wenn eine unveränderte `ki-erklaerung.md` existiert, am Sessionende einen knappen Eintrag anhängen. Eine bereits vor der Session geänderte Datei bleibt ohne Human Gate unangetastet.
- Bei KI-generierten Textpassagen in `.tex`-Dateien einen Kommentar setzen, damit der User sie später prüfen kann.
