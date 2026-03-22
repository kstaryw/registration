import yaml
import mysql.connector


def load_db_config(path="db.yaml"):
    with open(path, "r") as file:
        return yaml.safe_load(file)


def get_connection(use_database=True):
    config = load_db_config()

    connection_args = {
        "host": config["host"],
        "user": config["user"],
        "password": config["password"],
        "port": config["port"]
    }

    if use_database:
        connection_args["database"] = config["database"]

    return mysql.connector.connect(**connection_args)


if __name__ == "__main__":
    try:
        conn = get_connection(use_database=False)
        print("Connected to MySQL successfully.")
        conn.close()
    except mysql.connector.Error as err:
        print(f"Connection failed: {err}")
    except FileNotFoundError:
        print("db.yaml not found.")