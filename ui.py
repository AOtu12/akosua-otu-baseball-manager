# ui.py
# ------------------------------
# Presentation layer ONLY.
# Handles:
# - Menu display
# - User input
# - Input validation
# No business logic here.
# ------------------------------

from objects import POSITIONS


def display_menu():
    """
    Displays menu options to the user.
    Uses POSITIONS tuple from objects.py.
    """

    print("\n" + "=" * 60)
    print("Baseball Team Manager")
    print("=" * 60)

    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")

    # Show valid positions
    print("\nPositions:", ", ".join(POSITIONS))
    print("=" * 60)


def get_int(prompt):
    """
    Safely get integer input.
    Prevents crash if user types text instead of number.
    """

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Please try again.")


def get_position():
    """
    Ensures user enters a valid baseball position.
    """

    while True:
        pos = input("Position: ").upper()

        if pos in POSITIONS:
            return pos

        print("Invalid position. Choose from:", ", ".join(POSITIONS))
