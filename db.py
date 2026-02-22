# db.py
# ---------------------------------------------------------
# Data layer (file access only) - required architecture
# Supports:
# - Old CSV format: name,position,at_bats,hits  (4 fields)
# - New CSV format: first_name,last_name,position,at_bats,hits (5 fields)
# Always SAVES in the NEW format (5 fields).
# ---------------------------------------------------------

from pathlib import Path

DATA_FILE = Path("players.csv")


def split_name(full_name):
    """
    Split a full name into first and last.
    - First = first word
    - Last  = remaining words (can be empty)
    """
    full_name = full_name.strip()
    parts = full_name.split()

    if len(parts) >= 2:
        return parts[0], " ".join(parts[1:])
    elif len(parts) == 1:
        return parts[0], ""
    else:
        return "", ""


def load_lineup():
    """
    Load players from CSV.
    Returns list of dicts in NEW structure:
    {
      "first_name": "...",
      "last_name": "...",
      "position": "...",
      "at_bats": int,
      "hits": int
    }
    """
    lineup = []

    if not DATA_FILE.exists():
        return lineup

    with DATA_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = [p.strip() for p in line.split(",")]

            # OLD format (4 fields): name,position,ab,hits
            if len(parts) == 4:
                first, last = split_name(parts[0])
                pos = parts[1]
                try:
                    ab = int(parts[2])
                    hits = int(parts[3])
                except ValueError:
                    continue

            # NEW format (5 fields): first,last,position,ab,hits
            elif len(parts) == 5:
                first = parts[0]
                last = parts[1]
                pos = parts[2]
                try:
                    ab = int(parts[3])
                    hits = int(parts[4])
                except ValueError:
                    continue

            else:
                # Skip malformed lines safely
                continue

            lineup.append({
                "first_name": first,
                "last_name": last,
                "position": pos,
                "at_bats": ab,
                "hits": hits
            })

    return lineup


def save_lineup(lineup):
    """
    Save list of dicts to CSV in NEW (5-field) format.
    """
    with DATA_FILE.open("w", encoding="utf-8") as f:
        for p in lineup:
            line = (
                f"{p['first_name']},"
                f"{p['last_name']},"
                f"{p['position']},"
                f"{p['at_bats']},"
                f"{p['hits']}\n"
            )
            f.write(line)