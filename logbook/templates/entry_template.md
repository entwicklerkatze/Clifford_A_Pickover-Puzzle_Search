---
id: ""
zeitstempel: "YYYY-MM-DD HH:MM UTC"
agent: ""
aktionstyp: "SCAN|ARTICLE_SCAN|FILTER|ANALYSIS|DECISION|CORRECTION"
---

# Log-Eintrag: [Titel]

## Kontext

**Ziel-Startseite:** [welt.de|tagesschau.de|spiegel.de|stern.de]

**Auslöser:** 
- [ ] Geplanter Scan
- [ ] Follow-up zu Eintrag #[ID]
- [ ] Manuelle Überprüfung

## Durchgeführte Aktion

### Schritt 1: Startseiten-Scan

**Durchgeführt:** [Zeitstempel]

**Evidenz gesichert:**
- [ ] Screenshot Startseite
- [ ] HTML-Snapshot
- [ ] SHA256-Hash

### Schritt 2: Artikel-Extraktion

**Gefundene Artikel-URLs auf Startseite:**
```
1. [URL 1] - [Titel]
2. [URL 2] - [Titel]
3. ...
```

**Anzahl Artikel:** [N]

### Schritt 3: Einzelartikel-Analyse (FÜR JEDEN ARTIKEL)

**Artikel #[X]:** [URL]

**Durchgeführte Aktionen:**
- [ ] Artikel aufgerufen
- [ ] Screenshot gespeichert
- [ ] HTML-Snapshot gespeichert
- [ ] Zeitstempel analysiert (Meta-Tags, JSON-LD)
- [ ] Pickover-Filter angewendet

**Gefundene Indikatoren:**
- [ ] Keine
- [ ] Indikator A (Zeitlich)
- [ ] Indikator B (Quellen)
- [ ] Indikator C (Sprache)
- [ ] Indikator D (Netzwerk)

**Artikel-Status:**
- [ ] SAUBER
- [ ] VERDÄCHTIG → Eintrag #[ID]
- [ ] CONFIRMED → Eintrag #[ID]

## Gesamtergebnis

### Übersicht aller geprüften Artikel

| # | Artikel-URL | Titel | Status | Verknüpfter Eintrag |
|---|-------------|-------|--------|---------------------|
| 1 | | | UNGEPRÜFT/SAUBER/VERDÄCHTIG/CONFIRMED | |
| 2 | | | | |

### Identifizierte Verdächtige/CONFIRMED Fälle

**Anzahl VERDÄCHTIG:** [X]
**Anzahl CONFIRMED:** [Y]

## Evidenz

### Screenshots
**Startseite:**
- [ ] `screenshot_YYYY-MM-DD_HHMM_[domain]_startseite.png`

**Einzelne Artikel:**
- [ ] `screenshot_YYYY-MM-DD_HHMM_[domain]_artikel_[X].png`

### HTML-Snapshots
**Startseite:**
- [ ] `snapshot_YYYY-MM-DD_HHMM_[domain]_startseite.html`
- **SHA256:** `...`

**Einzelne Artikel:**
- [ ] `snapshot_YYYY-MM-DD_HHMM_[domain]_artikel_[X].html`
- **SHA256:** `...`

### Timestamp-Analysen
```json
{
  "article_url": "...",
  "timestamps_found": {
    "published": "...",
    "modified": "...",
    "audio_upload": "..."
  },
  "anomalies": []
}
```

## Entscheidung (Gesamt)

**Scan-Ergebnis:**
- [ ] KEINE VERDÄCHTIGEN ARTIKEL GEFUNDEN
- [ ] [X] VERDÄCHTIGE ARTIKEL IDENTIFIZIERT → Folge-Einträge erstellt
- [ ] [Y] CONFIRMED FAKE-NEWS → Analyse-Ordner erstellt

## Nächste Schritte

- [ ] Verdächtige Artikel detailliert analysieren
- [ ] Tiefe Analyse für CONFIRMED Fälle durchführen
- [ ] Tracking-Tabelle aktualisieren
- [ ] Evidence sammeln

## Kreuzreferenzen

- Verwandt mit: #
- Folge-Einträge (Artikel-Analysen): #
- Korrigiert: #
