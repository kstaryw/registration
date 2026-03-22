import hashlib
import mysql.connector
from faker import Faker
from db_connection import get_connection

fake = Faker()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def populate_users(n=1000):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO users (username, email, password, city, company, job_title)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        records = []
        for _ in range(n):
            username = fake.unique.user_name()
            email = fake.unique.email()
            password = hash_password(fake.password())
            city = fake.city()
            company = fake.company()
            job_title = fake.job()

            records.append((username, email, password, city, company, job_title))

        cursor.executemany(sql, records)
        conn.commit()

        print(f"{n} fake users inserted successfully.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error populating users: {err}")


if __name__ == "__main__":
    populate_users(1000)