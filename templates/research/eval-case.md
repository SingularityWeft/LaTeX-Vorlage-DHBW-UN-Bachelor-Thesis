# Eval Case

- **Template-Version:** `eval-case-v1`
- **Eval-Case-ID:**
- **Version:**
- **Status:** Entwurf / vorab freigegeben und gesperrt / durchgeführt
- **Stufe:** Exploration / Bestätigung
- **Zugehörige Serien-ID:**

## Zweck und Fall

- **Zu prüfende Aussage oder Fähigkeit:**
- **Methodenpfad und Evaluationsart:** quantitativ / qualitativ / gemischt
- **Abstrakter Input oder geschützte Referenz:**
- **Erwartetes Ergebnis oder bekannte Ground Truth:**
- **Nicht akzeptables Ergebnis:**
- **Vorbedingungen:**

## Bewertung

| Kriterium/Metrik | Richtung oder Skala | Gewicht | Schwelle | Begründung |
|---|---|---:|---:|---|
|  |  |  |  |  |

- **Aggregationsregel:**
- **Umgang mit fehlenden Werten und Crashs:**
- **Qualitative Rubrik und Ankerbeispiele:**
- **Was diese Bewertung nicht objektiv oder allgemein gültig macht:**

## Grader-Vertrag

- **Typ:** deterministisch / menschlich / LLM / gemischt
- **Implementierung oder bewertende Rolle:**
- **Modell und sichtbare Version, falls LLM:**
- **Prompt-/Rubrik-ID, Version und Hash:**
- **Kalibrierungsfälle mit bekannter Ground Truth:**
- **Kalibrierungsergebnis und Abweichungen:**
- **Bekannte Biases und Fehlermuster:**
- **Menschliche Stichprobe, Größe und Auswahlregel:**
- **Regel bei fehlender Kalibrierung:** `inconclusive` oder `human-review`

## Wiederholung

- **Nichtdeterministisch:** ja / nein
- **Geplante Repeats:**
- **Seeds oder Repeat-IDs:**
- **Streuungs- und Stabilitätsauswertung:**
- **Begründete Ausnahme bei Einzelmessung:**

## Zugriff und Sperre

- **Executor darf Fall sehen:** ja / nein / nur abstrakte Metadaten
- **Executor darf Datei schreiben:** nein nach Freigabe
- **Evaluator darf Datei schreiben:** nur neue versionierte Definition vor Serienstart; Ergebnis in Run Record
- **Freigegebener Speicherort:** `evals/exploration/` / `evals/confirmation/`
- **Datei-Hash nach Freigabe:**
- **Freigegeben und gesperrt durch, Datum:**

Jede Änderung an Fall, Input, Ground Truth, Metrik, Rubrik, Grader oder Harness erzeugt eine neue Eval-Version und eine neue Vergleichsserie. Frühere Scores sind dann nicht direkt vergleichbar.

## Ergebnisreferenzen

- **Run-Record-IDs:**
- **Experiment-Record-ID:**
- **Abweichungen vom Plan:**
- **Menschliche Interpretation und Grenzen:**
