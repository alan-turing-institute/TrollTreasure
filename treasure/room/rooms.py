from treasure.room.room import Room


class Rooms:
    """
    Collection of rooms
    """

    def __init__(self, rooms):
        # rooms dictionary keyed by (x, y) coordinate (grid cell indices)
        self.rooms = {r.point: r for r in rooms}

    def __iter__(self):
        """
        Allows Rooms objects to be iterated over (see Module 7)
        """
        return iter(self.rooms.values())

    def __getitem__(self, point):
        """
        rooms[(x, y)] will retrieve the room at coordinate (x, y) (where
        rooms is an instance of the Rooms class)
        """
        return self.rooms[point]

    def __contains__(self, point):
        """
        (x, y) in rooms will return True if a room at coordinates (x, y)
        is in rooms (where rooms is an instance of the Rooms class)
        """
        return point in self.rooms

    @classmethod
    def from_list(cls, room_list):
        rooms = [Room(r["point"], [Room(l) for l in r["links"]]) for r in room_list]
        return cls(rooms)
