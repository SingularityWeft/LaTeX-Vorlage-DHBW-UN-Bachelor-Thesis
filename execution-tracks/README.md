# Ausführungspfad wählen

## Welcher Weg passt?

Wähle den Pfad nach dem **schutzbedürftigsten Input**, nicht nach Bequemlichkeit. „Lokal“ beschreibt nur einzelne Verarbeitungsschritte und ist kein Sicherheitsnachweis für den Gesamtworkflow.

| Ausgangslage | Sicherer Start | Was vor echten Daten passieren muss |
|---|---|---|
| ausschließlich öffentliche, freigegebene Inhalte | [`Cloud-managed comfort`](cloud-managed.md) | Anbieter, Datenweg, Aufbewahrung und Freigabe prüfen |
| interne Inhalte, die vor externer Verarbeitung wirksam redigiert werden können | [`Hybrid-redacted`](hybrid-redacted.md) | Redaktionsplan, Reidentifikationsrisiko und Egress-Gate bestätigen |
| vertrauliche Inhalte oder Geschäftsgeheimnisse | [`Local/On-Prem`](local-on-prem.md) | vollständigen Private-Track-Preflight und Deployment-Manifest freigeben |

Bei unklarem Schutzbedarf gilt `Local/On-Prem` als Startpunkt, externe Verarbeitung bleibt aus und ein Mensch entscheidet. Ein sichererer Pfad ist immer zulässig; ein weniger restriktiver Pfad benötigt eine dokumentierte Freigabe.

## Gemeinsame Regeln

Jeder Pfad benötigt:

1. den [`Data/Ethics Check`](../templates/research/data-ethics-check.md);
2. ein ausgefülltes [`Deployment-Manifest`](../templates/research/deployment-manifest.md);
3. eine Data-Flow-Tabelle für alle Inputs, Zwischenprodukte, Logs, Embeddings und Backups;
4. benannte Owner, Aufbewahrung, Löschweg und Restrisiken;
5. getrennte Read-, Write-, Network- und Credential-Rechte;
6. ein menschliches Gate vor Datenimport, Egress, Veröffentlichung oder Rechteausweitung.

Ein Coding-Agent, Browser, OCR-Dienst, MCP-Server, Embedding-Dienst oder Telemetriekanal ist jeweils ein eigener Verarbeitungsschritt. Lokale Modellinferenz macht einen cloudbasierten Agenten oder ein externes Frontend nicht lokal.

## Sofort stoppen

Stoppe mit `human-review`, wenn ein Datenweg, Empfänger, Tool, Netzwerkziel, Log, Speicherort oder Löschweg fehlt; wenn ein untrusted Dokument neue Anweisungen erteilt; oder wenn privater Datenzugriff und unbeschränkte externe Kommunikation gleichzeitig möglich wären.

Die verbindlichen Sicherheitsgrenzen stehen in [`SECURITY.md`](../SECURITY.md). Für den lokalen technischen Preflight siehe [`LOCAL-PRIVATE-SETUP.md`](../LOCAL-PRIVATE-SETUP.md).
