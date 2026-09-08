# Artefaktspezifikation – Onboarding-Assistent v1

## Zweck und Begründung

- **Typ:** Python-CLI und Evaluations-Harness.
- **Problem/Zielgruppe:** Anfänger sollen einen vollständigen, ungefährlichen Research-Zyklus ausführen können.
- **Nicht-Ziele:** GUI, RAG, Datenbank, autonome Tools, Deployment, reale Daten oder allgemeine Modellkompatibilität.
- **Grundlage:** E-001 bis E-006 aus `evidence-log.md`.
- **Designanforderungen:** nur synthetische Fakten; Source IDs; transparente Nicht-Antwort; Dokumentinstruktionen untrusted; getrennte Policy-Signale; Offline-Default; Live nur explizit und eng validiert.
- **Neuheit im Repo:** erste ausführbare Verbindung der bereits dokumentierten Methoden-, Private-Track- und Agentic-Research-Verträge.
- **Erwarteter Beitrag:** Lehrmuster, kein allgemeiner Wirksamkeitsnachweis.

## Verhalten und Grenzen

- **Inputs:** Frage plus `data/documents.json`; optional expliziter Modell-/Runtime-/Endpoint-Vertrag.
- **Outputs:** Text mit `SYN-*`-Source IDs oder transparente Nicht-Antwort; bei Live-Aufruf Rohoutput und Run Record.
- **Funktionen:** deterministische Faktensuche, mehrdimensionale Bewertung, Hashprüfung, Rollenprüfung, enger Chat-Completions-Client, Repeat-Zusammenfassung und Ein-Variablen-Kontrolle.
- **Schnittstellen:** lokale JSON-/Textdateien; optional genau `POST /v1/chat/completions`.
- **Abhängigkeiten:** Python 3 Standardbibliothek; kein Paketdownload.
- **Erlaubte Daten:** ausschließlich die fünf versionierten synthetischen Quellen und synthetische Fragen.
- **Fehler/Abbruch:** Hashdrift, Confirmation-Zugriff durch Executor, unbekannter Endpoint-Pfad, nichtlokales HTTP, fehlendes Egress-Gate, Tool Calling, Streaming, strukturierter/leerer Content, unvollständige Response oder doppelter Run-Record-Pfad stoppen fail-closed.
- **Ausgeschlossen:** Toolausführung, Memory-Schreiben, automatischer Egress, API-Key-Logging, stilles Runtime-Adapterverhalten und automatische Claims.

## Nachweis

- **Demonstration:** `ask` beantwortet die Zugangsfrage mit `SYN-ACCESS-001`.
- **Akzeptanz:** 15 Unit Tests, acht Exploration- und vier Confirmation-Fälle, Hash- und Secret-Prüfung.
- **Exploration:** acht sichtbare Dimensionen; alle müssen einzeln bestehen.
- **Bestätigung:** vier gehashte Fälle durch `evaluator`; keine Rückkopplung.
- **Baseline:** Refusal-only; sicher, aber ohne Aufgaben- oder Quellenabdeckung.
- **Grenzen:** Token-Overlap ist absichtlich klein; keine semantische Retrieval- oder Modellqualitätsaussage.

## Entscheidungen

- **Bestätigt:** Standardbibliothek, CLI, localhost, deterministischer Mock, keine neuen Abhängigkeiten.
- **Offen:** reale Runtime, reales Modell, Anbieter, Latenz-/Kostenbudget, echte Nutzer- und Organisationsevaluation.
- **Version v1:** erster synthetischer SPEC‑05-Slice.
