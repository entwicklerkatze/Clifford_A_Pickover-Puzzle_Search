# AGENTS.md

## Anweisungen für KI-Agents und Mitarbeiter

### Primäre Aufgaben

1. **Content-Monitoring**
   - Regelmäßige Überprüfung der **Startseiten** der definierten Nachrichtenseiten
   - **Extraktion ALLER Artikel-URLs von der Startseite**
   - **Vollständiger Scan jedes einzelnen Artikels** mit Metadaten
   - Speicherung in strukturiertem Format

2. **Musteranalyse**
   - Anwendung der Pickover-Methode auf jeden neuen Artikel
   - Dokumentation auffälliger Muster
   - Flagging potenzieller FAKE-NEWS

3. **Dokumentation**
   - **Zwingende Protokollierung ALLER Aktivitäten im Logbook**
   - Pflege der zentralen Tracking-Tabelle
   - Erstellung tiefer Analysen in Unterordnern
   - Verknüpfung von verwandten Artikeln

### Technische Durchführung (Web-Scraping)

**Cookie-Consent und Datenschutz-Dialoge:**

Beim Aufruf jeder Webseite (Startseite UND einzelne Artikel) MUSS der Cookie-Consent-Dialog und/oder Datenschutz-Hinweis sofort akzeptiert werden:

- **Immer akzeptieren mit:**
  - "Alle akzeptieren"
  - "Akzeptieren"
  - "Annehmen"  
  - "Zustimmen"
  - "Alles akzeptieren"
  - "Erlauben"
  - "Weiter"
  - Oder ähnliche Variante des Haupt-Akzeptieren-Buttons

- **NIE ablehnen oder individualisieren**
- **NIE auf "Nur notwendige Cookies" klicken**
- **Ziel:** Vollständiger Zugriff auf alle Seiteninhalte ohne Einschränkungen

**Beispiel-Workflow:**
1. URL aufrufen
2. Sofort auf Cookie-Banner reagieren (falls vorhanden)
3. Button mit "Alle akzeptieren" / "Akzeptieren" etc. klicken
4. Erst danach Screenshot und HTML-Snapshot erstellen

### Workflow bei Identifikation

```
STARTSEITEN-SCAN INITIIERT
        ↓
    [LOGBOOK: SCAN-Eintrag erstellen]
        ↓
    [STARTSEITE AUFRUFEN]
        ↓
    [EVIDENZ SICHERN]
    (Screenshot + HTML-Snapshot + Hash)
        ↓
    [ARTIKEL-URLS EXTRAKTION]
    (ALLE Artikel-URLs von Startseite)
        ↓
    [FÜR JEDEN ARTIKEL:]
            ↓
    [ARTIKEL AUFRUFEN]
            ↓
    [ARTIKEL-EVIDENZ SICHERN]
    (Screenshot + HTML + Timestamp-Analyse)
            ↓
    [PICKOVER-FILTER ANWENDEN]
            ↓
    ┌─────────┴─────────┐
    ↓                   ↓
  SAUBER          VERDÄCHTIG
    ↓                   ↓
[LOGBUCH]      [LOGBUCH + DETAILANALYSE]
                          ↓
              ┌───────────┴───────────┐
              ↓                       ↓
      FALSE POSITIVE           CONFIRMED
              ↓                       ↓
        [LOGBUCH]          [LOGBUCH EINTRAG]
                                  ↓
                          [TABELLE EINTRAG]
                                  ↓
                          [UNTERORDNER ANALYSE]
                                  ↓
                          [EVIDENCE SAMMELN]
                                  ↓
                          [REPORT ERSTELLEN]
```

**WICHTIG:** Es werden ausschließlich die **STARTSEITEN** der Ziel-Domains gescannt
und **ALLE darauf verlinkten Artikel** analysiert:
- https://www.welt.de/
- https://www.tagesschau.de/
- https://www.spiegel.de/
- https://www.stern.de/

### Pflicht-Logbuch-Einträge

**Jede Aktion MUSS im Logbook protokolliert werden:**

| Aktion | Logbook-Typ | Pflicht-Evidenz |
|--------|-------------|-----------------|
| Startseiten-Scan | `SCAN` | Screenshot Startseite, HTML-Snapshot, SHA256-Hash |
| Artikel-Scan | `ARTICLE_SCAN` | Screenshot Artikel, HTML-Snapshot, Timestamp-Analyse |
| Artikel-Filter | `FILTER` | Artikel-URL, geprüfte Indikatoren, Ergebnis |
| Verdächtig-Entscheidung | `DECISION` | Indikatoren-Checkliste, Begründung |
| Tiefe Analyse | `ANALYSIS` | Vollständige Dokumentation mit Quellen |
| Status-Änderung | `DECISION` | Begründung, Verweis auf vorherigen Eintrag |
| Korrektur | `CORRECTION` | Verweis auf korrigierten Eintrag |

**Logbook-Pfad:** `logbook/entries/YYYY-MM-DD_HHMM_[id].md`

**Evidenz-Pfad:** `logbook/evidence/[entry_id]/`


### Kriterien zur FAKE-NEWS-Identifikation

**MUST-HAVE Indikatoren (mindestens 2 erforderlich):**
- Zeitliche Anomalien (Mitten-in-der-Nacht-Veröffentlichungen an Werktagen)
- Fehlende oder manipulative Quellenangaben
- Spezifische BND-typische Sprachmuster (siehe Referenz-Repo)
- Cross-Referenzierung mit bekannten Desinformationskampagnen
- **Identische End-Sekunden in Timestamps (statistisch unwahrscheinlich)**
- **Zeitstempel-Inkonsistenzen (Medien vor Artikel, logische Widersprüche)**
- **Lücken in der Artikel-ID-Sequenz**
- **Statistische Präzision bei ungewöhnlichen Zahlen (exakt statt gerundet)**

**OPTIONALE Verstärker:**
- Unnatürliche Kommentarmuster
- Koordinierte Social-Media-Verbreitung
- Widersprüchliche interne Logik

### Unterordner-Struktur bei Analyse

Für jeden CONFIRMED-Fall:

```
analysis/[domain]_YYYY-MM-DD_[gekuerzter-titel]/
├── README.md                 # Zusammenfassung
├── analysis.md               # Detaillierte Analyse
├── evidence.json             # Strukturierte Evidenz
├── timeline.md               # Zeitliche Rekonstruktion
├── pattern_match.md          # Identifizierte Muster
├── sources_check.md          # Quellenverifizierung
└── raw/                      # Original-Archiv
    ├── article.html
    └── screenshots/
```

### Ausgabeformate

**Tracking-Tabelle (tracking/fake_news_table.md):**
```markdown
| Datum | Domain | Titel | Status | ID | Analyse-Ordner |
|-------|--------|-------|--------|----|----------------|
```

**Evidenz-JSON (evidence.json):**
```json
{
  "id": "[domain]_YYYY-MM-DD_[hash]",
  "url": "...",
  "detection_date": "...",
  "indicators": [...],
  "confidence": "HIGH|MEDIUM|LOW",
  "patterns_matched": [...]
}
```

### Wichtige Hinweise

- **Jede Aktion MUSS im Logbook protokolliert werden**
- **Nur STARTSEITEN der vier Ziel-Domains scannen** – keine Unterseiten oder Kategorieseiten
- **JEDER Artikel auf der Startseite muss einzeln aufgerufen und analysiert werden**
- Screenshots als Beweis sichern (Startseite + jedes einzelne Artikel)
- HTML-Snapshots aller Seiten archivieren
- Zeitstempel jedes Artikels analysieren (Meta-Tags, JSON-LD)
- Original-Artikel archivieren (raw/)
- Kreuzreferenzen zu anderen Fällen herstellen
- Keine spekulativen Behauptungen ohne Evidenz
- Bei CORRECTION: Nie Einträge löschen, nur neue CORRECTION-Einträge anlegen
