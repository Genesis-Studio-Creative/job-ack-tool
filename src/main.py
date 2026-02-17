from database import init_db, insert_test_email, get_all_emails

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully")

    #insert_test_email()
    #print("Test email inserted successfully.")

    emails = get_all_emails()

    print("\nAll Emails in Database:")
    for email in emails:
        print(f"""ID: {email[0]}
              Subject: {email[1]}
              Sender: {email[2]}
              Received: {email[3]}
              Acknowledged By: {email[4]}
              Status: {email[5]}
              --------------------------
              """)
