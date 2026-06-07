import sqlite3
import os
 
DB_PATH = os.path.join(os.path.dirname(__file__), 'disasters.db')
 
 
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS disasters (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            title   TEXT    NOT NULL,
            type    TEXT    NOT NULL,
            lat     REAL,
            lon     REAL,
            date    TEXT,
            mag     REAL,
            info    TEXT,
            UNIQUE(title, date)
        )
    ''')
    conn.commit()
    conn.close()
 
 
def save_disasters(disasters: list):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    inserted = 0
    for d in disasters:
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO disasters (title, type, lat, lon, date, mag, info)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (d.title, d.type, d.lat, d.lon, d.date, d.mag, d.info))
            if cursor.rowcount > 0:
                inserted += 1
        except Exception as e:
            print(f"[DB] Błąd zapisu: {e}")
    conn.commit()
    conn.close()
    return inserted
 
 
def get_disasters(type_filter: str = None, limit: int = 1000) -> list[dict]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
 
    if type_filter:
        cursor.execute(
            'SELECT * FROM disasters WHERE type = ? ORDER BY date DESC LIMIT ?',
            (type_filter, limit)
        )
    else:
        cursor.execute(
            'SELECT * FROM disasters ORDER BY date DESC LIMIT ?',
            (limit,)
        )
 
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return rows
 
 
def get_stats() -> dict:
    """Zwraca podstawowe statystyki z bazy."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT type, COUNT(*) FROM disasters GROUP BY type')
    stats = {row[0]: row[1] for row in cursor.fetchall()}
    cursor.execute('SELECT COUNT(*) FROM disasters')
    stats['total'] = cursor.fetchone()[0]
    conn.close()
    return stats