from datetime import datetime
from database import get_all_emails, acknowledge_email, insert_email, get_pending_emails

def simulate_new_email():
    subject = "New Job Alert"
    sender = "hr@company.com"
    received_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    insert_email(subject, sender, received_at)
    print("New email simulated.")

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

def check_for_pending_emails():
    pending = get_pending_emails()

    if pending:
        print(f"\nYou have {len(pending)} unacknowledged email(s)!")
    else:
        print("\nNo pending emails.")    
