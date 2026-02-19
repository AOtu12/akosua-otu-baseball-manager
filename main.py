# main.py (SECTION 1 PROCEDURAL)
# -------------------------------------
# Uses:
# - list of lists for lineup
# - functions only (no classes)
# - CSV persistence via db.py
# -------------------------------------

import db

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Try again.")


def get_position():
    while True:
        pos = input("Position: ").upper()

        if pos in POSITIONS:
            return pos

        print("Invalid position.")


def calc_avg(ab, hits):
    if ab == 0:
        return 0.0
    return round(hits / ab, 3)


def display(lineup):
    """
    Section 2 improvement:
    Display lineup with cleaner formatting and 64-character lines.
    """

    print("\n" + "=" * 64)
    print(f"{'No':<4}{'Player':<20}{'POS':<6}{'AB':<6}{'H':<6}{'AVG':<6}")
    print("=" * 64)

    for i, player in enumerate(lineup, 1):
        name, pos, ab, hits = player
        avg = calc_avg(ab, hits)

        # Show avg with 3 decimals (required format)
        print(f"{i:<4}{name:<20}{pos:<6}{ab:<6}{hits:<6}{avg:<6.3f}")

    print("=" * 64)


def display_title():
    print("=" * 64)
    print(" Baseball Team Manager")
    print("=" * 64)


def display_menu():
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
    # Ask user for lineup number to delete
    num = get_int("Number: ")

    # Validate range
    if num < 1 or num > len(lineup):
        print("Invalid lineup number.")
        return

    # Get the player name before removing
    name = lineup[num - 1][0]

    # Remove from list
    lineup.pop(num - 1)

    # Save updated lineup to CSV
    db.save_lineup(lineup)

    print(f"{name} was deleted.")
   

def move_player(lineup):
    # Ask for current lineup number
    cur = get_int("Current lineup number: ")

    if cur < 1 or cur > len(lineup):
        print("Invalid lineup number.")
        return

    # Get player name before moving
    name = lineup[cur - 1][0]
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
    name, pos, ab, hits = lineup[num - 1]
    print(f"You selected {name} POS={pos}")

    # Ask for new position (must be valid)
    new_pos = get_position()

    # Update position in the list
    lineup[num - 1][1] = new_pos

    # Save to CSV
    db.save_lineup(lineup)

    print(f"{name} was updated.")

def edit_player_stats(lineup):
    # Ask which player to edit (user uses lineup number from display)
    num = get_int("Lineup number: ")

    # Validate the lineup number is within range
    if num < 1 or num > len(lineup):
        print("Invalid lineup number.")
        return

    # Get current player details
    name, pos, ab, hits = lineup[num - 1]
    print(f"You selected {name} AB={ab} H={hits}")

    # Ask for new stats
    new_ab = get_int("At bats: ")
    new_hits = get_int("Hits: ")

    # Validation rules (required)
    if new_ab < 0 or new_hits < 0:
        print("At bats and hits cannot be negative.")
        return

    if new_hits > new_ab:
        print("Hits cannot be greater than at bats.")
        return

    # Update the lineup list
    lineup[num - 1][2] = new_ab
    lineup[num - 1][3] = new_hits

    # Save updated data to CSV
    db.save_lineup(lineup)

    print(f"{name} was updated.")
   


def main():
    # Load saved lineup from CSV (or empty list if file missing)
    lineup = db.load_lineup()

    display_title()

    while True:
        display_menu()
        option = input("Menu option: ").strip()

        if option == "1":
            display(lineup)

       
        elif option == "2":
          name = input("Name: ").strip()
          pos = get_position()
          ab = get_int("At bats: ")
          hits = get_int("Hits: ")

          # Validation rules (same as edit stats)
          if ab < 0 or hits < 0:
             print("At bats and hits cannot be negative.")
          continue

          if hits > ab:
            print("Hits cannot be greater than at bats.")
          continue

          lineup.append([name, pos, ab, hits])
          db.save_lineup(lineup)

          print(f"{name} was added.")

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
