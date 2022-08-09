from treasure.room.utils import direction


class Room:
    def __init__(self, point, links=None):
        self.point = tuple(point)  # grid point of this room
        self.links = links  # other rooms this rooms connects to
        self._validate_links()

    def __contains__(self, point):
        """
        `(x, y) in room_instance` returns `True` if `room_instance` has a link to
        a room at point `(x, y)`
        """
        return point in [l.point for l in self.links]

    def _validate_links(self):
        """
        Verifies all linked rooms are at neighbouring grid points
        """
        if not self.links:
            return
        for link in self.links:
            if not direction(self.point, link.point):
                raise ValueError(
                    f"Invalid link: {link.point} is not connected to {self.point}"
                )
