# Research Program – series-onboarding-offline-v1

- **Status:** freigegeben ausschließlich als synthetischer Offline-Lehrvertrag
- **Serien-ID:** `series-onboarding-offline-v1`
- **Erstellt/festgelegt:** 2026-09-08
- **Reale Einsatzfreigabe:** keine

## Ziel und Vergleich

- **Profile:** DHBW-Thesis, Unternehmensprojekt, Informatikprojekt.
- **Methode:** DSR plus ergänzendes Benchmarking; synthetisch bestätigt.
- **Frage:** Wie werden Quellen- und Sicherheitsgrenzen im festgelegten Fall getrennt sichtbar?
- **Praktisches Ziel:** offline ausführbare CLI mit nachvollziehbaren Records.
- **Hypothese:** Quellengebundene Faktensuche deckt Aufgaben besser ab als Refusal-only, ohne die vorab festgelegten Policy-Grenzen zu verletzen.
- **Baseline:** Refusal-only-v1 auf Ausgangscommit `5be6afce66980f65e2e9d85ad4f9e30d07e4367a`.
- **Signal:** alle acht Explorationsdimensionen grün; danach einmalige Bestätigung.
- **Nicht belegt:** reale Nützlichkeit, Sicherheit, Organisationswirkung oder Modellranking.

## Vergleichsvertrag

- **Einzige Variable:** Artefaktlogik `refusal-only-v1` → `source-bound-offline-v1`.
- **Konstant:** synthetische Daten, Prompt, Harness, Evals, Python-Standardbibliothek und Rollenvertrag.
- **Konfundierung:** Baseline besitzt keine Source-Ausgabe; Aufgaben- und Quellenabdeckung sind erwartbar null. Dieser didaktische Vergleich ist kein Effektgrößen-Nachweis.
- **Typ:** Artefaktvergleich, weder Modell- noch Harnessvergleich.
- **Direkt vergleichbar:** nur diese beiden Logiken auf `onboarding-*-v1`.
- **Nicht vergleichbar:** spätere Live-, Modell-, Prompt-, Daten- oder Eval-Serien.

## Versionen

| Bestandteil | Version | Hash/Referenz | Status in Serie |
|---|---|---|---|
| Baseline | `refusal-only-v1` | Ausgangscommit `5be6afc` | konstant |
| Kandidat | `source-bound-offline-v1` | Python `a60b1d15…2c42e` | einzige Variable |
| Modell/Runtime | aus | kein Modell, Python-Standardbibliothek | konstant |
| Prompt | `onboarding-system-prompt-v1` | `f0fe32eb…02ea` | konstant |
| Harness | `onboarding-harness-v1` | Python `a60b1d15…2c42e` | konstant |
| Daten | `onboarding-data-v1` | `f0e4960c…df35` | gesperrt |
| Exploration | `onboarding-exploration-v1` | `36b63fc2…6bad2` | gesperrt |
| Bestätigung | `onboarding-confirmation-v1` | `6b494891…b4bc8` | gesperrt; Executor blockiert |
| Grader | `deterministic-grader-v1` | Funktion `grade_answer` | konstant |

## Erlaubter Raum

- **Write-Allowlist:** `artifact/onboarding_assistant.py`, `research/experiments/experiment-001.md`, `runs/example-offline/**` innerhalb dieses Beispiels.
- **Read-only:** `data/documents.json`, `artifact/system-prompt-v1.txt`, `evals/exploration/cases.json`, `evals/locked-hashes.json`.
- **Für Executor verboten/ausgeblendet:** `evals/confirmation/cases.json`; alle Pfade außerhalb des Beispiels außer erforderlicher Repository-Anweisung und Regression.
- **Tools:** Python 3, Unit Tests, Hash- und Git-Lesebefehle.
- **Verboten:** Netzwerk, Downloads, Modellaufruf, Deployment, Push, Reset, Datenimport und Rechteänderung.
- **Git:** der Lehr-Record ist Teil des fokussierten SPEC‑05-Commits; kein separater Experiment-Branch, weil kein autonomer Iterationslauf ausgeführt wird. Diese sichtbare Abweichung verhindert einen falschen SPEC‑04-Laufclaim.

## Daten und Netzwerk

- **Schutzbedarf/Track:** öffentlich-synthetisch, vollständig offline.
- **Netzwerkziele:** keine.
- **Datenklassen:** nur `synthetic: true`-Fixtures.
- **Private-Track:** nicht erforderlich für Offline; Live/Shared On-Prem offen.
- **Deployment-Manifest:** `deployment-manifest.md`, nur Offline-Status freigegeben.

## Evaluation und Repeats

- **Exploration:** acht Cases; jede Dimension muss bestehen.
- **Bestätigung:** vier Cases; einmal getrennt, keine Rückkopplung.
- **Grader:** deterministisch, keine LLM-Kalibrierung erforderlich.
- **Nichtdeterministisch:** nein.
- **Repeats:** zwei identische Offline-Records als Integritätsdemonstration; kein Reproduzierbarkeitsclaim aus ihrer Anzahl.
- **Zusammenfassung:** Einzelwerte, Hashgleichheit, identischer Output und Streuung null.

## Endliche Budgets

| Budget | Pro Lauf | Serie | Quelle |
|---|---:|---:|---|
| Artefaktversuche | 1 | 1 | Experiment Record |
| Offline-Eval | höchstens 12 Fälle | 2 vollständige Durchläufe | Testoutput/Records |
| Wall Clock | 60 Sekunden | 5 Minuten | monotone Laufzeit |
| Kosten/Tokens | 0 EUR / 0 Modelltokens | 0 EUR / 0 Modelltokens | kein Modell |
| Rechenressourcen | 1 lokaler Python-Prozess | seriell | Prozessbeobachtung |

## Stopbedingungen

Stop mit `human-review` bei Budgetende, Scope-/Hashdrift, Confirmation-Zugriff durch Executor, Netzwerkversuch, echter Datenklasse, Secret, Tool-/Memory-Aktion oder unklarer Interpretation. Ein technischer Abbruch ist `crash`; eine nicht trennbare Bewertung `inconclusive`.

## Rollen und Gates

- **Research Owner:** didaktische menschliche Rolle; bestätigt nur den synthetischen Lehrvertrag.
- **Executor:** Offline-Testrolle ohne Confirmation-Schreib-/Leserecht.
- **Evaluator:** getrennte Rolle für einmalige Confirmation.
- **Fachreview:** menschliches Repository-Review.
- **Interessenkonflikt:** öffentlich sichtbare Holdout-Fälle; deshalb keine Behauptung unabhängiger Blindbewertung.
- **Start-Gate:** nur synthetische Offline-Serie bestätigt; Evals gehasht, Budgets endlich, Netzwerk aus.
- **Promotion-Gate:** `candidate-keep` als Lehrartefakt möglich; wissenschaftliche oder reale Promotion bleibt offen.
