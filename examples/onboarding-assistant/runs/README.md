# Synthetische Run Records

`example-offline/` enthält zwei tatsächlich ausgeführte, deterministische Offline-Wiederholungen. Jeder Record verweist auf einen erhaltenen Rohoutput und nennt getrennte Daten-, Prompt-, Harness-, Eval- und Artefaktversionen. Beide Repeats verwenden denselben Konfigurationshash.

Die beiden Läufe zeigen Record-Integrität, nicht stochastische Reproduzierbarkeit. Latenzen schwanken durch den lokalen Prozessstart und werden als Einzelwerte plus Streuung berichtet. Null Modellaufrufe und null Kosten gelten nur für diesen Offline-Pfad.

Echte oder vertrauliche Live-Records gehören ausschließlich unter `runs/private/`; dieser Pfad ist im Root-`.gitignore` ausgeschlossen. Records dürfen keine API-Keys, personenbezogenen Daten oder vertraulichen Rohprompts enthalten.
