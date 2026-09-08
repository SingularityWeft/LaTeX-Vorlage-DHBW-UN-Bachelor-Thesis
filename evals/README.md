# Eval-Verzeichnisvertrag

Dieses Verzeichnis trennt Entwicklung und Bestätigung. Lege Eval Cases aus [`../templates/research/eval-case.md`](../templates/research/eval-case.md) vor dem Lauf an und versioniere sie.

## Struktur

```text
evals/
├── README.md
├── exploration/     # sichtbare Entwicklungs-Evals
└── confirmation/    # gesperrte Bestätigungs-Evals
```

Die Unterordner werden erst angelegt, wenn ein persönliches Research Program konkrete Eval Cases definiert. Dieses öffentliche Template enthält keine echten Projekt-, Personen- oder Unternehmensdaten.

## Exploration

- Die ausführende Rolle darf Explorationsfälle sehen und ausführen.
- Nach Serienstart sind Definition, Input, Ground Truth, Metrik, Rubrik, Grader und Harness versioniert und unveränderlich.
- Eine Änderung startet eine neue Serien-ID; frühere Scores werden als nicht direkt vergleichbar markiert.
- Ein besserer Explorationsscore erzeugt höchstens `candidate-keep`, keinen wissenschaftlichen Claim.

## Bestätigung

- Bestätigungsfälle werden vor der Vergleichsserie freigegeben, gehasht und gesperrt.
- Die ausführende Rolle hat keinen Schreibzugriff auf `confirmation/` und erhält möglichst weder Fälle noch erwartete Antworten in ihrem Arbeitskontext.
- Nur die getrennte Evaluator-Rolle führt die im Research Program vorgesehene Bestätigung einmalig aus.
- Das Ergebnis wird in einem Run Record gespeichert, nicht in die Eval-Definition zurückgeschrieben.
- Bestätigungsfeedback wird nicht zur weiteren Optimierung genutzt. Jede Folgeänderung beginnt eine neue Vergleichsserie.
- Eine versuchte Änderung oder unzulässige Einsicht stoppt den Lauf mit `human-review`.

## Rubriken und Grader

Qualitative menschliche Rubriken sind zulässig, aber keine objektiven Benchmarks. Eval Case und Research Program dokumentieren Kriterien, Skala, Version, Bewertungsrolle und Unsicherheit.

Bei einem LLM-Grader sind Modell/Version, Prompt/Rubrik, Kalibrierungsfälle mit bekannter Ground Truth, bekannte Biases und eine menschliche Stichprobe Pflicht. Ohne Kalibrierung lautet der Zustand `inconclusive` oder `human-review`.

## Schutz und Änderungskontrolle

- Keine Secrets oder vertraulichen Rohdaten in öffentlichen Eval-Dateien.
- Vertrauliche Inputs nur mit freigegebenem SPEC-03-Track.
- Zugriff und Dateirechte vor jedem Lauf prüfen und im Research Program dokumentieren.
- Korrekturen erfolgen als neue Version; bestehende freigegebene Definitionen bleiben referenzierbar.
