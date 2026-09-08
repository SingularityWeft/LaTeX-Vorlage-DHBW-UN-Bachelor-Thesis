# Datierte lokale Modellbeispiele – September 2026

**Geprüft am:** 2026-09-08
**Zweck:** reproduziertes Desktop-Beispiel, keine Bestenliste oder allgemeine Empfehlung

Modell- und Runtime-Angaben altern. Prüfe vor jeder Verwendung erneut offizielle Quelle, Version/Digest, Lizenz, Hardwarebedarf und Endpoint. Ein erfolgreicher synthetischer Test belegt weder Modellqualität noch die Sicherheit eines Gesamtworkflows.

## Reproduziertes Beispiel: Ollama + Qwen2.5 7B

| Merkmal | Geprüfter Stand |
|---|---|
| Betriebssystemklasse | macOS 26.6.2, arm64; keine Aussage für andere Systeme |
| Runtime | Ollama 0.23.1 |
| Runtime-Quelle | [offizielles Repository](https://github.com/ollama/ollama) und [macOS-Dokumentation](https://docs.ollama.com/macos) |
| Runtime-Lizenz | MIT laut [offizieller LICENSE](https://github.com/ollama/ollama/blob/main/LICENSE); konkrete Distribution/EULA separat prüfen |
| Modellname | `qwen2.5:7b` |
| Modell-Digest | `845dbda0ea48ed749caafd9e6037047aa19acfcfd82e704d7ca97d631a0b697e` |
| Format/Quantisierung | GGUF, Q4_K_M |
| Parameter | 7,6 Milliarden |
| lokale Dateigröße | 4.683.087.332 Byte laut `GET /api/tags` |
| Modellherkunft | [Ollama Library](https://ollama.com/library/qwen2.5) und [Qwen-Model Card](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) |
| Modelllizenz | Apache 2.0 laut [offizieller Lizenzdatei](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/LICENSE) und lokalem `POST /api/show` |
| Endpoint | native Ollama API auf `127.0.0.1:11434` |
| Ergebnis | synthetischer `POST /api/generate` antwortete exakt `SYNTHETIC-LOCAL-OK`; `done=true` |

## Hardware- und Kapazitätsgrenze

Die [offizielle Ollama-macOS-Dokumentation](https://docs.ollama.com/macos) nennt macOS Sonoma 14 oder neuer sowie Apple-M-Prozessoren oder x86-CPU-Betrieb. Das Modellartefakt benötigt im geprüften Quant mindestens rund 4,7 GB Speicherplatz; während der Inferenz entsteht zusätzlicher RAM-/GPU-Speicherbedarf. Die [Qwen-Inferenzdokumentation](https://qwen.readthedocs.io/en/v2.5/inference/chat.html) nennt für ein unquantisiertes 7B-Modell grob 14 GB allein zum Laden und weiteren Speicher für Aktivierungen. Dieser Wert ist **nicht** direkt auf den geprüften Q4_K_M-Quant übertragbar.

Deshalb gilt keine pauschale Mindest-RAM-Zahl. Vor Freigabe auf dem Zielsystem:

1. freien Speicherplatz und verfügbare System-/GPU-Ressourcen prüfen;
2. Modell mit synthetischem Input und geplantem Kontext testen;
3. `ollama ps` für CPU-/GPU-Belegung sowie Latenz und Stabilität dokumentieren;
4. Ressourcen-, Timeout- und Parallelitätsgrenzen im Deployment-Manifest festlegen.

## Nicht belegt

- keine Eignung für vertrauliche Daten ohne vollständigen Private-Track-Preflight;
- keine Qualität, Fairness, Robustheit oder wissenschaftliche Reproduzierbarkeit;
- keine allgemeine Kompatibilität mit OpenAI-Clients oder beliebigen API-Feldern;
- keine Shared-On-Prem-, Hochverfügbarkeits- oder Enterprise-Freigabe;
- keine Rechts- oder Lizenzberatung.

Der exakt geprüfte Endpoint-Vertrag und die Trennung von lokaler Inferenz und Cloud-Frontend stehen in [`LOCAL-PRIVATE-SETUP.md`](../LOCAL-PRIVATE-SETUP.md).
