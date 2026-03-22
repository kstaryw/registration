from create_database_and_table import create_database_and_table
from create_user import create_user
from read_users import read_one_user, read_all_users
from update_user import update_user
from delete_user import delete_user
from populate_users import populate_users
from cli_menu import show_menu


def main():
    create_database_and_table()

    while True:
        choice = show_menu()

        if choice == "1":
            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")
            city = input("City: ")
            company = input("Company: ")
            job_title = input("Job title: ")
            create_user(username, email, password, city, company, job_title)

        elif choice == "2":
            username = input("Enter username: ")
            read_one_user(username)

        elif choice == "3":
            read_all_users()

        elif choice == "4":
            username = input("Enter username: ")
            field = input("Field to update (email/password): ")
            new_value = input("New value: ")
            update_user(username, field, new_value)

        elif choice == "5":
            username = input("Enter username to delete: ")
            delete_user(username)

        elif choice == "6":
            populate_users(1000)

        elif choice == "7":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()