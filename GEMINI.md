# Gemini-CLI-Anweisungen für dieses Projekt

Dies ist ein LaTeX-Schreibprojekt im DHBW-Layout. Für Gemini CLI gelten dieselben Projektregeln wie in `AGENTS.md`; lies `AGENTS.md` zu Beginn jeder Sitzung vollständig.

## Thesis-Arbeitsmodus (private Arbeitskopie)

Prüfe zu Beginn jeder Sitzung, ob `thesis/STAND.md` existiert und die Zeile `Arbeitsmodus: produktiv` enthält. Wenn ja, gilt `THESIS-ARBEITSMODUS.md` vollständig und hat für Git, Datenweg und Provenance Vorrang vor den Setup-Regeln in `AGENTS.md`:

1. Mit `git pull --ff-only` synchronisieren, dann `thesis/STAND.md` und `thesis/GLIEDERUNG.md` lesen.
2. Nur die Dateien des aktuellen Auftrags laden.
3. Am Ende jeder Arbeitseinheit den Stand pflegen, eigene Pfade mit den KI-Angaben (`KI-System: Gemini CLI (Google)`, `KI-Arbeitsschritt`, `KI-Beitrag`) committen und zu `origin` hochladen, nie zu `vorlage`.

Will der User den Arbeitsmodus einrichten, folge `KI-SETUP.md`, Abschnitt „Thesis-Arbeitsmodus einrichten“.

## Kompilieren

Wenn der User „kompiliere“, „build“, „render“ oder „PDF erstellen“ sagt, führe die Build-Sequenz aus `AGENTS.md`, Abschnitt „Kompilieren“, aus.
