# db.py
# -------------------------------------
# Section 1 procedural database layer.
# Handles reading and writing player data
# using CSV file players.csv.
# No classes used yet.
# -------------------------------------

import csv
from pathlib import Path

DATA_FILE = Path("players.csv")


def load_lineup():
    """
    Load players from CSV file.
    Returns list of lists:
    [name, position, at_bats, hits]
    """

    lineup = []

    if not DATA_FILE.exists():
        return lineup

    with DATA_FILE.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)

        for row in reader:
            if not row:
                continue

            name, pos, ab, hits = row
            lineup.append([name, pos, int(ab), int(hits)])

    return lineup


def save_lineup(lineup):
    """
    Save lineup to CSV file.
    Overwrites file every time.
    """

    with DATA_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        for player in lineup:
            writer.writerow(player)
