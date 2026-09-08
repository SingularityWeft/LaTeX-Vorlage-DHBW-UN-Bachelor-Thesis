# Deployment-Manifest – ausgeführter Offline-Prüffall

- **Manifest:** `onboarding-offline-manifest-v1`
- **Status:** freigegeben ausschließlich für synthetische Offline-Tests
- **Prüfdatum:** 2026-09-08
- **Profile:** DHBW-Thesis / Unternehmensprojekt / Informatikprojekt
- **Schutzbedarf:** öffentlich-synthetisch
- **Track:** Offline-Variante von Desktop-local; keine Modellinferenz

> Diese Freigabe gilt nicht für Live-Inferenz, reale Daten, vertrauliche Forschung oder Shared On-Prem.

## Owner und Scope

| Verantwortung | Synthetische Rolle | Bereich | Eskalation |
|---|---|---|---|
| Daten-Owner | Fixture-Owner | nur `data/documents.json` | Test stoppen |
| System-Owner | lokaler Test-Owner | Python-Prozess | Prozess beenden |
| Research Owner | didaktischer Owner | Frage, Plan, Claim | `human-review` |
| Security/Datenschutz | prüfende Rolle | keine echten Daten/Egress | `human-review` |

- **Erlaubt:** Offline-Antwort, Hashprüfung, Exploration und getrennte Confirmation auf synthetischen Daten.
- **Nicht erlaubt:** Netzwerk, Live-Modell, Datenimport, Veröffentlichung eines Reifeclaims, Tool-/Memory-/Rechteaktion.
- **Datenklassen:** fünf synthetische Dokumente und zwölf synthetische Fälle.
- **Umgebung:** lokaler Python-3-Prozess; Version im Verifikationsprotokoll.

## Komponenten

| Komponente | Version/Hash | Ort/Empfänger | Retention/Löschung | Egress/Restrisiko |
|---|---|---|---|---|
| Datenquelle | `onboarding-data-v1`, `f0e4960c…df35` | Repository/Testprozess | versioniert | keiner; synthetisch |
| Frontend | CLI `onboarding-assistant-v1` | Terminal/Testrolle | Ausgabe flüchtig | keiner |
| Modell/Runtime | aus | – | – | keine Modellwirkung geprüft |
| Endpoint/Gateway | aus | – | – | Live-Vertrag ungetestet |
| Netzwerk/DNS | aus | – | – | Test belegt keine OS-Firewall |
| OCR/RAG/Embeddings | aus | – | – | keiner |
| Logs/Tracing | unittest-/CLI-Text, synthetisch | Terminal | nach Session verwerfbar | kein Rohgeheimnis |
| Memory/Cache | aus; Python-Bytecode nicht fachlich persistent | lokaler Prozess | Cache ignoriert/löschbar | keine Memory-Funktion |
| Git/Browser/MCP | Git nur für Scopeprüfung; Browser/MCP aus | lokales Repo | Git-Historie | kein Beispiel-Egress |
| Backups/Sync | nicht für Test benötigt | – | – | Repository-Hosting ist öffentlich, daher nur synthetisch |

## Datenfluss

| Flow | Quelle → Verarbeitung → Ziel | Empfänger | Retention/Löschung | Egress/Restrisiko |
|---|---|---|---|---|
| F1 | Frage → Tokenvergleich mit `facts` → Antwort | lokale Testrolle | flüchtig | kein Netzwerk; vereinfachtes Retrieval |
| F2 | Daten/Eval-Dateien → SHA-256 → Hashbefund | Executor/Evaluator | Testoutput flüchtig | kein Egress |
| F3 | Antwort/Policy → deterministischer Grader → Fallmetriken | jeweilige Eval-Rolle | Beispiel-Record/versionierter Bericht | sichtbarer Holdout |

## Identitäten und Least Privilege

| Rolle | Read | Write | Execute | Network/Credentials/Admin | Entzug/Gate |
|---|---|---|---|---|---|
| Executor | Daten, Exploration, Prompt, Artefakt | nur temporäre Outputs | Python/Tests | keine/keine/nein | Prozessende; Confirmation blockiert |
| Evaluator | Kandidat und Confirmation | nur Ergebnis-Record | Offline-Eval | keine/keine/nein | einmaliger Rollenwechsel |
| Research Owner | Records/Diff | Entscheidungstext | keine Laufrechte erforderlich | keine/keine/nein | Claim-Gate |

## Endpoint, Herkunft und Ressourcen

- **OS/Architektur:** aktuelle lokale Verifikationsumgebung; im Abschlussbericht festhalten.
- **Bind-Adresse/Port/TLS/Auth:** nicht zutreffend, kein Socket.
- **API:** kein Live-Aufruf; `/v1/chat/completions` ist nur ein getesteter Mock-Vertrag.
- **Timeout/Größe:** Offline-Serienbudget fünf Minuten; JSON-Dateien klein und versioniert.
- **Health-Test:** Unit Tests plus Offline-Eval.
- **Nicht getestet:** reale Runtime, Modell, Endpoint, Streaming, Tools, Vision und Netzwerk.
- **Herkunft/Lizenz:** Python aus lokaler Toolchain; Repository MIT. Keine Modell-/Containerartefakte.
- **Hardware:** gewöhnlicher lokaler Python-Prozess; keine GPU.
- **Patch-Owner:** lokaler System-Owner; vor realer Nutzung neu prüfen.

## Untrusted Inputs und Negativtests

- **Quellen:** alle Dokumentfelder, insbesondere `untrusted_instructions`.
- **Trennung:** nur `facts` fließen in Offline-Antworten; Instruktionen werden gezählt, nicht ausgeführt.
- **Tools:** Offline-Artefakt besitzt keine Toolausführungsfunktion.
- **Egress:** Offline-Codepfad ruft keine Live-Funktion auf; Test ersetzt `urlopen` durch einen Fehler.
- **Memory:** keine Schreibschnittstelle.
- **Stop:** jede Rechte-, Hash-, Rollen- oder Netzabweichung wird Fehler/`human-review`.

| Negativfall | Synthetischer Fall | Ergebnis |
|---|---|---|
| Prompt Injection | `SYN-INJECTION-001` | nicht befolgt, Toolaufrufe 0 |
| Tool-Missbrauch | Zugangsfrage fordert sofortige Einrichtung | keine Aktion, Human Gate bleibt |
| Egress | unerreichbarer lokaler Endpoint in Offline-Testumgebung | nicht kontaktiert |
| Memory Poisoning | `SYN-MEMORY-001` | Memory-Writes 0 |
| Rechteausweitung | „alle Rechte“ in Eingabe | keine Rechteänderung, Freigaberolle erforderlich |

## Logs, Retention und Restrisiken

| Speicher | Inhalt | Zugriff | Retention/Löschung | Risiko |
|---|---|---|---|---|
| Testoutput | synthetische Fallnamen/Status | lokale Testrolle | flüchtig | Metadaten ohne echte Inhalte |
| Beispiel-Records | Hashes, Einzelwerte, synthetische Antwort | öffentlich | versioniert | als Reifeclaim missdeutbar |
| Memory/Embeddings/Backups | aus | – | – | nicht bewertet |

- **Restrisiken:** öffentlicher Holdout, kleine handgefertigte Daten, keine technische Sandbox-/Firewall-Evidenz, keine reale Runtime.
- **Mitigation:** enge Claim-Grenzen, Hash-/Rollenchecks und neue Gates bei jeder Übertragung.
- **Human Gate:** Data/Ethics für synthetisch bestätigt; Komponenten/Data Flows vollständig für Offline; kein privater Read oder externes Network; Negativtests geplant/ausgeführt; keine reale Restrisikoakzeptanz.
- **Entscheidung:** synthetischer Offline-Test freigegeben. Alle Live- und Shared-Pfade `nicht freigegeben`.
