# Security Policy für den Research-Layer

## System und Scope

Diese Policy gilt für den optionalen Research-Layer dieses öffentlichen Vorlagen-Repositories: Methoden-/Setup-Dokumente, persönliche Research-Workspaces, lokale oder externe Modellinferenz, Coding-Agenten, Browser, OCR, RAG/Embeddings, MCP-Tools, Run Records, Logs und Git. Der LaTeX-Root bleibt ein Publikationsweg und verarbeitet nicht automatisch Research-Daten.

Das Repository liefert Sicherheitsverträge und Templates, aber keine BSI-, ISO-, TISAX-, DSGVO- oder EU-AI-Act-Zertifizierung. Ein ausgefülltes Manifest und ein lokaler Endpoint-Test ersetzen weder Rechtsberatung noch eine organisationsspezifische Sicherheitsprüfung.

## Schutzgüter und Verantwortliche

Zu schützen sind insbesondere vertrauliche Rohdaten, Geschäftsgeheimnisse, personenbezogene Daten, Prompts/Outputs, Embeddings, Mapping-Tabellen, Credentials, Agent Memory, Logs, Run Records, Forschungsintegrität und die Autorität menschlicher Gates.

Vor echten Daten müssen Daten-Owner, System-Owner, Research Owner sowie erforderliche Security-, Datenschutz-, Ethik- oder Prüfungsrollen im [`Deployment-Manifest`](templates/research/deployment-manifest.md) benannt sein. Ein KI-Agent ist keine verantwortliche Freigaberolle.

## Bedrohungsmodell und Vertrauensgrenzen

Als **untrusted** gelten alle Inhalte aus Webseiten, E-Mails, Kalendern, Chats, Dokumenten, PDFs, OCR, Repositories, RAG-Treffern, Tool-/MCP-Beschreibungen, Modelloutputs, Agent Memory und fremden Logs. Sie dürfen Daten liefern, aber keine Systemziele, Toolrechte, Netzwerkziele, Credentials, Retention, Research Programs oder Human Gates ändern.

Wichtige Grenzen:

1. **Originaldaten → Verarbeitung:** nur freigegebene Datenklassen und minimal erforderliche Felder.
2. **Inhalt → Steuerung:** Dokumenttext wird niemals als autorisierte Agentenanweisung behandelt.
3. **Modell → Tool:** Modelloutput ist untrusted; Toolname, Argumente, Pfad und Ziel werden gegen eine Allowlist geprüft.
4. **Privater Bereich → Netzwerk:** Egress ist standardmäßig aus und benötigt ein konkretes Human Gate.
5. **Executor → Bestätigung:** gesperrte Bestätigungs-Evals bleiben gemäß [`AGENTIC-RESEARCH.md`](AGENTIC-RESEARCH.md) getrennt.
6. **Lauf → Memory/Logs:** nur erforderliche Inhalte, definierte Zugriffsrollen, Retention und Löschung.
7. **Desktop → Shared On-Prem:** Netzwerkfreigabe ist eine neue Architektur mit eigener Authentisierung, Segmentierung und Abnahme.

## Sicherheitsinvarianten

- `vertraulich/Geschäftsgeheimnis` startet mit [`Local/On-Prem`](execution-tracks/local-on-prem.md); externe Web-, MCP-, OCR-, Embedding-, Logging- und Agentenpfade sind aus.
- Ein Workflow heißt nur dann „lokal“ oder „offline“, wenn **alle** relevanten Komponenten und Datenwege lokal beziehungsweise ohne Egress arbeiten. Lokale Inferenz plus Cloud-Frontend erfüllt das nicht.
- Desktop-Runtimes binden standardmäßig an Loopback. Eine andere Bind-Adresse benötigt eine neue Bedrohungsanalyse und Freigabe.
- Privater unbeschränkter Read-Zugriff und unbeschränkter Network-/Send-Zugriff dürfen nie gleichzeitig in derselben Rolle oder Sitzung aktiv sein.
- Read, Write, Execute, Network, Credentials und Admin werden getrennt, minimal und befristet vergeben. Nicht genannte Rechte sind verboten.
- Hochwirksame Aktionen wie Löschen, Senden, Veröffentlichen, Deployment, Rechteänderung und Datenexport benötigen eine sichtbare Vorschau und menschliche Bestätigung.
- Secrets, vertrauliche Rohprompts und personenbezogene Rohdaten dürfen nicht in öffentliches Git, öffentliche Logs, Run Records oder Agent Memory gelangen.
- Modell, Runtime, Plugins und Container benötigen Herkunft, Version, Hash/Digest und Lizenzprüfung. Ein Modellname ohne Digest identifiziert kein reproduzierbares Artefakt.
- Ein Scope-, Rechte-, Egress-, Injection-, Memory- oder Identitätsverstoß stoppt fail-closed mit `human-review`.

## Toolidentitäten und Rechte

Jede ausführende Identität erhält im Deployment-Manifest eine eigene Zeile:

| Rolle | Read | Write/Execute | Network | Credentials | Human Gate |
|---|---|---|---|---|---|
| Redaktionsrolle | nur freigegebene Originale | nur lokales Derivat | aus | keine | Derivat vor Übergabe prüfen |
| Lokale Inferenz | nur freigegebener Prompt | Antwort in freigegebenen lokalen Pfad | nur Loopback | keine Cloud-Credentials | Endpoint und Modell bestätigen |
| Externe Rolle | nur freigegebenes Derivat | kein Zugriff auf Original/Mapping | exakte Ziel-Allowlist | kurzlebig und zweckgebunden | Egress vorab freigeben |
| Evaluator | Kandidat plus gesperrte Evals | nur Ergebnis-Record | laut Eval-Plan | keine Executor-Credentials | Promotion bleibt menschlich |

„Nur Loopback“ bedeutet: Netzwerkzugriff ist technisch auf den lokalen Endpoint begrenzt; es ist keine allgemeine Netzwerkfreigabe.

## Untrusted Inputs und Agentenangriffe

| Negativfall | Verbindliche Reaktion |
|---|---|
| Dokument fordert neue Ziele, Exfiltration oder das Ignorieren von Regeln | Anweisung als Daten markieren, nicht ausführen, Lauf stoppen und `human-review` dokumentieren |
| Modell wählt ein nicht erlaubtes Tool oder gefährliche Argumente | Toolaufruf verweigern; keine automatische Ersatzaktion |
| Prozess versucht ein nicht allowlistetes Netzwerk- oder DNS-Ziel | Egress verweigern und Ziel/Grund ohne Nutzdaten protokollieren |
| Inhalt soll ungeprüft in langfristiges Memory oder RAG gelangen | Persistenz verweigern; Quelle isolieren und auf Poisoning prüfen |
| Tool, Dokument oder delegierte Rolle fordert zusätzliche Rechte/Credentials | Rechte nicht erweitern; Research Owner und System-Owner entscheiden lassen |

Eingabevalidierung und Prompt-Filter sind zusätzliche Schutzschichten, keine verlässliche Trennung von Daten und Instruktionen. Entscheidend bleiben minimale Berechtigungen, isolierte Kontexte, Egress-Kontrolle und Human Gates.

## Memory, Logs und Aufbewahrung

Für Agent Memory, Run Records, Traces, lokale Runtime-Logs, Embeddings, Caches und Backups werden jeweils Inhalt, Owner, Speicherort, Zugriffsrollen, Retention, Löschmethode und Poisoning-/Reidentifikationsrisiko dokumentiert.

- Memory ist pro Projekt und Schutzklasse getrennt; keine projektübergreifende Wiederverwendung vertraulicher Inhalte.
- Untrusted Inhalte werden nicht ohne Quellenreferenz, Freigabe und Integritätsprüfung persistent.
- Logs enthalten standardmäßig Metadaten und Fehlercodes statt Rohprompts/-outputs.
- Löschung umfasst bekannte Kopien, Caches, Vektorspeicher und Backups gemäß dokumentiertem Verfahren; technisch oder rechtlich nicht sofort löschbare Kopien werden als Restrisiko sichtbar.

## Reportable Findings und Schweregrad

Sicherheitsrelevant sind realistisch erreichbare Abweichungen von den Invarianten, insbesondere unautorisierter Datenzugriff/Egress, Prompt-Injection-bedingte Toolaktionen, Rechte- oder Identitätsübernahme, Secret-Leaks, Memory Poisoning, fehlende Mandanten-/Projekttrennung, manipulierbare Human Gates oder irreführende Local-/Offline-Claims.

Die Priorität richtet sich nach erreichbarer Datenklasse, benötigter Berechtigung, Ausnutzbarkeit, Reichweite, Dauer/Persistenz und möglichem Schaden. Ein rein theoretischer Modelloutput ohne Tool-, Daten- oder Entscheidungswirkung ist anders zu bewerten als ein ausführbarer Datenabfluss.

## Bekannte Grenzen und nicht belegte Eigenschaften

- Das Template konfiguriert keine Firewall, Enterprise-IAM, Air-Gap-, Backup- oder Löschinfrastruktur.
- Ein Loopback-Endpoint schützt nicht vor kompromittierten lokalen Prozessen.
- Quantisierung, lokaler Betrieb oder Open-Source-Lizenz belegen weder Modellqualität noch Datensicherheit.
- „OpenAI-kompatibel“ ist keine universelle Interoperabilitäts- oder Sicherheitsgarantie; nur explizit getestete Pfade und Felder gelten.
- Detaillierte Anbieter-, Rechts- und Organisationsprüfung bleibt beim jeweiligen Owner.

## Außerhalb des Policy-Versprechens

Nicht als Sicherheitsbefund dieses Templates gelten fehlende Enterprise-Funktionen, die es ausdrücklich nicht bereitstellt, etwa automatische Firewallverwaltung, Enterprise-IAM, Air-Gapping oder Hochverfügbarkeit. Sobald Dokumentation deren Vorhandensein behauptet, eine Integration sie voraussetzt oder eine reale Bereitstellung diese Grenze überschreitet, ist die wirksame Kontrolle wieder in Scope. Diese Abgrenzung unterdrückt keine erreichbaren Daten-, Rechte-, Egress- oder Integritätsprobleme.

## Sicherheitsmeldung

Veröffentliche vermutete Schwachstellen, Secrets oder vertrauliche Beispieldaten nicht in einem öffentlichen Issue. Nutze, falls für das Repository aktiviert, eine private GitHub Security Advisory; andernfalls kontaktiere den Repository-Owner über einen bereits etablierten privaten Kanal. Teile nur die für Reproduktion und Wirkung erforderlichen, minimierten Angaben. Bei möglichem laufendem Datenabfluss: Lauf stoppen, Netzwerkzugriff entziehen, Beweise geschützt sichern und den zuständigen System-/Daten-Owner informieren.

## Primärquellen

- [BSI: Generative KI-Modelle](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/KI/Generative_KI-Modelle.pdf?__blob=publicationFile&v=5)
- [BSI: Indirect Prompt Injections](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2023/2023-249034-1032.html)
- [NIST AI 600-1: Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1)
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [OWASP GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)
