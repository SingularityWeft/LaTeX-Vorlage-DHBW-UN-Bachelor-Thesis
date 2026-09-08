# Einstieg in AI-supported Research

## Welchen Weg brauche ich?

Du musst die Methodennamen noch nicht kennen. Beschreibe dein Vorhaben zunächst ohne vertrauliche Unternehmensdaten oder personenbezogene Angaben und prüfe diese vier Fragen:

1. Willst du etwas Neues entwerfen und daraus eine übertragbare Erkenntnis gewinnen?
2. Entsteht die Lösung erst dadurch, dass sie in einer Organisation eingesetzt, verändert und gleichzeitig bewertet wird?
3. Willst du Daten über Software, Entwicklung oder Nutzung sammeln und auswerten?
4. Oder willst du vor allem eine bekannte Lösung zuverlässig umsetzen?

Die Antworten geben eine Richtung vor, aber keine automatische Entscheidung. Öffne als Nächstes [`templates/research/method-choice.md`](templates/research/method-choice.md), fülle die Kurzfelder aus und lasse Methodenwahl und Autonomiestufe von einem Menschen bestätigen.

## Schnellentscheidung

| Wenn dein Hauptziel so aussieht ... | Prüfe zuerst ... | Passt nicht, wenn ... | Nächste Aktion |
|---|---|---|---|
| Du entwickelst und evaluierst ein neuartiges Artefakt – zum Beispiel ein Modell, eine Methode oder Software – und willst einen begründeten Wissensbeitrag über den Einzelfall hinaus liefern. | **Design Science Research (DSR)** | du nur eine bekannte Lösung implementierst, ohne Forschungsfrage, systematische Evaluation oder Wissensbeitrag. | Benenne Artefakt, Wissenslücke, erwarteten Beitrag und Evaluation im Methodenwahl-Template. |
| Bauen, betrieblicher Einsatz und Evaluation verändern sich wechselseitig und lassen sich im Organisationskontext nicht sinnvoll trennen. | **Action Design Research (ADR)** | das Artefakt außerhalb einer echten organisatorischen Intervention entwickelt und erst später separat getestet wird oder gar keine Intervention stattfindet. | Beschreibe Organisation, Intervention, Beteiligte und gleichzeitige Evaluation nur abstrakt; kläre Details erst nach dem Schutzbedarfs-Gate. |
| Du erhebst oder analysierst Daten über Software, Entwicklungsprozesse oder Nutzung – etwa in einem Experiment, Benchmark, Repository-Mining oder einer Fallstudie. | **Empirische Softwareforschung** | du keine Daten erhebst oder analysierst oder hauptsächlich ein neuartiges Artefakt mit eigenem Designbeitrag entwickelst. | Wähle in den [ACM-SIGSOFT-Standards](https://www2.sigsoft.org/EmpiricalStandards/docs/standards) den Standard für deine konkrete Methode; es gibt keine universelle Qualitätscheckliste für alle Studien. |
| Du setzt eine bekannte Anforderung mit etablierten Mitteln um und versprichst keinen wissenschaftlichen Erkenntnisgewinn. | **Engineering / kein Forschungsprojekt** | du wissenschaftliche Aussagen, einen neuen Wissensbeitrag oder eine systematische empirische Studie beanspruchst. | Plane Anforderungen, Umsetzung, Tests und Abnahme als Engineering-Projekt. Erfinde keinen Forschungsanspruch. |

„Engineering / kein Forschungsprojekt“ meint hier gewöhnliche Umsetzung ohne Forschungsanspruch. Das ist nicht dasselbe wie der ACM-SIGSOFT-Standard „Engineering Research“, der Forschung zu erfundenen und evaluierten technischen Artefakten beschreibt.

Methoden können sich ergänzen. Ein DSR-Projekt kann zum Beispiel ein Experiment oder eine Fallstudie zur Evaluation verwenden. ADR ist besonders dann zu prüfen, wenn Artefakt und Organisationsintervention gemeinsam entstehen. Wenn mehrere Pfade plausibel sind, bleibt die Wahl **offen**.

## Drei kurze Beispiele

### DHBW-Thesis

Du entwickelst einen neuen Prototyp zur Entscheidungsunterstützung, leitest Gestaltungsprinzipien aus Literatur ab und evaluierst, was der Prototyp leistet. **DSR ist ein plausibler Prüfpfad.** Baust du dagegen nur ein bekanntes Dashboard für einen Betrieb nach, ohne Wissensbeitrag und Forschungsfrage, ist das eher **Engineering**. Die endgültige Wahl und die lokalen Prüfungs- und KI-Vorgaben klärst du mit der Betreuung.

### Unternehmensprojekt

Ein Unternehmen führt einen neuen Onboarding-Assistenten ein. Rückmeldungen aus dem realen Einsatz verändern laufend das Artefakt und den Einführungsprozess; Entwicklung, Intervention und Evaluation sind untrennbar. **ADR ist ein plausibler Prüfpfad.** Ein gewöhnlicher Rollout eines vorhandenen Tools ohne Forschungsziel ist dagegen **kein Forschungsprojekt**. Vor konkreten Daten ist zuerst der Schutzbedarf zu klären.

### Informatikprojekt

Du vergleichst zwei Verfahren zur Fehlererkennung anhand eines vorab geplanten Benchmarks und analysierst die Messdaten. Das ist ein Kandidat für **empirische Softwareforschung**; nutze den passenden ACM-SIGSOFT-Standard, hier etwa „Benchmarking“. Erfindest und evaluierst du zusätzlich ein neuartiges Verfahren mit übertragbarem Designwissen, kann DSR als übergeordneter Pfad dazukommen – diese Kombination braucht ein Human Gate.

## Human Gate bei unklarer Wahl

Wenn du zwischen zwei Pfaden schwankst oder Forschungsfrage, Wissensbeitrag und Evaluation noch nicht klar benennen kannst, entscheidet der Router nicht. Markiere die Methode im Template als `offen` und hole eine dokumentierte Entscheidung ein:

- bei einer Thesis durch Betreuung oder zuständige methodische Fachperson;
- im Unternehmen durch den Research Owner und bei Bedarf Fach-, Datenschutz- oder Ethikreview;
- im Informatikprojekt durch Betreuung oder eine methodenkundige Fachperson.

Dokumentiere Entscheidung, Begründung, geprüfte Originalquelle und offene Bedingungen. Beginne das Forschungsdesign erst nach dieser Bestätigung. Ein Router ersetzt keine Prüfungsordnung, Ethikprüfung, Datenschutzentscheidung oder fachliche Begutachtung.

## Wie darf KI unterstützen?

**Safe Default: `Assist`.** Bleibe bei dieser Stufe, solange keine andere Stufe ausdrücklich menschlich bestätigt und dokumentiert wurde.

| Stufe | Was die KI darf | Was der Mensch tun muss |
|---|---|---|
| **Assist** | Optionen, Suchbegriffe, Gliederungen, Kritik oder Formulierungsentwürfe vorschlagen. | Jeden relevanten Input, jede Quelle, Entscheidung und Übernahme selbst prüfen und ausführen. |
| **Co-execute** | Einen klar beschriebenen Einzelschritt nach ausdrücklicher Bestätigung ausführen, zum Beispiel eine erlaubte Datei ändern oder eine freigegebene Auswertung starten. | Ziel, Daten, Werkzeuge und erwartetes Ergebnis vor jedem Schritt bestätigen; Resultat danach prüfen. |
| **Bounded autonomous** | Mehrere vorab erlaubte Schritte innerhalb eines freigegebenen Research Programs ausführen. | Research Program, Schreib- und Datenbereiche, Tools, Netzwerk, Evaluation, Budget, Stopbedingungen und Human Gates vorab freigeben; Ergebnisse und Claims prüfen. |

`Bounded autonomous` ist ausschließlich über den Vertrag in [`AGENTIC-RESEARCH.md`](AGENTIC-RESEARCH.md) zulässig. Diese Seite startet keinen Lauf. Ohne freigegebenes Research Program und versionierte Eval Cases bleibt die Stufe unzulässig.

## Was die Begriffe bedeuten

**AI-supported Research** ist menschlich geleitete Forschung, bei der KI ausgewählte Arbeitsschritte unterstützt. Forschungsfrage, Methode, Quellenannahme, Bewertung, wissenschaftliche Aussagen und Veröffentlichung bleiben menschlich verantwortet.

**Agentic Research** bezeichnet hier nur einen Ausführungsmodus: Ein Agent bearbeitet vorab begrenzte Schritte mit definierten Rechten, Budgets, Prüfungen und Stopbedingungen. Es ist weder ein Synonym für DSR noch autonome wissenschaftliche Autorenschaft.

KI kann dabei drei verschiedene Rollen haben:

- **Werkzeug:** Sie liefert auf eine einzelne Anfrage einen Vorschlag; der Mensch führt und entscheidet.
- **Ausführungsagent:** Sie führt bestätigte oder eng vorab begrenzte Schritte mit Werkzeugen aus.
- **Forschungsgegenstand:** Verhalten oder Wirkung eines KI-Systems selbst werden systematisch untersucht.

Diese Rollen können kombiniert werden, müssen aber im Projekt getrennt benannt werden. Auch wenn KI Forschungsgegenstand ist, darf ihre Nutzung als Werkzeug oder Agent nicht unsichtbar bleiben.

## Methodische Grundlagen und Grenzen

- DSR-Grundlagen und Artefaktbezug: [Hevner et al. (2004)](https://aisel.aisnet.org/misq/vol28/iss1/6/) und [Peffers et al. (2007)](https://doi.org/10.2753/MIS0742-1222240302)
- Wissensbeitrag in DSR: [Gregor und Hevner (2013)](https://aisel.aisnet.org/misq/vol37/iss2/3/)
- Verknüpfung von Bauen, Intervention und Evaluation in ADR: [Sein et al. (2011)](https://aisel.aisnet.org/misq/vol35/iss1/5/)
- Design- und empirischer Zyklus in Informationssystemen und Software Engineering: [Wieringa (2014)](https://doi.org/10.1007/978-3-662-43839-8)
- Planung von DSR-Evaluation: [Venable et al. (2016)](https://doi.org/10.1057/ejis.2014.36)
- Methodenspezifische empirische Standards: [ACM SIGSOFT Empirical Standards](https://www2.sigsoft.org/EmpiricalStandards/)
- KI an der DHBW: Das [DHBW-Positionspapier](https://www.dhbw.de/fileadmin/user_upload/Dokumente/Positionspapiere_und_Strategie/Positionspapier_zu_kuenstlicher_Intelligenz.pdf) betont Prüfung, Reflexion, Transparenz und akademische Integrität. Konkrete Standort-, Studiengangs- und Betreuungsvorgaben musst du zusätzlich lokal klären.

Das ist eine Entscheidungshilfe, keine vollständige Methodenlehre. Nach der Auswahl beginnt erst das eigentliche Forschungsdesign.

## Nach dem Human Gate weiterarbeiten

1. Wähle dein Profil: [`DHBW-Thesis`](profiles/dhbw-thesis.md), [`Unternehmensprojekt`](profiles/unternehmensprojekt.md) oder [`Informatikprojekt`](profiles/informatikprojekt.md).
2. Prüfe vor jedem Datenimport den [`Data/Ethics Check`](templates/research/data-ethics-check.md).
3. Starte den gemeinsamen Kern mit dem [`Project Brief`](templates/research/project-brief.md) und der [`Forschungsfrage`](templates/research/research-question.md).
4. Wenn DSR bestätigt wurde, lies zusätzlich [`DSR-START.md`](DSR-START.md). DSR wird nicht automatisch vorausgesetzt.

Du kannst alle Templates manuell kopieren und ausfüllen. Ein Coding-Agent, Setup-Assistent oder LaTeX ist dafür nicht nötig.
