# db.py
# Handles reading and writing player data to CSV file.
# This keeps file handling separate from business logic.

import csv
from objects import Player, Lineup

FILE_NAME = "players.csv"


def load_lineup():
    """
    Load players from CSV file into Lineup object.
    If file does not exist, return empty lineup.
    """
    lineup = Lineup()

    try:
        with open(FILE_NAME, newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if row:
                    # Create Player object from CSV row
                    lineup.add(Player(*row))

    except FileNotFoundError:
        # File not found = start with empty lineup
        pass

    return lineup


def save_lineup(lineup):
    """
    Save all players from Lineup object into CSV file.
    """
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)

        for p in lineup:
            writer.writerow([
                p.first_name,
                p.last_name,
                p.position,
                p.at_bats,
                p.hits
            ])
