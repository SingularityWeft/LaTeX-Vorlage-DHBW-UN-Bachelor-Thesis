# Thesis-Arbeitsmodus: produktiv schreiben mit Agenten

**Version:** `thesis-arbeitsmodus-v1`

Dieser Modus gilt in einer **privaten Arbeitskopie** der Vorlage. Die Autorin oder der Autor steuert die Arbeit über die Chats von Claude Code, OpenAI Codex oder Gemini CLI. Alle Agenten arbeiten im selben Repository, lesen denselben Stand aus Dateien und sichern jede Arbeitseinheit mit Commit und Push in das private Repository. Aus den Commits entsteht parallel die KI-Erklärung.

`CLAUDE.md`, `AGENTS.md` und `GEMINI.md` verweisen auf diese Datei. Sie ist der gemeinsame Vertrag aller Agenten; bei Widersprüchen gilt sie.

## Wann der Modus gilt

Alle drei Bedingungen müssen erfüllt sein:

1. `thesis/STAND.md` existiert und enthält die Zeile `Arbeitsmodus: produktiv`.
2. `origin` zeigt auf ein privates Repository der Autorin oder des Autors, nicht auf `SingularityWeft/LaTeX-Vorlage-DHBW-UN-Bachelor-Thesis`.
3. Das öffentliche Vorlagen-Remote heißt `vorlage` und hat eine gesperrte Push-Adresse.

Fehlt eine Bedingung, gelten die Setup-Regeln aus [`KI-SETUP.md`](KI-SETUP.md) und den Agenten-Dateien. Eingerichtet wird der Modus nach [`KI-SETUP.md`](KI-SETUP.md), Abschnitt „Thesis-Arbeitsmodus einrichten“.

## Datenweg

- **Eigener Text, eigene Notizen, Gliederung und Literatur:** Die Autorin oder der Autor gibt diese Inhalte bei der Einrichtung für die genutzten Agenten-Anbieter frei (Ausführungspfad Cloud-managed comfort). Freigabe, Datum und Anbieter stehen in `research/PROJECT.md`.
- **Forschungsdaten Dritter:** Personenbezogene oder vertrauliche Daten, etwa Interviews oder Unternehmensunterlagen, kommen erst nach bestätigtem Data/Ethics Gate (`research/data-ethics-check.md`) und nur auf dem dort festgelegten Weg in den Kontext.
- **Literatur-PDFs** bleiben lokal in `literatur/pdf/`; der Ordner ist git-ignoriert. Ins Repository kommen Literaturnotizen und `literatur.bib`.

## Dateien, die den Stand tragen

| Datei | Inhalt | Pflege |
|---|---|---|
| `thesis/STAND.md` | aktueller Fokus, zuletzt erledigt, offene Punkte, Fragen an die Betreuung, genau eine nächste Aktion | jeder Agent am Ende jeder Arbeitseinheit |
| `thesis/GLIEDERUNG.md` | Kapitel und Abschnitte mit Datei, Status, Quellen und nächstem Schritt | bei jeder Statusänderung |
| `kapitel/*.tex` | Text, ein Kapitel je Datei | Agent nach Auftrag, Autorin oder Autor für Korrekturen |
| `literatur/notizen/<bibkey>.md` | eine Notiz je Quelle nach [`templates/thesis/literaturnotiz.md`](templates/thesis/literaturnotiz.md) | Agent; Prüfung durch die Autorin oder den Autor |
| `literatur.bib` | BibTeX-Einträge | Agent; Prüfung durch die Autorin oder den Autor |
| `research/` | DSR-Dokumentation: Forschungsfrage, Artefakt, Evaluation, Entscheidungen | nach [`DSR-START.md`](DSR-START.md) |
| Git-Historie | was wann mit welcher KI geändert wurde | Commits mit KI-Angaben |

Der Chatverlauf ist kein Speicher. Was im Chat entschieden oder erarbeitet wird, steht vor dem Ende der Arbeitseinheit in einer dieser Dateien. Entscheidungen zur Forschung gehören in `research/decision-log.md`.

## Ablauf jeder Arbeitseinheit

Eine Arbeitseinheit ist ein abgegrenzter Auftrag: ein Abschnitt, eine Quelle, eine Überarbeitung oder ein Build.

1. **Synchronisieren:** `git pull --ff-only`. Scheitert das, anhalten und den Zustand melden; nichts überschreiben oder zurücksetzen.
2. **Kontext laden, nicht mehr:** `thesis/STAND.md` und `thesis/GLIEDERUNG.md`, danach nur die Dateien des aktuellen Auftrags, etwa die betroffene `kapitel/*.tex`, die zugehörigen Literaturnotizen und bei Bedarf einzelne `research/`-Dateien.
3. **Auftrag ausführen** nach den Regeln unten.
4. **Stand pflegen:** `thesis/STAND.md` aktualisieren, bei Statusänderung auch `thesis/GLIEDERUNG.md`.
5. **Prüfen:** Nach Änderungen an `.tex`- oder `.bib`-Dateien die Thesis kompilieren und Fehler beheben oder melden.
6. **Sichern:** eigene Pfade einzeln stagen, mit KI-Angaben committen und zu `origin` hochladen.

Arbeiten zwei Agenten gleichzeitig, bearbeiten sie verschiedene Dateien. Weicht der Remote-Stand ab, wird zusammengeführt, nicht überschrieben.

## Commits und KI-Angaben

```text
Kapitel 2.1: Entwurf Grundlagen der Unternehmensnachfolge

KI-System: Claude Code (Anthropic)
KI-Arbeitsschritt: Struktur und Formulierung
KI-Beitrag: Entwurf aus Stichpunkten des Autors; Quellen aus geprüften Literaturnotizen.
```

- **`KI-System`:** Werkzeug und Anbieter, zum Beispiel `Claude Code (Anthropic)`, `Codex (OpenAI)` oder `Gemini CLI (Google)`. Mehrere Zeilen sind erlaubt.
- **`KI-Arbeitsschritt`:** genau einer dieser Werte:
  - `Ideen und Konzeption`
  - `Literatursuche und -analyse`
  - `Literaturverwaltung`
  - `Methoden und Modelle`
  - `Code, Formeln und Berechnungen`
  - `Tabellen und Übersichten`
  - `Visualisierungen`
  - `Struktur und Formulierung`
  - `Prüfung und Korrektur`
  - `Projektorganisation`
- **`KI-Beitrag`:** ein Satz dazu, was die KI beigetragen hat und was die Autorin oder der Autor vorgegeben oder geprüft hat.

Eigene Commits ohne KI-Beteiligung tragen keine KI-Angaben.

## KI-Erklärung

```bash
python scripts/ki-erklaerung.py
```

Unter Windows funktioniert auch `py scripts/ki-erklaerung.py`. Das Skript liest die KI-Angaben aus der Git-Historie seit der Einrichtung des Arbeitsmodus und schreibt `thesis/ki-erklaerung-entwurf.md`: eine Übersicht nach Arbeitsschritt und KI-System, die Beiträge je Arbeitsschritt und Hinweise auf unvollständige Angaben. Die Autorin oder der Autor prüft und formuliert den Entwurf; danach überträgt ein Agent ihn in das Kapitel „Erklärung zur Verwendung von KI-Systemen“ in `main.tex`.

Im Arbeitsmodus ersetzen die KI-Angaben in den Commits die laufenden Einträge in `ki-erklaerung.md`. Forschungsmethodisch relevanter KI-Einsatz, etwa im Artefakt oder in der Evaluation, gehört zusätzlich in `research/ai-provenance-log.md`.

## Literatur

1. **Aufnehmen:** BibTeX-Eintrag in `literatur.bib` mit `keywords = {ungeprueft}` und eine Literaturnotiz `literatur/notizen/<bibkey>.md`.
2. **Auswerten:** Kernaussagen mit Seitenangabe aus der Quelle selbst, also aus dem lokalen PDF oder dem Volltext. Was nicht in der Quelle steht, gehört nicht in die Notiz.
3. **Prüfen:** Autor, Jahr, Titel, Verlag oder Zeitschrift, Seiten und DOI gegen die Quelle abgleichen. Danach `ungeprueft` entfernen und das Prüfdatum in der Notiz eintragen.
4. **Zitieren:** im Text nur Einträge ohne `ungeprueft`, mit der Seitenangabe aus der Notiz.

Agenten erfinden keine Quellen, Seitenzahlen oder DOIs. Eine über Suche gefundene Quelle bleibt ein Vorschlag, bis sie geprüft ist. Mit Zotero und dem Plugin Better BibTeX kann `literatur.bib` auch automatisch exportiert werden; die Prüfung gilt dann genauso.

## Abschnittsweise schreiben

- Ein Kapitel je Datei in `kapitel/`, eingebunden über `main.tex`.
- Pro Arbeitseinheit ein Abschnitt. Die Autorin oder der Autor liefert Stichpunkte, Rohtext oder eine Anweisung; der Agent schreibt den LaTeX-Code.
- KI-geschriebene oder stark überarbeitete Abschnitte beginnen mit `% [KI-Vorschlag YYYY-MM-DD, <KI-System> — bitte prüfen]`. Erst wenn die Autorin oder der Autor den Abschnitt geprüft hat, entfernt der Agent den Marker und setzt den Status in `thesis/GLIEDERUNG.md` auf `geprüft`.
- Statuswerte: `offen`, `Stichpunkte`, `Entwurf`, `überarbeitet`, `geprüft`, `final`.

## Was weiterhin Menschen entscheiden

- Methodenwahl und Forschungsfrage;
- das Data/Ethics Gate vor Forschungsdaten Dritter;
- wissenschaftliche Aussagen, Bewertungen und Schlussfolgerungen;
- Aufnahme und Prüfung jeder Quelle;
- Abgabe, Veröffentlichung und jede Weitergabe außerhalb des privaten Repositories.

Commit und Push in das private Repository brauchen im Arbeitsmodus keine einzelne Freigabe.

## Git-Regeln im Arbeitsmodus

- Commit und Push nach jeder Arbeitseinheit, ausschließlich zu `origin`; nie zu `vorlage`.
- Nur eigene Pfade einzeln stagen; kein `git add -A` und kein `git add .`.
- Kein `reset --hard`, kein `push --force`, kein `clean -f` und kein Löschen fremder Arbeit.
- Bei Konflikten zusammenführen; bei inhaltlichen Widersprüchen anhalten und fragen.
- Bei Anmelde- oder Netzfehlern anhalten und melden; die Arbeit bleibt lokal committed.
