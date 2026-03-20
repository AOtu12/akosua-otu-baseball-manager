# db_sqlite.py
# -----------------------------------------
# SQLite database access for MY Baseball Team Manager
# -----------------------------------------

import sqlite3

DB_FILE = "baseball.sqlite"


def connect():
    """Create and return a database connection."""
    return sqlite3.connect(DB_FILE)


def get_all_players():
    """Return all players ordered by batOrder."""
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT playerID, batOrder, firstName, lastName, position, atBats, hits
        FROM Player
        ORDER BY batOrder
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


if __name__ == "__main__":
    players = get_all_players()

    for player in players:
        print(player)