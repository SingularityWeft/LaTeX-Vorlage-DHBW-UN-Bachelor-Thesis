# Local/On-Prem Private-Track-Preflight

## Erst die Verarbeitungskette prüfen

„Das Modell läuft auf meinem Rechner“ bedeutet nicht automatisch „der Workflow ist lokal“. Prüfe Agenten-Frontend, Runtime, Modell, Endpoint, Browser, OCR, RAG/Embeddings, MCP, Logs, Memory, Git und Backups einzeln im [`Deployment-Manifest`](templates/research/deployment-manifest.md).

Bis alle Gates bestätigt sind:

- nur synthetische Inputs;
- `Assist` statt autonomem Lauf;
- keine Cloudmodelle, Websuche oder Remote-MCPs;
- keine externe OCR, Embeddings, Telemetrie oder Synchronisation;
- keine Installation oder Modell-Downloads ohne ausdrückliche Freigabe.

## Desktop-local mit Ollama

Dieser reproduzierte Referenzpfad ist ein **Beispiel**, keine Produkt- oder Modellrangliste. Geprüft wurde am 8. September 2026 auf der Betriebssystemklasse macOS/arm64 mit Ollama 0.23.1 und einem bereits lokal vorhandenen Modell. Die aktuelle offizielle macOS-Dokumentation nennt macOS Sonoma 14 oder neuer sowie Apple-M-Prozessoren oder x86 im CPU-Betrieb als unterstützte Klassen.

### 1. Herkunft und Lizenz prüfen

- Runtime ausschließlich aus der [offiziellen Ollama-Quelle](https://github.com/ollama/ollama) beziehungsweise dem [offiziellen macOS-Pfad](https://docs.ollama.com/macos) beziehen und Version/Hash dokumentieren.
- Runtime-Lizenz und Modelllizenz getrennt prüfen. Der Ollama-Quellcode führt eine MIT-Lizenz; das getestete Qwen2.5-7B-Modell führt Apache 2.0. Eine Lizenzangabe ist keine rechtliche Freigabe für den konkreten Einsatz.
- Modellname, Digest, Quantisierung, Dateigröße und Herkunft in [`models/examples-2026-09.md`](models/examples-2026-09.md) beziehungsweise dem persönlichen Manifest festhalten.

### 2. Lokalmodus und Bindung

Die [Ollama-FAQ](https://docs.ollama.com/faq) dokumentiert `127.0.0.1:11434` als Standardbindung und `OLLAMA_NO_CLOUD=1` beziehungsweise `disable_ollama_cloud` als Schalter für den Local-only-Modus. Änderungen erfolgen nur nach Owner-Freigabe und werden nicht als Secret ins Repository geschrieben.

Prüfen:

```bash
ollama --version
curl --fail --silent http://127.0.0.1:11434/api/version
lsof -nP -iTCP:11434 -sTCP:LISTEN
```

Erwartet: dokumentierte Runtime-Version und ausschließlich `127.0.0.1:11434` für den Desktop-Pfad. `0.0.0.0`, LAN-IP, Proxy oder Tunnel stoppen den Desktop-Preflight und erfordern eine neue On-Prem-Bewertung.

### 3. Exakt unterstützter Endpoint-Vertrag

Für dieses Template sind nur folgende native Ollama-Pfade geprüft:

| Methode/Pfad | Verwendete Request-Felder | Erwartete Response-Felder |
|---|---|---|
| `GET /api/version` | keine | `version` |
| `GET /api/tags` | keine | `models[].name`, `models[].digest`, `models[].size`, `models[].details` |
| `POST /api/show` | `model` | `details`, `capabilities`, `license` |
| `POST /api/generate` | `model`, `prompt`, `stream`, `keep_alive`, `options.temperature`, `options.num_predict` | `model`, `response`, `done`, `done_reason`, `prompt_eval_count`, `eval_count`, `total_duration` |

Die [native API-Dokumentation](https://docs.ollama.com/api/introduction) nennt `http://localhost:11434/api` als lokale Basis. Andere Pfade, Felder, Streamingvarianten oder eine OpenAI-kompatible Oberfläche sind **nicht** durch diesen Test abgedeckt.

Synthetischer Test ohne Download:

```bash
curl --fail --silent --show-error --max-time 60 \
  http://127.0.0.1:11434/api/generate \
  -H 'Content-Type: application/json' \
  -d '{"model":"qwen2.5:7b","prompt":"Antworte exakt mit: SYNTHETIC-LOCAL-OK","stream":false,"keep_alive":0,"options":{"temperature":0,"num_predict":16}}'
```

Verifiziert am 8. September 2026: HTTP-Erfolg, `response="SYNTHETIC-LOCAL-OK"`, `done=true`, Modell-Digest `845dbda0ea48ed749caafd9e6037047aa19acfcfd82e704d7ca97d631a0b697e`. Der Test verwendet keine vertraulichen Daten und belegt nur diesen Endpoint auf dieser Umgebung.

### 4. Frontend und Tools getrennt bewerten

Ein lokal laufendes Ollama macht Codex, Claude Code, einen Browser-Chat oder ein anderes Cloud-Frontend nicht lokal. Für einen als lokal bezeichneten Gesamtworkflow müssen Frontend, Toolausführung, Telemetrie und alle Datenwege ohne externen Egress geprüft sein. Andernfalls heißt der Befund präzise: „lokale Modellinferenz in einem teilweise externen Workflow“.

## Shared On-Prem

Nutze einen verwalteten Serverpfad, sobald mehrere Personen, zentrale Daten oder ein Netzwerkendpoint benötigt werden. Das Desktop-Beispiel ist keine Enterprise-Referenzarchitektur.

Vor Freigabe müssen mindestens ausgefüllt und getestet sein:

| Bereich | Mindestnachweis |
|---|---|
| Betriebssystem/Host | gehärtete, unterstützte Serverklasse; Patch-Owner und Wartungsfenster |
| Dienstidentität | eigene nicht-interaktive Identität ohne Benutzer-Credentials |
| Netzwerk | internes Segment, deny-by-default Firewall, dokumentierte DNS-/Egress-Allowlist |
| Transport | TLS am freigegebenen Gateway; kein nackter Runtime-Port im allgemeinen LAN |
| Authentisierung/Autorisierung | Nutzer-/Serviceidentitäten, Rollen, Projekt-/Datentrennung und Entzugstest |
| Secrets | externer Secret Store oder OS-geschützter Speicher; nie Manifest/Git/Prompt |
| Modell/Runtime | Version, Digest, Herkunft, Lizenz, SBOM/Artefaktprüfung soweit verfügbar |
| Logs/Monitoring | minimierte Logs, Zugriff, Alarmierung, Uhrzeitsynchronisation und Retention |
| Backup/Löschung | verschlüsselte Backups, Restore-Test, Lösch- und Ablaufverfahren |
| Kapazität/Verfügbarkeit | Hardware-, Queue-, Timeout- und Ressourcenlimits; kein Reifeclaim aus Desktop-Test |
| Incident Response | Stop-, Isolations-, Owner- und privater Meldeweg gemäß [`SECURITY.md`](SECURITY.md) |

Der Endpoint wird erst nach Authentisierungs-, Autorisierungs-, Mandanten-/Projekttrennungs-, Egress- und Negativtests für Shared Inference freigegeben. Die genaue Plattformwahl bleibt organisationsspezifisch.

## Abschluss

1. Persönliche Kopie des Deployment-Manifests außerhalb des öffentlichen Git ausfüllen; für einen lokalen vertraulichen Workspace ist `research/private/deployment-manifest.md` durch die mitgelieferte `.gitignore` ausgeschlossen.
2. Data-Flow-Zeilen und Rechte gegen den realen Systemzustand prüfen.
3. Fünf Negativfälle aus `SECURITY.md` mit synthetischen Inputs ausführen.
4. Restrisiken und nicht getestete Komponenten sichtbar lassen.
5. Daten-, System-, Security-/Datenschutz- und Research-Owner bestätigen das Human Gate.

Erst danach dürfen die im Manifest explizit freigegebenen vertraulichen Datenklassen importiert werden. Das Gate gilt nur für die dokumentierte Version und Umgebung.
