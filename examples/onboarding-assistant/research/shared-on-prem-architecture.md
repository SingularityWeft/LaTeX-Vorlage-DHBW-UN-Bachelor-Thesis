# Shared On-Prem – synthetischer, nicht bereitgestellter Architektur-Prüffall

> **Status: nicht freigegeben, nicht eingerichtet, nicht deployt.** Dieses Dokument ist ein einsteigerfreundliches Denk- und Prüfmodell. Es nennt bewusst keine reale Organisation, Serveradresse, Distribution, Runtime, Modell, Zugangsdaten oder produktive Konfiguration. Es ist weder einsatzbereit noch produktionsreif und nicht für vertrauliche Forschung freigegeben.

## Wann dieser Pfad grundsätzlich sinnvoll sein könnte

Shared On-Prem könnte geprüft werden, wenn mehrere berechtigte Personen dieselbe kontrollierte Inferenzleistung benötigen, synthetische Desktop-Tests nicht mehr genügen und eine Organisation Datenhaltung, Identitäten, Netzwerk, Betrieb und Incident Response selbst verantworten kann. Der mögliche Nutzen liegt in zentralen Rollen, versionierten Artefakten, internem Routing und einer gemeinsamen Betriebsaufsicht.

Das ist kein Beleg, dass Shared On-Prem sicherer, günstiger oder geeigneter ist. Die zusätzliche Netzwerk- und Mehrbenutzerarchitektur schafft neue Angriffsflächen: Identitätsmissbrauch, Projektvermischung, Gateway-Fehler, Adminzugriffe, Log-/Backup-Leaks, Verfügbarkeit und Supply Chain.

## Rollen – wer verantwortet was?

| Rolle | Aufgabe | Darf ausdrücklich nicht |
|---|---|---|
| Daten-Owner | Datenklassen, Zweck, Minimierung und Löschung freigeben | technische Freigabe an Modell/Agent delegieren |
| Research Owner | Frage, Programm, Evals, Interpretation und Claims verantworten | einen Score automatisch promovieren |
| Projekt-Nutzerrolle | freigegebene Fragen stellen und Ergebnisse prüfen | fremde Projekte, Adminfunktionen oder externes Netz nutzen |
| Frontend-Service | authentisierte Requests lesen und Ergebnisse in den Projektbereich schreiben | allgemeine Dateisystem-, Browser- oder Senderechte erhalten |
| Gateway-Service | Identität, Projekt, Rate/Größe und erlaubten API-Pfad prüfen | den nackten Runtime-Port allgemein erreichbar machen |
| Runtime-Service | freigegebenes Modell ausführen und Antwort zurückgeben | Benutzer-Credentials, Internet oder Projektspeicher pauschal erhalten |
| Plattform-Admin | Patchen, Kapazität, Restore und Isolation betreiben | fachliche Inhalte routinemäßig lesen oder allein Gates freigeben |
| Security-/Datenschutzrolle | Bedrohungsmodell, Logs, Egress, Datenschutz und Incidents prüfen | Business-/Research-Claim ersetzen |
| Evaluator-Rolle | gesperrte Bestätigung einmal ausführen | Explorationsfeedback zurückspielen oder Evals für Executor öffnen |

Serviceidentitäten sind eigenständig, kurzlebig und entziehbar. Nutzer-Credentials werden nicht an Frontend, Gateway oder Runtime weitergereicht. Admin- und fachliche Rollen bleiben getrennt.

## Komponenten und Topologie

```text
 [Projekt-Nutzer]
        |
        | TB-1: Identität, Projektrolle, Session
        v
 [internes Frontend] -----> [Projekt-Ergebnisbereich]
        |
        | nur freigegebener Request; keine Browser-/Internetroute
        v
 [TLS/API-Gateway]  <----- [interner Identity-Dienst]
        |
        | TB-2: AuthZ, Projekttrennung, Pfad-/Feld-Allowlist,
        |       Größen-, Zeit-, Queue- und Ratenlimit
        v
 [Inferenz-Service] -----> [geprüftes Modellartefakt-Register]
        |
        | flüchtige Antwort; kein Tool Calling/Memory im ersten Scope
        v
 [TLS/API-Gateway] -----> [internes Frontend]

 [Projekt-Quelldaten] --read-only--> [Frontend-Promptaufbereitung]

 [technische Metadaten] -----------> [internes Monitoring]
 [verschlüsselte Backups] <--------- [getrennter Backup-Service]
 [Plattform-Admin] ----------------> [separate Management-Zone]

 TB-3: Projekt-Datenzone <-> Inferenzzone
 TB-4: Nutzdatenpfad <-> Betriebs-/Monitoringzone
 TB-5: internes Netz <-> externer Egress (deny by default)
```

Die Pfeile beschreiben nur den zu prüfenden Sollfluss. Sie sind keine Netzwerkkonfiguration. OCR, RAG/Embeddings, Agent Memory, Browser, Remote-MCP, externe Logs, Git-Remote und Internet-Egress bleiben im ersten Prüfscope **aus**.

## Datenfluss Schritt für Schritt

1. Eine Projekt-Nutzerrolle authentisiert sich intern; TB‑1 ordnet Session, Projekt und minimale Rolle zu.
2. Das Frontend liest nur freigegebene Projektquellen und baut einen minimierten Request. Dokumentinhalt bleibt untrusted und kann keine Rechte ändern.
3. Das Gateway prüft Identität, Projekt, Endpoint-Pfad, Request-Felder, Größe, Rate und Zeit. Unbekannte Felder oder Toolwünsche werden abgewiesen.
4. Der Runtime-Service erhält nur den freigegebenen Request und ein gepinntes Modellartefakt. Er besitzt weder Benutzer-Credentials noch eine externe Route.
5. Die Antwort geht über dasselbe Gateway zurück. Sie ist untrusted, wird nicht automatisch ausgeführt und landet nur im Ergebnisbereich des Projekts.
6. Monitoring erhält technische Minimalmetadaten, keine Rohprompts oder Rohoutputs. Security prüft Alarm- und Retentionregeln.
7. Die Nutzer-/Research-Rolle prüft Ergebnis, Quellen und Claim. Eine freigabepflichtige Aktion bleibt beim Menschen.
8. Confirmation läuft später in einer getrennten Evaluator-Rolle; Ergebnis wird nicht zur weiteren Optimierung zurückgespielt.

## Vertrauens- und Sicherheitsgrenzen

| Grenze | Zu prüfende Kontrolle | Warum sie nötig ist | Aktueller Status |
|---|---|---|---|
| TB‑1 Nutzer → Frontend | starke Authentisierung, Projektrolle, Sessionablauf, Entzugstest | verhindert Zugriff mit falscher Identität oder auf fremde Projekte | nicht implementiert/getestet |
| TB‑2 Frontend → Gateway | TLS, Serviceidentität, API-/Feld-Allowlist, Limits | trennt Benutzeroberfläche vom Runtime-Port und stoppt Vertragsdrift | nicht ausgewählt/getestet |
| TB‑3 Datenzone → Inferenz | Read-only-Minimierung, Projektisolation, flüchtige Verarbeitung | begrenzt Reichweite bei Fehlern und verhindert Quervermischung | nicht implementiert/getestet |
| TB‑4 Nutzdaten → Betrieb | Metadaten statt Rohinhalt, getrennte Adminrolle, Logretention | reduziert Log-/Admin-Leaks und Poisoning | nicht implementiert/getestet |
| TB‑5 intern → extern | deny-by-default DNS/Proxy/Firewall und Egress-Negativtest | verhindert unbeabsichtigte externe Übertragung | nicht konfiguriert/getestet |
| Executor → Confirmation | getrennte Identität, Rechte und Arbeitskontext | reduziert Eval-Overfitting und Manipulation | nur Prozessvertrag im Repo |

## Sicherheitsgründe hinter dem Entwurf

- **Gateway statt offener Runtime-Port:** zentrale AuthZ, Projekttrennung und Limits müssen vor Inferenz greifen.
- **Eigene Serviceidentitäten:** ein kompromittierter Dienst soll weder Nutzer- noch Adminrechte erben.
- **Deny-by-default Egress:** vertrauliche Daten plus unbeschränkte Senderechte dürfen nicht zusammentreffen.
- **Getrennte Daten-, Betriebs- und Backupzonen:** Logs, Adminzugriff und Restore-Kopien sind eigene Datenwege.
- **Kein Tool Calling/Memory im ersten Scope:** weniger Berechtigungen, Persistenz- und Injectionwirkung.
- **Gepinnte Artefakte:** Runtime, Modell und Container benötigen Quelle, Digest, Lizenz- und Supply-Chain-Prüfung.
- **Menschliche Gates:** technische Erreichbarkeit trifft keine Datenschutz-, Forschungs-, Claim- oder Einsatzentscheidung.

## Warum SPEC‑05 hier nichts bereitstellt

SPEC‑05 soll einen ungefährlichen Onboarding-Fall und einen prüfbaren Architekturvertrag liefern. Eine reale Shared-On-Prem-Installation würde Plattform-, Netzwerk-, IAM-, Secrets-, Betriebs- und Datenschutzentscheidungen vorziehen, für die keine Organisation, Owner, Zielumgebung oder Freigabe vorliegt. Ein synthetischer Unit Test könnte diese reale Wirksamkeit nicht belegen.

Deshalb wurden keine Hosts, Ports, DNS-Namen, Zertifikate, Firewalls, Konten, Serviceidentitäten, Secrets, Container, Runtimes, Modelle, Speicher, Backups oder Monitoringziele eingerichtet. Auch der lokale Desktop-Endpoint wird nicht als Shared-On-Prem-Komponente umgedeutet.

## Fehlende Gates vor einem realen Einsatz

### Betrieb

- [ ] Zielplattform, unterstützte OS-/Hardwareklasse, Kapazität, Queue-/Timeout- und Verfügbarkeitsziel gewählt
- [ ] Patch-, Wartungs-, Monitoring-, On-call-, Backup-, Restore-, Lösch- und Exit-Prozess mit Owner getestet
- [ ] Betriebsdokumentation, Änderungsfreigabe und Rollback in einer realen Umgebung geprobt

### Datenschutz und Daten

- [ ] konkrete Datenklassen, Zweck, Rechts-/Berechtigungsgrundlage, Minimierung und Betroffenenrisiken geprüft
- [ ] vollständige Data-Flow-, Empfänger-, Retention-, Lösch- und Backup-Matrix bestätigt
- [ ] Datenschutz-/Ethikrolle sowie Daten-Owner akzeptieren dokumentierte Restrisiken

### Security

- [ ] Threat Model für reale Umgebung, Identitäten, Projekt-/Mandantentrennung und Adminpfad freigegeben
- [ ] TLS, AuthN/AuthZ, Secret Store, PAM/JIT, Segmentierung, DNS/Proxy/Firewall und Egress technisch getestet
- [ ] Herkunft, Signatur/Digest, Lizenz, SBOM und Updateweg für Runtime, Modell und Container geprüft
- [ ] Injection-, Tool-, Egress-, Memory-, Rechte-, Auth-, Projekttrennungs-, Log- und Restore-Negativtests bestanden
- [ ] Incident-Stop, Isolation, Beweissicherung und privater Meldeweg geprobt

### Human und Research

- [ ] Daten-, System-, Security-/Datenschutz- und Research Owner namentlich in geschützter Dokumentation benannt
- [ ] Forschungsfrage, Programm, Evals, Budgets, Stopbedingungen und Confirmation-Trennung freigegeben
- [ ] Nutzer-, Admin- und Evaluatorrollen geschult; Entzug und Rollenwechsel getestet
- [ ] Fachreview bestätigt Ergebnisgrenzen; kein automatischer Claim, Deployment oder Datenimport

**Entscheidung:** Der Architektur-Prüffall bleibt `nicht freigegeben`. Erst eine separate, organisationsspezifische Implementierung mit technischen Positiv-/Negativtests und allen Human Gates könnte überhaupt eine begrenzte Freigabeentscheidung ermöglichen.
