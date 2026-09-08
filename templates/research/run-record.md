# Run Record

- **Template-Version:** `run-record-v1`
- **Run-ID:**
- **Serien-ID:**
- **Experiment-ID:**
- **Repeat-ID:**
- **Seed oder Determinismusangabe:**
- **Status:** `candidate-keep` / `discard` / `crash` / `inconclusive` / `human-review` / `promoted`

> Nach Abschluss ist dieser Record unveränderlich. Korrekturen erfolgen als neuer, verlinkter Record; der ursprüngliche Record bleibt erhalten.

## Identität und Ausführung

- **Start-/Endzeit mit Zeitzone:**
- **Branch und Commit:**
- **Ausführende Rolle:**
- **Evaluator-Rolle, falls Bestätigung:**
- **Autonomiestufe:** Assist / Co-execute / Bounded autonomous
- **Research-Program-Version und Hash:**

## Konfiguration und Inputs

- **Inputs in abstrakter Form oder geschützte Referenzen:**
- **Artefakt-/Konfigurationsversion:**
- **Modell-ID und sichtbare Version:**
- **Runtime/Provider und Version:**
- **Prompt-ID, Version und Hash:**
- **Harness-ID, Version und Hash:**
- **Daten-ID, Version und Hash:**
- **Eval-Case-ID, Version und Hash:**
- **Grader-ID, Version und Kalibrierungsnachweis:**
- **Veränderte Variable dieser Serie:**
- **Konstant gehaltene Faktoren:**

## Umgebung

- **Betriebssystem/Architektur:**
- **Relevante Tool- und Dependency-Versionen:**
- **Hardware/Ressourcenklasse:**
- **Netzwerkmodus und erlaubte Ziele:**
- **Abweichungen von der geplanten Umgebung:**

## Ergebnis

- **Rohoutput-Referenz und Zugriffsklasse:**
- **Agenten-Trajektorie oder Toolereignis-Referenz:**
- **Erzeugte Artefakte mit Pfad/Hash:**
- **Quantitative Einzelmetriken:**
- **Qualitative Bewertung und Rubrikversion:**
- **Quellen-/Zitationsmetriken:**
- **Schwelle erreicht:** ja / nein / unklar
- **Kurzinterpretation ohne neuen Claim:**

## Ressourcen

- **Wall-Clock-Latenz:**
- **Modell-/Tool-Latenz:**
- **Input-/Output-Tokens oder Anfragen:**
- **Kosten mit Währung:**
- **CPU/GPU/RAM/sonstige Ressourcen:**
- **Verbleibendes Serienbudget:**

## Fehler und Grenzen

- **Exit-/Fehlerstatus:**
- **Fehlermeldung in minimierter Form:**
- **Crash-Ursache:**
- **Fehlende oder unvollständige Outputs:**
- **Abweichung, Konfundierung oder Validitätsgrenze:**
- **Stopbedingung ausgelöst:** keine / welche

## Daten, Traces und Aufbewahrung

- **Schutzbedarf:**
- **Enthält dieser Record Rohdaten:** nein / Ausnahme mit Gate
- **Secret-/Personenbezug-Prüfung:** bestanden / human-review
- **Geschützter Speicherort für Rohoutput/Trace:**
- **Zugriffsrollen:**
- **Retention und Lösch-/Archivregel:**
- **Öffentliches Git zulässig:** ja / nein

Traces enthalten keine Secrets und nur Ereignisse, die für Reproduktion oder Sicherheitsprüfung erforderlich sind. Vertrauliche Inhalte werden nur referenziert und niemals in das öffentliche Git geschrieben.

## Abschluss und Integrität

- **Finaler Zustand und Begründung:**
- **Zugehöriger Experiment Record:**
- **Vorheriger/ersetzter Record bei Korrektur:**
- **Record-Hash nach Abschluss:**
- **Geprüft durch und Datum:**
