# main.py
# ---------------------------------------------------------
# Baseball Team Manager
# Section 3 (Object-Oriented Version)
#
# Uses:
# - Player and Lineup classes from objects.py
# - CSV persistence through db.py
# - Dictionary format for saving/loading:
#   first_name,last_name,position,at_bats,hits
# ---------------------------------------------------------

import db
from datetime import date
from objects import Player, Lineup

# Valid positions (required)
POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


def get_int(prompt):
    """Get an integer from the user with validation."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Try again.")


def get_position():
    """Get a valid baseball position from the user."""
    while True:
        pos = input("Position: ").strip().upper()
        if pos in POSITIONS:
            return pos
        print("Invalid position.")


def calc_avg(player_dict):
    """Calculate batting average for a player dictionary."""
    ab = player_dict["at_bats"]
    hits = player_dict["hits"]

    if ab == 0:
        return 0.0

    return round(hits / ab, 3)


def display(lineup_dicts):
    """
    Display lineup with 64-character separator lines.
    Expects list of dictionaries with:
    first_name, last_name, position, at_bats, hits
    """
    print("\n" + "=" * 64)
    print(f"{'No':<4}{'Player':<20}{'POS':<6}{'AB':<6}{'H':<6}{'AVG':<6}")
    print("=" * 64)

    for i, p in enumerate(lineup_dicts, 1):
        # Build full name for display
        name = f"{p['first_name']} {p['last_name']}".strip()
        avg = calc_avg(p)

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
    """Display the title banner."""
    print("=" * 64)
    print(" Baseball Team Manager")
    print("=" * 64)


def display_menu(game_date):
    """
    Section 2 requirement:
    - Show CURRENT DATE always
    - Show GAME DATE if provided
    - Show DAYS UNTIL GAME only if future
    """
    today = date.today()

    print("=" * 64)
    print(" Baseball Team Manager")
    print(f"CURRENT DATE: {today:%Y-%m-%d}")

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
    """Remove a player using Lineup methods and save to CSV."""
    num = get_int("Number: ")

    if num < 1 or num > len(lineup):
        print("Invalid lineup number.")
        return

    name = lineup.remove_player(num)

    # Save objects -> dicts
    db.save_lineup(lineup.to_dicts())

    print(f"{name} was deleted.")


def move_player(lineup):
    """Move a player using Lineup methods and save to CSV."""
    cur = get_int("Current lineup number: ")

    if cur < 1 or cur > len(lineup):
        print("Invalid lineup number.")
        return

    # Get selected player (Player object)
    player = lineup.get_player(cur)
    print(f"{player.full_name} was selected.")

    new = get_int("New lineup number: ")

    if new < 1 or new > len(lineup):
        print("Invalid lineup number.")
        return

    lineup.move_player(cur, new)

    db.save_lineup(lineup.to_dicts())

    print(f"{player.full_name} was moved.")


def edit_player_position(lineup):
    """Edit a player's position using Player objects and save to CSV."""
    num = get_int("Lineup number: ")

    if num < 1 or num > len(lineup):
        print("Invalid lineup number.")
        return

    player = lineup.get_player(num)

    print(f"You selected {player.full_name} POS={player.position}")

    new_pos = get_position()
    player.position = new_pos

    db.save_lineup(lineup.to_dicts())

    print(f"{player.full_name} was updated.")


def edit_player_stats(lineup):
    """Edit a player's stats (AB/H) using Player objects and save to CSV."""
    num = get_int("Lineup number: ")

    if num < 1 or num > len(lineup):
        print("Invalid lineup number.")
        return

    player = lineup.get_player(num)

    print(f"You selected {player.full_name} AB={player.at_bats} H={player.hits}")

    new_ab = get_int("At bats: ")
    new_hits = get_int("Hits: ")

    if new_ab < 0 or new_hits < 0:
        print("At bats and hits cannot be negative.")
        return

    if new_hits > new_ab:
        print("Hits cannot be greater than at bats.")
        return

    player.at_bats = new_ab
    player.hits = new_hits

    db.save_lineup(lineup.to_dicts())

    print(f"{player.full_name} was updated.")


def get_game_date():
    """Ask user for game date YYYY-MM-DD, or Enter to skip."""
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
    Add a player (first + last name required).
    Validate stats, then save to CSV.
    """
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()

    pos = get_position()

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

    # Create Player object using first/last (required)
    lineup.add_player(Player(first_name, last_name, pos, ab, hits))

    # Save objects -> dicts (new format)
    db.save_lineup(lineup.to_dicts())

    print(f"{first_name} {last_name} was added.")


def main():
    """Program entry point."""
    # Load dicts from CSV using db.py
    data = db.load_lineup()

    # Convert dicts -> Player objects inside Lineup
    lineup = Lineup()
    lineup.load_from_dicts(data)

    display_title()

    game_date = get_game_date()

    while True:
        display_menu(game_date)
        option = input("Menu option: ").strip()

        if option == "1":
            # Display expects dicts, so convert objects -> dicts
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