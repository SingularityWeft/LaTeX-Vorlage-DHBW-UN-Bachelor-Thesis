# Decision Log – synthetisches Beispiel

## D-001: Lehrartefakt behalten

- **Datum:** 2026-09-08
- **Status:** bestätigt ausschließlich für den synthetischen Repository-Scope
- **Frage:** Soll `source-bound-offline-v1` als Beispiel gegenüber Refusal-only behalten werden?
- **Verantwortliche Rolle:** menschlicher Repository-/Research-Owner; als Rolle dokumentiert, keine Personendaten
- **Option:** als `candidate-keep` in SPEC‑05 aufnehmen.
- **Alternativen:** nur Dokumentation; Refusal-only; produktionsnahes RAG oder Live-Deployment.
- **Evidenz:** E-001 bis E-006, Unit Tests, Exploration und getrennte Confirmation.
- **Begründung:** Der kleine Standardbibliotheksfall verbindet Methode, Quellen, Policy, Evals und Records ohne echte Daten oder Infrastruktur.
- **Unsicherheit:** öffentlicher Holdout, kleine Ground Truth, kein unabhängiger Nutzertest und kein realer Live-Endpoint.
- **Risiken:** Leser könnten Testgrün als Produktions-/Sicherheitsfreigabe missverstehen.
- **Konsequenz:** Warnhinweise, Einzelmetriken und offene Gates bleiben sichtbar; SPEC‑06-CI wird nicht vorgezogen.
- **Review:** nach SPEC‑07-Walkthroughs oder bei jeder Daten-/Prompt-/Harness-/Eval-/Runtime-Änderung.
- **Human Gate:** Lehrartefakt ja; reale Nutzung, Claim und Veröffentlichung nein/offen.

## D-002: Shared On-Prem nicht bereitstellen

- **Status:** bestätigt.
- **Frage:** Soll der Shared-On-Prem-Pfad in SPEC‑05 implementiert werden?
- **Entscheidung:** nur als synthetischer Architektur-Prüffall dokumentieren.
- **Begründung:** Es fehlen reale Owner, Plattform-, IAM-, Netzwerk-, Datenschutz-, Betriebs- und Security-Gates.
- **Konsequenz:** keine Hosts, Endpoints, Modelle, Accounts oder Secrets; Status `nicht freigegeben`.

## Decision Memo

- **Empfehlung:** synthetischen Offline-Fall fortsetzen; Live und Shared On-Prem stoppen bis zu neuen Gates.
- **Evidenz zeigt:** versionierte synthetische Prüfungen und Vertragsgrenzen sind ausführbar.
- **Evidenz zeigt nicht:** reale Sicherheit, Datenschutzkonformität, Wirksamkeit, Usability oder Produktionsreife.
- **Nächste Rolle/Aktion:** Maintainer prüft SPEC‑05-Diff; SPEC‑06 bleibt separater Slice.
