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
    print("\nPlayer POS AB H AVG")
    print("-" * 40)

    for i, player in enumerate(lineup, 1):
        name, pos, ab, hits = player
        avg = calc_avg(ab, hits)

        print(f"{i} {name:20}{pos:4}{ab:5}{hits:5}{avg:.3f}")


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
            # Add player (we will enhance validation in a later commit)
            name = input("Name: ").strip()
            pos = get_position()
            ab = get_int("At bats: ")
            hits = get_int("Hits: ")

            lineup.append([name, pos, ab, hits])
            db.save_lineup(lineup)
            print(f"{name} was added.")

        elif option == "3":
            remove_player(lineup)


        elif option == "4":
            print("Move player - coming next commit")

        elif option == "5":
            print("Edit position - coming next commit")

        elif option == "6":
            print("Edit stats - coming next commit")

        elif option == "7":
            print("Bye!")
            break

        else:
            print("Invalid menu option. Please try again.")


if __name__ == "__main__":
    main()
