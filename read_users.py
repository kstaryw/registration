import mysql.connector
from db_connection import get_connection


def read_all_users():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, username, email, city, company, job_title
            FROM users
        """)
        users = cursor.fetchall()

        if not users:
            print("No users found.")
        else:
            for user in users:
                print(user)

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error reading users: {err}")


def read_one_user(username):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, username, email, city, company, job_title
            FROM users
            WHERE username = %s
        """, (username,))
        user = cursor.fetchone()

        if user:
            print(user)
        else:
            print("User not found.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error reading user: {err}")


if __name__ == "__main__":
    print("All users:")
    read_all_users()

    print("\nOne user:")
    read_one_user("alice01")