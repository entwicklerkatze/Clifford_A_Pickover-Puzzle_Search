# LOGBOOK

## Zweck

Dieses Logbook dient als **zwingende, evidenzbasierte Dokumentation** aller Projektaktivitäten. Jede Aktion, jede Entdeckung und jede Analyseentscheidung MUSS hier protokolliert werden.

## Struktur

```
logbook/
├── index.md              # Chronologischer Index aller Einträge
├── templates/
│   └── entry_template.md # Standard-Template für neue Einträge
├── entries/
│   └── YYYY-MM-DD_HHMM_[id].md  # Individuelle Log-Einträge
└── evidence/
    └── [entry_id]/       # Evidenz-Anhänge pro Eintrag
        ├── screenshots/
        ├── html_snapshots/
        └── metadata.json
```

## Pflichtfelder pro Eintrag

Jeder Log-Eintrag MUSS enthalten:

1. **Zeitstempel** (UTC): Wann wurde die Aktion durchgeführt?
2. **Agent**: Wer hat die Aktion durchgeführt?
3. **Aktionstyp**: SCAN | FILTER | ANALYSIS | DECISION | CORRECTION
4. **Ziel**: Welche Startseite wurde bearbeitet?
5. **Evidenz**: Screenshots, Snapshots, Hashes
6. **Ergebnis**: Was wurde festgestellt?
7. **Nächste Schritte**: Was folgt daraus?

## Aktionstypen

| Typ | Beschreibung |
|-----|--------------|
| SCAN | Startseite wurde aufgerufen und gescannt |
| FILTER | Artikel wurde durch Mustererkennung geprüft |
| ANALYSIS | Tiefergehende Analyse eines verdächtigen Artikels |
| DECISION | Entscheidung über Status (SAUBER/VERDÄCHTIG/CONFIRMED) |
| CORRECTION | Korrektur eines vorherigen Eintrags |

## Evidenz-Sicherung

Jeder SCAN-Vorgang erfordert:
- Screenshot der Startseite (mit Zeitstempel)
- HTML-Snapshot der Seite
- SHA256-Hash des Snapshots
- Metadaten (URL, Zeit, User-Agent)

## Index-Format

```markdown
| Zeitstempel | ID | Aktion | Ziel | Ergebnis | Verknüpft |
|-------------|----|--------|------|----------|-----------|
| 2026-03-27 21:00 | 001 | SCAN | welt.de | 23 Artikel gefunden | - |
| 2026-03-27 21:15 | 002 | FILTER | welt.de | 2 VERDÄCHTIG | 001 |
```

## Verwendung

1. Neue Einträge IMMER mit Template erstellen
2. Evidenz direkt an den Eintrag anhängen
3. Index nach jeder Aktion aktualisieren
4. Keine Einträge löschen – nur korrigieren (CORRECTION-Eintrag)
