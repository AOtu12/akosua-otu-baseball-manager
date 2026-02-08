# objects.py
# This file contains the business logic layer.
# It defines the Player class and Lineup class.

# Tuple storing all valid baseball positions (constant)
POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


class Player:
    """
    Player class represents one baseball player.
    Stores player personal info and batting statistics.
    """

    def __init__(self, first_name, last_name, position, at_bats, hits):
        # Remove extra spaces from names
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()

        # Store position in uppercase
        self.position = position.upper()

        # Convert numeric inputs to integers
        self.at_bats = int(at_bats)
        self.hits = int(hits)

    @property
    def full_name(self):
        """Returns player's full name."""
        return f"{self.first_name} {self.last_name}"

    @property
    def average(self):
        """
        Calculate batting average.
        If at_bats is zero, avoid division by zero.
        """
        if self.at_bats == 0:
            return 0.0

        # Round to 3 decimal places as required
        return round(self.hits / self.at_bats, 3)


class Lineup:
    """
    Lineup class stores the list of players.
    Provides methods to manage players.
    """

    def __init__(self):
        # Initialize empty player list
        self.players = []

    def __iter__(self):
        """
        Allows iteration through players:
        for p in lineup:
        """
        return iter(self.players)

    @property
    def count(self):
        """Return number of players."""
        return len(self.players)

    def add(self, player):
        """Add new player to lineup."""
        self.players.append(player)

    def remove(self, number):
        """
        Remove player by lineup number.
        number is 1-based for user friendliness.
        """
        return self.players.pop(number - 1)

    def get(self, number):
        """Retrieve player by lineup number."""
        return self.players[number - 1]

    def move(self, current, new):
        """
        Move player from one position to another.
        """
        player = self.players.pop(current - 1)
        self.players.insert(new - 1, player)

    def edit_position(self, number, new_pos):
        """Update player's position."""
        self.players[number - 1].position = new_pos

    def edit_stats(self, number, ab, hits):
        """Update player's batting stats."""
        player = self.players[number - 1]
        player.at_bats = ab
        player.hits = hits
