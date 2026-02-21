# db.py
# -------------------------------------
# Section 2 improvement:
# Work with a list of DICTIONARIES, not a list of lists.
# We use simple text file I/O (not csv module) so it works cleanly
# with dictionaries, as required by the spec.
# -------------------------------------

from pathlib import Path

DATA_FILE = Path("players.csv")


def load_lineup():
    """
    Load players from players.csv.
    Returns a list of dictionaries like:
    {
        "name": "Tommy La Stella",
        "position": "3B",
        "at_bats": 1316,
        "hits": 360
    }
    """

    lineup = []

    # If file doesn't exist, return empty lineup (required behavior)
    if not DATA_FILE.exists():
        return lineup

    # Read each line from the file
    with DATA_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # Skip blank lines
            if not line:
                continue

            # Split into 4 parts: name, position, at_bats, hits
            parts = line.split(",")

            # If the line doesn't have exactly 4 fields, skip it safely
            if len(parts) != 4:
                continue

            name = parts[0].strip()
            pos = parts[1].strip()

            # Convert numbers safely
            try:
                ab = int(parts[2].strip())
                hits = int(parts[3].strip())
            except ValueError:
                # Skip lines with bad numeric data
                continue

            lineup.append({
                "name": name,
                "position": pos,
                "at_bats": ab,
                "hits": hits
            })

    return lineup


def save_lineup(lineup):
    """
    Save list of dictionaries back to players.csv.
    Overwrites the file each time.
    """

    with DATA_FILE.open("w", encoding="utf-8") as f:
        for player in lineup:
            # Write each player dict as a CSV line (no header)
            line = f"{player['name']},{player['position']},{player['at_bats']},{player['hits']}\n"
            f.write(line)