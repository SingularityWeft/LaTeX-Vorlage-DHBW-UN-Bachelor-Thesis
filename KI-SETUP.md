# KI-Setup: „Ja, bitte einrichten“

**Setup-Version:** `research-setup-v2`

Diese Datei ist der verbindliche Ablauf für einen lokalen Coding-Agenten, wenn der User „Ja, bitte einrichten“, „richte die Vorlage ein“, „mach das arbeitsfertig“ oder ähnlich sagt. Das Setup unterstützt drei Profile:

- DHBW-Thesis
- Unternehmensprojekt
- Informatikprojekt

Der bestehende LaTeX-Schnellstart bleibt für die DHBW-Thesis erhalten. Der optionale Research-Weg richtet nur einen manuellen, kontrollierten Arbeitsbereich ein: keine Agentenläufe, keine Runtime-, Modell- oder Endpoint-Auswahl und keine autonome wissenschaftliche Autorenschaft.

Ein reines Chatmodell ohne lokalen Datei- und Terminalzugriff kann den Ablauf nur erklären, nicht ausführen.

## Unveränderliche Sicherheitsregeln

1. Vor echten Projektdaten werden nur fehlendes Profil und fehlender Schutzbedarf erfragt.
2. `Assist` ist die Standard-Autonomiestufe. `Bounded autonomous` ist ohne den Vertrag aus `AGENTIC-RESEARCH.md` und ein bestätigtes Research Program nicht zulässig und wird auf `Assist` zurückgesetzt.
3. Ist die Methodenwahl uneindeutig, bleibt sie `offen`; der Agent entscheidet sie nicht automatisch.
4. Vor einem bestätigten Data/Ethics Gate werden ausschließlich abstrakte oder synthetische Angaben verwendet.
5. Bestehende Dateien, vorhandene Änderungen und der aktuelle Git-Staging-Bereich werden nicht überschrieben, übernommen oder bereinigt.
6. Remotes werden nicht automatisch geändert. Es gibt keinen automatischen Commit und keinen automatischen Push.
7. Installationen und Downloads erfordern eine ausdrückliche Freigabe.
8. Geheimnisse, personenbezogene Daten und vertrauliche Inhalte werden weder erfunden noch in Prompts, Logs oder Commits aufgenommen.
9. Bei `vertraulich/Geschäftsgeheimnis` sind Cloudmodelle, Websuche und Remote-MCPs bis zum freigegebenen Preflight aus [`LOCAL-PRIVATE-SETUP.md`](LOCAL-PRIVATE-SETUP.md) ausgeschaltet.

## Ablauf für den Coding-Agenten

### 1. Bestand aufnehmen

Lies vollständig:

- `README.md` und `RESEARCH-START.md`;
- `AGENTS.md` beziehungsweise `CLAUDE.md`;
- `templates/research/method-choice.md`;
- das gewählte Profil unter `profiles/`, sobald es bekannt ist;
- `templates/research/data-ethics-check.md`.

Prüfe vor jeder Änderung mindestens:

```bash
git status --short --branch
git diff --name-only
git diff --cached --name-only
git ls-files --others --exclude-standard
git remote -v
```

Dokumentiere getrennt:

- bereits geänderte oder unversionierte fremde Dateien;
- bereits gestagte Dateien;
- vorhandene Ziel-Dateien unter `research/` samt Version und Hash;
- das aktuelle Remote.

Diese Dateien bleiben unverändert und ungestagt. Lösche oder initialisiere `.git` nie neu.

Wenn ein Remote auf `SingularityWeft/LaTeX-Vorlage-DHBW-UN-Bachelor-Thesis` zeigt, markiere es als **öffentliches Vorlagen-Remote: Push verboten**. Eine Umbenennung oder ein eigenes Remote ist eine separate, ausdrücklich freizugebende Aktion.

### 2. Nur fehlende Router-Angaben erfragen

Werte Angaben aus dem Startprompt aus und frage sie nicht erneut. Beim generischen „Ja, bitte einrichten“ stelle nur diese noch offenen Fragen, bevor echte Projektdaten genannt werden:

1. „Welches Profil brauchst du: DHBW-Thesis, Unternehmensprojekt oder Informatikprojekt?“
2. „Welchen Schutzbedarf hat das Projekt: öffentlich, intern oder vertraulich/Geschäftsgeheimnis?“

Wenn eine Antwort fehlt, pausiere dort. Frage noch nicht nach Thema, Firma, Personen, Daten, Zugangsdaten oder Dokumenten.
Sind Profil, Methode, Schutzbedarf oder Ausführungspfad bereits im Prompt genannt, übernimmst du jeden dieser Werte sichtbar und fragst ihn nicht erneut ab.

### 3. Sichere Route ableiten und bestätigen lassen

Nutze `RESEARCH-START.md` und `templates/research/method-choice.md`:

- Übernimm einen bereits ausdrücklich genannten Methodenpfad.
- Leite bei eindeutigen abstrakten Angaben höchstens einen **Vorschlag** ab.
- Bei mehreren plausiblen Pfaden bleibt die Methode `offen` und das dokumentierte Human Gate ist erforderlich.
- Die Autonomiestufe ist `Assist`, sofern nicht ausdrücklich und zulässig anders bestätigt.

Lege den Ausführungspfad aus dem Schutzbedarf fest:

| Schutzbedarf | Sicherer Startpfad | Externe Verarbeitung | Human Gate |
|---|---|---|---|
| öffentlich | Cloud-managed comfort | möglich, aber nicht automatisch gestartet | Profil, Methode und Datenweg bestätigen |
| intern | Hybrid-redacted | aus, bis Redaktion und Datenweg bestätigt sind | Redaktions- und Data/Ethics-Freigabe |
| vertraulich/Geschäftsgeheimnis | Local/On-Prem, nicht still überschreibbar | aus; bis zum freigegebenen Private-Track-Preflight auch keine Cloudmodelle, Websuche oder Remote-MCPs | Datenschutz-, Security- und Data/Ethics-Freigabe |

Ein sichererer Pfad darf gewählt werden. Ein weniger restriktiver Pfad braucht eine ausdrücklich dokumentierte menschliche Freigabe. Dieses Setup wählt keine Runtime, kein Modell und keinen Endpoint.

Die technischen und organisatorischen Grenzen des gewählten Pfads stehen in [`execution-tracks/README.md`](execution-tracks/README.md). Vor echten Daten wird das [`Deployment-Manifest`](templates/research/deployment-manifest.md) manuell ausgefüllt und gemäß [`SECURITY.md`](SECURITY.md) freigegeben. Das Workspace-Setup selbst startet weiterhin keine Runtime und konfiguriert keinen Endpoint.

### 4. Zielplan und Konflikte anzeigen

Ziel des Research-Workspace ist ausschließlich `research/`. Nur beim DHBW-Profil dürfen die separat beschriebenen LaTeX-Artefakte `ki-erklaerung.md` und `main.pdf` hinzukommen. Zeige vor dem Schreiben diese geplante Zuordnung:

| Ziel | Quelle |
|---|---|
| `research/PROJECT.md` | `templates/research/project-manifest.md` |
| `research/method-choice.md` | `templates/research/method-choice.md` |
| `research/data-ethics-check.md` | `templates/research/data-ethics-check.md` |
| `research/deployment-manifest.md` | `templates/research/deployment-manifest.md` |
| `research/project-brief.md` | `templates/research/project-brief.md` |
| `research/research-question.md` | `templates/research/research-question.md` |
| `research/evidence-log.md` | `templates/research/evidence-log.md` |
| `research/artifact-spec.md` | `templates/research/artifact-spec.md` |
| `research/evaluation-plan.md` | `templates/research/evaluation-plan.md` |
| `research/decision-log.md` | `templates/research/decision-log.md` |
| `research/ai-provenance-log.md` | `templates/research/ai-provenance-log.md` |

Für jedes Ziel gilt:

- **fehlend:** aus der Quelle anlegen und im Manifest als `erstellt` inventarisieren;
- **vorhanden:** Version und SHA-256-Hash prüfen, aber nicht überschreiben, auch nicht wenn die Datei leer ist; als `beibehalten` inventarisieren;
- **Versions- oder Inhaltskonflikt:** Eine abweichende oder fehlende Version oder ein vom Quelltemplate beziehungsweise letzten Inventar abweichender Hash wird nicht migriert; protokolliere Pfad, gefundene Version, Hash, Konflikt und sichere nächste Aktion;
- **erneuter Lauf:** nur weiterhin fehlende Dateien ergänzen.

Damit ist der Ablauf idempotent: persönliche Inhalte bleiben erhalten und ein zweiter Lauf erzeugt keine Duplikate. Das Setup darf auch bei einem späteren Revert keine persönlichen Inhalte unter `research/` löschen.

Beim Erstellen von `research/PROJECT.md` trägst du nur Metadaten ein, die bereits sicher bekannt sind: Setup-/Template-Version, Profil, Schutzbedarf, vorgeschlagener oder offener Methodenstatus, `Assist`, Ausführungspfad, Dateiinventar und Konflikte. Alle Projektdaten bleiben Platzhalter.

### 5. Profilspezifisch abschließen

#### DHBW-Thesis

- Lege `ki-erklaerung.md` nach der README-Vorlage nur an, wenn sie fehlt, und dokumentiere darin den Setup-Beitrag. Eine vorhandene Datei überschreibst du nie.
- Suche offene Platzhalter, erfinde aber keine persönlichen Daten.
- Prüfe die vorhandene Toolchain. Fehlt ein Werkzeug, stoppe ohne Installation und nenne es.
- Führe die vollständige Sequenz aus:

```bash
pdflatex main.tex
biber main
makeglossaries main
pdflatex main.tex
pdflatex main.tex
```

- Prüfe, dass `main.pdf` existiert und nicht leer ist, und kontrolliere `main.log` auf echte Fehler.

#### Unternehmensprojekt und Informatikprojekt

Für diese Profile ist LaTeX keine Voraussetzung. Markiere den Build als `nicht erforderlich` und schließe ein ansonsten erfolgreiches Setup ohne `pdflatex` ab.

### 6. Git Human Gate

Nach dem Erstellen bleibt alles zunächst ungestagt. Zeige:

1. den Git-Zustand vor dem Setup;
2. die exakte Liste eigener neuer oder geänderter Pfade;
3. beibehaltene Dateien und Konflikte;
4. die exakte Staging-Allowlist.

Pauschales Staging mit `git add -A` oder `git add .` ist verboten. Warte auf eine ausdrückliche Staging-Freigabe und stage danach ausschließlich sichtbare, eigene Pfade:

```bash
git add -- research/PROJECT.md research/method-choice.md
```

Ersetze die Beispiel-Allowlist durch die tatsächlich freigegebenen Pfade. Zeige anschließend `git diff --cached --name-only` und `git diff --cached`. Ein Commit benötigt ein zweites ausdrückliches Human Gate. Ein Push findet niemals automatisch statt; zum öffentlichen Vorlagen-Remote ist er verboten.

### 7. Abschlussbericht

Melde kompakt und vollständig:

- Profil;
- Methode und Status (`offen` oder menschlich bestätigt);
- Autonomiestufe;
- Ausführungspfad und Bestätigungsstatus;
- Schutzbedarf;
- erzeugte Dateien;
- übersprungene/beibehaltene Dateien;
- Konflikte mit Version und Hash;
- Build-Ergebnis oder `nicht erforderlich`;
- Remote-Schutzstatus;
- Git-Zustand vorher/nachher und Staging-Allowlist;
- nächsten sicheren Prompt.

Geeigneter nächster Prompt: „Prüfe mit mir Methodenwahl, Datenweg und Human Gates, ohne echte Projektdaten zu importieren.“
