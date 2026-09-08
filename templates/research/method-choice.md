# Methoden- und Autonomiewahl

**Template-Version:** `research-template-v1`

> Fülle zunächst nur abstrakte Angaben aus. Trage vor der Schutzbedarfswahl keine echten Unternehmensdaten, personenbezogenen Daten oder Geheimnisse ein. Der Router entscheidet nicht automatisch.

## 1. Kurzbeschreibung

- **Nutzungsprofil:** [ ] DHBW-Thesis · [ ] Unternehmensprojekt · [ ] Informatikprojekt
- **Vorhaben in zwei Sätzen:**
- **Problemtyp:** Was soll verstanden, verändert, entwickelt oder geprüft werden?
- **Erkenntnisziel:** Welche neue, nachvollziehbare Erkenntnis soll entstehen?
- **Geplantes Artefakt:** Keines / Modell / Methode / Software / Prozess / anderes:
- **Organisationsintervention:** Keine / getrennt von der Entwicklung / untrennbar mit Entwicklung und Evaluation:
- **Wissensbeitrag:** Was soll über die einmalige Umsetzung hinaus gelten?
- **Evaluation:** Woran und mit welchen Daten oder Beobachtungen soll die Aussage geprüft werden?

## 2. Methodenpfad prüfen

Markiere zunächst Kandidaten, keine automatische Entscheidung.

### Design Science Research (DSR)

- [ ] Ein neuartiges Artefakt wird entwickelt und systematisch evaluiert.
- [ ] Ein begründeter Wissensbeitrag über den Einzelfall hinaus ist benennbar.
- [ ] **Passt nicht**, weil nur eine bekannte Lösung ohne Forschungsfrage oder Wissensbeitrag umgesetzt wird.

### Action Design Research (ADR)

- [ ] Artefaktentwicklung, Einsatz in einer Organisation und Evaluation sind untrennbar.
- [ ] Erkenntnisse entstehen durch die wechselseitige Veränderung von Artefakt und Organisationskontext.
- [ ] **Passt nicht**, weil keine echte Organisationsintervention stattfindet oder Entwicklung und Evaluation getrennt erfolgen.

### Empirische Softwareforschung

- [ ] Daten über Software, Entwicklung, Betrieb oder Nutzung werden systematisch erhoben oder analysiert.
- [ ] Der konkrete Studientyp ist benannt, zum Beispiel Experiment, Benchmarking, Fallstudie, Repository Mining oder Data Science.
- [ ] Der passende [ACM-SIGSOFT-Methodenstandard](https://www2.sigsoft.org/EmpiricalStandards/docs/standards) wurde ausgewählt:
- [ ] **Passt nicht**, weil keine Daten erhoben oder analysiert werden.

### Engineering / kein Forschungsprojekt

- [ ] Eine bekannte Anforderung wird mit etablierten Mitteln umgesetzt.
- [ ] Es wird kein wissenschaftlicher Wissensbeitrag oder empirischer Forschungsclaim versprochen.
- [ ] **Passt nicht**, weil das Vorhaben wissenschaftliche Erkenntnisse beansprucht, die ein Forschungsdesign und Evidenz benötigen.

## 3. Vorläufige Entscheidung

- **Status:** [ ] offen · [ ] menschlich bestätigt
- **Gewählter Hauptpfad:** [ ] DSR · [ ] ADR · [ ] empirische Softwareforschung · [ ] Engineering / kein Forschungsprojekt
- **Ergänzende Methode oder Standard:**
- **Begründung:** Warum passt dieser Pfad besser als die Alternativen?
- **Originalquellen oder lokale Vorgaben geprüft:**
- **Offene Bedingungen und Grenzen:**

Wenn mehrere Pfade plausibel sind oder die Begründung fehlt, bleibt der Status `offen`. Vor dem Forschungsdesign ist dann das Human Gate in Abschnitt 5 verpflichtend.

## 4. Autonomiestufe

Wähle genau eine Stufe. Ohne ausdrücklich bestätigte Änderung bleibt `Assist` markiert.

- [x] **Assist – Safe Default:** KI macht Vorschläge; der Mensch prüft, entscheidet und führt relevante Schritte aus.
- [ ] **Co-execute:** KI führt jeweils einen klar beschriebenen und zuvor bestätigten Schritt aus; der Mensch prüft danach das Ergebnis.
- [ ] **Bounded autonomous:** KI darf mehrere Schritte nur innerhalb eines vorab freigegebenen Research Programs ausführen.

`Bounded autonomous` ist erst mit dem in SPEC-04 vorgesehenen Vertrag zulässig. SPEC-04 ist in diesem Slice nicht implementiert; diese Auswahl startet keinen Lauf.

- **Begründung einer Abweichung von `Assist`:**
- **Erlaubte KI-Rolle:** [ ] Werkzeug · [ ] Ausführungsagent · [ ] Forschungsgegenstand
- **Abgrenzung der Rollen:**

## 5. Human Gate

- **Prüfende Rolle:** Betreuung / Research Owner / methodische Fachperson / anderes:
- **Methodenentscheidung:** bestätigt / offen / zurück zur Überarbeitung
- **Autonomiestufe:** bestätigt / auf `Assist` zurückgesetzt
- **Dokumentierte Begründung:**
- **Noch erforderliche Fach-, Ethik-, Datenschutz- oder Prüfungsklärung:**
- **Bestätigungsdatum:** YYYY-MM-DD
- [ ] Ein Mensch hat Methodenpfad und Autonomiestufe ausdrücklich bestätigt.

Ohne diese Bestätigung bleibt die Methodenentscheidung offen und die Autonomiestufe `Assist`. Das Human Gate ersetzt keine Prüfungsordnung, Ethikprüfung, Datenschutzentscheidung oder fachliche Begutachtung.

## 6. Nächste Aktion

- **Erster Schritt nach dem Gate:**
- **Verantwortliche Rolle:**
- **Noch nicht beginnen, solange:**
