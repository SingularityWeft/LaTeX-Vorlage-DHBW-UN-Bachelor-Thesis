# Design Science Research manuell beginnen

Nutze diesen Pfad nur, wenn die [`Methodenwahl`](templates/research/method-choice.md) DSR menschlich bestätigt hat. Bei offener Wahl kehrst du zum [`Research-Einstieg`](RESEARCH-START.md) zurück.

## Wann aus einem Artefakt Forschung wird

Ein Artefakt allein ist noch kein wissenschaftlicher Beitrag. DSR passt, wenn du ein relevantes Problem untersuchst, ein neuartiges oder begründet verbessertes Artefakt entwickelst, es systematisch evaluierst und nachvollziehbar erklärst, welches übertragbare Wissen daraus entsteht.

Reine Umsetzung liegt näher, wenn du eine bekannte Lösung nach Anforderungen implementierst, nur Funktionstests und Abnahme planst und keinen Wissensbeitrag über den Einzelfall hinaus beanspruchst. Nenne ein solches Vorhaben ehrlich Engineering; füge DSR nicht nur wegen eines Prototyps hinzu.

## Nächste Aktion

Fülle zuerst [`project-brief.md`](templates/research/project-brief.md), [`research-question.md`](templates/research/research-question.md) und [`artifact-spec.md`](templates/research/artifact-spec.md) aus. Halte Wissensbeitrag und Evaluation offen, wenn sie noch nicht begründet sind, und hole ein Human Gate ein.

## Der DSR-Zyklus

### 1. Problem und Relevanz

Beschreibe das praktische Problem, die betroffenen Rollen und die belegte Wissenslücke. Trenne Beobachtungen von Annahmen. Sammle Belege im [`Evidence Log`](templates/research/evidence-log.md).

### 2. Ziel und Forschungsfrage

Formuliere das gewünschte Ergebnis und eine beantwortbare Forschungsfrage. Das Ziel soll weder nur „Software bauen“ noch bereits die Antwort vorwegnehmen.

### 3. Theoretische Grundlage

Dokumentiere Konzepte, Theorien und bisherige Artefakte, aus denen Anforderungen oder Gestaltungsentscheidungen abgeleitet werden. Jede übernommene Aussage braucht eine geprüfte Quelle.

### 4. Artefakt und Gestaltungsbegründung

Beschreibe Artefakt, Zielgruppe, Anforderungen, Grenzen und Version. Verknüpfe zentrale Designentscheidungen mit Problem, Theorie oder Evidenz; technische Funktion allein begründet keinen Wissensbeitrag.

### 5. Wissensbeitrag

Formuliere, was andere aus dem Projekt lernen können: etwa ein begründetes Gestaltungsprinzip, eine Methode, ein Modell oder Wissen über Wirksamkeit und Grenzen. Benenne Geltungsbereich und Neuheitsgrad. Ein nur lokal nützliches Ergebnis darf wertvoll sein, ist aber nicht automatisch ein wissenschaftlicher Beitrag.

### 6. Demonstration

Zeige nachvollziehbar, dass das Artefakt im vorgesehenen Szenario verwendet werden kann. Eine Demonstration belegt Anwendung, aber noch nicht Wirksamkeit oder Übertragbarkeit.

### 7. Explorative Evaluation

Nutze frühe Tests, Pilotfeedback oder Analysen, um Artefakt und Messplan zu verbessern. Halte Änderungen und negative Ergebnisse fest. Explorative Ergebnisse sind vorläufig und dürfen nicht nachträglich als unabhängige Bestätigung ausgegeben werden.

### 8. Gesperrte Bestätigungs-Evaluation

Lege vorab Forschungsfrage, Artefaktversion, Fälle oder Stichprobe, Metriken beziehungsweise Rubrik, Vergleich, Schwellen, Analyse und Stopbedingungen im [`Evaluationsplan`](templates/research/evaluation-plan.md) fest. Markiere diesen Plan als gesperrt. Nach Einsicht in die Bestätigungsergebnisse wird nicht auf denselben Fällen weiter optimiert; Änderungen beginnen eine neue, klar benannte Evaluation. Wissenschaftliche Claims benötigen danach ein Human Gate.

### 9. Grenzen und Kommunikation

Dokumentiere Unsicherheiten, Threats to Validity, fehlende Evidenz, nicht übertragbare Kontexte und verworfene Alternativen. Trenne Ergebnis, Interpretation und Empfehlung. Erfasse die abschließende Entscheidung im [`Decision Log`](templates/research/decision-log.md) und KI-Beiträge im [`AI-Provenance Log`](templates/research/ai-provenance-log.md).

## Human Gates

Mindestens Methodenwahl, Forschungsfrage, Daten-/Ethikfreigabe, Bestätigungs-Evaluation, Wissensclaims und Veröffentlichung werden von der zuständigen menschlichen Rolle bestätigt. Betreuung, Research Owner oder Fachreview können zusätzliche Gates verlangen.

## Methodische Grundlage

Der Pfad orientiert sich an [Hevner et al. (2004)](https://aisel.aisnet.org/misq/vol28/iss1/6/), [Peffers et al. (2007)](https://doi.org/10.2753/MIS0742-1222240302), [Gregor und Hevner (2013)](https://aisel.aisnet.org/misq/vol37/iss2/3/), [Wieringa (2014)](https://doi.org/10.1007/978-3-662-43839-8) und [Venable et al. (2016)](https://doi.org/10.1057/ejis.2014.36). Diese Kurzfassung ersetzt keine Methodenliteratur oder fachliche Betreuung.
