# Methoden- und Autonomiewahl – synthetisches Beispiel

- **Vorhaben:** Ein kleiner Onboarding-Assistent beantwortet Fragen nur aus fünf synthetischen Quelldokumenten und macht Sicherheitsgrenzen messbar.
- **Profile:** DHBW-Thesis, Unternehmensprojekt und Informatikprojekt können denselben Fall mit unterschiedlichen Outputs betrachten.
- **Problemtyp:** Entwurf und Prüfung eines neuen, eng begrenzten Softwareartefakts.
- **Erkenntnisziel:** Prüfen, ob Source-ID-Bindung, transparente Nicht-Antwort und getrennte Policy-Signale in den versionierten Fällen beobachtbar sind.
- **Artefakt:** Python-CLI mit deterministischem Offline-Pfad und optionalem engem Live-Client.
- **Organisationsintervention:** keine; das Beispiel wird nicht eingeführt oder im realen Betrieb beobachtet.
- **Wissensbeitrag:** ein begrenztes, übertragbar zu prüfendes Designmuster – untrusted Dokumente als Daten, belegte Antworten und getrennte Evals – ohne Wirksamkeitsclaim.
- **Evaluation:** gehashte synthetische Exploration und Bestätigung, Unit Tests sowie Repeat-/Konfigurationskontrollen.

## Geprüfte Methodenpfade

| Pfad | Entscheidung | Begründung |
|---|---|---|
| DSR | als Hauptpfad für den Lehrfall synthetisch bestätigt | Ein Artefakt mit begründeten Designanforderungen wird gebaut, demonstriert und mehrdimensional evaluiert. |
| ADR | nicht gewählt | Es gibt keine echte Organisation, Intervention oder wechselseitige Veränderung von Artefakt und Betrieb. |
| empirische Softwareforschung | ergänzendes Benchmarking | Versionierte Fälle, Ground Truth und deterministische Messungen prüfen beobachtbares Softwareverhalten. |
| Engineering ohne Forschungsanspruch | Alternative für reine Nutzung | Wer nur die CLI übernimmt, ohne Forschungsfrage oder Wissensbeitrag, betreibt Engineering. |

- **Status:** menschlich bestätigte, aber ausschließlich synthetische Methodenentscheidung im Lehrszenario
- **Originalquellen/Verträge geprüft:** Root-Dateien `RESEARCH-START.md`, `DSR-START.md`, `AGENTIC-RESEARCH.md` und die versionierten Eval-Verträge
- **Grenzen:** keine reale Stichprobe, keine Organisationswirkung, keine Modellqualität und keine Generalisierung belegt

## Autonomiestufe und Rollen

- **Default:** `Assist`.
- **Offline-Prüfserie:** begrenztes `Co-execute`; ein bestätigter Testbefehl, danach Ergebnisreview.
- **Bounded autonomous:** im Beispielprogramm nur als endlicher synthetischer Vertrag beschrieben; kein autonomer Live-Lauf gestartet.
- **KI-Rolle:** Werkzeug und implementierendes Assistenzsystem; der Assistent selbst ist Forschungsgegenstand.
- **Nicht delegiert:** Methode, Datenfreigabe, Bestätigung, Interpretation, Claim und Veröffentlichung.

## Human Gate

- **Prüfende Rolle:** didaktischer Research Owner; keine reale Person benannt
- **Methodenentscheidung:** DSR plus ergänzendes Benchmarking nur für den synthetischen Fall
- **Autonomiestufe:** `Assist`/einzeln bestätigtes `Co-execute`; Live und Shared On-Prem gesperrt
- **Offene Klärungen:** lokale Prüfungsregeln bei Thesis-Nutzung; reale Datenschutz-, Security-, Betriebs- und Owner-Gates bei jeder Übertragung
- **Bestätigungsstatus:** Beispielvertrag vollständig; keine reale Einsatzfreigabe
- **Nächster Schritt:** nur die Offline-Tests ausführen und Einzelmetriken prüfen
