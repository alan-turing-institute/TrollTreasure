import random

from treasure.agents.base import Agent
from treasure.room.utils import direction


class RandomAgent(Agent):
    """
    Agent that makes random moves
    """

    def move(self, rooms):
        if not rooms[self.point].links:
            # this room isn't linked to anything, can't move
            if self.verbose:
                print(f"{self.name} is trapped")
            return

        # pick a random room to move to
        options = rooms[self.point].links
        if self.allow_wait:
            options.append(self)
        new_room = random.choice(options)

        if self.verbose:
            move = direction(self.point, new_room.point)
            print(f"{self.name} moves {move}")
        self.point = new_room.point
