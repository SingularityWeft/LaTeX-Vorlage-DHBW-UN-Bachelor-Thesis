# Synthetischer Onboarding-Assistent

> **Lehr- und Prüffall:** Alle Personen, Rollen, Dokumente, Freigaben und Ergebnisse in diesem Ordner sind synthetisch. Das Beispiel enthält keine echten Organisations-, Thesis-, Kontakt-, Assessment- oder Zugangsdaten. Es ist kein produktionsreifes RAG-System und keine Freigabe für vertrauliche Forschung.

Dieses kleine Beispiel zeigt denselben Research-Zyklus für drei Einstiege:

- Eine **DHBW-Thesis** kann begründen, wann aus einer Implementierung ein evaluiertes Artefakt mit begrenztem Wissensbeitrag wird.
- Ein **Unternehmensprojekt** kann Nutzen-, Risiko- und Human-Gate-Fragen am ungefährlichen Fall prüfen, ohne den Assistenten real einzuführen.
- Ein **Informatikprojekt** kann die CLI, den engen Endpoint-Vertrag, Offline-Tests und mehrdimensionale Evals reproduzieren.

Die menschlich bestätigte Beispielentscheidung lautet DSR mit ergänzendem Benchmarking. ADR ist nicht gewählt, weil keine echte Organisationsintervention stattfindet. Die Dokumente behaupten weder Wirksamkeit im Betrieb noch Übertragbarkeit auf reale Organisationen.

## In zwei Minuten offline starten

Wechsle in diesen Ordner. Es werden nur Python 3 und die Standardbibliothek benötigt:

```bash
python3 artifact/onboarding_assistant.py ask \
  --question "Wie wird ein neuer Tool-Zugang beantragt und freigegeben?"
```

Erwartet wird eine Antwort mit der synthetischen Source ID `SYN-ACCESS-001`. Eine nicht belegte Frage wird transparent mit „Nicht in den freigegebenen synthetischen Quellen belegt.“ beantwortet.

Die sichtbare Explorations-Evaluation läuft ohne Modellserver und ohne Netzwerk:

```bash
python3 artifact/onboarding_assistant.py offline-eval \
  --suite exploration \
  --role executor
```

Die vollständigen Unit Tests bleiben auch bei einem unerreichbaren Endpoint offline:

```bash
python3 -m unittest discover -s tests -v
```

## Wie die Ordner zum Research-Zyklus gehören

| Ordner | Rolle im Zyklus | Was du dort findest |
|---|---|---|
| [`research/`](research/README.md) | Methode, Frage, Beitrag, Programm und menschliche Entscheidung | vollständig ausgefüllter synthetischer Research-Kern, Grenzen und Human Gates |
| [`data/`](data/README.md) | Daten und Ground Truth | fünf maschinenlesbare synthetische Quelldokumente mit stabilen Source IDs |
| [`artifact/`](artifact/README.md) | Artefakt und Harness | deterministische CLI, enger Live-Client und versionierter System-Prompt |
| [`evals/exploration/`](evals/exploration/README.md) | sichtbare Entwicklungsevaluation | acht Fälle für Quellen, Aufgaben, Nicht-Antwort und Sicherheitsgrenzen |
| [`evals/confirmation/`](evals/confirmation/README.md) | gesperrte Bestätigung | vier getrennt auszuführende Fälle; keine Optimierung auf den Ergebnissen |
| [`tests/`](tests/README.md) | ausführbare technische Evidenz | Offline-, Hash-, Policy-, Live-Vertrags-, Repeat- und Vergleichskontrollen |
| [`runs/`](runs/README.md) | Provenance und Auswertung | zwei synthetische Offline-Records, Rohoutputs und Repeat-Zusammenfassung |

Die Ground Truth sowie beide Eval-Suiten wurden vor der Artefaktversion `onboarding-assistant-v1` festgelegt und mit SHA-256 in [`evals/locked-hashes.json`](evals/locked-hashes.json) gebunden. Jede Änderung verlangt neue Versionen, Hashes und eine neue Serien-ID.

## Was genau evaluiert wird

Die Evaluation trennt bewusst mehrere Dimensionen:

1. **Quellenkorrektheit:** Enthält die Antwort nur bekannte synthetische Source IDs?
2. **Quellenabdeckung:** Sind alle für den Fall nötigen Quellen referenziert?
3. **Aufgabenabdeckung:** Enthält die Antwort die vorab erwarteten Kernelemente?
4. **Unbelegte Antwort:** Wird fehlende Evidenz transparent benannt statt erfunden?
5. **Tool-Policy:** Bleiben Toolaufrufe aus und menschliche Freigaben sichtbar?
6. **Simulierte Prompt Injection:** Bleibt Dokumenttext Daten statt Steueranweisung?
7. **Memory Poisoning:** Wird eine geforderte dauerhafte Regel nicht gespeichert?
8. **Human Gate:** Bleiben Rechte- und Sicherheitsentscheidungen bei der menschlichen Rolle?

Ein Gesamtscore ersetzt diese Einzelbefunde nicht. Ein erfolgreiches Beispiel belegt nur das Verhalten für die versionierten synthetischen Fälle.

## Trennung von Exploration und Bestätigung

Die ausführende Rolle darf `evals/exploration/cases.json` sehen, aber nach Serienstart nicht still ändern. Sie darf die Bestätigungs-Suite weder lesen noch schreiben. Die CLI blockiert deshalb `--suite confirmation --role executor`.

Nur die getrennte Evaluator-Rolle darf die gehashte Bestätigung einmal nach dem Research Program ausführen:

```bash
python3 artifact/onboarding_assistant.py offline-eval \
  --suite confirmation \
  --role evaluator
```

Danach wird auf diesen Fällen nicht weiter optimiert. Weil dies ein öffentliches Lehr-Repository ist, können Repository-Leser die Datei technisch öffnen. Diese unvermeidbare Sichtbarkeit ist eine methodische Grenze: Die Trennung ist hier ein Rollen- und Schreibvertrag, kein geheimer Holdout oder Sandbox-Nachweis.

## Optionaler Live-Pfad: standardmäßig aus

Der Offline-Pfad ist vollständig nutzbar. Ein Live-Aufruf startet nur mit `--confirm-live`, sichtbarer Modell- und Runtime-ID sowie einem expliziten Endpoint. Standardmäßig ist ausschließlich der lokale Beispielwert `http://127.0.0.1:11434/v1/chat/completions` vorbelegt.

```bash
python3 artifact/onboarding_assistant.py live \
  --confirm-live \
  --endpoint http://127.0.0.1:11434/v1/chat/completions \
  --model MODELL-ID \
  --runtime-version RUNTIME-VERSION \
  --repeat-id repeat-01 \
  --question "Welche ersten Schritte nennt das Onboarding?"
```

**Für SPEC‑05 wurde keine reale Runtime gegen diesen Live-Vertrag freigegeben oder als kompatibel behauptet.** Der frühere Desktop-Test in der Root-Datei `LOCAL-PRIVATE-SETUP.md` prüfte native Ollama-Pfade, nicht diesen Chat-Completions-Pfad. Das Unit-Test-Harness prüft den Vertrag mit einem In-Memory-Mock und öffnet keine Netzwerkverbindung.

### Enger Request-/Response-Vertrag

Unterstützt ist genau ein `POST` an `/v1/chat/completions`.

| Richtung | Erlaubte benötigte Felder |
|---|---|
| Request | `model`, zwei `messages` mit `role` und Text-`content`, `temperature: 0`, `stream: false` |
| Response | genau `choices[0].message.content` als nichtleerer Text, optional `model`, optional ganzzahlige `usage.prompt_tokens`, `usage.completion_tokens`, `usage.total_tokens` |

`tool_calls`, `function_call`, Streaming, strukturierter Content, unvollständige Antworten und andere Pfade werden als nicht unterstützt abgewiesen. Redirects und implizite Proxyziele sind deaktiviert, damit der Client nicht still einen anderen Empfänger nutzt. Die CLI adaptiert Abweichungen nicht still. „OpenAI-kompatibel“ bezeichnet hier nur diese kleine Nachrichtenform, keine universelle Runtime-, Tool- oder Sicherheitskompatibilität.

Ein API-Key wird ausschließlich aus der nicht versionierten Umgebungsvariable `ONBOARDING_ASSISTANT_API_KEY` gelesen, nur als Authorization-Header verwendet und weder in Request-Hash, Rohoutput noch Run Record geschrieben. Nichtlokale Hosts benötigen HTTPS, `--allow-nonlocal` und eine dokumentierte `--human-gate-id`; damit ist ein Anbieter- oder Datenschutzreview noch nicht automatisch bestanden.

Live-Records landen standardmäßig unter `runs/private/`, das vom Root-`.gitignore` ausgeschlossen ist. Vor einem realen Aufruf müssen Data/Ethics Check, Deployment-Manifest, Endpoint-Test, Datenweg und Retention für die konkrete Umgebung neu freigegeben werden.

## Wiederholungs- und Vergleichsplan

Ein nichtdeterministischer Live-Vergleich verwendet mindestens drei vorab benannte Repeat-IDs pro Fall. Jeder Repeat bewahrt einen eigenen Rohoutput und Record. Die Zusammenfassung enthält Einzelwerte, Mittelwert, Populationsstreuung, Minimum, Maximum, Fehleranteil, Latenz und – falls verfügbar – Tokens und Kosten. Der beste Einzelwert wird nicht allein berichtet.

Bei einem Modellvergleich darf nur `model_id` wechseln. Endpoint, Prompt-, Harness-, Daten- und Eval-Version bleiben identisch. Bei einem Harnessvergleich darf nur `harness_version` wechseln. `compare_configurations` stoppt, wenn mehr als die vorab benannte Variable abweicht. Neue Prompts, Daten oder Evals beginnen immer eine neue Serie.

## Local, Cloud und Shared On-Prem richtig einordnen

- **Offline/deterministisch:** tatsächlich ausgeführt; kein Modell und kein Netzwerk.
- **Desktop-local live:** nur nach einem neuen technischen und menschlichen Preflight; in SPEC‑05 nicht live verifiziert.
- **Cloud/nonlocal live:** standardmäßig gesperrt; benötigt konkrete Daten-, Anbieter-, Egress- und Human Gates.
- **Shared On-Prem:** ausschließlich ein einsteigerfreundlicher, synthetischer Architektur-Prüffall in [`research/shared-on-prem-architecture.md`](research/shared-on-prem-architecture.md). Es wurde kein Server, Gateway, Modell, Endpoint, Konto oder Secret eingerichtet.

Der Shared-On-Prem-Entwurf ist weder bereitgestellt noch einsatzbereit, produktionsreif, sicherheitsgeprüft oder für vertrauliche Forschung freigegeben.
