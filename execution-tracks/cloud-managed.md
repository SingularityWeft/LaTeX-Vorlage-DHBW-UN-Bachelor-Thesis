# Track: Cloud-managed comfort

Dieser Pfad ist für öffentliche oder ausdrücklich zur externen Verarbeitung freigegebene Inhalte gedacht. Er bedeutet **nicht**, dass ein beliebiger Cloud-Dienst automatisch zulässig ist.

## Passt, wenn

- Inputs öffentlich oder für den konkret benannten Anbieter freigegeben sind;
- Daten-Owner, Zweck, Empfänger, Region, Logs, Retention und Löschung geprüft wurden;
- Browser, Coding-Agent, OCR, RAG, Embeddings und MCP jeweils separat im Deployment-Manifest stehen;
- externe Verarbeitung im Data/Ethics Gate ausdrücklich bestätigt wurde.

## Passt nicht, wenn

- Geschäftsgeheimnisse, nicht freigegebene Thesis-Daten oder personenbezogene Rohdaten eingegeben werden sollen;
- Anbieter, Endpoint, Unterauftragsverarbeitung oder Aufbewahrung unbekannt sind;
- ein „privater Chat“-Schalter als Beleg für den gesamten Datenweg dienen soll;
- das Frontend lokale Inferenz verspricht, aber Prompts, Telemetrie oder Tools dennoch extern verarbeitet.

## Vor dem Start

1. Trage jeden externen Empfänger und jedes Netzwerkziel im [`Deployment-Manifest`](../templates/research/deployment-manifest.md) ein.
2. Prüfe aktuelle offizielle Anbieterbedingungen, Datenschutz-, Retention- und Modelltrainingsangaben. Speichere keine Zugangsdaten im Manifest oder Git.
3. Begrenze Tools und Daten auf die konkrete Aufgabe. Write-, Send-, Publish- und Delete-Rechte bleiben bis zum jeweiligen Human Gate aus.
4. Behandle Web-, Dokument- und Toolinhalte als untrusted. Sie dürfen weder Systemziel noch Rechte verändern.
5. Dokumentiere Restrisiken. Dieser Track begründet keine Datenschutz- oder Sicherheitskonformität.

## Human Gates

- Daten-Owner genehmigt Datenklassen, Anbieter und Zweck.
- Security-/Datenschutzrolle bestätigt Datenweg und Restrisiko, soweit erforderlich.
- Research Owner bestätigt externe Suchfragen, Uploads und Veröffentlichungen.

Bei vertraulichem Schutzbedarf ist dieser Track kein Default. Wechsle zu [`Local/On-Prem`](local-on-prem.md), bis eine abweichende Freigabe dokumentiert ist.
