# Clifford A. Pickover Puzzle Search

## Projektbeschreibung

Dieses Projekt dient der **systematischen Identifikation und Analyse von FAKE-NEWS-Artikeln** auf deutschen Nachrichtenseiten mittels Mustererkennung. Die Methodik basiert auf den "Clifford A. Pickover Puzzles" – einer spezifischen Analysetechnik, die von BND-Kontexten inspiriert wurde und spezifische narrative Muster in Medienberichterstattung erkennt.

## Zielsetzung

- **Automatisierte Überwachung** der vier Nachrichtenseiten:
  - welt.de (Startseite + alle Artikel)
  - tagesschau.de (Startseite + alle Artikel)
  - spiegel.de (Startseite + alle Artikel)
  - stern.de (Startseite + alle Artikel)

- **Vollständige Artikel-Analyse:**
  - Startseite scannen und sichern
  - ALLE Artikel-URLs extrahieren
  - JEDEN Artikel einzeln aufrufen und analysieren
  - Zeitstempel, Meta-Daten und HTML prüfen

- **Mustererkennung** basierend auf charakteristischen Merkmalen:
  - Narrative Strukturen
  - Sprachliche Indikatoren
  - Zeitliche Veröffentlichungsmuster
  - Quellenreferenzierungsmuster
  - Semantische Anomalien

- **Kategorisierung und Dokumentation**:
  - Zentrale Tracking-Tabelle für identifizierte FAKE-NEWS
  - Tiefgehende Analyse in dedizierten Unterordnern pro Fall

## Projektstruktur

```
/
├── README.md                 # Diese Datei
├── AGENTS.md                 # Anweisungen für KI-Agents
├── ASSUMPTIONS.txt           # Grundannahmen und Methodik
├── tracking/                 # Zentrale Tracking-Datenbank
│   └── fake_news_table.md    # Übersicht aller identifizierten Fälle
├── analysis/                 # Tiefe Analysen pro Fall
│   ├── [domain]_YYYY-MM-DD_[title]/
│   │   ├── analysis.md
│   │   ├── evidence.json
│   │   └── pattern_report.md
├── data/                     # Rohdaten und Scrapes
├── scripts/                  # Automatisierungsskripte
└── docs/                     # Zusätzliche Dokumentation
```

## Methodik: Die Pickover-Musteranalyse

Die Pickover-Analyse identifiziert FAKE-NEWS durch folgende Kriterien:

1. **Strukturelle Indikatoren**
   - Abweichende journalistische Standards
   - Ungewöhnliche Quellenhierarchien
   - Inkonsistente Zeitstempel

2. **Semantische Muster**
   - Spezifische Sprachkonstrukte
   - Wiederkehrende narrative Frameworks
   - Emotionale Manipulationstechniken

3. **Netzwerkanalyse**
   - Cross-Referenzierung verdächtiger Artikel
   - Identifikation koordinierter Veröffentlichungsmuster
   - Autoren- und Quellenzuordnung

## Referenzen

- [Merz Regierung Verfolgt mich mit Hackern](https://github.com/sigridfuhrenkamp-cyber/Merz_Regierung_Verfolgt_mich_mit_Hackern) - Beispiel für BND-typische Muster
- [Der Wal von Niendorf Teil 2](https://github.com/entwicklerkatze/Der_Wal_von_Niendorf-Teil2) - Methodische Vorlage
- [12000 Straftaten bei 189 Nationalitäten](https://github.com/entwicklerkatze/12000_Straftaten_bei_189_Nationalitaeten) - Analyseframework

## Nutzung

1. **Monitoring**: Startseite scannen + ALLE verlinkten Artikel analysieren
2. **Filterung**: Pickover-Muster auf jeden Artikel anwenden
3. **Bewertung**: Einordnung verdächtiger Artikel in Tracking-Tabelle
4. **Analyse**: Tiefe Untersuchung markierter Fälle mit vollständiger Evidenz

## Lizenz

Siehe LICENSE Datei

## Kontakt & Beiträge

Dies ist ein rein analytisches Forschungsprojekt zur Medienbeobachtung.
