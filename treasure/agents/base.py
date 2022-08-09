class Agent:
    """
    Base functionality to create and load (but not move) an Agent
    """

    def __init__(self, point, name, symbol, verbose=True, allow_wait=True, **kwargs):
        self.point = tuple(point)  # (x, y) grid location of the agent
        self.name = name  # e.g. adventurer or troll
        self.symbol = symbol  # single char symbol to show the agent on dungeon maps
        self.verbose = verbose  # print output on agent behaviour if True
        self.allow_wait = allow_wait  # allow the agent to move nowhere

    def move(self, rooms):
        raise NotImplementedError("Use an Agent base class")

    @classmethod
    def from_dict(cls, agent_dict):
        return cls(
            agent_dict["point"],
            agent_dict["name"],
            agent_dict["symbol"],
            allow_wait=agent_dict["allow_wait"],
        )
