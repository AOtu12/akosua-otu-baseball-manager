# objects.py
# ---------------------------------------------------------
# Section 3: Object-Oriented Version
# This module defines:
# 1) Player class - represents one baseball player
# 2) Lineup class - manages a list of Player objects
# ---------------------------------------------------------


class Player:
    """
    Represents a single baseball player.
    """

    def __init__(self, name, position, at_bats, hits):
        # Store player data (basic properties)
        self.name = name
        self.position = position
        self.at_bats = at_bats
        self.hits = hits

    def batting_average(self):
        """
        Calculate batting average.
        Return 0.0 if at_bats is 0 to avoid divide-by-zero.
        """
        if self.at_bats == 0:
            return 0.0
        return round(self.hits / self.at_bats, 3)

    def to_dict(self):
        """
        Convert this Player object into a dictionary.
        This helps us reuse your Section 2 db.py which saves dictionaries.
        """
        return {
            "name": self.name,
            "position": self.position,
            "at_bats": self.at_bats,
            "hits": self.hits
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Player object from a dictionary.
        """
        return Player(
            data["name"],
            data["position"],
            data["at_bats"],
            data["hits"]
        )


class Lineup:
    """
    Manages a list of Player objects.
    Provides methods for all lineup actions.
    """

    def __init__(self):
        # Start with an empty list of Player objects
        self.players = []

    def load_from_dicts(self, dict_list):
        """
        Convert a list of dictionaries into Player objects.
        """
        self.players = []
        for d in dict_list:
            self.players.append(Player.from_dict(d))

    def to_dicts(self):
        """
        Convert lineup of Player objects back into a list of dictionaries.
        """
        return [p.to_dict() for p in self.players]

    def add_player(self, player):
        """
        Add a Player object to the end of the lineup.
        """
        self.players.append(player)

    def remove_player(self, number):
        """
        Remove a player by lineup number (1-based).
        Returns removed player's name.
        """
        removed = self.players.pop(number - 1)
        return removed.name

    def move_player(self, current_number, new_number):
        """
        Move a player from one lineup position to another (1-based).
        Returns moved player's name.
        """
        player = self.players.pop(current_number - 1)
        self.players.insert(new_number - 1, player)
        return player.name