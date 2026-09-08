# AI-Provenance Log – synthetisches Beispiel

## AI-001

- **Datum:** 2026-09-08
- **Tool/Modell:** OpenAI Codex; genaue sichtbare Modellversion durch die lokale Ausführungsoberfläche bestimmt
- **Aufgabe:** SPEC‑05 als synthetischen Onboarding-Fall implementieren und verifizieren.
- **Umfang:** Dokumentationsentwurf, Python-Code, Testfälle, Eval-Fixtures, Run-Record-Struktur und Review-Unterstützung.
- **Inputs:** leitende SPEC‑05, Repository-Anweisungen und bestehende Methoden-/Security-Verträge; keine echten personenbezogenen oder vertraulichen Daten.
- **Ergebnis:** `examples/onboarding-assistant/` mit Offline-CLI, engem optionalem Live-Vertrag, Research-Kern und Architektur-Prüffall.
- **Menschliche Prüfung:** Scope-, Diff-, Test-, Build-, Baseline- und Claim-Review.
- **Entscheidung:** in den fokussierten lokalen SPEC‑05-Commit übernehmen, sofern alle Checks grün sind.
- **Übernommener Umfang:** ausschließlich explizit gelistete Beispielpfade und neu gebaute `main.pdf`, falls der vorgeschriebene Build sie ändert.
- **Externe Quellen:** keine neuen externen Quellen in diesem Slice importiert.
- **Geprüfte Evidence IDs:** E-001 bis E-006.
- **Grenzen:** KI ist keine Human-Gate-Rolle; keine Live-, Deployment-, Datenschutz- oder Produktionsfreigabe.
- **Verantwortliche Rolle:** menschlicher Repository-Owner für Commit/Claims; kein Push autorisiert.

## Zusammenfassung

- **Unterstützte Schritte:** Strukturierung, Formulierung, Code, Tests und technische Ausführung.
- **Nicht delegiert:** Methoden-/Daten-/Security-/Deployment-/Claim-/Release-Entscheidungen.
- **Prüfung:** deterministische Tests, statische Scans, LaTeX-Build, Baseline-Diff und skeptisches Diff-Review.
