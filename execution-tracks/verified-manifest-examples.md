# Synthetische Deployment-Manifest-Prüffälle

Diese beiden vollständig ausgefüllten Kurzmanifeste prüfen, ob der Vertrag für Desktop-local und Shared On-Prem praktisch ausfüllbar ist. Sie enthalten keine echten Projekte, Personen, Secrets oder vertraulichen Daten. Nur der Desktop-Endpoint wurde tatsächlich ausgeführt; das On-Prem-Beispiel ist ein **nicht freigegebener Architektur-Prüffall**.

Für reale Projekte ist die vollständige Vorlage [`deployment-manifest.md`](../templates/research/deployment-manifest.md) maßgeblich.

## A. Desktop-local – verifizierter synthetischer Prüffall

### Identität und Gate

| Feld | Wert |
|---|---|
| Manifest/Status | `desktop-synthetic-2026-09-v1` / technisch geprüft, nicht für echte Daten freigegeben |
| Profil/Schutzbedarf | Informatikprojekt / öffentlich-synthetisch |
| Owner | Daten-, System- und Research-Owner: lokale Testrolle; Security-Prüfung: dokumentierende Rolle |
| Geltungsbereich | ein synthetischer Prompt, keine Tools, kein RAG, kein Browser, keine echten Daten |
| Human Gate | nicht erforderlich für den rein synthetischen Read-only-Test; vor echten Daten ausdrücklich offen |

### Komponenten

| Komponente | Version/Herkunft | Ort/Empfänger | Retention/Löschung | Egress/Restrisiko |
|---|---|---|---|---|
| Datenquelle | Literal `SYNTHETIC-LOCAL-OK` | lokaler Prozess | nur Testlauf; Shellhistorie nach lokaler Policy | kein Egress; geringe Metadatenreste möglich |
| Frontend | `curl` aus lokaler Shell | kontrollierter Desktop | keine eigene Persistenz | nur Loopback |
| Modell | `qwen2.5:7b`, Digest `845dbd…97e` | lokaler Ollama-Modellspeicher | manuell entfernbar; nicht im Repo | kein Egress; Modell-/Supply-Chain-Risiko bleibt |
| Runtime | Ollama 0.23.1, offizielle Quelle | lokaler Desktop | lokale App-/Serverlogs nach Owner-Regel | Bindung `127.0.0.1:11434`; lokale Prozesse bleiben Risiko |
| Endpoint | native `/api/version`, `/api/tags`, `/api/show`, `/api/generate` | Loopback | keine serverseitige Testdatenablage behauptet | kein allgemeiner Netzwerkzugriff freigegeben |
| OCR/RAG/Embeddings | aus | – | – | kein Egress |
| Logs/Memory | Memory aus; Runtime-Logs minimiert prüfen | lokal | projektspezifisch vor echten Daten festzulegen | Rohprompt könnte in lokalen Diagnosepfaden erscheinen |
| Git/Browser/MCP | Git nur Repo-Metadaten; Browser und MCP aus | lokal | keine Testdaten committed | kein Egress im Test |
| Backups/Sync | für Testdaten nicht erforderlich; Modell/Logs nicht bewertet | lokal | offen vor echten Daten | Restrisiko vor echtem Einsatz ungeklärt |

### Data Flow und Rechte

| Flow | Quelle → Schritt → Ziel | Empfänger | Retention/Löschung | Egress/Restrisiko |
|---|---|---|---|---|
| `D1` | synthetisches Literal → `POST /api/generate` → Antwort im Terminal | lokale Testrolle | flüchtig; Terminalhistorie prüfen | Loopback; lokale Prozesse könnten mitlesen |
| `D2` | Runtime-/Modelldaten → API-Response → dokumentierter Versionsbefund | öffentliche Prüfdokumentation | dauerhaft ohne Prompt-/Personendaten | nur technische Metadaten |

| Rolle | Read | Write/Execute | Network | Credentials/Admin | Entzug/Gate |
|---|---|---|---|---|---|
| Test-Client | nur synthetisches Literal | `curl` gegen vier erlaubte Pfade | nur `127.0.0.1:11434` | keine / nein | Prozessende; Scope-Abweichung stoppt |
| Ollama-Runtime | lokales Modell | Antwort/Runtime-Log | Loopback; Cloudfunktion nicht für Test genutzt | keine Projekt-Credentials / nein | Dienst stoppen; Konfiguration vor echten Daten prüfen |

### Endpoint und Negativtests

- **OS/Architektur:** macOS 26.6.2 / arm64
- **Bindung:** `127.0.0.1:11434`, mit `lsof` bestätigt
- **API:** Ollama 0.23.1, native Pfade/Felder gemäß [`LOCAL-PRIVATE-SETUP.md`](../LOCAL-PRIVATE-SETUP.md)
- **Positivtest:** Antwort exakt `SYNTHETIC-LOCAL-OK`, `done=true`
- **Limits:** 60 s Client-Timeout, maximal 16 neue Tokens, keine Parallelität
- **Nicht getestet:** Auth, TLS, OpenAI-kompatible API, Tools, Vision, Streaming, Shared Access

| Negativfall | Ergebnis |
|---|---|
| Dokument fordert Egress | verweigern; kein Dokumentzugriff im Test, Policy wäre `human-review` |
| nicht allowlistetes Tool | verweigern; nur `curl` auf vier Pfade erlaubt |
| externes Netzwerkziel | verweigern; nur Loopback allowlistet |
| Memory-Persistenz | verweigern; Memory im Test aus |
| Rechteausweitung | verweigern; keine Credentials/Adminrechte vorhanden |

### Restrisiken und Entscheidung

Lokale Prozesskompromittierung, Runtime-/Modell-Supply-Chain, Diagnose-Logs und nicht geprüfte Backups bleiben offen. **Entscheidung:** Nur der synthetische Desktop-Endpoint-Test ist bestanden. Vor vertraulichen Daten ist ein neues, reales Manifest samt Owner-, Lösch-, Backup- und Local-only-Prüfung erforderlich.

## B. Shared On-Prem – vollständig ausgefüllter, nicht bereitgestellter Prüffall

### Identität und Gate

| Feld | Wert |
|---|---|
| Manifest/Status | `onprem-synthetic-2026-09-v1` / nicht freigegeben |
| Profil/Schutzbedarf | Unternehmensprojekt / vertraulich-Geschäftsgeheimnis |
| Owner | Daten-Owner: Business-Rolle; System-Owner: Plattformrolle; Research Owner: Forschungsrolle; Security/Datenschutz: zuständige Prüfrollen |
| Geltungsbereich | synthetische Dokumentklassifikation; keine reale Organisation oder Daten |
| Human Gate | offen, weil keine reale Serverumgebung, Rollenprüfung oder technische Abnahme existiert |

### Komponenten

| Komponente | Geplanter Vertrag | Ort/Empfänger | Retention/Löschung | Egress/Restrisiko |
|---|---|---|---|---|
| Datenquelle | freigegebene interne Dokumentklasse | verschlüsselter interner Projektspeicher | 30 Tage nach Projektende; Owner bestätigt Löschung | kein externer Empfänger; Replikate möglich |
| Frontend | intern betrieben, versioniert | internes Anwendungssegment | Sessiondaten maximal 24 h | kein Internet; Frontend muss technisch geprüft werden |
| Modell/Runtime | gepinnter Digest und geprüfte Lizenz; konkrete Auswahl offen | internes Inferenzsegment | Artefakte bis Versionsablösung | Supply-Chain- und Modellrisiko offen |
| Endpoint/Gateway | internes TLS-Gateway mit Projektrollen | nur internes Frontend | Zugriffsmetadaten 30 Tage | Runtime-Port nicht im allgemeinen LAN; Fehlkonfiguration möglich |
| Netzwerk/DNS | deny-by-default, interne Allowlist | interne DNS-/Zeit-/Monitoringdienste | Netzwerklogs 30 Tage | keine externe DNS-/Proxyroute; technische Prüfung fehlt |
| OCR/RAG/Embeddings | aus im ersten Release | – | – | kein Egress; spätere Aktivierung neues Gate |
| Logs/Memory | minimierte Metadaten; Memory aus | internes Logsegment | 14 Tage; kontrollierte Löschung | Adminzugriff und Log-Injection bleiben Risiken |
| Git/Browser/MCP | Git-Remote, Browser und Remote-MCP aus | nur internes Artefaktregister | gemäß Artefaktpolicy | keine externe Kommunikation |
| Backups | verschlüsselt, getrennte Backup-Rolle | internes Backupsegment | 30 Tage; Restore-/Ablauftest erforderlich | Löschverzögerung und Restore-Kopien |

### Data Flow und Rechte

| Flow | Quelle → Schritt → Ziel | Empfänger | Retention/Löschung | Egress/Restrisiko |
|---|---|---|---|---|
| `O1` | Projektspeicher → Read-only-Frontend → Runtime | interne Serviceidentitäten | keine Frontendkopie; Runtime-Memory nach Request verwerfen | kein Egress; Isolation ungeprüft |
| `O2` | Runtime-Antwort → freigegebener Ergebnisordner | Research-Rolle | 30 Tage nach Projektende | kein Egress; Output kann vertrauliche Fragmente enthalten |
| `O3` | technische Metadaten → internes Monitoring | Plattform-/Security-Rolle | 14–30 Tage | kein Rohprompt; Korrelation kann sensibel sein |

| Rolle | Read | Write/Execute | Network | Credentials/Admin | Entzug/Gate |
|---|---|---|---|---|---|
| Frontend-Service | nur Projektinput | nur Ergebnisordner | nur TLS-Gateway | kurzlebige Serviceidentität / nein | Sessionende und zentraler Entzug |
| Runtime-Service | Modell plus Request | flüchtige Antwort | keine externe Route | eigene Serviceidentität / nein | Dienst-/Tokenentzug |
| Plattform-Admin | Systemkonfiguration, keine fachliche Nutzung | Wartung | interne Managementziele | PAM/JIT / ja | Vier-Augen-Gate und Ablauf |
| Research-Rolle | freigegebene Inputs/Outputs | kein Systemwrite | keine externe Kommunikation | Benutzeridentität / nein | Projektentzug; Egress separates Gate |

### Endpoint, Tests und Restrisiken

- **OS/Host:** gehärtete unterstützte Serverklasse, konkrete Distribution/Version offen – dadurch nicht freigegeben.
- **Bindung:** Runtime nur internes Inferenzsegment; Zugriff ausschließlich über TLS-Gateway.
- **API-Vertrag:** vor Auswahl exakt festzulegen; keine OpenAI-Kompatibilitätsbehauptung.
- **Limits:** Projekt-, Request-, Größen-, Zeit-, Queue- und Ressourcenlimits erforderlich.
- **Negativtests:** Injection, Tool-Missbrauch, externer Egress, Memory Poisoning, Rechteausweitung sowie Auth-/Projekttrennung müssen technisch verweigert werden; noch nicht ausgeführt.
- **Restrisiken:** Plattform- und Modellwahl, Mandantentrennung, PAM, Backup/Restore, Monitoring, Patchen, Löschverifikation und Incident Response ungeprüft.

**Entscheidung:** `nicht freigegeben`. Der vollständig dokumentierte Entwurf zeigt alle offenen Felder und darf nicht als bereitgestellte oder sichere On-Prem-Architektur bezeichnet werden. Freigabe erst nach realer Implementierung, technischen Negativtests und Human Gate durch Daten-, System-, Security-/Datenschutz- und Research-Owner.
