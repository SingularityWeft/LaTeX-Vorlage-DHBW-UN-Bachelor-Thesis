# Project Brief – synthetischer Onboarding-Assistent

## Orientierung

- **Profile:** gemeinsamer Fall für DHBW-Thesis, Unternehmensprojekt und Informatikprojekt
- **Methode:** DSR plus ergänzendes Benchmarking, synthetisch bestätigt
- **Autonomie:** `Assist`; einzelne Offline-Prüfung als `Co-execute`
- **Schutzbedarf:** öffentlich-synthetisch; Data/Ethics Gate nur dafür bestätigt

## Problem und Kontext

- **Problem:** Anfänger sehen bei KI-Beispielen häufig nur eine Antwort, nicht den Weg von Quelle, Sicherheitsgrenze und Eval zur menschlichen Entscheidung.
- **Belegte Ausgangslage:** Die Root-Verträge verlangen Source-/Eval-Trennung, Human Gates und sichere Datenwege; der neue Fall macht diese Regeln ausführbar.
- **Betroffene Rollen:** Lernende, ausführende Rolle, getrennte Evaluator-Rolle und Research Owner – alle nur synthetisch benannt.
- **Baseline:** eine transparente Nicht-Antwort auf jede Frage; sicher, aber ohne Aufgabenabdeckung.
- **Relevanz:** Ein ungefährlicher, offline reproduzierbarer Fall verbindet die bisherigen Dokumentverträge.

## Ziel und Ergebnisse

- **Praktisches Ziel:** Fragen aus fünf synthetischen Quellen mit Source IDs beantworten oder transparent verweigern.
- **Erkenntnisziel:** Beobachten, welche Designkontrollen in den festgelegten Fällen Quellen- und Policy-Fehler sichtbar machen.
- **Artefakt:** Standardbibliotheks-CLI, Tests, Evals und Run Records.
- **Wissensbeitrag:** ein eng begrenztes Lehrmuster, kein Nachweis allgemeiner Wirksamkeit.
- **Nicht-Ziele:** Produktion, RAG, GUI, reale Daten, Runtime-Empfehlung, Serverbereitstellung oder Sicherheitszertifizierung.

## Evidenz und Theorie

- **Grundlage:** Methoden-/Autonomierouter, DSR-Zyklus, Agentic-Research-Vertrag und Security Policy dieses Repositories.
- **Geprüfte Quellen:** siehe `evidence-log.md`.
- **Lücke:** reale Nutzerverständlichkeit wird erst in SPEC‑07 unabhängig geprüft.

## Evaluation und Entscheidung

- **Aussage:** Für die versionierten synthetischen Fälle sind Belege, Nicht-Antwort und vier Sicherheitsgrenzen getrennt prüfbar.
- **Demonstration:** Offline-Frage erzeugt Antwort mit Source ID.
- **Exploration:** acht sichtbare Fälle.
- **Bestätigung:** vier vorab gehashte Fälle, getrennte Evaluator-Rolle.
- **Erfolg:** alle Einzeldimensionen grün; keine Hash-, Rollen-, Secret- oder Netzabweichung.
- **Stop:** Scope-, Hash-, Egress-, Tool-, Memory- oder Rechteabweichung.
- **Entscheidung:** Beispiel als Lehrartefakt behalten, ohne Einsatzclaim.

## Grenzen, Risiken und Gates

- **Risiken:** sichtbarer Holdout, kleine regelbasierte Ground Truth, keine reale Modell- oder Nutzerstudie.
- **Geltung:** nur Dateien, Versionen und synthetische Fälle dieses Ordners.
- **Gates:** Bestätigung durch getrennte Rolle; Claims und jede reale Nutzung menschlich prüfen.
- **Nächste Aktion:** Unit Tests und Offline-Eval ausführen.
