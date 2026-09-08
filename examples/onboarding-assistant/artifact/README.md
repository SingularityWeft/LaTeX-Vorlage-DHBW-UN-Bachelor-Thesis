# Artefakt

`onboarding_assistant.py` ist eine Python-Standardbibliotheks-CLI mit drei Grenzen:

1. `ask` und `offline-eval` sind deterministisch und öffnen kein Netzwerk.
2. `live` benötigt ein ausdrückliches Live-Gate, validiert den engen `/v1/chat/completions`-Vertrag fail-closed und folgt weder Redirects noch impliziten Proxys.
3. Die CLI führt keine Modell-Toolaufrufe aus, schreibt kein Agent Memory und trifft keine Freigabeentscheidung.

`system-prompt-v1.txt` ist versioniert und verlangt Source IDs, transparente Nicht-Antwort und die Trennung von Dokumentinhalt und Instruktion. Eine Änderung an Prompt oder Harness beginnt eine neue Vergleichsserie.
