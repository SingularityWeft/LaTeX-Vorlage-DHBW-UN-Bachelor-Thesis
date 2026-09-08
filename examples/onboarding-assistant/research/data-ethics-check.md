# Data/Ethics Check – synthetisches Beispiel

## Dateninventar

- **Datenkategorien:** fünf frei erfundene Onboarding-Karten, synthetische Fragen, erwartete Begriffe, Source IDs und Policy-Erwartungen
- **Quelle/Owner:** Repository-Lehrfall; didaktischer Daten-Owner
- **Personenbezogene Daten:** nein
- **Geschäftsgeheimnisse:** nein
- **Urheber-/Lizenzgrenze:** eigens für dieses MIT-Repository erstellte Inhalte
- **Schutzbedarf:** öffentlich und synthetisch

## Zweck und Minimierung

- **Zweck:** belegte Antwort, Nicht-Antwort und Sicherheitsgrenzen reproduzierbar demonstrieren.
- **Erforderlich:** nur kurze Fakten, simulierte Angriffstexte und Ground Truth.
- **Entfallen:** Namen, reale Standorte, Accounts, interne Prozesse, freie personenbezogene Texte und Secrets.
- **Alternative:** bereits vollständig synthetisch; keine echten Daten erforderlich.
- **Retention/Löschung:** versionierte Lehrfixtures bleiben im Repo; temporäre Testoutputs werden nach Testende gelöscht.

## Verarbeitung

- **Speicher/Zugriff:** öffentliche Repository-Dateien; Unit-Test-Prozess liest sie lokal.
- **Erlaubte Tools:** Python 3 Standardbibliothek, Git-Read und LaTeX-Regression außerhalb des Beispiels.
- **Externe Verarbeitung:** aus. Ein Live-Pfad benötigt ein neues Gate.
- **Logs/Backups:** Tests geben nur synthetische Ergebnisse aus; versionierte Beispiel-Records enthalten keine Secrets.
- **Berechtigung:** synthetischer Repository-Scope geprüft.

## Ethik- und Schadensprüfung

- **Mögliche Schäden:** falsches Vertrauen in Sicherheit, Reife oder Übertragbarkeit; Verwechslung synthetischer Freigaben mit realer Zulässigkeit.
- **Betroffene Gruppen:** keine realen Versuchspersonen; Anfänger könnten Grenzen überlesen.
- **Mitigation:** Warnhinweise, getrennte Einzelmetriken, fail-closed Live-Vertrag und offene Gates.
- **Stopkriterium:** reale, personenbeziehbare oder vertrauliche Daten; externer Egress; neue Toolrechte; Reifeclaim.
- **Review:** bei realer Übertragung sind Daten-, Datenschutz-/Ethik-, Security- und Research-Owner neu erforderlich.

## Human Gate

- **Entscheidung:** nur synthetischer Offline-Datenimport freigegeben
- **Bestätigende Rolle:** didaktischer Daten-/Research-Owner im Beispielvertrag
- **Datum/Begründung:** 2026-09-08; alle Fixtures wurden auf synthetische Inhalte begrenzt
- **Offene Bedingungen:** jeder Live-, Organisations- oder vertrauliche Pfad bleibt nicht freigegeben
