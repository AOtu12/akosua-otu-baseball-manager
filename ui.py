# ui.py
# ---------------------------------------------------------
# User Interface module
# Handles:
# - All input/output (print, input)
# - Display formatting
# - Menu rendering
# Keeps main.py clean.
# ---------------------------------------------------------

from datetime import date

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


def get_int(prompt):
    """Get integer safely from user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Try again.")


def get_position():
    """Get a valid baseball position."""
    while True:
        pos = input("Position: ").strip().upper()
        if pos in POSITIONS:
            return pos
        print("Invalid position.")


def display_title():
    print("=" * 64)
    print(" Baseball Team Manager")
    print("=" * 64)


def display_menu(game_date):
    """Show current date, optional game date, and menu."""
    today = date.today()

    print("=" * 64)
    print(" Baseball Team Manager")
    print(f"CURRENT DATE: {today:%Y-%m-%d}")

    if game_date:
        print(f"GAME DATE: {game_date:%Y-%m-%d}")
        diff = (game_date - today).days
        if diff > 0:
            print(f"DAYS UNTIL GAME: {diff}")

    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")

    print("POSITIONS")
    print(", ".join(POSITIONS))
    print("=" * 64)


def display(lineup_dicts):
    """Display lineup in table format."""
    print("\n" + "=" * 64)
    print(f"{'No':<4}{'Player':<20}{'POS':<6}{'AB':<6}{'H':<6}{'AVG':<6}")
    print("=" * 64)

    for i, p in enumerate(lineup_dicts, 1):
        name = f"{p['first_name']} {p['last_name']}".strip()

        ab = p["at_bats"]
        hits = p["hits"]
        avg = 0.0 if ab == 0 else round(hits / ab, 3)

        print(
            f"{i:<4}"
            f"{name:<20}"
            f"{p['position']:<6}"
            f"{ab:<6}"
            f"{hits:<6}"
            f"{avg:<6.3f}"
        )

    print("=" * 64)