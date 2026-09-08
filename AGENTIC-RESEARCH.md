# Begrenztes Agentic Research

## Darf ein Lauf starten?

**Kurzantwort:** Nur wenn alle folgenden Punkte vor dem ersten Versuch sichtbar dokumentiert und menschlich freigegeben sind.

- [ ] `research/research-program.md` wurde aus [`templates/research/research-program.md`](templates/research/research-program.md) erstellt und trägt den Status `freigegeben`.
- [ ] Mindestens ein versionierter Eval Case aus [`templates/research/eval-case.md`](templates/research/eval-case.md) existiert.
- [ ] Profil, Methode, Schutzbedarf, Datenweg und Data/Ethics Gate sind bestätigt.
- [ ] Schreibpfade, erlaubte Tools und Netzwerkzugriffe sind exakt begrenzt.
- [ ] Baseline, Ziel, Hypothese, Metriken, Schwellen und Stopbedingungen stehen vorab fest.
- [ ] Versuchs-, Zeit-, Kosten- und Ressourcenbudget sind endlich.
- [ ] Bei nichtdeterministischen Ergebnissen sind mehrere Repeats vorgesehen oder eine begründete Ausnahme ist dokumentiert.
- [ ] Explorations- und Bestätigungs-Evals sind getrennt; der ausführende Agent kann Bestätigungs-Evals nicht schreiben.
- [ ] Ausführende Rolle, getrennte Evaluator-Rolle und menschlicher Research Owner sind benannt.

Fehlt ein Punkt, startet kein autonomer Lauf. Der sichere Zustand ist `Assist`. Ein Agent darf dann beim Ausfüllen helfen, aber nicht iterieren.

## Was „Agentic Research“ hier bedeutet

Agentic Research ist ein **Ausführungsmodus innerhalb einer bereits gewählten Methode**. Es ist weder ein Synonym für Design Science Research noch autonome wissenschaftliche Autorenschaft. Forschungsfrage, Methodenwahl, Datenfreigabe, Interpretation, Claims, Promotion und Veröffentlichung bleiben menschlich verantwortet.

Die Stufen aus [`RESEARCH-START.md`](RESEARCH-START.md) gelten weiter:

- **Assist:** Vorschläge ohne selbstständige Versuchsfolge; Safe Default.
- **Co-execute:** genau ein bestätigter Schritt, danach menschliche Prüfung.
- **Bounded autonomous:** mehrere Versuche nur innerhalb eines freigegebenen Research Programs und bis zur ersten Stopbedingung.

## Rollen und Trennung

| Rolle | Darf | Darf nicht |
|---|---|---|
| Research Owner | Programm, Budget, Datenweg, Claims und Promotion freigeben | Verantwortung an den Agenten abgeben |
| Ausführende Agentenrolle | erlaubte Dateien ändern, Versuche committen, Explorations-Evals ausführen und Records schreiben | Bestätigungs-Evals ändern, Scope erweitern oder Claims freigeben |
| Evaluator-Rolle | gesperrte Bestätigungs-Evals nach dem vorab festgelegten Plan einmalig ausführen und dokumentieren | Explorationsfeedback zur weiteren Optimierung zurückspielen |
| Fach-/Methodenreview | Rubrik, Interpretation, Geltungsgrenzen und menschliche Stichprobe prüfen | ungeprüfte Scores als Evidenz akzeptieren |

„Getrennt“ bezeichnet mindestens getrennte Berechtigungen und einen getrennten Arbeitskontext. Dieselbe Person darf Rollen nacheinander übernehmen, muss den Rollenwechsel und mögliche Interessenkonflikte aber dokumentieren.

## Zusätzliche Gates je Profil

| Profil | Kurzes Beispiel | Zusätzlich vor dem Start prüfen | Sofort stoppen, wenn |
|---|---|---|---|
| DHBW-Thesis | Varianten eines Artefakts explorativ vergleichen | Betreuung, Prüfungs-/KI-Vorgaben, Forschungsfrage und Evaluationsplan | Eigenständigkeit, Zulässigkeit oder Claim-Verantwortung unklar sind |
| Unternehmensprojekt | einen abstrakten Pilotprozess gegen eine Baseline prüfen | Business Owner, Daten-/Security-Verantwortung, Akzeptanz- und Risikokriterien | Datenweg, Eingriffsrecht oder verantwortliche Entscheidung fehlt |
| Informatikprojekt | eine Prompt-, Modell- oder Implementierungsvariante vergleichen | Studientyp, reproduzierbare Baseline, Harness und Threats to Validity | mehr als die geplante Variable wechselt oder Versionen fehlen |

Die Methode wird dadurch nicht automatisch bestimmt. Alle drei Profile nutzen dieselben endlichen Budgets, Zustände, Records und Promotion-Gates.

## Verzeichnisvertrag

```text
artifact/                 # nur vorab erlaubte Artefaktdateien
evals/
├── README.md             # Eval- und Sperrvertrag
├── exploration/          # sichtbare, versionierte Entwicklungs-Evals
└── confirmation/         # gesperrte Bestätigungs-Evals; nur Evaluator schreibt
research/
├── research-program.md   # freigegebener Vertrag der Vergleichsserie
└── experiments/          # ein Experiment Record pro Versuch
runs/
├── README.md             # Append-only- und Datenschutzvertrag
└── <series-id>/          # ein unveränderlicher Run Record pro Repeat
```

- Der ausführende Agent schreibt nur in die im Research Program einzeln genannten Pfade unter `artifact/`, `research/experiments/` und `runs/`.
- Explorationsdefinitionen liegen unter `evals/exploration/`; die getrennt gesperrten Bestätigungsdefinitionen liegen unter `evals/confirmation/`.
- Freigegebene Eval-Definitionen sind während einer Vergleichsserie unveränderlich.
- `evals/confirmation/` ist für die ausführende Rolle nicht beschreibbar und wird möglichst nicht in ihren Arbeitskontext gegeben.
- Rohoutputs und Traces werden referenziert, nicht ungeprüft in öffentliche Records kopiert.
- Persönliche oder vertrauliche Research-Inhalte werden weder beim Abbruch noch bei einem Revert gelöscht.

## Vertrag einer Vergleichsserie

Eine Vergleichsserie verändert genau **eine vorab benannte Variable**, zum Beispiel Artefaktlogik, Modell oder Prompt. Alle anderen Faktoren bleiben versioniert konstant. Sind mehrere Variablen technisch untrennbar, wird die Konfundierung vor dem Lauf sichtbar dokumentiert.
Für jede Serie gelten ein Experiment-Branch und ein Commit pro Versuch.

Vor dem Start hält das [`Research Program`](templates/research/research-program.md) fest:

1. Ziel, Forschungsfrage, Hypothese und Baseline;
2. veränderte Variable und konstant gehaltene Faktoren;
3. Artefakt-, Modell-/Runtime-, Prompt-, Harness-, Daten- und Eval-Version;
4. qualitative, quantitative oder gemischte Metriken samt Schwellen;
5. Repeats, Seeds, Aggregation, Streuungs- und Stabilitätsbericht;
6. erlaubte Schreibpfade, Tools, Netzwerk- und Datenklassen;
7. Zeit-, Versuchs-, Kosten-, Token- und Ressourcenbudget;
8. Stopbedingungen, Rollen und Human Gates.

Ändern sich Daten, Prompt, Harness oder Eval-Definition, endet die Vergleichbarkeit. Die Änderung erhält eine neue Version und eine neue Serien-ID; frühere Scores werden nicht fortgeschrieben oder gemeinsam gerankt.

## Ablauf eines begrenzten Loops

1. **Start-Gate:** Research Owner bestätigt Research Program, Eval Cases und Schutzpfad.
2. **Serie eröffnen:** Ein neuer Branch `experiment/<series-id>` wird von einem dokumentierten Ausgangscommit erstellt. Existiert er bereits, stoppt der Start.
3. **Baseline:** Baseline mit den geplanten Repeats ausführen und als Run Records festhalten.
4. **Versuch definieren:** Hypothese, einzige Änderungsvariable und erwartetes Signal im Experiment Record eintragen.
5. **Änderung committen:** Genau die erlaubten Pfade ändern und einen Versuch-Commit erstellen. Der Commit ist Teil der vorab freigegebenen Serie; ein Push ist nicht erlaubt.
6. **Exploration ausführen:** Sichtbare Explorations-Evals gemäß Wiederholungsplan ausführen. Für jeden Repeat einen [`Run Record`](templates/research/run-record.md) schreiben.
7. **Entscheiden:** Ergebnis mit Baseline, Schwellen, Streuung, Kosten, Risiken und Komplexität vergleichen und einen Zustand setzen.
8. **Fortsetzen oder stoppen:** Nur `candidate-keep` darf Basis des nächsten Versuchs werden. Budgetende, Scope-Verstoß, Sicherheitsereignis oder Unsicherheit stoppen die Serie.
9. **Bestätigen:** Genau die im Programm vorgesehene Kandidatenversion wird von der getrennten Evaluator-Rolle einmal nach dem gesperrten Plan geprüft.
10. **Promotion-Gate:** Nur der Research Owner kann nach Fachreview auf `promoted` setzen. Ein Score erzeugt weder automatisch einen Claim noch eine Veröffentlichung.

## Zustände

| Zustand | Bedeutung | Nächste Aktion |
|---|---|---|
| `candidate-keep` | Explorativ besser und innerhalb aller Grenzen | im Experiment-Branch behalten; noch kein Claim |
| `discard` | Schwelle verfehlt, schlechter oder unverhältnismäßig komplex | normalen Revert-Commit erstellen; Evidenz behalten |
| `crash` | technischer Laufabbruch | Fehler und Ressourcen dokumentieren; Budgetregel anwenden |
| `inconclusive` | Evidenz reicht nicht oder Streuung ist zu groß | stoppen oder neues menschlich freigegebenes Design |
| `human-review` | Scope-, Sicherheits-, Eval- oder Vertragsgrenze berührt | sofort stoppen und Research Owner entscheiden lassen |
| `promoted` | Bestätigungsplan bestanden und menschlich freigegeben | begrenzte Übernahme; Claims separat prüfen |

Ein verworfener Versuch bleibt durch Versuch-Commit, normalen Revert-Commit, Experiment Record, Run Records und Begründung referenzierbar. `git reset --hard`, Force Push sowie das Löschen negativer oder unklarer Evidenz sind verboten.

## Exploration und Bestätigung

### Explorations-Evals

Explorations-Evals sind für die ausführende Rolle sichtbar. Sie helfen beim Entwickeln, dürfen aber keine wissenschaftliche Bestätigung vortäuschen. Eine Verbesserung führt höchstens zu `candidate-keep`.

### Bestätigungs-Evals

Bestätigungs-Evals werden vor der Serie versioniert und gesperrt. Der ausführende Agent erhält keinen Schreibzugriff und möglichst keine Fälle oder erwarteten Antworten. Die getrennte Evaluator-Rolle führt den vorab geplanten Check einmalig aus. Ergebnisse werden nicht zur weiteren Optimierung zurückgespielt; weitere Änderungen beginnen eine neue Serie.

## Wiederholungen und Auswertung

Bei nichtdeterministischen Systemen sind mindestens zwei Läufe erforderlich. Eine Einzelmessung ist nur mit sichtbarer methodischer Begründung zulässig und darf keine Reproduzierbarkeit behaupten.

Der Experiment Record berichtet:

- alle Einzelwerte mit Seed oder Repeat-ID;
- Lagewert, Streuung und Wertebereich;
- Stabilitätsgrenzen, Ausreißer und fehlgeschlagene Runs;
- Latenz, Kosten und Ressourcen neben der Qualitätsmetrik.

## Qualitative Evaluation und LLM-Grader

Eine menschliche Rubrik ist für qualitative DSR-Evaluation zulässig, wird aber nicht als objektiver Benchmark bezeichnet. Kriterien, Skala, Bewertungsrolle und Unsicherheiten müssen versioniert sein.

Wenn ein LLM als Grader dient, dokumentiert der Eval Case:

- Modell und sichtbare Version;
- vollständige Prompt- und Rubrikversion;
- Kalibrierungsfälle mit bekannter Ground Truth;
- Übereinstimmung und Abweichungen gegenüber menschlicher Bewertung;
- bekannte Biases und Größe der menschlichen Stichprobe.

Ohne Kalibrierung bleibt das Ergebnis `inconclusive` oder geht in `human-review`.

## Run Records und Datenschutz

Jeder Versuch und jeder Repeat wird dokumentiert – auch Crashs, Discards und unklare Ergebnisse. Ein [`Run Record`](templates/research/run-record.md) enthält Commit, Konfiguration, abstrakte Inputs, Modell/Runtime, Prompt/Harness, Daten-/Eval-Version, Seed/Repeat-ID, Ergebnis, Rohoutput-/Trace-Referenz, Artefakte, Ressourcen, Latenz, Kosten und Fehlerstatus.

Records minimieren Rohdaten, enthalten keine Secrets und verweisen bei geschützten Quellen nur auf freigegebene Speicherorte oder IDs. Zugriff und Aufbewahrung werden angegeben. Vertrauliche Inputs dürfen ausschließlich einen nach SPEC-03 freigegebenen Track verwenden und nie in das öffentliche Git gelangen.

## Sofortige Stopbedingungen

Der Lauf stoppt mit `human-review`, sobald:

- ein Schreibpfad, Tool, Netzwerkziel oder Datenzugriff nicht erlaubt ist;
- eine freigegebene Eval-, Prompt-, Harness- oder Datenversion still geändert werden soll;
- ein Bestätigungs-Eval geändert, eingesehen oder zur Optimierung verwendet werden soll;
- ein Budget erreicht oder nicht mehr zuverlässig messbar ist;
- ein Secret, personenbezogenes Datum oder vertraulicher Inhalt im Record droht;
- die Auswertung nicht eindeutig, die Streuung nicht vertretbar oder ein Sicherheitsereignis möglich ist.

Ein `crash` verbraucht einen Versuch, sofern das Research Program keine engere, vorab definierte Wiederholungsregel für reine Infrastrukturfehler enthält.

## Nächster sicherer Prompt

```text
Hilf mir im Assist-Modus, ein Research Program und mindestens einen Eval Case auszufüllen. Starte keinen Lauf, bis alle Gates sichtbar bestätigt sind.
```

## Quellen und Abgrenzung

- Andrej Karpathy: [`autoresearch` program.md](https://github.com/karpathy/autoresearch/blob/master/program.md) – Implementierungsinspiration für engen Änderungsraum, feste Laufzeit und Versuch-Logging; kein wissenschaftlicher Methodenbeleg.
- Venable, Pries-Heje und Baskerville: [FEDS](https://doi.org/10.1057/ejis.2014.36) – methodengerechte DSR-Evaluationsstrategien.
- Yehudai et al.: [A Survey on Evaluation of LLM-based Agents](https://aclanthology.org/2026.findings-acl.1330/) – mehrdimensionale Agenten-Evaluation einschließlich Kosten, Sicherheit und Robustheit.
- Du et al.: [DeepResearch Bench](https://arxiv.org/abs/2506.11763) – getrennte Qualitäts- sowie Quellen-/Zitationsmetriken für Deep-Research-Systeme.
