# create_user.py
# Handles creating a new user record in the database.
# Includes input validation, password hashing, and a parameterized SQL insert.

import hashlib
import re
import mysql.connector
from db_connection import get_connection


def hash_password(password):
    """
    Hashes a plaintext password using SHA-256.

    Inputs:
        password (str): The plaintext password to hash.

    Returns:
        str: The hexadecimal SHA-256 digest of the password.
    """
    # Encode the string to bytes before hashing, then return as a hex string
    return hashlib.sha256(password.encode()).hexdigest()


def is_valid_email(email):
    """
    Checks whether an email address has a valid format.

    Inputs:
        email (str): The email address to validate.

    Returns:
        bool: True if the email matches the expected pattern, False otherwise.
    """
    # Regex pattern requires at least one character before @, a domain, and a TLD
    pattern = r"^[^@]+@[^@]+\.[^@]+$"
    return re.match(pattern, email) is not None


def create_user(username, email, password, city, company, job_title):
    """
    Inserts a new user into the users table in the database.

    Validates required fields and email format before inserting.
    Stores the password as a SHA-256 hash rather than plaintext.

    Inputs:
        username  (str): The user's chosen username.
        email     (str): The user's email address.
        password  (str): The user's plaintext password (will be hashed before storage).
        city      (str): The user's city.
        company   (str): The user's company or organization.
        job_title (str): The user's job title.

    Returns:
        None. Prints a success or error message to the console.
    """
    # Ensure the three required fields are not empty or None
    if not username or not email or not password:
        print("Username, email, and password are required.")
        return

    # Reject addresses that don't follow a basic email structure
    if not is_valid_email(email):
        print("Invalid email format.")
        return

    # Hash the password so it is never stored in plaintext
    hashed_password = hash_password(password)

    try:
        # Open a connection to the database using credentials from db.yaml
        conn = get_connection()
        # A cursor lets us execute SQL statements and retrieve results
        cursor = conn.cursor()

        # Parameterized query — %s placeholders prevent SQL injection
        sql = """
        INSERT INTO users (username, email, password, city, company, job_title)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        # Tuple of values that map positionally to the %s placeholders above
        values = (username, email, hashed_password, city, company, job_title)

        # Execute the INSERT statement with the provided values
        cursor.execute(sql, values)
        # Commit saves the transaction to the database permanently
        conn.commit()

        print("User created successfully.")

        # Release the cursor and connection resources
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error creating user: {err}")


if __name__ == "__main__":
    create_user(
        username="alice01",
        email="alice@example.com",
        password="mypassword123",
        city="Boston",
        company="MIT",
        job_title="Student"
    )