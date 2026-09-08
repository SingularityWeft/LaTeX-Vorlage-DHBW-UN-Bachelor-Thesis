# Deployment-Manifest

- **Template-Version:** `deployment-manifest-v1`
- **Status:** Entwurf / geprüft / freigegeben / gesperrt
- **Manifest-ID und Version:**
- **Prüfdatum:** YYYY-MM-DD
- **Profil:** DHBW-Thesis / Unternehmensprojekt / Informatikprojekt
- **Schutzbedarf:** öffentlich / intern / vertraulich/Geschäftsgeheimnis
- **Track:** Cloud-managed comfort / Hybrid-redacted / Desktop-local / Shared On-Prem

> Bis dieses Manifest vollständig geprüft und menschlich freigegeben ist, nur synthetische Inputs verwenden. Reale Werte, Secrets, personenbezogene Inhalte und vertrauliche Systemdetails gehören nicht in das öffentliche Vorlagen-Repository. Speichere die persönliche Fassung in einem gemäß der Root-Datei `SECURITY.md` geschützten, nicht öffentlichen Bereich. Die Vorlage muss nach dem Kopieren nach `research/` ohne pfadabhängigen Markdown-Link funktionieren.

## 1. Owner und Geltungsbereich

| Verantwortung | Rolle | Freigabebereich | Kontakt-/Eskalationsweg |
|---|---|---|---|
| Daten-Owner |  |  | geschützte Referenz |
| System-Owner |  |  | geschützte Referenz |
| Research Owner |  |  | geschützte Referenz |
| Security/Datenschutz/Ethik |  |  | geschützte Referenz |

- **Zweck und erlaubte Aufgaben:**
- **Explizit nicht erlaubte Aufgaben:**
- **Freigegebene Datenklassen:**
- **Ausgeschlossene Datenklassen:**
- **Gültige Umgebung und Version:**

## 2. Komponenten der Verarbeitungskette

Fülle jede Zeile aus. `aus` ist ein gültiger und für vertrauliche Projekte oft erforderlicher Wert.

| Komponente | Produkt/Version/Hash | Owner | Ausführungs-/Speicherort | Empfänger/Netzwerkziel | Retention/Löschung | Egress | Restrisiko |
|---|---|---|---|---|---|---|---|
| Datenquelle |  |  |  |  |  |  |  |
| Agenten-Frontend |  |  |  |  |  |  |  |
| Modell |  |  |  |  |  |  |  |
| Runtime |  |  |  |  |  |  |  |
| Endpoint/Gateway |  |  |  |  |  |  |  |
| Netzwerk/DNS/Proxy |  |  |  |  |  |  |  |
| OCR | aus /  |  |  |  |  |  |  |
| RAG/Embeddings/Vektorspeicher | aus /  |  |  |  |  |  |  |
| Logs/Tracing/Telemetrie |  |  |  |  |  |  |  |
| Agent Memory/Cache | aus /  |  |  |  |  |  |  |
| Git/Remote |  |  |  |  |  |  |  |
| Browser/Websuche | aus /  |  |  |  |  |  |  |
| MCP/Plugins/Tools | aus /  |  |  |  |  |  |  |
| Backups/Synchronisation | aus /  |  |  |  |  |  |  |

## 3. Datenfluss

Eine Zeile pro Quelle, Verarbeitungsschritt und Zwischenprodukt. Keine Sammelzeile „lokal“ verwenden.

| Flow-ID | Quelle/Input | Schutzbedarf | Verarbeitungsschritt | Speicherort | Empfänger/Rolle | Aufbewahrung | Löschweg | Egress | Restrisiko |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | nein / Ziel |  |

## 4. Identitäten und Least Privilege

Nicht genannte Rechte sind aus. Privater unbeschränkter Read-Zugriff und unbeschränkter Network-/Send-Zugriff dürfen nicht in derselben Rolle oder Sitzung zusammenfallen.

| Identität/Rolle | Read-Pfade/Daten | Write-Pfade | Execute/Tools | Network-Ziele | Credentials | Admin | Ablauf/Entzug | Human Gate |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  | keine / Allowlist | keine / geschützte Referenz | nein |  |  |

## 5. Endpoint-Vertrag

- **Betriebssystemklasse/Architektur:**
- **Bind-Adresse und Port:**
- **TLS/Auth/Gateway:**
- **Runtime- und API-Version:**
- **Exakt erlaubte Methoden/Pfade:**
- **Exakt erlaubte Request-Felder:**
- **Erwartete Response-Felder:**
- **Timeout-, Größen- und Ratenlimits:**
- **Synthetischer Health-/Endpoint-Test, Datum und Ergebnis:**
- **Nicht getestete/unterstützte Pfade:**

„OpenAI-kompatibel“ darf nur als Anbieterbezeichnung erscheinen, nie als universelle Interoperabilitätsgarantie. Dokumentiere immer die tatsächlich getesteten Pfade und Felder.

## 6. Herkunft, Lizenz und Hardware

| Artefakt | Offizielle Quelle | Version/Digest | Lizenzquelle und Prüfung | Hardware-/Speicherbedarf | Prüfer/Datum |
|---|---|---|---|---|---|
| Runtime |  |  |  |  |  |
| Modell |  |  |  |  |  |
| Container/Plugin | aus /  |  |  |  |  |

- **Signatur/Hash/SBOM-Prüfung:**
- **Patch-/Update-Owner und Intervall:**
- **Nicht aufgelöste Lizenz- oder Herkunftsfrage:**

## 7. Untrusted Inputs und Schutzmaßnahmen

- **Mögliche untrusted Quellen:**
- **Trennung Inhalt/Instruktion:**
- **Toolargument-/Allowlist-Prüfung:**
- **Isolation/Sandbox:**
- **Egress-Kontrolle:**
- **Memory-/RAG-Poisoning-Schutz:**
- **Identity-/Privilege-Schutz:**
- **Stop- und Incident-Pfad:**

| Negativtest | Synthetischer Testfall | Erwartung | Ergebnis/Datum |
|---|---|---|---|
| indirekte Prompt Injection |  | verweigert + `human-review` |  |
| Tool-Missbrauch |  | verweigert + `human-review` |  |
| Egress-Versuch |  | verweigert + `human-review` |  |
| Memory Poisoning |  | nicht persistiert + `human-review` |  |
| Rechteausweitung |  | verweigert + `human-review` |  |

## 8. Redaktionsplan für Hybrid-redacted

- **Nicht zutreffend:** ja / nein
- **Entfernte direkte Merkmale:**
- **Entfernte indirekte Merkmale und Kombinationen:**
- **Pseudonymisierung/Generalisierung:**
- **Getrennte Mapping-Tabelle, Speicherort und Löschung:**
- **Reidentifikations-/Inferenzrisiko:**
- **Exakt freigegebene Suchfragen oder Prompt-Hashes:**
- **Menschliche Derivatprüfung vor Egress:**

## 9. Logs, Memory, Backups und Löschung

| Speicherklasse | Inhalt | Ort | Zugriff | Retention | Löschung/Verifikation | Poisoning-/Reidentifikationsrisiko |
|---|---|---|---|---|---|---|
| Logs/Traces |  |  |  |  |  |  |
| Run Records |  |  |  |  |  |  |
| Memory/Cache |  |  |  |  |  |  |
| Embeddings/RAG |  |  |  |  |  |  |
| Backups |  |  |  |  |  |  |

## 10. Restrisiken und Human Gate

| Restrisiko | Eintritt/Wirkung | Mitigation | Akzeptierende Rolle | Ablauf/Re-Review |
|---|---|---|---|---|
|  |  |  |  |  |

- [ ] Data/Ethics Gate bestätigt
- [ ] alle Komponenten und Data Flows vollständig
- [ ] private Read- und externe Network-Rechte wirksam getrennt
- [ ] Endpoint, Herkunft, Lizenz und Hardware geprüft
- [ ] Negativtests bestanden
- [ ] Retention, Löschung, Backup und Incident-Pfad bestätigt
- [ ] Restrisiken durch zuständige Rollen akzeptiert

**Entscheidung:** nicht freigegeben / freigegeben mit Grenzen / zurück zur Überarbeitung

**Bestätigende Rollen, Datum und Begründung:**

**Gültigkeitsgrenzen und nächster Review:**
