from email_service import list_emails, acknowledge, simulate_new_email, check_for_pending_emails

if __name__ == "__main__":

    simulate_new_email()

    check_for_pending_emails()

    # Show current emails
    emails = list_emails()
    print("\nCurrent Emails:")
    for email in emails:
        print(f"""
              ID: {email[0]}
              Subject: {email[1]}
              Sender: {email[2]}
              Received: {email[3]}
              Acknowledged By: {email[4]}
              Status: {email[5]}
              --------------------------
              """)

    # User input
    email_id = int(input("\nEnter Email ID to Acknowledge: "))
    ack_by = input("Enter your Name: ")

    # Business logic handled by service layer
    acknowledge(email_id, ack_by)

    # Show updated emails
    updated_emails = list_emails()
    print("\nUpdated Emails:")
    for email in updated_emails:
        print(f"""
              ID: {email[0]}
              Subject: {email[1]}
              Sender: {email[2]}
              Received: {email[3]}
              Acknowledged By: {email[4]}
              Status: {email[5]}
              --------------------------
              """)
