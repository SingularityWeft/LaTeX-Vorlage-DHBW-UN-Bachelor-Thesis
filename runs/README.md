# Run-Record-Verzeichnisvertrag

Dieses Verzeichnis bewahrt die Provenance aller Versuche. Verwende für jeden Repeat eine eigene Datei nach [`../templates/research/run-record.md`](../templates/research/run-record.md).

## Struktur und Benennung

```text
runs/
├── README.md
└── <series-id>/
    └── <experiment-id>-<repeat-id>.md
```

Serien-, Experiment- und Run-ID müssen eindeutig und mit Research Program, Experiment Record und Commit verknüpft sein.

## Append-only-Regel

- Jeder beendete oder abgebrochene Repeat erhält einen Record.
- `candidate-keep`, `discard`, `crash`, `inconclusive`, `human-review` und `promoted` bleiben sichtbar.
- Ein finalisierter Record wird nicht überschrieben oder gelöscht.
- Korrekturen werden als neuer Record mit Verweis auf den ursprünglichen Eintrag angelegt.
- Negative, unklare oder fehlgeschlagene Evidenz bleibt auch nach einem normalen Revert-Commit referenzierbar.

## Mindestinhalt

Jeder Run Record nennt mindestens:

- Serien-, Experiment-, Repeat- und Seed-ID;
- Branch und Versuch-Commit;
- Konfiguration und abstrakte Input-Referenzen;
- Modell/Runtime sowie Prompt-, Harness-, Daten-, Eval- und Grader-Version;
- Einzelmetriken, Ergebnis und Fehlerstatus;
- Rohoutput-/Trace-Referenz und erzeugte Artefakte;
- Quellen-/Zitationsmetriken, wenn relevant;
- Umgebung, Latenz, Kosten, Ressourcen und verbleibendes Budget;
- ausgelöste Stopbedingung und Statusbegründung.

## Datenminimierung

- Keine Secrets in Records oder Traces.
- Keine vertraulichen Rohdaten in öffentlichem Git; nur geschützte IDs oder Speicherreferenzen verwenden.
- Agenten-Trajektorien und Toolereignisse auf das für Reproduktion oder Sicherheitsprüfung erforderliche Maß begrenzen.
- Zugriffsklasse, zugriffsberechtigte Rollen und Retention dokumentieren.
- Vertrauliche Runs benötigen einen nach [`../LOCAL-PRIVATE-SETUP.md`](../LOCAL-PRIVATE-SETUP.md) und [`../SECURITY.md`](../SECURITY.md) freigegebenen Track.

## Auswertung

Ein nichtdeterministischer Vergleich berichtet alle Repeat-IDs und Einzelwerte sowie Lagewert, Streuung, Wertebereich und Crash-Anteil im Experiment Record. Der beste Einzelwert allein ist keine Zusammenfassung und ein einzelner Lauf belegt keine Reproduzierbarkeit.
