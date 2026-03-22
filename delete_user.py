import mysql.connector
from db_connection import get_connection


def delete_user(username):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = "DELETE FROM users WHERE username = %s"
        cursor.execute(sql, (username,))
        conn.commit()

        if cursor.rowcount == 0:
            print("User not found.")
        else:
            print("User deleted successfully.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error deleting user: {err}")


if __name__ == "__main__":
    delete_user("alice01")