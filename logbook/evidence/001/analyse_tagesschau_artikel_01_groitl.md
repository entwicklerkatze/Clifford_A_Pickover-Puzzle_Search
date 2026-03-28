---
artikel_id: "tagesschau_001"
url: "https://www.tagesschau.de/ausland/asien/groitl-interview-nahost-100.html"
titel: "Interview zum Iran-Krieg: Warum Trump auf Zeit spielt"
domain: "tagesschau.de"
scan_zeitstempel: "2026-03-28T01:47:33.743Z"
---

# Artikel-Scan: tagesschau.de - Groitl Interview

## ⚠️ ZEITSTEMPEL-ANOMALIE ENTDECKT

### Gefundene Timestamps

| Element | Timestamp | UTC-Zeit |
|---------|-----------|----------|
| **Video** | `datePublished`: 2026-03-27T15:13:46.620Z | 15:13 UTC |
| **Video** | `uploadDate`: 2026-03-27T16:13:46.635+01:00 | 15:13 UTC |
| **Artikel** | `datePublished`: 2026-03-27T16:43:27.823Z | 16:43 UTC |
| **Artikel** | `dateModified`: 2026-03-27T17:57:43.587Z | 17:57 UTC |
| **Artikel** | Meta `date`: 2026-03-27T17:43:27 | 16:43 UTC (MEZ) |

### Kritische Analyse

**Zeitstempel-Inkonsistenz (Indikator A - VERDÄCHTIG):**
- Video veröffentlicht: 15:13 UTC
- Artikel veröffentlicht: 16:43 UTC
- **Zeitdifferenz: 1 Stunde 30 Minuten**

**Bedeutung:**
Das Video wurde 90 Minuten vor dem Artikel veröffentlicht. Dies ist technisch eine Zeitstempel-Inkonsistenz gemäß den Pickover-Indikatoren.

**Erklärung:**
Dies ist wahrscheinlich ein **False Positive** - logisch erklärbar durch:
- TV-Sendung (tagesschau24) läuft um 15:00 Uhr
- Artikel wird nach der Sendung online gestellt (16:43 UTC = 17:43 MEZ)
- Normale redaktionelle Arbeitsweise bei ARD

### Pickover-Filter-Ergebnis

### Indikator A: Zeitliche Anomalien
- [ ] Veröffentlichung zwischen 02:00-05:00 Uhr
- [x] **VERDÄCHTIG** - Zeitstempel-Inkonsistenz (Video vor Artikel)
- [ ] Identische End-Sekunden

**Bewertung:** FALSE POSITIVE (redaktionell bedingt)

### Indikator B: Quellenmanipulation
- [x] **SAUBER** - Quelle klar identifiziert (Groitl, Uni Regensburg)

### Indikator C: Sprachmuster
- [x] **SAUBER** - Keine statistischen Auffälligkeiten

### Indikator D: Netzwerk-Anomalien
- [x] **SAUBER** - Artikel-ID 100 folgt Sequenz

## Gesamtbewertung

**Status:** ⚠️ **VERDÄCHTIG (FALSE POSITIVE)**

**Begründung:**
Zwar wurde eine Zeitstempel-Inkonsistenz gefunden (Video vor Artikel), diese ist aber durch die redaktionelle Arbeitsweise von ARD (TV zuerst, dann Online-Artikel) vollständig erklärbar.

**Confidence:** HIGH (Fehlalarm durch normale TV-Online-Workflow)

**Empfohlene Maßnahme:**
Keine weitere Analyse erforderlich - als SAUBER markieren mit Anmerkung.

## Artikel-ID-Sequenz
- Artikel-ID: `100`
- Video-ID: `1569548`
- Keine Lücke in Sequenz erkennbar (unterschiedliche ID-Systeme für Videos/Artikel)
