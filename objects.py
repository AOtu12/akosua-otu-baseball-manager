# objects.py
# ---------------------------------------------------------
# Section 3: Object-Oriented Version
# Player: stores first name, last name, position, at_bats, hits
# Lineup: manages a list of Player objects (add/remove/move)
# ---------------------------------------------------------


class Player:
    """
    Represents a single baseball player.
    Stores first and last name separately (Section 3 requirement).
    """

    def __init__(self, first_name, last_name, position, at_bats, hits):
        # Player identity
        self.first_name = first_name
        self.last_name = last_name

        # Player baseball info
        self.position = position
        self.at_bats = at_bats
        self.hits = hits

    @property
    def full_name(self):
        """
        Return the player's full name (first + last).
        """
        return f"{self.first_name} {self.last_name}".strip()

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
        Convert this Player object into a dictionary for saving to CSV.
        New format uses first_name and last_name.
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
        """
        Create a Player object from a dictionary.

        Supports BOTH formats:
        1) Old format: {"name": "Tommy La Stella", ...}
        2) New format: {"first_name": "Tommy", "last_name": "La Stella", ...}
        """
        # New format (preferred)
        if "first_name" in data and "last_name" in data:
            first = data["first_name"]
            last = data["last_name"]
        else:
            # Old format: split name into first + last
            name = data.get("name", "").strip()
            parts = name.split()

            # If name has at least 2 parts, first = first word, last = rest
            if len(parts) >= 2:
                first = parts[0]
                last = " ".join(parts[1:])
            elif len(parts) == 1:
                first = parts[0]
                last = ""
            else:
                first = ""
                last = ""

        return Player(
            first,
            last,
            data["position"],
            data["at_bats"],
            data["hits"]
        )


class Lineup:
    """
    Manages a list of Player objects.
    Includes iterator + count (Section 3 requirement).
    """

    def __init__(self):
        self.players = []

    def __len__(self):
        """
        Return number of players in the lineup.
        Allows: len(lineup)
        """
        return len(self.players)

    def __iter__(self):
        """
        Iterator support.
        Allows: for player in lineup:
        """
        return iter(self.players)

    def load_from_dicts(self, dict_list):
        """
        Convert a list of dictionaries into Player objects.
        """
        self.players = []
        for d in dict_list:
            self.players.append(Player.from_dict(d))

    def to_dicts(self):
        """
        Convert lineup of Player objects back into list of dictionaries.
        """
        return [p.to_dict() for p in self.players]

    def add_player(self, player):
        """
        Add a Player object to the lineup.
        """
        self.players.append(player)

    def remove_player(self, number):
        """
        Remove a player by lineup number (1-based).
        Returns removed player's full name.
        """
        removed = self.players.pop(number - 1)
        return removed.full_name

    def move_player(self, current_number, new_number):
        """
        Move a player from one lineup position to another (1-based).
        Returns moved player's full name.
        """
        player = self.players.pop(current_number - 1)
        self.players.insert(new_number - 1, player)
        return player.full_name