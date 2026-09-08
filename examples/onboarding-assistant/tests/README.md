# Tests

Aus dem Beispielordner ausführen:

```bash
python3 -m unittest discover -s tests -v
```

Die Tests benötigen weder Modell noch Netzwerk. Sie prüfen Synthetik und Hashes, Offline-Antworten, Nicht-Antwort, Injection-/Memory-Grenzen, Eval-Rollen, lokalen und nichtlokalen Endpoint-Gate, exakte Request-/Response-Felder, fail-closed Tool-/Streaming-/Structured-Output-Reaktionen, secret-freie Records, eindeutige Repeat-IDs, Konfigurationshashes, Streuung und Modell-vs.-Harness-Kontrolle.
