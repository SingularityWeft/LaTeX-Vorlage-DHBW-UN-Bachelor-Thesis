# Research Program

- **Template-Version:** `research-program-v1`
- **Status:** Entwurf / freigegeben / gestoppt / abgeschlossen
- **Serien-ID:** [eindeutig, zum Beispiel `series-YYYYMMDD-kurzname-v1`]
- **Erstellt am:** YYYY-MM-DD
- **Freigegeben am:** YYYY-MM-DD

> Ohne Status `freigegeben`, mindestens einen freigegebenen Eval Case und vollständig bestätigte Gates startet kein `Bounded autonomous`-Lauf.

## 1. Forschungs- und Vergleichsziel

- **Profil:** DHBW-Thesis / Unternehmensprojekt / Informatikprojekt
- **Methodenpfad und Status:**
- **Forschungsfrage oder Entscheidungsfrage:**
- **Praktisches Ziel:**
- **Hypothese:**
- **Baseline mit Commit und Version:**
- **Erwartetes Signal:**
- **Was der Vergleich ausdrücklich nicht belegt:**

## 2. Vergleichsvertrag

- **Einzige veränderte Variable:**
- **Konstant gehaltene Faktoren:**
- **Unvermeidbare Konfundierung und Auswirkung:** keine / [Begründung]
- **Modellvergleich oder Harnessvergleich:**
- **Direkt vergleichbare Serien:**
- **Nicht vergleichbare frühere Serien:**

Ändert sich während der Serie Daten-, Prompt-, Harness- oder Eval-Version, endet diese Serie. Lege eine neue Serien-ID an und führe frühere Scores nicht als direkt vergleichbar fort.

## 3. Versionen und Inputs

| Bestandteil | ID/Version | Hash oder Commit | Speicherort/Referenz | Während der Serie |
|---|---|---|---|---|
| Artefakt/Baseline |  |  |  | veränderlich nur laut Scope |
| Modell und Runtime |  |  |  | konstant / Vergleichsvariable |
| Prompt |  |  |  | konstant / Vergleichsvariable |
| Harness |  |  |  | konstant / Vergleichsvariable |
| Daten |  |  |  | konstant |
| Explorations-Evals |  |  | `evals/exploration/` | gesperrt nach Start |
| Bestätigungs-Evals |  |  | `evals/confirmation/` | gesperrt; Executor ohne Schreibzugriff |
| Rubrik/Grader |  |  |  | konstant |

## 4. Erlaubter Ausführungsraum

### Schreibpfade – exakte Allowlist

- `artifact/[Pfad]`
- `research/experiments/[Pfad]`
- `runs/[Serien-ID]/[Pfad]`

### Nur lesbare Pfade

- [Pfad]

### Verbotene oder ausgeblendete Pfade

- `evals/confirmation/` für die ausführende Agentenrolle
- [weitere Pfade]

### Tools und Aktionen

- **Erlaubte Tools/Befehle:**
- **Verbotene Tools/Befehle:**
- **Git:** Branch `experiment/[Serien-ID]`; Commit pro Versuch; kein Push; kein Reset; Discard nur per normalem Revert-Commit
- **Installationen/Downloads:** aus / einzeln freigegeben:

### Netzwerk und Daten

- **Schutzbedarf:** öffentlich / intern / vertraulich/Geschäftsgeheimnis
- **Freigegebener Track:**
- **Erlaubte Netzwerkziele:** keine / exakte Allowlist:
- **Erlaubte Datenklassen:**
- **Nicht erlaubte Datenklassen:**
- **Data/Ethics Gate und bestätigende Rolle:**
- **Private-Track-Preflight gemäß Root-Dateien `LOCAL-PRIVATE-SETUP.md` und `SECURITY.md`:** nicht erforderlich / offen / bestätigt
- **Deployment-Manifest-Version und Hash:**

## 5. Evaluation

### Explorativ

- **Eval-Case-IDs und Versionen:**
- **Quantitative Metriken und Richtung:**
- **Qualitative Rubrik und Skala:**
- **Schwellen für `candidate-keep`:**
- **Komplexitäts-, Kosten- und Sicherheitskriterien:**

### Bestätigung

- **Gesperrte Eval-Case-IDs und Versionen:**
- **Geplanter einmaliger Ausführungszeitpunkt:**
- **Evaluator-Rolle:**
- **Schwellen für eine Promotionsprüfung:**
- **Regel:** Kein Feedback zur weiteren Optimierung; jede Folgeänderung startet eine neue Serie.

### Grader und Kalibrierung

- **Grader-Typ:** deterministisch / menschlich / LLM / gemischt
- **Grader-Modell und Version, falls LLM:**
- **Prompt-/Rubrikversion:**
- **Kalibrierungsfälle mit bekannter Ground Truth:**
- **Ergebnis der Kalibrierung:**
- **Bekannte Biases:**
- **Menschliche Stichprobe und prüfende Rolle:**

## 6. Wiederholungsplan

- **Nichtdeterministisch:** ja / nein
- **Anzahl Repeats:** [mindestens 2 bei ja]
- **Seeds oder Repeat-IDs:**
- **Reihenfolge/Randomisierung:**
- **Zusammenfassung:** Lagewert, Streuung, Min/Max und Crash-Anteil
- **Stabilitätsgrenze:**
- **Begründete Ausnahme bei nur einem Lauf:**

## 7. Endliche Budgets

| Budget | Pro Lauf | Gesamte Serie | Messquelle |
|---|---:|---:|---|
| Versuche | 1 |  | Experiment Records |
| Wall-Clock-Zeit |  |  | Start-/Endzeit |
| Kosten |  |  | Provider-/lokales Kostenprotokoll |
| Tokens/Anfragen |  |  | Run Record |
| Rechenressourcen |  |  | Laufzeitmetrik |

Ein `crash` verbraucht einen Versuch, außer eine eng beschriebene Infrastruktur-Ausnahme wurde vorab freigegeben:

## 8. Stopbedingungen

Der Lauf stoppt spätestens bei:

- [ ] Versuchs-, Zeit-, Kosten- oder Ressourcenbudget erreicht
- [ ] Änderung oder Zugriff außerhalb der Allowlist
- [ ] versuchte Änderung/Einsicht eines Bestätigungs-Evals
- [ ] stille Änderung an Prompt, Harness, Daten oder Eval
- [ ] Datenschutz-, Secret-, Lizenz- oder Sicherheitsrisiko
- [ ] zu großer Streuung, widersprüchlicher Evidenz oder unklarer Interpretation
- [ ] manueller Stopp durch Research Owner
- [ ] weiterer projektspezifischer Bedingung:

Der resultierende Zustand ist `human-review`, sofern nicht eindeutig `crash` oder `inconclusive` zutrifft.

## 9. Rollen und Human Gates

- **Research Owner:**
- **Ausführende Agentenrolle:**
- **Getrennte Evaluator-Rolle:**
- **Fach-/Methodenreview:**
- **Interessenkonflikte oder Rollenkombinationen:**

### Start-Gate

- [ ] Research Program vollständig
- [ ] Eval Cases versioniert und freigegeben
- [ ] Bestätigungs-Evals für Executor nicht beschreibbar
- [ ] Datenweg und Data/Ethics Gate bestätigt
- [ ] Budgets und Stopbedingungen bestätigt
- [ ] Research Owner hat `Bounded autonomous` für exakt diese Serien-ID freigegeben

**Bestätigende Person/Rolle, Datum und Begründung:**

### Promotion-Gate

- **Kandidatencommit:**
- **Bestätigungs-Ergebnis:**
- **Fachreview:**
- **Entscheidung:** offen / promoted / nicht promoted
- **Bestätigende Person/Rolle, Datum und Grenzen:**
