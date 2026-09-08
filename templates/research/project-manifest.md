# Research Project Manifest

- **Template-Version:** `research-project-v3`
- **Setup-Version:** `research-setup-v2`

> Dieses Manifest dokumentiert die sichere Einrichtung. Bis zum bestätigten Data/Ethics Gate nur abstrakte oder synthetische Angaben eintragen; keine Namen, Unternehmensgeheimnisse, personenbezogenen Daten, Zugangsdaten oder vertraulichen Dokumentinhalte.

## 1. Gewählte Route

- **Profil:** [DHBW-Thesis / Unternehmensprojekt / Informatikprojekt]
- **Quellprofil:** [`profiles/dhbw-thesis.md` / `profiles/unternehmensprojekt.md` / `profiles/informatikprojekt.md`]
- **Schutzbedarf:** [öffentlich / intern / vertraulich/Geschäftsgeheimnis]
- **Methodenpfad:** [offen / DSR / ADR / empirische Softwareforschung / Engineering – kein Forschungsprojekt]
- **Methodenstatus:** [offen / menschlich bestätigt]
- **Abstrakte Begründung:** [Platzhalter]
- **Autonomiestufe:** `Assist`
- **Ausführungspfad:** [Cloud-managed comfort / Hybrid-redacted / Local/On-Prem]
- **Pfadstatus:** [sicherer Default / menschlich bestätigt]
- **Externe Verarbeitung:** [nicht gestartet / aus bis Freigabe]
- **Data/Ethics Gate:** [offen / bestätigt mit Grenzen]

Wenn Methode oder Datenweg nicht eindeutig sind, bleiben sie offen. Das Setup trifft keine automatische Methodenentscheidung. `Bounded autonomous` ist ohne den Vertrag aus der Root-Datei `AGENTIC-RESEARCH.md` und ein bestätigtes Research Program nicht zulässig.

## 2. Abstrakter Projektsteckbrief

- **Problemklasse:** [abstrakter Platzhalter]
- **Erkenntnisziel:** [abstrakter Platzhalter]
- **Mögliches Artefakt oder Untersuchungsobjekt:** [abstrakter Platzhalter]
- **Vorgesehene Evaluation:** [abstrakter Platzhalter]
- **Lokale Prüfungs-, Organisations- oder Repository-Vorgaben:** [noch zu prüfen]

## 3. Human Gates

| Gate | Status | Bestätigende Rolle | Datum | Grenzen oder nächste Aktion |
|---|---|---|---|---|
| Profil und Methode | offen | – | – | Methodenwahl gemeinsam prüfen |
| Autonomiestufe | `Assist` | – | – | Abweichung ausdrücklich begründen |
| Research Program | nicht freigegeben | – | – | Vor `Bounded autonomous` den Vertrag aus `AGENTIC-RESEARCH.md` erfüllen |
| Daten und Ethik | offen | – | – | Vor echten Daten `data-ethics-check.md` abschließen |
| Ausführungspfad | sicherer Default | – | – | Datenweg vor externer Verarbeitung bestätigen |
| Deployment/Security | nicht freigegeben | – | – | Vor echten Daten `deployment-manifest.md` und passenden Track prüfen |
| Git-Staging | offen | – | – | Exakte Allowlist anzeigen |
| Git-Commit | offen | – | – | Gestagten Diff separat freigeben |

## 4. Dateiinventar

Für jede Setup-Zieldatei Status, Quellversion und SHA-256-Hash dokumentieren. Erlaubte Statuswerte: `erstellt`, `beibehalten`, `Konflikt`.

| Zielpfad | Quelle | Template-Version | SHA-256 | Status | Hinweis |
|---|---|---|---|---|---|
| `research/PROJECT.md` | `templates/research/project-manifest.md` | `research-project-v3` | [Hash] | [Status] | [Hinweis] |
| `research/method-choice.md` | `templates/research/method-choice.md` | `research-template-v2` | [Hash] | [Status] | [Hinweis] |
| `research/data-ethics-check.md` | `templates/research/data-ethics-check.md` | `research-template-v1` | [Hash] | [Status] | [Hinweis] |
| `research/project-brief.md` | `templates/research/project-brief.md` | `research-template-v1` | [Hash] | [Status] | [Hinweis] |
| `research/research-question.md` | `templates/research/research-question.md` | `research-template-v1` | [Hash] | [Status] | [Hinweis] |
| `research/evidence-log.md` | `templates/research/evidence-log.md` | `research-template-v1` | [Hash] | [Status] | [Hinweis] |
| `research/artifact-spec.md` | `templates/research/artifact-spec.md` | `research-template-v1` | [Hash] | [Status] | [Hinweis] |
| `research/evaluation-plan.md` | `templates/research/evaluation-plan.md` | `research-template-v1` | [Hash] | [Status] | [Hinweis] |
| `research/decision-log.md` | `templates/research/decision-log.md` | `research-template-v1` | [Hash] | [Status] | [Hinweis] |
| `research/ai-provenance-log.md` | `templates/research/ai-provenance-log.md` | `research-template-v1` | [Hash] | [Status] | [Hinweis] |
| `research/deployment-manifest.md` | `templates/research/deployment-manifest.md` | `deployment-manifest-v1` | [Hash] | [Status] | [Hinweis] |

## 5. Konfliktprotokoll

Bestehende Dateien werden nie automatisch überschrieben oder migriert.

| Pfad | Gefundene Version | SHA-256 | Konflikt | Sichere nächste Aktion |
|---|---|---|---|---|
| [Pfad oder „keine“] | [Version] | [Hash] | [Beschreibung] | [menschlich prüfen / getrennte Migration planen] |

## 6. Setup-Bericht

- **Setup-Datum:** YYYY-MM-DD
- **Erzeugte Dateien:** [Liste]
- **Beibehaltene Dateien:** [Liste]
- **Konflikte:** [Liste oder keine]
- **Build:** [erfolgreich / fehlgeschlagen / nicht erforderlich]
- **Remote-Schutz:** [öffentliches Vorlagen-Remote – Push verboten / eigenes Remote / kein Remote]
- **Git-Zustand vorher:** [geändert / gestagt / unversioniert getrennt aufführen]
- **Git-Zustand nachher:** [Setup-Dateien weiterhin ungestagt / nach Human Gate exakt gestagt]
- **Staging-Allowlist:** [exakte Pfade oder keine]
- **Nächster sicherer Prompt:** „Prüfe mit mir Methodenwahl, Datenweg und Human Gates, ohne echte Projektdaten zu importieren.“
