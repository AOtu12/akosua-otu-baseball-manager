# db_sqlite.py
# -----------------------------------------
# SQLite database access for my Baseball Team Manager
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


def get_player(player_id):
    """Return one player by playerID, or None if not found."""
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT playerID, batOrder, firstName, lastName, position, atBats, hits
        FROM Player
        WHERE playerID = ?
    """, (player_id,))

    row = cursor.fetchone()
    conn.close()
    return row

def update_player(player_id, position, at_bats, hits):
    """Update a player's position and batting stats."""
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Player
        SET position = ?,
            atBats = ?,
            hits = ?
        WHERE playerID = ?
    """, (position, at_bats, hits, player_id))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    update_player(1, "1B", 1400, 400)
    print(get_player(1))