import yaml

from treasure.agents.human import HumanAgent
from treasure.agents.random import RandomAgent
from treasure.room.rooms import Rooms
from treasure.treasure import Treasure


class Dungeon:
    """
    Dungeon with:
    - Connected set of rooms on a square grid
    - The location of some treasure
    - An adventurer agent with an initial position
    - A troll agent with an initial position
    """

    def __init__(self, rooms, treasure, adventurer, troll, verbose=True):
        self.rooms = rooms
        self.treasure = treasure
        self.adventurer = adventurer
        self.troll = troll
        self.verbose = True

        # the extent of the square grid
        self.xlim = (
            min(r.point[0] for r in self.rooms),
            max(r.point[0] for r in self.rooms),
        )
        self.ylim = (
            min(r.point[1] for r in self.rooms),
            max(r.point[1] for r in self.rooms),
        )

        self._validate()

    def _validate(self):
        if self.treasure.point not in self.rooms:
            raise ValueError(f"Treasure{self.treasure.point} is not in the dungeon")
        if self.adventurer.point not in self.rooms:
            raise ValueError(
                f"{self.adventure.name}{self.treasure.point} is not in the dungeon"
            )
        if self.troll.point not in self.rooms:
            raise ValueError(
                f"{self.troll.name}{self.treasure.point} is not in the dungeon"
            )

    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            spec = yaml.safe_load(f)

        rooms = Rooms.from_list(spec["rooms"])
        treasure = Treasure.from_dict(spec["treasure"])

        agent_keys = ["adventurer", "troll"]
        agents = {}
        for agent in agent_keys:
            if spec[agent]["type"] == "random":
                agent_class = RandomAgent
            elif spec[agent]["type"] == "human":
                agent_class = HumanAgent
            else:
                raise ValueError(f"Unknown agent type {spec[agent]['type']}")
            agents[agent] = agent_class(**spec[agent])

        return cls(rooms, treasure, agents["adventurer"], agents["troll"])

    def update(self):
        """
        Move the adventurer and the troll
        """
        self.adventurer.move(self.rooms)
        self.troll.move(self.rooms)
        if self.verbose:
            print()
            self.draw()

    def outcome(self):
        """
        Check whether the adventurer found the treasure or the troll
        found the adventurer
        """
        if self.adventurer.point == self.troll.point:
            return -1
        if self.adventurer.point == self.treasure.point:
            return 1
        return 0

    def set_verbose(self, verbose):
        """Set whether to print output"""
        self.verbose = verbose
        self.adventurer.verbose = verbose
        self.troll.verbose = verbose

    def draw(self):
        """Draw a map of the dungeon"""
        layout = ""

        for y in range(self.ylim[0], self.ylim[1] + 1):
            for x in range(self.xlim[0], self.xlim[1] + 1):
                # room and character symbols
                if (x, y) in self.rooms:
                    if self.troll.point == (x, y):
                        layout += self.troll.symbol
                    elif self.adventurer.point == (x, y):
                        layout += self.adventurer.symbol
                    elif self.treasure.point == (x, y):
                        layout += self.treasure.symbol
                    else:
                        layout += "o"
                else:
                    layout += " "

                # horizontal connections
                if ((x, y) in self.rooms) and (((x + 1), y) in self.rooms[(x, y)]):
                    layout += " - "
                else:
                    layout += "   "

            # vertical connections
            if y < self.ylim[1]:
                layout += "\n"
                for x in range(self.xlim[0], self.xlim[1] + 1):
                    if ((x, y) in self.rooms) and ((x, y + 1) in self.rooms[(x, y)]):
                        layout += "|"
                    else:
                        layout += " "
                    if x < self.xlim[1]:
                        layout += "   "
                layout += "\n"

        print(layout)
