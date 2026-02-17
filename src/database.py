import sqlite3
from datetime import datetime

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

def insert_test_email():
    conn = sqlite3.connect("job_ack.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO emails (subject, sender, received_at, acknowledged_by, status)
        VALUES (?, ?, ?, ?, ?)
    """, (
        "Test Job Email",
        "test@example.com",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        None,
        "Pending"
    ))

    conn.commit()
    conn.close()

def get_all_emails():
    conn = sqlite3.connect("job_ack.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emails")
    rows = cursor.fetchall()

    conn.close()
    return rows

