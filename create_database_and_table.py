from db_connection import get_connection, load_db_config
import mysql.connector


def create_database_and_table():
    config = load_db_config()

    try:
        conn = get_connection(use_database=False)
        cursor = conn.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config['database']}")
        print(f"Database '{config['database']}' is ready.")

        cursor.execute(f"USE {config['database']}")

        create_table_sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) NOT NULL UNIQUE,
            email VARCHAR(150) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            city VARCHAR(100),
            company VARCHAR(150),
            job_title VARCHAR(150)
        )
        """

        cursor.execute(create_table_sql)
        print("Table 'users' is ready.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    create_database_and_table()