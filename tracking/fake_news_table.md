# Fake-News Tracking-Tabelle

## Scan-Ergebnisse vom 27.03.2026

| Zeitstempel | Domain | Artikel-ID | Titel | Status | Pickover-Indikatoren | Analyse-Datei |
|-------------|--------|------------|-------|--------|---------------------|---------------|
| 2026-03-27 20:24 | welt.de | welt_001 | Merz stellt sich offen gegen Trumps Krieg | ✅ SAUBER | Keine | analyse_welt_artikel_01_merz_iran.md |
| 2026-03-27 20:09 | welt.de | welt_002 | Christian Ulmen zu Vorwürfen | ✅ SAUBER | Keine | analyse_welt_artikel_02_ulmen.md |
| 2026-03-27 20:17 | welt.de | welt_003 | Merz kündigt Reformpaket an | ✅ SAUBER | Keine | analyse_welt_artikel_03_merz_reformen.md |
| 2026-03-27 17:32 | welt.de | welt_004 | Deutsche Bahn Bilanz | ✅ SAUBER | Keine | analyse_welt_artikel_04_bahn.md |
| 2026-03-27 16:43 | tagesschau.de | tagesschau_001 | Groitl Interview Iran-Krieg | ⚠️ FALSE POSITIVE | Zeitstempel-Inkonsistenz (Video vor Artikel) | analyse_tagesschau_artikel_01_groitl.md |
| 2026-03-27 20:33 | tagesschau.de | tagesschau_002 | Iran Liveblog | ✅ SAUBER | Keine | analyse_tagesschau_artikel_02_liveblog.md |
| 2026-03-27 12:24 | tagesschau.de | tagesschau_003 | Airlines Krise | ⚠️ FALSE POSITIVE | Zeitstempel-Inkonsistenz (Audio vor Artikel) | analyse_tagesschau_artikel_03_airlines.md |
| 2026-03-24 07:19 | spiegel.de | spiegel_001 | Juso-Chef Türmer SPD-Krise | ⚠️ FALSE POSITIVE | Zeitliche Lücke (4h 51min) | analyse_spiegel_artikel_01_tuermer.md |
| 2026-03-27 22:11 | spiegel.de | spiegel_002 | Rubio wirft Selenskyj Lügen vor | ✅ SAUBER | Keine | analyse_spiegel_artikel_02_rubio.md |
| 2026-03-27 19:54 | stern.de | stern_001 | Deutsche Bahn ruiniert | ✅ SAUBER | Keine | analyse_stern_artikel_01_bahn.md |

## Zusammenfassung

**Gesamt gescannte Artikel:** 10
- ✅ **SAUBER:** 7 Artikel (70%)
- ⚠️ **FALSE POSITIVE:** 3 Artikel (30%)
- ❌ **CONFIRMED FAKE-NEWS:** 0 Artikel (0%)

## Identifizierte Muster (False Positives)

### 1. tagesschau.de - Groitl Interview (tagesschau_001)
- **Indikator:** Zeitstempel-Inkonsistenz (Video 15:13 UTC vor Artikel 16:43 UTC)
- **Erklärung:** TV-Sendung (tagesschau24) um 15:00 Uhr, Artikel danach
- **Bewertung:** Normaler redaktioneller Workflow

### 2. spiegel.de - Türmer Interview (spiegel_001)
- **Indikator:** Zeitliche Lücke 4h 51min zwischen Veröffentlichung und Modifikation
- **Erklärung:** Wahrscheinlich zeitversetzte Publikation oder Nachbearbeitung
- **Bewertung:** Nicht verdächtig, aber ungewöhnlich

### 3. tagesschau.de - Airlines Krise (tagesschau_003)
- **Indikator:** Audio 22 Stunden vor Artikel veröffentlicht
- **Erklärung:** Audio-Podcast zuerst, dann Online-Artikel
- **Bewertung:** Redaktionell bedingt

## Statistik nach Domain

| Domain | Gescannt | SAUBER | FALSE POSITIVE | CONFIRMED |
|--------|----------|--------|---------------|-----------|
| welt.de | 4 | 4 | 0 | 0 |
| tagesschau.de | 3 | 1 | 2 | 0 |
| spiegel.de | 2 | 1 | 1 | 0 |
| stern.de | 1 | 1 | 0 | 0 |
| **GESAMT** | **10** | **7** | **3** | **0** |

## Zeitliche Verteilung

- **Früh (06:00-12:00 UTC):** 1 Artikel (spiegel_001)
- **Mittag (12:00-18:00 UTC):** 3 Artikel (welt_004, tagesschau_001, tagesschau_003)
- **Abend (18:00-24:00 UTC):** 6 Artikel (alle anderen)

## Nächste Schritte

- [ ] Weitere Artikel aus den Startseiten scannen (Ziel: 20+ Artikel)
- [ ] Zeitraum erweitern (mehr Tage scannen)
- [ ] Tiefe Analyse bei VERDÄCHTIG-Befunden (falls False Positive ausgeschlossen)
- [ ] Kreuzreferenzen zwischen Artikeln herstellen
- [ ] Statistische Auswertung über Zeitstempel-Muster

---

*Letzte Aktualisierung: 28.03.2026 02:22 UTC*
