import sqlite3

DB_NAME = "job_ack.db"

def init_db():
    # Connect to SQLite database (creates file if not exists)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create emails table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY,
            subject TEXT,
            sender TEXT,
            received_at TEXT,
            acknowledged_by TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()
