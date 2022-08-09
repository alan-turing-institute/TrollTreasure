from treasure.agents.base import Agent


class HumanAgent(Agent):
    """
    Agent that prompts the user where to move next
    """

    def move(self, rooms):
        if not rooms:
            if self.verbose:
                print(f"{self.name} is trapped")
            return
        options = ["wait"] if self.allow_wait else []
        if (self.point[0] - 1, self.point[1]) in rooms:
            options.append("left")
        if (self.point[0] + 1, self.point[1]) in rooms:
            options.append("right")
        if (self.point[0], self.point[1] - 1) in rooms:
            options.append("up")
        if (self.point[0], self.point[1] + 1) in rooms:
            options.append("down")
        choice = None
        while choice not in options:
            choice = input(f"Where will {self.name} move \n{options}? ")
        if choice == "left":
            self.point = self.point[0] - 1, self.point[1]
        elif choice == "right":
            self.point = self.point[0] + 1, self.point[1]
        elif choice == "up":
            self.point = self.point[0], self.point[1] - 1
        elif choice == "down":
            self.point = self.point[0], self.point[1] + 1
