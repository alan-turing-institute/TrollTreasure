class Treasure:
    def __init__(self, point, symbol):
        self.point = tuple(point)  # (x, y) grid location of the treasure
        self.symbol = symbol  # single char symbol to show the treasure on dungeon maps

    @classmethod
    def from_dict(cls, treasure_dict):
        return cls(treasure_dict["point"], treasure_dict["symbol"])
