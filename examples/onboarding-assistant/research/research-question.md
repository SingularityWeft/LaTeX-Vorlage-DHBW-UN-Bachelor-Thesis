# Forschungsfrage – synthetisches Beispiel

- **Problem/Zielgruppe:** Anfänger benötigen einen nachvollziehbaren Zusammenhang zwischen belegter Antwort, Sicherheitsgrenze, Eval und Entscheidung.
- **Wissenslücke:** Die bestehenden Repository-Verträge waren vor SPEC‑05 dokumentiert, aber nicht an einem gemeinsamen ausführbaren Fall demonstriert.
- **Praktisches Ziel:** kleine offline testbare CLI.
- **Grundlage:** DSR-, Agentic-Research- und Security-Verträge des Repositories.

## Hauptfrage

**Wie kann ein kleiner synthetischer Onboarding-Assistent gestaltet und in vorab versionierten Fällen evaluiert werden, sodass Quellenbezug, transparente Nicht-Antwort, Tool-Policy, Prompt-Injection-, Memory-Poisoning- und Human-Gate-Grenzen getrennt sichtbar werden?**

- **Unterfragen:** Welche Source-ID-Regel genügt für den Lehrfall? Welche Vertragsabweichungen müssen fail-closed stoppen? Wie bleiben Exploration und Bestätigung getrennt?
- **Fragetyp:** Designfrage mit ergänzender vergleichender Wissensfrage.
- **Untersuchungseinheit:** Artefaktversion `onboarding-assistant-v1` auf zwölf synthetischen Eval-Fällen.
- **Geltungsbereich:** dieses Repository, Python 3 Standardbibliothek, synthetische Daten.

## Antwortbarkeit

- **Evidenz:** Unit-Test-Ergebnisse, Eval-Einzelmetriken, Hashprüfung, Records und Diff-Review.
- **Datenerhebung:** deterministische Programmausgaben; kein Mensch und keine reale Organisation.
- **Artefakt:** `artifact/onboarding_assistant.py` plus Prompt und Verträge.
- **Baseline:** transparente Nicht-Antwort auf jede Frage.
- **Schwächende Beobachtung:** falsche Source ID, erfundene Antwort, befolgter Angriffstext, Memory-/Toolaktion, umgangenes Gate oder Hashdrift.
- **Nicht beantwortet:** reale Nützlichkeit, Modellranking, Organisationswirkung, Datenschutzkonformität oder Produktionsreife.

## Beitrag und Gate

- **Erwarteter Beitrag:** reproduzierbares Lehrmuster und explizite Grenzen.
- **Praktische Relevanz:** Anfänger können einen ungefährlichen End-to-End-Zyklus ausführen.
- **Methode:** DSR plus Benchmarking; siehe `method-choice.md`.
- **Status:** für den synthetischen Prüffall methodisch festgelegt; reale Übertragung offen.
- **Prüfrolle:** didaktischer Research Owner; Claims bleiben Human Gate.
