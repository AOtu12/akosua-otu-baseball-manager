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


def main():
    lineup = db.load_lineup()

    while True:
        print("\nMENU OPTIONS")
        print("1 Display lineup")
        print("2 Add player")
        print("7 Exit")

        option = input("Option: ")

        if option == "1":
            display(lineup)

        elif option == "2":
            name = input("Name: ")
            pos = get_position()
            ab = get_int("At bats: ")
            hits = get_int("Hits: ")

            lineup.append([name, pos, ab, hits])
            db.save_lineup(lineup)

        elif option == "7":
            break


if __name__ == "__main__":
    main()
