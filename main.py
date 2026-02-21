# main.py (SECTION 1 PROCEDURAL)
# -------------------------------------
# Uses:
# - list of lists for lineup
# - functions only (no classes)
# - CSV persistence via db.py
# -------------------------------------

import db
from datetime import date
from objects import Player, Lineup


POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Try again.")


def get_position():
    while True:
        pos = input("Position: ").strip().upper()

        if pos in POSITIONS:
            return pos

        print("Invalid position.")


def calc_avg(player):
    """
    Calculate batting average for a player dict.
    """
    ab = player["at_bats"]
    hits = player["hits"]

    if ab == 0:
        return 0.0

    return round(hits / ab, 3)


def display(lineup):
    """
    Section 2 improvement:
    Display lineup with cleaner formatting and 64-character lines.
    Uses dictionaries for players.
    """
    print("\n" + "=" * 64)
    print(f"{'No':<4}{'Player':<20}{'POS':<6}{'AB':<6}{'H':<6}{'AVG':<6}")
    print("=" * 64)

    for i, player in enumerate(lineup, 1):
        avg = calc_avg(player)

        print(
            f"{i:<4}"
            f"{player['name']:<20}"
            f"{player['position']:<6}"
            f"{player['at_bats']:<6}"
            f"{player['hits']:<6}"
            f"{avg:<6.3f}"
        )

    print("=" * 64)


def display_title():
    print("=" * 64)
    print(" Baseball Team Manager")
    print("=" * 64)


def display_menu(game_date):
    """
    Section 2 requirement:
    Show CURRENT DATE always.
    Show GAME DATE if provided.
    Show DAYS UNTIL GAME only if game is in the future.
    """
    today = date.today()

    print("=" * 64)
    print(" Baseball Team Manager")
    print(f"CURRENT DATE: {today:%Y-%m-%d}")

    # If user entered a game date, show it
    if game_date is not None:
        print(f"GAME DATE: {game_date:%Y-%m-%d}")

        diff = (game_date - today).days

        # Only show days until game if game is in the future
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
    Section 3 improvement:
    Remove a player using the Lineup object method.
    """
    num = get_int("Number: ")

    # Validate range using number of Player objects
    if num < 1 or num > len(lineup.players):
        print("Invalid lineup number.")
        return

    # Remove the player and get their name
    name = lineup.remove_player(num)

    # Save updated lineup back to CSV (convert objects -> dicts)
    db.save_lineup(lineup.to_dicts())

    print(f"{name} was deleted.")
    
def move_player(lineup):
    # Ask for current lineup number
    cur = get_int("Current lineup number: ")

    if cur < 1 or cur > len(lineup):
        print("Invalid lineup number.")
        return

    # Get player name before moving
    name = lineup[cur - 1]["name"]
    print(f"{name} was selected.")

    # Ask for new lineup position
    new = get_int("New lineup number: ")

    if new < 1 or new > len(lineup):
        print("Invalid lineup number.")
        return

    # Remove player from old position
    player = lineup.pop(cur - 1)

    # Insert player at new position
    lineup.insert(new - 1, player)

    # Save updated lineup
    db.save_lineup(lineup)

    print(f"{name} was moved.")

def edit_player_position(lineup):
    # Ask which player to edit
    num = get_int("Lineup number: ")

    if num < 1 or num > len(lineup):
        print("Invalid lineup number.")
        return

    # Current player details
    player = lineup[num - 1]
    print(f"You selected {player['name']} POS={player['position']}")

    # Ask for new position (must be valid)
    new_pos = get_position()
    
    # Update position in the list
    player["position"] = new_pos



    # Save to CSV
    db.save_lineup(lineup)
    print(f"{player['name']} was updated.")

def edit_player_stats(lineup):
   # Get the selected player dictionary from the lineup list
   # We subtract 1 because lineup numbers start at 1 for users,
   # but Python list indexes start at 0.
   player = lineup[num - 1]

   # Display current player stats before editing
   print(f"You selected {player['name']} AB={player['at_bats']} H={player['hits']}")

   # Ask user for new statistics
   new_ab = get_int("At bats: ")
   new_hits = get_int("Hits: ")

   # Validation: at-bats and hits must not be negative
   if new_ab < 0 or new_hits < 0:
      print("At bats and hits cannot be negative.")
      return

   # Validation: hits cannot exceed at-bats
   if new_hits > new_ab:
      print("Hits cannot be greater than at bats.")
      return

   # Update the player dictionary with new values
   player["at_bats"] = new_ab
   player["hits"] = new_hits

   # Save updated lineup back to CSV file
   db.save_lineup(lineup)

   # Confirm update to user
   print(f"{player['name']} was updated.")

def get_game_date():
    """
    Ask user for a game date in YYYY-MM-DD format.
    User can press Enter to skip (no game date).
    """
    while True:
        text = input("GAME DATE (YYYY-MM-DD) or Enter to skip: ").strip()

        # If user skips, return None
        if text == "":
            return None

        try:
            year, month, day = map(int, text.split("-"))
            return date(year, month, day)
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD (example: 2026-03-10).")

def days_until_game(game_date):
    """
    Returns the number of days from today until the game date.
    Can be negative if the date is in the past.
    """
    today = date.today()
    return (game_date - today).days



def add_player(lineup):
    """
    Section 2 improvement:
    Add player with a friendlier input flow.
    Keeps asking until the user enters valid at-bats and hits.
    """

    # Get player name
    name = input("Name: ").strip()

    # Get valid position
    pos = get_position()

    # Keep asking until stats are valid
    while True:
        ab = get_int("At bats: ")
        hits = get_int("Hits: ")

        # Validation: no negatives
        if ab < 0 or hits < 0:
            print("At bats and hits cannot be negative. Try again.")
            continue

        # Validation: hits cannot exceed at-bats
        if hits > ab:
            print("Hits cannot be greater than at bats. Try again.")
            continue

        # If input is valid, break out of loop
        break

    # Create a Player object and add it to Lineup object
    lineup.add_player(Player(name, pos, ab, hits))

    # Save lineup by converting Player objects back to dictionaries
    db.save_lineup(lineup.to_dicts())
    

    print(f"{name} was added.")


   


def main():
    # Load list of dictionaries from CSV using db.py
    data = db.load_lineup()

    # Convert dictionary data into Player objects inside a Lineup object
    lineup = Lineup()
    lineup.load_from_dicts(data)

    display_title()

    # Section 2 improvement: ask for game date once at start
    game_date = get_game_date()


    while True:
        display_menu(game_date)
        option = input("Menu option: ").strip()

        if option == "1":
     # Convert Player objects back into dicts for the existing display() function
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
