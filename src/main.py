from database import init_db, insert_test_email

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully")

    insert_test_email()
    print("Test email inserted successfully.")
