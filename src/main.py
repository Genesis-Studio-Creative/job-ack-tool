from database import init_db, get_all_emails, acknowledge_email

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully")

    #insert_test_email()
    #print("Test email inserted successfully.")

    # Show current emails
    emails = get_all_emails()
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

    # Take user input
    email_id = int(input("Enter Email ID to acknowledge: "))
    ack_by = input("Enter your name: ")

    acknowledge_email(email_id, ack_by)
    print("\nEmail acknowledged successfully")

    # Show updated emails
    updated_emails = get_all_emails()
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