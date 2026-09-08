# Track: Hybrid-redacted

Dieser Pfad hält Originaldaten lokal und gibt nur ein menschlich geprüftes, redigiertes Derivat an exakt benannte externe Dienste. Redigieren senkt Risiken, beseitigt sie aber nicht automatisch.

## Passt, wenn

- der externe Arbeitsschritt einen klaren Nutzen hat;
- die benötigte Aussage ohne direkte Identifikatoren und vertrauliche Details möglich ist;
- Original, Redaktionsschritt und externes Derivat getrennt gespeichert werden;
- Reidentifikations- und Inferenzrisiken prüfbar dokumentiert sind.

## Passt nicht, wenn

- Kontext, seltene Merkmale oder Kombinationen eine Person oder Organisation weiterhin erkennbar machen;
- Geschäftsgeheimnisse für die Aufgabe erhalten bleiben müssen;
- Browser, Cloud-Agent oder Remote-MCP auf den lokalen Originalbestand zugreifen kann;
- keine Person das konkrete Derivat vor dem Egress prüft.

## Pflicht: Redaktionsplan

| Feld | Eintrag |
|---|---|
| Originaldaten und Owner | abstrakte Datenklassen; keine Rohwerte im öffentlichen Git |
| Zweck des externen Schritts | konkrete Frage oder Transformation |
| entfernte direkte Merkmale | Namen, Adressen, IDs, Accounts, Dateimetadaten |
| entfernte indirekte Merkmale | seltene Rollen, Orte, Zeitpunkte, Kombinationen, Freitextdetails |
| ersetzte Werte | stabile Pseudonyme oder generalisierte Kategorien |
| verbleibendes Reidentifikationsrisiko | Szenario, Wahrscheinlichkeit/Impact und Restrisiko |
| freigegebene Suchfragen/Prompts | exakte, redigierte Fassungen oder Hash-Referenzen |
| externe Empfänger und Ziele | Anbieter, Endpoint, Region, Logs und Retention |
| Rückfluss | erwartete Outputs, lokale Prüfung und Speicherort |
| Human Gate | bestätigende Rolle, Datum, Grenzen |

## Technische und prozessuale Trennung

- Die redigierende Rolle besitzt privaten **Read**-Zugriff, aber keinen externen Network-/Send-Zugriff.
- Die extern arbeitende Rolle erhält nur das freigegebene Derivat und keinen Zugriff auf Originale, Mapping-Tabelle oder lokale Secrets.
- Das Mapping bleibt getrennt vom Derivat und wird nach dokumentierter Retention gelöscht oder geschützt archiviert.
- Ein untrusted Dokument darf keine Redaktionsregel, Suchfrage, Tool-Allowlist oder Netzwerkfreigabe ändern.
- Jede neue Datenklasse oder Suchfrage durchläuft das Egress-Gate erneut.

Scheitert die Trennung technisch, werden die beiden Schritte nacheinander in getrennten Arbeitskontexten ausgeführt und menschlich kontrolliert. Ist das nicht möglich, gilt [`Local/On-Prem`](local-on-prem.md).
