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

def get_positions():
    """Return all valid position values from the Position table."""
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT positionValue
        FROM Position
        ORDER BY positionID
    """)

    rows = cursor.fetchall()
    conn.close()

    # Convert list of tuples into a simple list of strings
    return [row[0] for row in rows]

def update_player(player_id, first_name, last_name, position, at_bats, hits):
    """Update a player's name, position, and batting stats."""
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Player
        SET firstName = ?,
            lastName = ?,
            position = ?,
            atBats = ?,
            hits = ?
        WHERE playerID = ?
    """, (first_name, last_name, position, at_bats, hits, player_id))

    conn.commit()
    conn.close()

def add_player(bat_order, first_name, last_name, position, at_bats, hits):
    """Add a new player to the database."""
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Player (batOrder, firstName, lastName, position, atBats, hits)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (bat_order, first_name, last_name, position, at_bats, hits))

    conn.commit()
    conn.close()    

def delete_player(player_id):
    """Delete a player by playerID."""
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM Player
        WHERE playerID = ?
    """, (player_id,))

    conn.commit()
    conn.close()

def update_bat_order(player_id, new_bat_order):
    """Update a player's batting order."""
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Player
        SET batOrder = ?
        WHERE playerID = ?
    """, (new_bat_order, player_id))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    positions = get_positions()
    print(positions)