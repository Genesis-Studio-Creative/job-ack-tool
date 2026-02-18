# email_service.py
from database import get_all_emails, acknowledge_email

# -----------------------------
# Business logic layer
# -----------------------------

def list_emails():
    """
    Fetch all emails from database.
    Returns a list of tuples.
    """
    return get_all_emails()


def acknowledge(email_id, acknowledged_by):
    """
    Acknowledge an email safely.
    - Blocks if ID does not exist.
    - Blocks if email is already acknowledged.
    """
    # Call the database function
    acknowledge_email(email_id, acknowledged_by)
