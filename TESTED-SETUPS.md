# Getestete Setups und offene Release-Gates

**Prüfdatum:** 2026-09-08

**Funktionaler Teststand:** lokaler Parent-Commit `bc535af8ce1a5617315eb392065e308a07d5ae28` (`Add repository verification workflow`)

**Release-Status:** **BLOCKIERT – nicht veröffentlicht**

Dieser Bericht dokumentiert tatsächliche technische Läufe und ihre Grenzen. Er behauptet weder einen öffentlichen Release noch allgemeine Kompatibilität mit allen Codex-, Claude-, Modell- oder Runtime-Versionen. Die Upgrade-Commits waren beim Test nicht auf `origin/main`; deshalb wurden die Profil-Clones mit `git clone --no-local` aus dem lokalen Commitstand erzeugt und anschließend auf das öffentliche Read-only-Ziel-Remote gesetzt. Nur der Baseline-Test wurde direkt vom öffentlichen Remote geklont.

## Umgebung

| Komponente | Tatsächlich verwendet |
|---|---|
| Betriebssystem | Darwin 25.6.0, arm64 |
| Git | 2.50.1 (Apple Git-155) |
| Python | 3.14.4 |
| Codex | `codex-cli 0.150.0-alpha.12.2`, sichtbares Modell `gpt-5.6-sol` |
| Claude Code | 2.1.263 |
| LaTeX | pdfTeX 1.40.29 / TeX Live 2026, Biber 2.21 |
| Testdaten | ausschließlich synthetische Platzhalter in den Profil-Clones |

## Paarweise Clean-Clone-Matrix

| Profil und Schutzbedarf | Track und Client | Tatsächliches Ergebnis | Status und Grenze |
|---|---|---|---|
| DHBW-Thesis, öffentlich | Cloud-managed comfort als nicht freigegebener Default; Codex | Elf `research/`-Zieldateien und `ki-erklaerung.md` erzeugt; Methode offen, `Assist`, Data/Ethics Gate offen. Vollbuild und lokaler Verify-Vertrag erfolgreich; `main.pdf` hat 11 A4-Seiten und 65.882 Byte. Lokale Prüfungs-/Betreuungsvorgaben blieben sichtbar offen. | **BLOCKIERT als Release-Evidenz:** Codex las wegen globaler Client-Instruktionen zusätzlich echten Kontext außerhalb des Test-Clones. Der Lauf wurde beendet und darf trotz korrekter Artefakte nicht als synthetisch isolierter End-to-End-Test gelten. Ein unversioniertes `tmp/` mit PDF-Renderings blieb als `friction` zurück; nichts war gestagt. |
| Unternehmensprojekt, vertraulich/Geschäftsgeheimnis | Local/On-Prem als nicht freigegebener Default; Claude Code | Genau elf `research/`-Zieldateien erzeugt; Methode offen, `Assist`, Egress aus, Data/Ethics Gate offen. Kein LaTeX-Build erforderlich. Zweiter read-only Lauf erkannte den manuellen Konflikt, stellte keine Rückfragen und erhielt fremde Dateien sowie leeren Index. | **Technischer Setup-Test bestanden.** Der verwendete gehostete Claude-Client beweist ausdrücklich keinen lokalen Gesamtworkflow. Keine Runtime, kein Endpoint, kein Web, kein Remote-MCP, kein OCR-/Embedding-/Logging-Pfad und keine reale On-Prem-Infrastruktur wurden freigegeben oder getestet. |
| Informatikprojekt, intern | Hybrid-redacted als nicht freigegebener Default; Codex | Genau elf `research/`-Zieldateien erzeugt; Methode offen, `Assist`, Redaktions-/Egress-Gate offen. Artefakt-, Explorations-/Bestätigungs-Eval- und Run-Verträge vorhanden. Alle 19 Offline-/Vertragstests bestanden. | **BLOCKIERT als Release-Evidenz:** Artefakte und Tests sind korrekt, aber der Client überschritt auch hier beim Prüfkontext die synthetische Read-Grenze. Der erste und zweite Lauf wurden nach den relevanten Prüfungen wegen sehr langer, wiederholter Ausgaben beendet; kein Abschlussdialog wird behauptet. |

## Unspezifischer Start mit dem zweiten Client

Claude Code erhielt in einem weiteren sauberen Clone nur `Ja, bitte einrichten` plus die synthetische Testgrenze. Der Client nahm keine Änderungen vor und fragte ausschließlich:

1. Profil: `DHBW-Thesis`, `Unternehmensprojekt` oder `Informatikprojekt`;
2. Schutzbedarf: `öffentlich`, `intern` oder `vertraulich/Geschäftsgeheimnis`.

Der Client pausierte danach vor Track-Ableitung und Dateierstellung. Git-Status und Index blieben sauber; das öffentliche Vorlagen-Remote blieb unverändert. **Ergebnis: bestanden.**

## Zweitlauf, Idempotenz und Fremdänderungsschutz

Vor jedem Zweitlauf wurden `research/project-brief.md` manuell geändert, `README.md` als fremde tracked Datei geändert und `foreign-untracked-synthetic.txt` angelegt. Kein Lauf durfte stage'n, committen oder pushen.

| Clone | Beobachtung | Unabhängige Nachprüfung |
|---|---|---|
| DHBW + Codex | Route ohne Rückfrage wiederverwendet; fremde Pfade früh erkannt. Der Lauf wurde beim unerlaubten externen Kontextlesen beendet. | SHA-256 vor/nach identisch: Project Brief `09d8a4ac…04dad7f`, README `58fdbb3b…45f83fe`, Fremddatei `d50e263a…b77215d`; Index leer, Remote unverändert. **Dateischutz bestanden, Client-Isolation blockiert.** |
| Unternehmensprojekt + Claude Code | Zehn unveränderte Ziele als beibehalten und `research/project-brief.md` als Konflikt gemeldet; keine Migration. README und Fremddatei ausdrücklich erhalten. | SHA-256 vor/nach identisch: Project Brief `5cf35fd7…505877`, README `58fdbb3b…45f83fe`, Fremddatei `a7a6f38d…f42a785`; Index leer, Remote unverändert. **Bestanden.** |
| Informatikprojekt + Codex | Route ohne Rückfrage wiederverwendet und manueller Marker als Konflikt erkannt. Der read-only Lauf wurde beim erneuten externen Kontextzugriff beendet. | SHA-256 vor/nach identisch: Project Brief `f0530002…e5bb0`, README `58fdbb3b…45f83fe`, Fremddatei `d50e263a…b77215d`; Index leer, Remote unverändert. **Dateischutz bestanden, Client-Isolation blockiert.** |

Die Codex-Lücke ist kein Beleg gegen die Repository-Dateilogik: Der erzwungene read-only Modus und die unabhängigen Hashprüfungen belegen den Erhalt der Dateien. Sie ist aber ein Datenschutz- und Reproduzierbarkeitsblocker für den behaupteten synthetisch isolierten Clienttest. Erforderlich ist ein erneuter Codex-Lauf mit isoliertem Client-Profil und technisch auf den Clone begrenztem Read-Zugriff.

## Verify, CI und LaTeX

- `bash scripts/verify-repo.sh --require-latex` lief lokal vollständig erfolgreich: 156 relative Markdown-Ziele, Repository-Struktur, 19 Python-Tests, nichtleere PDF und vollständige Sequenz `pdflatex`, `biber`, `makeglossaries`, `pdflatex`, `pdflatex`.
- Die lokale Workflow-Definition verwendet `ubuntu-24.04`, minimale `contents: read`-Rechte, `persist-credentials: false` und `actions/checkout` v7.0.1 am offiziellen Tag-Commit `3d3c42e5aac5ba805825da76410c181273ba90b1`.
- Ein gehosteter GitHub-Actions-Lauf ist noch **nicht** möglich, weil keine Upgrade-Commits gepusht wurden. Er bleibt eigenes Push-Human-Gate und darf nicht durch den lokalen Lauf ersetzt werden.
- Der Vollbuild erzeugt 11 A4-Seiten und 65.882 Byte ohne LaTeX-Fehler. Verbleibend: 1 Overfull- und 19 Underfull-`hbox`-Warnungen, eine doppelte `page.i`-PDF-Destination, eine fehlende Glossar-Destination sowie zwei ungenutzte `caption`-Setups. Alle 11 Seiten wurden gerendert und visuell geprüft; kein Text ist abgeschnitten oder überlagert. Der lange Titel der KI-Erklärung und die Tabellenumbrüche bleiben sichtbar lesbar.

## Baseline und Rückbauanker

Der annotierte Tag `baseline-before-research-upgrade-2026-09-08` wurde direkt vom öffentlichen Remote in eine separate Arbeitskopie geklont:

- Tag-Objekt: `79e61d8f05885dc7584c428bd559d58785e3f32c`;
- `HEAD` und dereferenzierter Tag-Commit: `25075698e9be72d892ac2eee9d2b5cc3d22878f0`;
- Upgrade-Dateien `RESEARCH-START.md`, `AGENTIC-RESEARCH.md`, `LOCAL-PRIVATE-SETUP.md`, `SECURITY.md`, `TESTED-SETUPS.md` und `scripts/verify-repo.sh`: nicht enthalten;
- Root-Vollbuild: erfolgreich, 11 A4-Seiten, 65.882 Byte, dieselben 1 Overfull- und 19 Underfull-Warnungen sowie dieselben PDF-/Caption-Warnungen;
- aktuelle und Baseline-PDF: binär wegen Build-Metadaten verschieden, aber alle 11 gerenderten Seiten haben paarweise identische SHA-256-Hashes.
- Ein abschließender Verify in einem frischen Clone bestand vollständig; anschließend war dort ausschließlich `main.pdf` wegen des neuen eingebetteten Build-Zeitstempels als geändert markiert. Quellen und sonstige Artefakte blieben unverändert.

Der Tag wurde weder verschoben noch neu erzeugt. Rollback bleibt ein normaler Revert gegen diesen Anker; Force Push und Reset sind nicht Teil des Verfahrens.

## Quellen-, Lizenz-, Datenschutz-, Secret- und Claim-Review

- Die verlinkten DSR-/ADR-/Empirie-, DHBW-, NIST-, BSI-, OWASP-, Ollama- und Modellquellen wurden am 2026-09-08 erneut aufgerufen. 24 geprüfte Zielseiten antworteten mit HTTP 200. Zwei DOI-Ziele blockierten automatisierten Publisher-Zugriff mit HTTP 403; Crossref bestätigte DOI und Titel für Peffers et al. sowie Venable et al. Diese Einschränkung ist keine inhaltliche Neuverifikation der Paper.
- Die datierten Modellangaben bleiben ein reproduziertes Beispiel, keine Bestenliste oder Empfehlung. Offizielle Quellen bestätigen MIT für Ollama und Apache 2.0 für `Qwen2.5-7B-Instruct`; eine Lizenzangabe ersetzt keine Einsatzfreigabe.
- Das Repository steht unter MIT; im Upgrade kamen keine neuen Paketabhängigkeiten hinzu. Die einzige neue externe CI-Komponente ist die auf einen vollständigen Commit gepinnte offizielle Checkout-Action.
- Der aktuelle Baum und die gesamte Upgrade-Historie wurden auf typische Secret-Muster geprüft: keine Treffer. Im Upgrade-Scope wurden keine E-Mail-Adressen, absoluten Benutzerpfade, privaten IPs oder internen Hostnamen gefunden. Git-Autor-Metadaten enthalten die bereits bewusst verwendete öffentliche Maintainer-Identität und bleiben Teil des Owner-Reviews.
- Claims wurden gegen Scope und Non-goals gelesen: keine Produktionsreife, Datenschutzkonformität, Zertifizierung, universelle Modellkompatibilität oder bereitgestellte Shared-On-Prem-Infrastruktur wird behauptet. Der frühere pauschale Client-Satz im README wurde auf getestete Versionen und die globale Client-Konfigurationsgrenze eingeschränkt.

## Vorbereitete unabhängige Anfänger-Walkthroughs

Es standen keine drei unbeteiligten realen Testpersonen zur Verfügung. Die Walkthroughs wurden **nicht simuliert** und sind **nicht bestanden**. Außerdem zeigt der öffentliche Link bis zum separaten Push-Gate noch nicht auf die lokalen Upgrade-Commits. Folgende Aufgaben sind nach einem freigegebenen Push mit ausschließlich synthetischen Angaben durchzuführen:

### W-01 – DHBW-Thesis

Nur den öffentlichen Repo-Link und diese Aufgabe geben: „Richte eine öffentliche synthetische DHBW-Thesis ein. Finde den LaTeX-Primärweg, lass die Methode offen und erreiche einen Research-Workspace sowie eine gebaute PDF. Gib keine echten Namen, Matrikel-, Standort-, Betreuungs- oder Kontaktdaten ein.“

Erwartet: LaTeX-Primärweg und optionalen Research-Weg unterscheiden; Profil und Schutzbedarf wählen; lokale Standort-/Studiengangs-/Betreuungsvorgaben als offen erkennen; `research/PROJECT.md` und `main.pdf` erreichen.

### W-02 – Unternehmensprojekt

Nur den öffentlichen Repo-Link und diese Aufgabe geben: „Richte ein vertrauliches synthetisches Unternehmensprojekt ein. Verwende keine echten Unternehmens-, Personen- oder Kontaktdaten und erreiche den ersten sicheren Projekt-Workspace.“

Erwartet: Unternehmensprofil und vertraulichen Schutzbedarf wählen; Local/On-Prem als nicht freigegebenen Default erkennen; vor Datenimport stoppen; `research/PROJECT.md` und offenes Deployment-/Data-Ethics-Gate erreichen.

### W-03 – Informatikprojekt

Nur den öffentlichen Repo-Link und diese Aufgabe geben: „Richte ein internes synthetisches Informatikprojekt ein. Halte Methode und Hybrid-Datenweg offen und führe nur die Offline-Tests aus.“

Erwartet: Informatikprofil und internen Schutzbedarf wählen; Redaktions-/Egress-Gate erkennen; `research/PROJECT.md`, Artefakt-/Eval-/Run-Strukturen und erfolgreiche Offline-Tests erreichen.

### Protokollvorlage je Testperson

- **Pseudonyme Test-ID und Bestätigung:** nicht an Umsetzung beteiligt; Einwilligung zur anonymisierten Ergebnisdokumentation;
- **Aufgabe/Profil und Startpunkt:** öffentlicher Repo-Link, kein weiterer Kontext;
- **Beginn/Ende/Dauer:** mit Zeitzone;
- **Weg:** gelesene Einstiegsdateien, Eingaben, Irrwege und Rückfragen;
- **Hilfe:** keine mündliche Hilfe; falls doch, exakter Anlass und Umfang;
- **Erreichtes Artefakt:** Pfad, Test-/Buildstatus, offene Gates;
- **Befunde:** jeweils `release-blocker`, `friction` oder `question` mit reproduzierbarem Schritt;
- **Folge:** Release-Blocker beheben und den betroffenen Pfad von einer anderen unbeteiligten Person vollständig neu testen.

## Offene Human Gates

- [ ] Codex mit isoliertem Client-Profil und technisch auf den synthetischen Clone begrenztem Read-Zugriff erneut testen.
- [ ] Drei reale, voneinander unabhängige Anfänger-Walkthroughs durchführen; jeden Release-Blocker beheben und unbeteiligt neu testen.
- [ ] Estelle prüft README-Wording, öffentliche Claims, Git-Autor-Metadaten und entscheidet über Push.
- [ ] Erst nach separater Push-Freigabe sämtliche geordneten Upgrade-Commits veröffentlichen und den gehosteten GitHub-Actions-Lauf abwarten.
- [ ] Nach Push öffentlichen Link, README-Links und PDF prüfen.
- [ ] Estelle entscheidet separat über Versionsnummer oder neuen Release-Tag; Safe Default ist kein neuer Tag.

Bis alle Veröffentlichungsgates erfüllt sind, erfolgen weder Push noch Release-Tag noch öffentliche Release-Behauptung. Shared On-Prem bleibt ausschließlich ein nicht bereitgestellter Architektur-Prüffall.
