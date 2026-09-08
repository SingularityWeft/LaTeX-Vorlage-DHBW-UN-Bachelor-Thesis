# Profil: DHBW-Thesis

Dieser Pfad hilft dir, eine wissenschaftliche Arbeit methodisch zu dokumentieren. Der LaTeX-Schnellstart im [`README`](../README.md) bleibt dein Publikationsweg; Research-Templates ergänzen ihn, ersetzen aber keine lokalen Vorgaben.

## Als Erstes klären

Fülle vor Projektdaten den [`Data/Ethics Check`](../templates/research/data-ethics-check.md) aus. Bleiben Regeln oder Freigaben unbekannt, markiere sie als `offene lokale Vorgabe` – leite sie nicht aus allgemeinen DHBW-Dokumenten ab.

- **DHBW-Standort:**
- **Studiengang und Prüfungsordnung/Fassung:**
- **Aktuelle lokale Prüfungs- und KI-Regeln:** offen / geprüft, Quelle und Stand:
- **Betreuungsfreigabe für Methode und Vorgehen:** offen / bestätigt:
- **Verlangtes Format der KI-Erklärung oder Dokumentation:** offen / geprüft:
- **Abgabeform und weitere formale Vorgaben:**

## Erwartete Ergebnisse

- bestätigte Methoden- und Autonomiewahl;
- Project Brief und tragfähige Forschungsfrage;
- nachvollziehbare Literatur- und Evidenzbasis;
- dokumentiertes Artefakt oder empirisches Studiendesign;
- Evaluationsplan, Grenzen und Entscheidung;
- fortlaufende KI-Provenance;
- optional die kompilierte Thesis im vorhandenen LaTeX-Root.

## Benötigte Inputs

- abstrakte Problem- und Zielbeschreibung;
- lokaler Studien- und Prüfungskontext;
- verfügbare Zeit, Zugang und erlaubte Datenklassen;
- erwartete wissenschaftliche und praktische Ergebnisse;
- Betreuungshinweise und freigegebene Quellen.

## Zulässige Methodenpfade

- **DSR**, wenn ein neuartiges Artefakt mit Wissensbeitrag entwickelt und evaluiert wird – dann zusätzlich [`DSR-START.md`](../DSR-START.md) nutzen.
- **ADR**, wenn Artefakt, Organisationsintervention und Evaluation beim Dualen Partner untrennbar entstehen.
- **Empirische Forschung**, wenn die Arbeit primär Daten erhebt oder analysiert; bei Softwareforschung den passenden [ACM-SIGSOFT-Standard](https://www2.sigsoft.org/EmpiricalStandards/docs/standards) wählen.
- **Engineering / kein Forschungsprojekt** ist für eine Thesis nur dann tragfähig, wenn die lokale Prüfungsordnung einen anderen wissenschaftlichen Untersuchungsanteil zulässt und die Betreuung das Design bestätigt. Eine reine Implementierung wird nicht automatisch Forschung.

## Templates in Reihenfolge

1. [`method-choice.md`](../templates/research/method-choice.md)
2. [`data-ethics-check.md`](../templates/research/data-ethics-check.md)
3. [`project-brief.md`](../templates/research/project-brief.md)
4. [`research-question.md`](../templates/research/research-question.md)
5. [`evidence-log.md`](../templates/research/evidence-log.md)
6. [`artifact-spec.md`](../templates/research/artifact-spec.md) oder ein passend begründetes empirisches Design
7. [`evaluation-plan.md`](../templates/research/evaluation-plan.md)
8. [`decision-log.md`](../templates/research/decision-log.md) und [`ai-provenance-log.md`](../templates/research/ai-provenance-log.md)

## Human Gates

- lokale Prüfungs-/KI-Regeln und Betreuungsfreigabe;
- Methodenwahl und Forschungsfrage;
- Datenzugang, Einwilligung und Ethik;
- Evaluationsplan vor Datenerhebung;
- wissenschaftliche Claims, KI-Erklärung und Abgabe.

## Erster Prompt

```text
Hilf mir im Assist-Modus, den Project Brief für eine DHBW-Thesis vorzubereiten. Nutze nur meine abstrakte Problembeschreibung. Erfinde keine Standort-, Prüfungs-, Betreuungs- oder KI-Regeln, markiere fehlende lokale Vorgaben als offen und triff keine automatische Methodenentscheidung.
```
