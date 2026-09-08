# Profil: Informatikprojekt

Dieser Pfad eignet sich für Artefaktentwicklung und empirische Studien in Informatik oder Software Engineering. Er funktioniert ohne LaTeX.

## Als Erstes klären

Fülle vor Daten, Repository-Inhalten oder Nutzerbeobachtungen den [`Data/Ethics Check`](../templates/research/data-ethics-check.md) aus. Nutze bis zur Freigabe nur abstrakte oder synthetische Beispiele.

Dokumentiere anschließend alle Runtime-, Modell-, Endpoint-, Tool- und Netzwerkgrenzen im [`Deployment-Manifest`](../templates/research/deployment-manifest.md). Für vertrauliche Inputs beginnt der Pfad mit [`Local/On-Prem`](../execution-tracks/local-on-prem.md).

## Erwartete Ergebnisse

- bestätigte Methodenwahl;
- Project Brief und Forschungs- oder Engineering-Frage;
- Spezifikation eines Artefakts oder Studiendesigns;
- benannte Baseline und versionierte Inputs;
- methodenspezifischer Evaluationsplan;
- reproduzierbare Beschreibung von Umgebung, Daten, Schritten und Ergebnissen;
- Threats to Validity, Decision Log und KI-Provenance.

## Benötigte Inputs

- Problem, Zielgruppe und Anwendungskontext;
- vorhandene Ansätze und Vergleichsbaseline;
- Artefaktidee oder konkreter Studientyp;
- verfügbare Daten, Repositories, Systeme oder Testumgebungen;
- Qualitäts-, Ressourcen- und Risikogrenzen.

## Zulässige Methodenpfade

- **DSR / Design Cycle nach [Wieringa](https://doi.org/10.1007/978-3-662-43839-8)**, wenn ein neuartiges technisches Artefakt entwickelt und mit einem Wissensbeitrag evaluiert wird – dann [`DSR-START.md`](../DSR-START.md) nutzen.
- **Empirischer Zyklus**, wenn eine Wissensfrage durch Datenerhebung und Analyse beantwortet wird. Wähle den konkreten [ACM-SIGSOFT-Standard](https://www2.sigsoft.org/EmpiricalStandards/docs/standards), zum Beispiel Experiment, Benchmarking, Repository Mining, Data Science oder Case Study.
- **ADR**, wenn das Artefakt in einer echten Organisation durch Intervention und Evaluation mitgeformt wird.
- **Engineering / kein Forschungsprojekt**, wenn bekannte Anforderungen implementiert und getestet werden, ohne wissenschaftlichen Erkenntnisclaim.

Design- und empirischer Zyklus können sich ergänzen: Die Artefaktentwicklung beantwortet eine Designfrage, die Evaluation eine Wissensfrage. Methode und Qualitätskriterien bleiben dennoch konkret benannt; eine universelle Checkliste reicht nicht.

## Pflichtangaben für Evaluation

- **Baseline:** Was ist der faire Vergleich und warum?
- **Reproduzierbarkeit:** Welche Versionen, Inputs, Umgebung und Schritte benötigt eine Wiederholung?
- **Threats to Validity:** Welche Konstrukt-, interne, externe und Schlussfolgerungsgrenzen sind für genau dieses Design relevant? Unpassende Kategorien werden nicht mechanisch erzwungen.
- **Stochastik:** Welche Wiederholungen oder begründete Ausnahme sind nötig?

## Templates in Reihenfolge

1. [`method-choice.md`](../templates/research/method-choice.md)
2. [`data-ethics-check.md`](../templates/research/data-ethics-check.md)
3. [`deployment-manifest.md`](../templates/research/deployment-manifest.md)
4. [`project-brief.md`](../templates/research/project-brief.md)
5. [`research-question.md`](../templates/research/research-question.md)
6. [`evidence-log.md`](../templates/research/evidence-log.md)
7. [`artifact-spec.md`](../templates/research/artifact-spec.md), sofern ein Artefakt entsteht
8. [`evaluation-plan.md`](../templates/research/evaluation-plan.md)
9. [`decision-log.md`](../templates/research/decision-log.md) und [`ai-provenance-log.md`](../templates/research/ai-provenance-log.md)

## Human Gates

- Daten-, Repository-, Lizenz- und Ethikfreigabe;
- Methode, Forschungsfrage und ACM-SIGSOFT-Standard;
- Baseline, Evaluationsplan und Bestätigungsfälle;
- Ergebnisinterpretation, Threats to Validity und Claims;
- Veröffentlichung und Reproduktionspaket.

## Erster Prompt

```text
Hilf mir im Assist-Modus, ein Informatikprojekt einzuordnen. Trenne Designfrage und Wissensfrage, frage nach Artefakt, Daten, Baseline und Studientyp und schlage passende ACM-SIGSOFT-Standards nur als zu prüfende Optionen vor. Triff keine automatische Methodenentscheidung.
```
