# Profil: Unternehmensprojekt

Dieser Pfad eignet sich für einen Forschungs- oder Pilotauftrag im Unternehmen. Er funktioniert ohne LaTeX und beginnt ohne echte Geschäfts-, Kontakt- oder Personendaten.

## Als Erstes klären

Fülle vor jedem Datenimport den [`Data/Ethics Check`](../templates/research/data-ethics-check.md) aus. Bis Schutzbedarf, zulässiger Datenweg und Owner bestätigt sind, verwendest du nur abstrakte oder synthetische Beschreibungen.

## Erwartete Ergebnisse

- bestätigte Methodenwahl oder bewusstes Pilot-/Engineering-Design;
- Project Brief mit Businessziel und Forschungsanspruch;
- Artefakt- oder Interventionsbeschreibung;
- Business-, Akzeptanz- und Risikokriterien;
- Evaluationsplan und Evidence Log;
- Decision Memo im Decision Log: fortsetzen, ändern, stoppen oder weitere Evidenz erheben;
- KI-Provenance und klar benannte Grenzen.

## Benötigte Inputs

- abstraktes Geschäftsproblem und gewünschte Entscheidung;
- Sponsor-, Research-Owner- und betroffene Rollen ohne Personennamen;
- erwarteter Nutzen und nicht akzeptable Schäden;
- verfügbare Zeit, Systeme und Datenklassen;
- bestehende Baseline oder heutiger Prozess.

## Zulässige Methodenpfade

- **DSR**, wenn ein neuartiges Artefakt mit begründetem Wissensbeitrag entwickelt und evaluiert wird – dann [`DSR-START.md`](../DSR-START.md) nutzen.
- **ADR**, wenn Bauen, organisatorische Intervention und Evaluation im laufenden Betrieb untrennbar sind.
- **Empirischer Pilot**, wenn eine vorab formulierte Frage mit Daten beantwortet wird, ohne einen DSR-Wissensbeitrag zu behaupten.
- **Engineering / kein Forschungsprojekt**, wenn eine bekannte Lösung umgesetzt und gegen Liefer- und Akzeptanzkriterien abgenommen wird.

Ein Pilot ist nicht automatisch Forschung. Dokumentiere, ob das Ziel eine lokale Geschäftsentscheidung, ein wissenschaftlicher Beitrag oder beides ist.

## Kriterien

- **Businesskriterien:** Welche Entscheidung oder Verbesserung soll ermöglicht werden?
- **Akzeptanzkriterien:** Woran erkennt der Auftraggeber eine brauchbare Lieferung?
- **Risikokriterien:** Welche Datenschutz-, Sicherheits-, Fairness-, Betriebs- oder Reputationsgrenze darf nicht überschritten werden?
- **Stopkriterien:** Wann wird der Pilot pausiert oder beendet?

## Templates in Reihenfolge

1. [`method-choice.md`](../templates/research/method-choice.md)
2. [`data-ethics-check.md`](../templates/research/data-ethics-check.md)
3. [`project-brief.md`](../templates/research/project-brief.md)
4. [`research-question.md`](../templates/research/research-question.md), falls ein Forschungs- oder Erkenntnisziel besteht
5. [`evidence-log.md`](../templates/research/evidence-log.md)
6. [`artifact-spec.md`](../templates/research/artifact-spec.md)
7. [`evaluation-plan.md`](../templates/research/evaluation-plan.md)
8. [`decision-log.md`](../templates/research/decision-log.md) und [`ai-provenance-log.md`](../templates/research/ai-provenance-log.md)

## Human Gates

- Schutzbedarf, Datenzugang und zulässiger Verarbeitungsweg;
- Research Owner bestätigt Methode und Forschungsanspruch;
- Business Owner bestätigt Nutzen-, Akzeptanz-, Risiko- und Stopkriterien;
- Fach-/Ethik-/Datenschutzreview, soweit erforderlich;
- Bestätigungs-Evaluation, Claims und externe Kommunikation.

## Erster Prompt

```text
Hilf mir im Assist-Modus, einen abstrakten Project Brief für ein Unternehmensprojekt zu erstellen. Frage nach Businessentscheidung, Forschungsanspruch, Baseline, Akzeptanz- und Risikokriterien. Verwende keine echten Unternehmens- oder Personendaten und lasse Methode sowie Datenweg bis zum Human Gate offen.
```
