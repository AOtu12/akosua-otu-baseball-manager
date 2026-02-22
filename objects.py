# objects.py
# ---------------------------------------------------------
# Section 3: Object-Oriented Version
# - Player: first_name, last_name, position, at_bats, hits
# - Lineup: manages Player objects (add/remove/move/retrieve/edit)
# - Includes iterator and count (len) for looping
# ---------------------------------------------------------


class Player:
    """
    Represents a single baseball player.
    Stores first and last name separately (required).
    """

    def __init__(self, first_name, last_name, position, at_bats, hits):
        # Identity
        self.first_name = first_name
        self.last_name = last_name

        # Baseball data
        self.position = position
        self.at_bats = at_bats
        self.hits = hits

    @property
    def full_name(self):
        """Return full name as 'First Last'."""
        return f"{self.first_name} {self.last_name}".strip()

    def batting_average(self):
        """Return batting average rounded to 3 decimals."""
        if self.at_bats == 0:
            return 0.0
        return round(self.hits / self.at_bats, 3)

    def to_dict(self):
        """
        Convert to dict for db layer.
        We use keys that match the NEW CSV format.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "position": self.position,
            "at_bats": self.at_bats,
            "hits": self.hits
        }

    @staticmethod
    def from_dict(data):
        """Create a Player object from a dictionary."""
        return Player(
            data["first_name"],
            data["last_name"],
            data["position"],
            data["at_bats"],
            data["hits"]
        )


class Lineup:
    """Manages a list of Player objects."""

    def __init__(self):
        self.players = []

    def __len__(self):
        """Allow: len(lineup)"""
        return len(self.players)

    def __iter__(self):
        """Allow: for player in lineup:"""
        return iter(self.players)

    def load_from_dicts(self, dict_list):
        """Convert list of dicts -> Player objects."""
        self.players = []
        for d in dict_list:
            self.players.append(Player.from_dict(d))

    def to_dicts(self):
        """Convert Player objects -> list of dicts."""
        return [p.to_dict() for p in self.players]

    def add_player(self, player):
        """Add Player to end."""
        self.players.append(player)

    def get_player(self, number):
        """Retrieve Player by lineup number (1-based)."""
        return self.players[number - 1]

    def remove_player(self, number):
        """Remove Player by lineup number (1-based)."""
        removed = self.players.pop(number - 1)
        return removed.full_name

    def move_player(self, current_number, new_number):
        """Move Player from one position to another (1-based)."""
        player = self.players.pop(current_number - 1)
        self.players.insert(new_number - 1, player)
        return player.full_name