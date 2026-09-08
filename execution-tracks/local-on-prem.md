# Track: Local/On-Prem

Dieser Pfad ist der sichere Start für `vertraulich/Geschäftsgeheimnis`. Alle externen Web-, MCP-, OCR-, Embedding-, Logging- und Agentenpfade bleiben aus, bis der vollständige Private-Track-Preflight menschlich freigegeben ist.

## Zwei verschiedene Betriebsformen

### Desktop-local

Modell und Runtime laufen auf einem einzelnen kontrollierten Rechner und binden standardmäßig nur an Loopback. Dieser Pfad eignet sich für einen benannten Owner und begrenzte lokale Forschung. Er ist keine Enterprise-Plattform.

### Shared On-Prem

Mehrere berechtigte Personen greifen über eine intern betriebene, gehärtete Serverumgebung zu. Erforderlich sind mindestens eigene Service-Identitäten, Authentisierung/Autorisierung, TLS, Netzwerksegmentierung, Patch- und Backup-Verantwortung, Monitoring, Kapazitätsplanung und Incident-Prozess. Ein Desktop-Tool wird nicht durch Freigabe im LAN zu einer belastbaren Unternehmensplattform.

## Was „lokal“ nicht automatisch umfasst

- Ein cloudbasierter Coding-Agent oder Browser bleibt extern, auch wenn er einen lokalen Modellendpoint aufruft.
- Remote-MCP, externe OCR, externe Embeddings, Telemetrie, DNS-Auflösung und Backups können Daten oder Metadaten ausleiten.
- Modellgewichte, Runtime, Plugins und Container benötigen Herkunfts-, Hash- und Lizenzprüfung.
- Loopback schützt nicht vor überprivilegierten lokalen Prozessen, Prompt Injection, Memory Poisoning oder unsicheren Logs.

## Start-Gate

- [ ] [`Deployment-Manifest`](../templates/research/deployment-manifest.md) vollständig, einschließlich Data Flow und Restrisiken
- [ ] Daten-Owner, System-Owner, Security-/Datenschutzrolle und Research Owner benannt
- [ ] Modell, Runtime und Artefakte mit Version, Hash/Digest, Herkunft und Lizenz geprüft
- [ ] Endpoint nur an freigegebene Interfaces gebunden; Desktop standardmäßig `127.0.0.1`
- [ ] Read-, Write-, Network-, Credential- und Admin-Rechte einzeln geprüft
- [ ] Browser, Remote-MCP, externe OCR/RAG/Embeddings und Cloudmodelle aus
- [ ] Logs, Memory, Run Records, Backups, Retention und Löschweg bestätigt
- [ ] untrusted Inputs isoliert; Dokumentinstruktionen können Ziel und Rechte nicht ändern
- [ ] synthetischer Endpoint- und Negativtest bestanden
- [ ] menschliche Freigabe mit Restrisiken dokumentiert

Fehlt ein Punkt, werden keine vertraulichen Inputs importiert. Der Agent bleibt in `Assist`; ein Lauf stoppt bei `human-review`.

Die reproduzierbaren Desktop- und On-Prem-Prüfschritte stehen in [`LOCAL-PRIVATE-SETUP.md`](../LOCAL-PRIVATE-SETUP.md). Ein datiertes, nicht empfehlendes Modellbeispiel steht unter [`models/examples-2026-09.md`](../models/examples-2026-09.md).

Zwei vollständig ausgefüllte, ausschließlich synthetische Manifest-Prüffälle dokumentiert [`verified-manifest-examples.md`](verified-manifest-examples.md). Nur der Desktop-Endpoint wurde real ausgeführt; das On-Prem-Beispiel bleibt ausdrücklich nicht freigegeben.
