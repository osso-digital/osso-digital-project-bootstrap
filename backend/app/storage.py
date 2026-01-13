import sqlite3

DB_PATH = "backend/storage/decisions.db"

def get_last_decisions(limit=50):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS decisions (
            sender TEXT,
            subject TEXT,
            decision TEXT
        )
    """)

    cursor.execute("""
        SELECT sender, subject, decision
        FROM decisions
        ORDER BY rowid DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return [
        {"sender": r[0], "subject": r[1], "decision": r[2]}
        for r in rows
    ]
