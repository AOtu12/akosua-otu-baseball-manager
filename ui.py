# ui.py
# ---------------------------------------------------------
# Section 3: UI layer (presentation)
# This file contains only input/output functions.
# ---------------------------------------------------------


def display_title():
    """Display the program title."""
    print("=" * 64)
    print(" Baseball Team Manager")
    print("=" * 64)


def display_menu(game_date, current_date_text, positions_text, days_until_text=""):
    """
    Display menu and date info.
    main.py will prepare the text (keeps UI simple).
    """
    print("=" * 64)
    print(" Baseball Team Manager")
    print(f"CURRENT DATE: {current_date_text}")

    if game_date:
        print(f"GAME DATE: {game_date}")
        if days_until_text:
            print(days_until_text)

    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print("POSITIONS")
    print(positions_text)
    print("=" * 64)