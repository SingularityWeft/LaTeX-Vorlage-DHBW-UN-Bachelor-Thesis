# Experiment Record

- **Template-Version:** `experiment-record-v1`
- **Experiment-ID:**
- **Serien-ID:**
- **Versuchsnummer:**
- **Status:** `candidate-keep` / `discard` / `crash` / `inconclusive` / `human-review` / `promoted`

## Vor dem Versuch

- **Research-Program-Version und Hash:**
- **Branch:** `experiment/[Serien-ID]`
- **Ausgangscommit:**
- **Hypothese:**
- **Einzige geplante Änderung:**
- **Erwartetes Signal:**
- **Erlaubte Pfade und Tools:**
- **Verbleibendes Versuchs-/Zeit-/Kostenbudget:**

## Änderung

- **Versuch-Commit:**
- **Tatsächlich geänderte Pfade:**
- **Konfiguration:**
- **Prompt-/Harness-/Daten-/Eval-Version:**
- **Abweichung oder Konfundierung:** keine /

Liegt eine nicht vorab erlaubte Abweichung vor, stoppt der Versuch als `human-review`; die Werte werden nicht mit früheren Scores fortgeschrieben.

## Runs und Einzelwerte

| Run-ID | Repeat-ID/Seed | Ergebnis | Qualitätsmetriken | Latenz | Kosten/Ressourcen | Fehlerstatus |
|---|---|---|---|---:|---:|---|
|  |  |  |  |  |  |  |

## Zusammenfassung

- **Baseline-Werte:**
- **Lagewert:**
- **Streuung:**
- **Min/Max:**
- **Crash-/Fehleranteil:**
- **Stabilitätsgrenze eingehalten:** ja / nein / unklar
- **Qualitative Befunde und Rubrikversion:**
- **Quellen-/Zitationsmetriken, falls relevant:**
- **Komplexitäts-, Kosten-, Sicherheits- und Robustheitsbefund:**
- **Was das Ergebnis nicht belegt:**

## Entscheidung

- **Zustand:**
- **Begründung gegenüber vorab definierten Schwellen:**
- **Menschliche Prüfung erforderlich:** ja / nein
- **Nächste Aktion:** nächster Versuch / Serie stoppen / Bestätigungs-Eval beantragen / Revert / neues Design

### Bei `discard`

- **Normaler Revert-Commit:**
- **Grund für Verwerfung:**
- **Referenzen auf erhaltene Run Records und Rohoutputs:**

Kein Reset, Force Push oder Löschen negativer Evidenz.

### Bei `crash` oder `inconclusive`

- **Fehler beziehungsweise Unklarheit:**
- **Verbrauchtes Budget:**
- **Darf laut Research Program wiederholt werden:** ja / nein
- **Stop- oder Eskalationsentscheidung:**

### Bei `candidate-keep`

- **Kandidatencommit:**
- **Warum nur explorativer Kandidat:**
- **Noch ausstehende Bestätigung:**

### Bei `promoted`

- **Bestätigungs-Run-IDs:**
- **Fach-/Methodenreview:**
- **Human-Gate-Entscheidung, Rolle und Datum:**
- **Geltungsbereich und Claim-Grenzen:**
