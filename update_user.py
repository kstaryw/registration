import hashlib
import re
import mysql.connector
from db_connection import get_connection


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def is_valid_email(email):
    pattern = r"^[^@]+@[^@]+\.[^@]+$"
    return re.match(pattern, email) is not None


def update_user(username, field, new_value):
    if field not in ["email", "password"]:
        print("You can only update email or password.")
        return

    if field == "email" and not is_valid_email(new_value):
        print("Invalid email format.")
        return

    if field == "password":
        new_value = hash_password(new_value)

    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = f"UPDATE users SET {field} = %s WHERE username = %s"
        cursor.execute(sql, (new_value, username))
        conn.commit()

        if cursor.rowcount == 0:
            print("User not found.")
        else:
            print(f"{field} updated successfully.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error updating user: {err}")


if __name__ == "__main__":
    update_user("alice01", "email", "alice_new@example.com")