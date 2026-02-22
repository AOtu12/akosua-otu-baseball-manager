# main.py
# ---------------------------------------------------------
# Baseball Team Manager (Murach Case Study)
# Section 3: Object-Oriented Version (Option 2)
#
# This module should NOT handle formatting or input validation UI.
# Instead:
# - ui.py handles user interaction (input/output)
# - db.py handles file access (load/save CSV)
# - objects.py handles business objects (Player, Lineup)
#
# main.py acts as the "controller":
# - loads data
# - calls UI functions to get input and show output
# - calls Lineup/Player methods to perform actions
# - saves changes using db.py
# ---------------------------------------------------------

import db
import ui
from datetime import date
from objects import Player, Lineup


def get_game_date():
    """
    Ask user for game date in YYYY-MM-DD format.
    User can press Enter to skip.
    Returns:
      - date object if entered
      - None if skipped
    NOTE: This can stay in main.py or be moved to ui.py later.
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
    Menu option 2: Add a player.
    Uses ui.py for input helpers and saves to CSV.
    """
    # Get first/last name (required in Section 3)
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()

    # Get a valid position using UI helper
    pos = ui.get_position()

    # Keep asking until valid stats are entered
    while True:
        ab = ui.get_int("At bats: ")
        hits = ui.get_int("Hits: ")

        if ab < 0 or hits < 0:
            print("At bats and hits cannot be negative. Try again.")
            continue

        if hits > ab:
            print("Hits cannot be greater than at bats. Try again.")
            continue

        break

    # Add Player object to the Lineup
    lineup.add_player(Player(first_name, last_name, pos, ab, hits))

    # Save lineup (objects -> dicts -> CSV)
    db.save_lineup(lineup.to_dicts())

    print(f"{first_name} {last_name} was added.")


def remove_player(lineup):
    """
    Menu option 3: Remove a player.
    """
    num = ui.get_int("Number: ")

    if num < 1 or num > len(lineup):
        print("Invalid lineup number.")
        return

    removed_name = lineup.remove_player(num)

    db.save_lineup(lineup.to_dicts())

    print(f"{removed_name} was deleted.")


def move_player(lineup):
    """
    Menu option 4: Move a player to a new lineup position.
    """
    cur = ui.get_int("Current lineup number: ")

    if cur < 1 or cur > len(lineup):
        print("Invalid lineup number.")
        return

    player = lineup.get_player(cur)
    print(f"{player.full_name} was selected.")

    new = ui.get_int("New lineup number: ")

    if new < 1 or new > len(lineup):
        print("Invalid lineup number.")
        return

    lineup.move_player(cur, new)

    db.save_lineup(lineup.to_dicts())

    print(f"{player.full_name} was moved.")


def edit_player_position(lineup):
    """
    Menu option 5: Edit a player's position.
    """
    num = ui.get_int("Lineup number: ")

    if num < 1 or num > len(lineup):
        print("Invalid lineup number.")
        return

    player = lineup.get_player(num)
    print(f"You selected {player.full_name} POS={player.position}")

    # Get new position from UI helper
    player.position = ui.get_position()

    db.save_lineup(lineup.to_dicts())

    print(f"{player.full_name} was updated.")


def edit_player_stats(lineup):
    """
    Menu option 6: Edit a player's stats (AB/H) with validation.
    """
    num = ui.get_int("Lineup number: ")

    if num < 1 or num > len(lineup):
        print("Invalid lineup number.")
        return

    player = lineup.get_player(num)
    print(f"You selected {player.full_name} AB={player.at_bats} H={player.hits}")

    new_ab = ui.get_int("At bats: ")
    new_hits = ui.get_int("Hits: ")

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


def main():
    """
    Program entry point:
    - Load CSV -> list of dicts (db.py)
    - Convert dicts -> Player objects in Lineup (objects.py)
    - Menu loop (ui.py displays)
    """
    # Load dicts from CSV
    data = db.load_lineup()

    # Convert to Player objects inside a Lineup object
    lineup = Lineup()
    lineup.load_from_dicts(data)

    # Title from UI layer
    ui.display_title()

    # Ask for game date once
    game_date = get_game_date()

    # Menu loop
    while True:
        # Show menu from UI layer
        ui.display_menu(game_date)

        option = input("Menu option: ").strip()

        if option == "1":
            # Display expects dictionaries
            ui.display(lineup.to_dicts())

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