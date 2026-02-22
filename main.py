# main.py
# ---------------------------------------------------------
# Baseball Team Manager (Murach Case Study)
# Section 3: Object-Oriented Version
#
# Program responsibilities:
# - Get user input (menu options)
# - Call methods on Lineup / Player objects (business logic)
# - Save and load data using db.py (file/data access)
#
# Data format (dictionary / CSV):
# first_name,last_name,position,at_bats,hits
# ---------------------------------------------------------

import db
from datetime import date
from objects import Player, Lineup

# Valid positions tuple (required by spec)
POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


def get_int(prompt):
    """
    Get an integer from the user.
    Re-prompts until the user enters a valid integer.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Try again.")


def get_position():
    """
    Get a valid baseball position from the user.
    Re-prompts until the user enters one from POSITIONS.
    """
    while True:
        pos = input("Position: ").strip().upper()
        if pos in POSITIONS:
            return pos
        print("Invalid position.")


def calc_avg(player_dict):
    """
    Calculate batting average from a player dictionary:
      avg = hits / at_bats
    Always return a float rounded to 3 decimals.
    """
    ab = player_dict["at_bats"]
    hits = player_dict["hits"]

    # Avoid divide by zero
    if ab == 0:
        return 0.0

    return round(hits / ab, 3)


def display(lineup_dicts):
    """
    Display the lineup in a formatted table.
    Expects a list of dictionaries with keys:
      first_name, last_name, position, at_bats, hits
    """
    print("\n" + "=" * 64)
    print(f"{'No':<4}{'Player':<20}{'POS':<6}{'AB':<6}{'H':<6}{'AVG':<6}")
    print("=" * 64)

    for i, p in enumerate(lineup_dicts, 1):
        # Build full name for display
        name = f"{p['first_name']} {p['last_name']}".strip()
        avg = calc_avg(p)

        # Print one row (spaces used for alignment, no tabs)
        print(
            f"{i:<4}"
            f"{name:<20}"
            f"{p['position']:<6}"
            f"{p['at_bats']:<6}"
            f"{p['hits']:<6}"
            f"{avg:<6.3f}"
        )

    print("=" * 64)


def display_title():
    """Display program title banner."""
    print("=" * 64)
    print(" Baseball Team Manager")
    print("=" * 64)


def display_menu(game_date):
    """
    Display menu + required date information.

    Requirements:
    - Always show current date
    - Ask user for game date once (done in get_game_date)
    - If game date is provided:
        - show game date
        - show days until game ONLY if the date is in the future
    """
    today = date.today()

    print("=" * 64)
    print(" Baseball Team Manager")
    print(f"CURRENT DATE: {today:%Y-%m-%d}")

    # Show game date info only if the user entered a game date
    if game_date is not None:
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


def remove_player(lineup):
    """
    Remove a player using Lineup object methods.
    Saves changes back to CSV after removal.
    """
    num = get_int("Number: ")

    # Validate range
    if num < 1 or num > len(lineup):
        print("Invalid lineup number.")
        return

    # Remove and get player name (Lineup returns full name)
    name = lineup.remove_player(num)

    # Save updated lineup (objects -> dicts -> CSV)
    db.save_lineup(lineup.to_dicts())

    print(f"{name} was deleted.")


def move_player(lineup):
    """
    Move a player from one lineup position to another.
    Saves changes back to CSV after move.
    """
    cur = get_int("Current lineup number: ")

    if cur < 1 or cur > len(lineup):
        print("Invalid lineup number.")
        return

    # Get selected player object so we can print a friendly message
    player = lineup.get_player(cur)
    print(f"{player.full_name} was selected.")

    new = get_int("New lineup number: ")

    if new < 1 or new > len(lineup):
        print("Invalid lineup number.")
        return

    # Move player using Lineup method
    lineup.move_player(cur, new)

    # Save to CSV
    db.save_lineup(lineup.to_dicts())

    print(f"{player.full_name} was moved.")


def edit_player_position(lineup):
    """
    Change a player's position.
    Saves changes back to CSV after editing.
    """
    num = get_int("Lineup number: ")

    if num < 1 or num > len(lineup):
        print("Invalid lineup number.")
        return

    player = lineup.get_player(num)

    # Show the selected player and current position
    print(f"You selected {player.full_name} POS={player.position}")

    # Ask for new position and update the Player object
    player.position = get_position()

    # Save to CSV
    db.save_lineup(lineup.to_dicts())

    print(f"{player.full_name} was updated.")


def edit_player_stats(lineup):
    """
    Change a player's at-bats and hits with validation:
    - no negatives
    - hits cannot exceed at-bats
    Saves changes back to CSV after editing.
    """
    num = get_int("Lineup number: ")

    if num < 1 or num > len(lineup):
        print("Invalid lineup number.")
        return

    player = lineup.get_player(num)

    # Show current stats
    print(f"You selected {player.full_name} AB={player.at_bats} H={player.hits}")

    # Get new stats
    new_ab = get_int("At bats: ")
    new_hits = get_int("Hits: ")

    # Validate input
    if new_ab < 0 or new_hits < 0:
        print("At bats and hits cannot be negative.")
        return

    if new_hits > new_ab:
        print("Hits cannot be greater than at bats.")
        return

    # Apply update to Player object
    player.at_bats = new_ab
    player.hits = new_hits

    # Save to CSV
    db.save_lineup(lineup.to_dicts())

    print(f"{player.full_name} was updated.")


def get_game_date():
    """
    Ask user for game date in YYYY-MM-DD format.
    User can press Enter to skip.
    Returns:
      - date object if entered
      - None if skipped
    """
    while True:
        text = input("GAME DATE (YYYY-MM-DD) or Enter to skip: ").strip()

        if text == "":
            return None

        try:
            year, month, day = map(int, text.split("-"))
            return date(year, month, day)
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD (example: 2026-03-10).")


def add_player(lineup):
    """
    Add a new player (first + last name required).
    Validates at-bats and hits.
    Saves to CSV after adding.
    """
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()

    pos = get_position()

    # Keep asking until user enters valid stats
    while True:
        ab = get_int("At bats: ")
        hits = get_int("Hits: ")

        if ab < 0 or hits < 0:
            print("At bats and hits cannot be negative. Try again.")
            continue

        if hits > ab:
            print("Hits cannot be greater than at bats. Try again.")
            continue

        break

    # Create Player object and add to Lineup
    lineup.add_player(Player(first_name, last_name, pos, ab, hits))

    # Save updated lineup
    db.save_lineup(lineup.to_dicts())

    print(f"{first_name} {last_name} was added.")


def main():
    """
    Main program flow:
    - Load CSV into dictionaries (db.py)
    - Convert dictionaries into Player objects (objects.py)
    - Loop menu until exit
    """
    # Load dicts from CSV
    data = db.load_lineup()

    # Create Lineup object and load Player objects into it
    lineup = Lineup()
    lineup.load_from_dicts(data)

    display_title()

    # Ask for game date once at start
    game_date = get_game_date()

    # Menu loop
    while True:
        display_menu(game_date)
        option = input("Menu option: ").strip()

        if option == "1":
            display(lineup.to_dicts())
        elif option == "2":
            add_player(lineup)
        elif option == "3":
            remove_player(lineup)
        elif option == "4":
            move_player(lineup)
        elif option == "5":
            edit_player_position(lineup)
        elif option == "6":
            edit_player_stats(lineup)
        elif option == "7":
            print("Bye!")
            break
        else:
            print("Invalid menu option. Please try again.")


if __name__ == "__main__":
    main()