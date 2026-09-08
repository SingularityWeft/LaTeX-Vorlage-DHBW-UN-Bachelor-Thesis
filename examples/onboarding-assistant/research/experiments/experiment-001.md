# Experiment Record – ONBOARDING-EXP-001

- **Serie:** `series-onboarding-offline-v1`
- **Versuch:** 1 von 1
- **Status:** `candidate-keep`
- **Research Program:** `research-program.md`, Version/Hash bei finalem SPEC‑05-Diff geprüft
- **Ausgangscommit:** `5be6afce66980f65e2e9d85ad4f9e30d07e4367a`
- **Hypothese:** Source-bound Offline-Logik erhöht Aufgabenabdeckung gegenüber Refusal-only, ohne Policy-Verletzung.
- **Einzige Änderung:** Artefaktlogik.
- **Erwartung:** alle sichtbaren Einzeldimensionen grün.
- **Allowlist/Tools:** laut Research Program; Python und Hashprüfung, kein Netzwerk.
- **Budget vor Start:** ein Versuch, zwei Offline-Durchläufe, fünf Minuten, null Modellkosten.

## Änderung und Runs

- **Versuch-Referenz:** Datei-/Konfigurationshashes im Research Program; der einschließende fokussierte Git-Commit wird durch die Repository-Historie identifiziert und kann nicht selbstreferenziell in seinem eigenen Inhalt stehen.
- **Geänderte Beispielpfade:** `artifact/`, `research/`, `data/`, `evals/`, `tests/`, `runs/`.
- **Prompt/Harness/Daten/Eval:** jeweils v1 und während der Serie konstant.
- **Abweichung:** kein eigener `experiment/*`-Branch oder Versuch-Commit; dies ist eine dokumentierte SPEC‑05-Lehrdemonstration, kein tatsächlich autorisierter `Bounded autonomous`-Lauf.

| Run | Repeat | Ergebnis | Metriken | Latenz/Kosten | Fehler |
|---|---|---|---|---|---|
| `offline-repeat-01` | `repeat-01` | bestanden | 8/8 Dimensionen | dokumentierter lokaler Python-Lauf / 0 EUR | keiner |
| `offline-repeat-02` | `repeat-02` | bestanden | 8/8 Dimensionen | dokumentierter lokaler Python-Lauf / 0 EUR | keiner |

## Zusammenfassung und Entscheidung

- **Baseline:** Quellen-/Aufgabenabdeckung null, Nicht-Antwort sicher.
- **Kandidat:** alle acht sichtbaren Dimensionen im deterministischen Offline-Test bestanden.
- **Streuung:** null für boolesche Fallwerte; keine stochastische Aussage.
- **Crash-Anteil:** 0/2.
- **Sicherheit:** keine Tool-/Memory-/Netzaktion; simulierte Angriffe werden nicht befolgt.
- **Nicht belegt:** Blindheit des öffentlichen Holdouts, Live-Modellverhalten, reale Sicherheit oder Nutzbarkeit.
- **Entscheidung:** `candidate-keep` als synthetisches Lehrartefakt; Confirmation und menschliches Claim-Gate bleiben getrennt.
- **Nächster Schritt:** einmalige Confirmation durch Evaluator, danach keine Optimierung auf denselben Fällen.
