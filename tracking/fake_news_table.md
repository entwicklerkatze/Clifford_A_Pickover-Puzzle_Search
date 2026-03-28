# Fake-News Tracking-Tabelle

## Scan-Ergebnisse vom 27.03.2026

| Zeitstempel | Domain | Artikel-ID | Titel | Status | Pickover-Indikatoren | Analyse-Datei |
|-------------|--------|------------|-------|--------|---------------------|---------------|
| 2026-03-27 20:24 | welt.de | welt_001 | Merz stellt sich offen gegen Trumps Krieg | ✅ SAUBER | Keine | analyse_welt_artikel_01_merz_iran.md |
| 2026-03-27 20:09 | welt.de | welt_002 | Christian Ulmen zu Vorwürfen | ✅ SAUBER | Keine | analyse_welt_artikel_02_ulmen.md |
| 2026-03-27 16:43 | tagesschau.de | tagesschau_001 | Groitl Interview Iran-Krieg | ⚠️ FALSE POSITIVE | Zeitstempel-Inkonsistenz (Video vor Artikel) | analyse_tagesschau_artikel_01_groitl.md |
| 2026-03-27 20:33 | tagesschau.de | tagesschau_002 | Iran Liveblog | ✅ SAUBER | Keine | analyse_tagesschau_artikel_02_liveblog.md |
| 2026-03-24 07:19 | spiegel.de | spiegel_001 | Juso-Chef Türmer SPD-Krise | ⚠️ FALSE POSITIVE | Zeitliche Lücke (4h 51min) | analyse_spiegel_artikel_01_tuermer.md |
| 2026-03-27 19:54 | stern.de | stern_001 | Deutsche Bahn ruiniert | ✅ SAUBER | Keine | analyse_stern_artikel_01_bahn.md |

## Zusammenfassung

**Gesamt gescannte Artikel:** 6
- ✅ **SAUBER:** 4 Artikel
- ⚠️ **VERDÄCHTIG (False Positive):** 2 Artikel
- ❌ **CONFIRMED FAKE-NEWS:** 0 Artikel

## Identifizierte Muster (False Positives)

### 1. tagesschau.de - Groitl Interview
- **Indikator:** Zeitstempel-Inkonsistenz (Video 15:13 UTC vor Artikel 16:43 UTC)
- **Erklärung:** TV-Sendung (tagesschau24) um 15:00 Uhr, Artikel danach
- **Bewertung:** Normaler redaktioneller Workflow

### 2. spiegel.de - Türmer Interview
- **Indikator:** Zeitliche Lücke 4h 51min zwischen Veröffentlichung und Modifikation
- **Erklärung:** Wahrscheinlich zeitversetzte Publikation oder Nachbearbeitung
- **Bewertung:** Nicht verdächtig, aber ungewöhnlich

## Statistik nach Domain

| Domain | Gescannt | SAUBER | VERDÄCHTIG | CONFIRMED |
|--------|----------|--------|-----------|-----------|
| welt.de | 2 | 2 | 0 | 0 |
| tagesschau.de | 2 | 1 | 1 | 0 |
| spiegel.de | 1 | 0 | 1 | 0 |
| stern.de | 1 | 1 | 0 | 0 |

## Nächste Schritte

- [ ] Weitere Artikel aus den Startseiten scannen
- [ ] Tiefe Analyse bei VERDÄCHTIG-Befunden (falls False Positive ausgeschlossen)
- [ ] Kreuzreferenzen zwischen Artikeln herstellen
- [ ] Zeitraum erweitern (mehr Tage scannen)
