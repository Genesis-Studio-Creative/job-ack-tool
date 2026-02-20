import sqlite3
import os
from datetime import datetime

DB_NAME = "job_ack.db"

# Get absolute path of this file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Absolute path to database file
DB_PATH = os.path.join(BASE_DIR, "job_ack.db")


def init_db():
    # Connect to SQLite database (creates file if not exists)
    conn = sqlite3.connect(DB_PATH)
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


def insert_email(subject, sender, received_at, status="Pending"):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO emails (subject, sender, received_at, acknowledged_by, status)
        VALUES (?, ?, ?, ?, ?)
    """, (subject, sender, received_at, None, status))

    conn.commit()
    conn.close()


def get_all_emails():
    # Fetch all emails from database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emails")
    rows = cursor.fetchall()

    conn.close()
    return rows


def acknowledge_email(email_id, acknowledged_by):
    # Update email acknowledgement status
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT status FROM emails WHERE id = ?", (email_id,))
    result = cursor.fetchone()

    if not result:
        print("Email ID not found.")
        conn.close()
        return
    
    if result[0] and result[0].strip().lower() == "acknowledged":
        print("Email already acknowledged.")
        conn.close()
        return

    cursor.execute("""
        UPDATE emails
        SET status = ?, acknowledged_by = ?
        WHERE id = ?
    """, ("Acknowledged", acknowledged_by, email_id))

    conn.commit()
    conn.close()

def get_pending_emails():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emails WHERE status = 'Pending'")
    rows = cursor.fetchall()

    conn.close()
    return rows