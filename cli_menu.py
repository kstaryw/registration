from rich.console import Console
from rich.panel import Panel

console = Console()


def show_menu():
    console.print(
        Panel.fit(
            "[1] Create a new user\n"
            "[2] Read/display one user\n"
            "[3] Read/display all users\n"
            "[4] Update an existing user\n"
            "[5] Delete a user\n"
            "[6] Populate 1000 fake users\n"
            "[7] Exit",
            title="User Registration System"
        )
    )
    return input("Enter your choice: ")