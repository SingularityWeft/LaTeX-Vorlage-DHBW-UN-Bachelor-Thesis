# Evidence Log – synthetisches Beispiel

| ID | Quelle | Institution/Autorrolle | Version/Datum | Abruf | Fundstelle | Belegte Aussage | Status/Entscheidung | Menschlich angenommen? |
|---|---|---|---|---|---|---|---|---|
| E-001 | Root `RESEARCH-START.md` | Repository-Maintainer | Commit vor SPEC‑05 | 2026-09-08 | Methoden- und Autonomierouter | DSR ist bedingt; `Assist` ist Default. | geprüft/ein | ja, im Lehrvertrag |
| E-002 | Root `DSR-START.md` | Repository-Maintainer | Commit vor SPEC‑05 | 2026-09-08 | DSR-Zyklus | Demonstration, Exploration und Bestätigung sind verschieden. | geprüft/ein | ja, im Lehrvertrag |
| E-003 | Root `AGENTIC-RESEARCH.md` | Repository-Maintainer | Commit `fa676d1` | 2026-09-08 | Rollen, Serien, Records | Bestätigung, Repeats und Human Gates bleiben getrennt. | geprüft/ein | ja, im Lehrvertrag |
| E-004 | Root `SECURITY.md` | Repository-Maintainer | Commit `5be6afc` | 2026-09-08 | Trust Boundaries | Dokumenttext ist untrusted und erweitert keine Rechte. | geprüft/ein | ja, im Lehrvertrag |
| E-005 | `../data/documents.json` | synthetischer Daten-Owner | Datenhash `f0e4960c…df35` | 2026-09-08 | fünf Source IDs/Faktenlisten | alleinige Ground Truth für Antworten. | geprüft/ein | ja, nur synthetisch |
| E-006 | `../evals/locked-hashes.json` | synthetischer Evaluations-Owner | `onboarding-eval-lock-v1` | 2026-09-08 | drei SHA-256-Werte | Daten und beide Eval-Suiten sind versionsgebunden. | geprüft/ein | ja, nur synthetisch |

## Synthese

- **Übereinstimmung:** Alle Verträge verlangen begrenzte Autonomie, Quellen-/Rechtetrennung und menschliche Claims.
- **Widerspruch:** keiner innerhalb des synthetischen Scopes festgestellt.
- **Lücke:** keine reale Nutzer-, Organisations- oder Live-Runtime-Evidenz.
- **Übertragbarkeit:** nur als zu prüfendes Muster; kein Einsatzbeleg.
- **Nächste Prüfung:** unabhängige Anfänger-Walkthroughs erst in SPEC‑07.

## Human Gate

- **Angenommene Quellen:** E-001 bis E-006.
- **Prüfrolle:** didaktischer Research Owner.
- **Entscheidung:** ausreichend für synthetische Offline-Implementierung; nicht ausreichend für reale Daten oder Deployment.
