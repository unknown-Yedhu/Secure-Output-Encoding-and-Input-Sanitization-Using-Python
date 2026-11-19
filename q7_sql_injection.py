import sqlite3

DATABASE = "q7_users.db"


def setup_database():
    """Create the database and sample user table."""

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Insert a sample user
    cursor.execute("""
        INSERT OR IGNORE INTO users (username, password)
        VALUES (?, ?)
    """, ("admin", "admin123"))

    connection.commit()
    connection.close()


def authenticate(username, password):
    """Authenticate using a parameterized SQL query."""

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Secure parameterized query
    query = "SELECT * FROM users WHERE username = ? AND password = ?"

    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    connection.close()

    return user is not None


def test_login(username, password):
    print("\nTesting Login")
    print("-" * 40)
    print(f"Username: {username}")
    print(f"Password: {password}")

    if authenticate(username, password):
        print("RESULT: Login Successful")
    else:
        print("RESULT: Login Failed")


if __name__ == "__main__":
    setup_database()

    print("=" * 60)
    print("SQL INJECTION PREVENTION USING PARAMETERIZED QUERIES")
    print("=" * 60)

    # Test 1: Valid credentials
    test_login("admin", "admin123")

    # Test 2: Invalid credentials
    test_login("admin", "wrongpassword")

    # Test 3: SQL injection attempt
    test_login("' OR '1'='1", "anything")

    print("\n" + "=" * 60)
    print("SECURITY VERIFICATION")
    print("=" * 60)
    print("Parameterized queries prevent SQL injection.")
    print("User input is treated as data, not SQL code.")
    print("=" * 60)