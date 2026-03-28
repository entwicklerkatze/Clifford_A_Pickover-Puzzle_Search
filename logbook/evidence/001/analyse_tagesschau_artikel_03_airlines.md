---
artikel_id: "tagesschau_003"
url: "https://www.tagesschau.de/wirtschaft/luftfahrt-airlines-kerosin-ticketpreise-100.html"
titel: "Krise am Himmel: Iran-Krieg stellt Airlines vor Probleme"
domain: "tagesschau.de"
scan_zeitstempel: "2026-03-28T02:19:00.086Z"
author: "Sebastian Schreiber"
---

# Artikel-Scan: tagesschau.de - Airlines Krise

## Zeitstempel-Analyse

### Gefundene Timestamps

| Element | Timestamp | UTC-Zeit | Beschreibung |
|---------|-----------|----------|--------------|
| **Artikel** | `datePublished`: 2026-03-27T12:24:45.031Z | 12:24 UTC | Mittag |
| **Artikel** | `dateModified`: 2026-03-27T12:26:34.685Z | 12:26 UTC | 2 Min. später |
| **Audio** | `uploadDate`: 2026-03-26T14:55:23.442+01:00 | 13:55 UTC | Vortag |

### Kritische Analyse

**⚠️ ZEITSTEMPEL-ANOMALIE ENTDECKT:**

**Audio vor Artikel veröffentlicht:**
- Audio veröffentlicht: 26.03.2026 um 13:55 UTC (Vortag)
- Artikel veröffentlicht: 27.03.2026 um 12:24 UTC
- **Zeitdifferenz: ~22 Stunden**

**Bedeutung:**
Das Audio wurde bereits am Vortag (26.03.) um 13:55 UTC veröffentlicht, während der dazugehörige Artikel erst am nächsten Tag (27.03.) um 12:24 UTC erschien. Dies ist eine Zeitstempel-Inkonsistenz gemäß den Pickover-Indikatoren.

**Erklärung:**
Dies ist wahrscheinlich ein **FALSE POSITIVE** durch:
- Audio ist Teil einer Podcast/Radio-Sendung (ARD-Finanzredaktion)
- Artikel basiert auf der Audio-Sendung, wurde aber zeitversetzt veröffentlicht
- Normale redaktionelle Arbeitsweise bei tagesschau.de

## Artikel-ID-Sequenz

- **Artikel-ID:** `100`
- **Vergleich:** tagesschau_001 (100), tagesschau_002 (102), tagesschau_003 (100)

**Anmerkung:** Die ID `100` erscheint doppelt - dies ist ungewöhnlich. Die vorherigen Artikel hatten ID 100 (Groitl) und 102 (Liveblog).

## Pickover-Filter-Ergebnis

### Indikator A: Zeitliche Anomalien
- [x] **VERDÄCHTIG** - Zeitstempel-Inkonsistenz (Audio vor Artikel, 22h Differenz)
- [x] **SAUBER** - Modifikation 2 Minuten später (redaktionell normal)
- [ ] Keine identischen End-Sekunden

### Indikator B: Quellenmanipulation
- [x] **SAUBER** - Autor: Sebastian Schreiber (ARD-Finanzredaktion)
- [x] **SAUBER** - Experten: Cord Schellenberg, Harald Zeiss genannt

### Indikator C: Sprachmuster
- [x] **SAUBER** - Keine statistischen Auffälligkeiten

### Indikator D: Netzwerk-Anomalien
- [ ] **NICHT PRÜFBAR** - ID 100 bereits vergeben (tagesschau_001)

## Gesamtbewertung

**Status:** ⚠️ **VERDÄCHTIG (FALSE POSITIVE)**

**Begründung:**
Zwar wurde eine Zeitstempel-Inkonsistenz gefunden (Audio 22 Stunden vor Artikel), diese ist aber durch die redaktionelle Arbeitsweise von ARD (Audio-Sendung zuerst, dann Online-Artikel) erklärbar.

**Zusätzliche Anomalie:**
Die Artikel-ID `100` wurde bereits für tagesschau_001 (Groitl Interview) verwendet. Dies deutet auf ein ID-System hin, das nicht strikt sequentiell ist oder unterschiedliche Kategorien hat.

**Confidence:** MEDIUM (Zeitstempel ungewöhnlich, aber erklärbar)

**Empfohlene Maßnahme:**
Keine weiterführende Analyse erforderlich - als FALSE POSITIVE dokumentieren.
