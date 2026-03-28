#!/usr/bin/env python3
"""
Scan Report Generator für Pickover Puzzle Search

Dieses Script generiert automatisch HTML-Reports aus Logbook-Daten
und aktualisiert die index.html mit neuen Scan-Einträgen.

Verwendung:
    python generate_scan_report.py --date 2026-03-28 --time 1430 --articles 8
"""

import argparse
import json
import os
import re
from datetime import datetime
from pathlib import Path


def generate_scan_html(scan_id: str, date: str, time: str, articles_data: list) -> str:
    """Generiert eine einzelne Scan-Report HTML-Datei."""
    
    # Statistiken berechnen
    clean_count = sum(1 for a in articles_data if a['status'] == 'clean')
    suspicious_count = sum(1 for a in articles_data if a['status'] == 'suspicious')
    confirmed_count = sum(1 for a in articles_data if a['status'] == 'confirmed')
    
    # Artikel-HTML generieren
    articles_html = ""
    for article in articles_data:
        status_class = article['status']
        status_icon = "✓" if article['status'] == 'clean' else "⚠" if article['status'] == 'suspicious' else "✗"
        status_text = "SAUBER" if article['status'] == 'clean' else "FALSE POSITIVE" if article['status'] == 'suspicious' else "CONFIRMED FAKE"
        
        articles_html += f'''
                <div class="article-item {status_class}">
                    <div class="article-status-icon {status_class}">{status_icon}</div>
                    <div class="article-info">
                        <div class="article-domain">{article['domain']}</div>
                        <div class="article-title">{article['title']}</div>
                        <div class="article-time">{article['timestamp']}</div>
                        <span class="article-status {status_class}">{status_text}</span>
                        <div class="indicators">{article.get('indicators', 'Keine Pickover-Indikatoren gefunden')}</div>
                    </div>
                </div>
'''
    
    # Gesamtes HTML-Dokument
    html = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scan Report - {date} | Pickover Puzzle Search</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #1a1a2e;
            --secondary: #16213e;
            --accent: #0f3460;
            --danger: #e94560;
            --success: #00d9ff;
            --warning: #ffc107;
            --text: #eaeaea;
            --text-muted: #a0a0a0;
            --card-bg: rgba(255, 255, 255, 0.05);
            --border: rgba(255, 255, 255, 0.1);
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: var(--text);
            min-height: 100vh;
            line-height: 1.6;
        }}
        .container {{ max-width: 1000px; margin: 0 auto; padding: 2rem; }}
        .back-link {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--text-muted);
            text-decoration: none;
            margin-bottom: 2rem;
            transition: color 0.3s ease;
        }}
        .back-link:hover {{ color: var(--success); }}
        header {{
            padding: 2rem 0;
            border-bottom: 1px solid var(--border);
            margin-bottom: 3rem;
        }}
        .scan-id {{
            font-size: 0.85rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 0.5rem;
        }}
        h1 {{ font-size: 2rem; font-weight: 700; margin-bottom: 1rem; }}
        .scan-meta {{
            display: flex;
            gap: 2rem;
            color: var(--text-muted);
            font-size: 0.9rem;
            flex-wrap: wrap;
        }}
        .scan-meta span {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .summary-cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 3rem;
        }}
        .summary-card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
        }}
        .summary-number {{
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }}
        .summary-number.clean {{ color: var(--success); }}
        .summary-number.suspicious {{ color: var(--warning); }}
        .summary-number.confirmed {{ color: var(--danger); }}
        .summary-label {{ color: var(--text-muted); font-size: 0.85rem; }}
        .section {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
        }}
        .section-title {{
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}
        .article-list {{
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }}
        .article-item {{
            display: flex;
            align-items: flex-start;
            gap: 1rem;
            padding: 1.25rem;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 8px;
            border-left: 4px solid var(--success);
        }}
        .article-item.suspicious {{ border-left-color: var(--warning); }}
        .article-item.confirmed {{ border-left-color: var(--danger); }}
        .article-status-icon {{
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
            flex-shrink: 0;
        }}
        .article-status-icon.clean {{ background: rgba(0, 217, 255, 0.1); }}
        .article-status-icon.suspicious {{ background: rgba(255, 193, 7, 0.1); }}
        .article-status-icon.confirmed {{ background: rgba(233, 69, 96, 0.1); }}
        .article-info {{ flex: 1; }}
        .article-domain {{
            font-size: 0.8rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 0.25rem;
        }}
        .article-title {{ font-weight: 600; margin-bottom: 0.5rem; }}
        .article-time {{
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-bottom: 0.5rem;
        }}
        .article-status {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 500;
        }}
        .article-status.clean {{
            background: rgba(0, 217, 255, 0.1);
            color: var(--success);
        }}
        .article-status.suspicious {{
            background: rgba(255, 193, 7, 0.1);
            color: var(--warning);
        }}
        .article-status.confirmed {{
            background: rgba(233, 69, 96, 0.1);
            color: var(--danger);
        }}
        .indicators {{
            margin-top: 0.75rem;
            font-size: 0.85rem;
            color: var(--text-muted);
        }}
        footer {{
            text-align: center;
            padding: 2rem;
            color: var(--text-muted);
            border-top: 1px solid var(--border);
            margin-top: 3rem;
        }}
        @media (max-width: 768px) {{
            .container {{ padding: 1rem; }}
            .scan-meta {{ flex-direction: column; gap: 0.5rem; }}
            .article-item {{ flex-direction: column; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="index.html" class="back-link">← Zurück zur Übersicht</a>

        <header>
            <div class="scan-id">Scan #{scan_id}</div>
            <h1>Scan Report - {date}</h1>
            <div class="scan-meta">
                <span>🕐 {time} Uhr</span>
                <span>📄 {len(articles_data)} Artikel analysiert</span>
                <span>🌐 4 Domains</span>
            </div>
        </header>

        <div class="summary-cards">
            <div class="summary-card">
                <div class="summary-number clean">{clean_count}</div>
                <div class="summary-label">SAUBER</div>
            </div>
            <div class="summary-card">
                <div class="summary-number suspicious">{suspicious_count}</div>
                <div class="summary-label">FALSE POSITIVE</div>
            </div>
            <div class="summary-card">
                <div class="summary-number confirmed">{confirmed_count}</div>
                <div class="summary-label">CONFIRMED</div>
            </div>
            <div class="summary-card">
                <div class="summary-number" style="color: var(--text);">{len(articles_data)}</div>
                <div class="summary-label">ARTIKEL</div>
            </div>
        </div>

        <div class="section">
            <h2 class="section-title">📋 Analysierte Artikel</h2>
            <div class="article-list">
{articles_html}
            </div>
        </div>

        <footer>
            <p>Clifford A. Pickover Puzzle Search • Automatisierte Medienanalyse</p>
            <p style="font-size: 0.85rem; margin-top: 0.5rem;">Scan ID: {scan_id} • {date}</p>
        </footer>
    </div>
</body>
</html>'''
    
    return html


def update_index_html(scan_id: str, date: str, time: str, total_articles: int, status: str):
    """Fügt einen neuen Scan-Eintrag zur index.html hinzu."""
    
    index_path = Path('index.html')
    if not index_path.exists():
        print("Fehler: index.html nicht gefunden!")
        return False
    
    content = index_path.read_text(encoding='utf-8')
    
    # Status-Farbe bestimmen
    status_class = 'clean' if status == 'clean' else 'suspicious' if status == 'suspicious' else 'confirmed'
    status_text = '✓ SAUBER' if status == 'clean' else '⚠ FALSE POSITIVE' if status == 'suspicious' else '✗ CONFIRMED FAKE'
    
    # Neuer Scan-Eintrag
    new_scan_entry = f'''                <a href="scan_{date.replace('.', '-').replace(' ', '_')}_{time.replace(':', '')}.html" class="scan-item">
                    <div class="scan-info">
                        <span class="scan-date">{date}, {time} Uhr</span>
                        <span class="scan-meta">Scan #{scan_id} • {total_articles} Artikel analysiert • 4 Domains</span>
                    </div>
                    <span class="scan-status {status_class}">{status_text}</span>
                </a>
'''
    
    # Füge vor dem schließenden </div> der scan-list hinzu
    if '<div class="scan-list" id="scanList">' in content:
        content = content.replace(
            '<div class="scan-list" id="scanList">',
            f'<div class="scan-list" id="scanList">\n{new_scan_entry}'
        )
    
    index_path.write_text(content, encoding='utf-8')
    print(f"✓ index.html aktualisiert mit Scan #{scan_id}")
    return True


def main():
    parser = argparse.ArgumentParser(description='Generiert Scan-Report HTML-Dateien')
    parser.add_argument('--date', required=True, help='Datum (DD.MM.YYYY)')
    parser.add_argument('--time', required=True, help='Zeit (HH:MM)')
    parser.add_argument('--articles', type=int, default=0, help='Anzahl Artikel')
    parser.add_argument('--data', help='JSON-Datei mit Artikel-Daten')
    
    args = parser.parse_args()
    
    # Scan-ID generieren (basierend auf vorhandenen Scans)
    existing_scans = list(Path('.').glob('scan_*.html'))
    scan_id = str(len(existing_scans) + 1).zfill(3)
    
    # Beispiel-Daten laden oder generieren
    if args.data and os.path.exists(args.data):
        with open(args.data, 'r', encoding='utf-8') as f:
            articles_data = json.load(f)
    else:
        # Demo-Daten für Test
        articles_data = [
            {
                'domain': 'beispiel.de',
                'title': 'Beispiel-Artikel für Demo',
                'timestamp': f'{args.date} • {args.time} Uhr',
                'status': 'clean',
                'indicators': 'Keine Pickover-Indikatoren gefunden'
            }
        ]
    
    # HTML-Datei generieren
    filename = f"scan_{args.date.replace('.', '-').replace(' ', '_')}_{args.time.replace(':', '')}.html"
    html_content = generate_scan_html(scan_id, args.date, args.time, articles_data)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ Scan-Report erstellt: {filename}")
    
    # Index aktualisieren
    overall_status = 'suspicious' if any(a['status'] == 'suspicious' for a in articles_data) else 'clean'
    update_index_html(scan_id, args.date, args.time, len(articles_data), overall_status)
    
    print(f"\n✓ Scan #{scan_id} erfolgreich verarbeitet!")
    print(f"  - Report: {filename}")
    print(f"  - Index: index.html aktualisiert")


if __name__ == '__main__':
    main()
