import copy

from art import text2art, tprint

preamble = f"""{text2art('Troll Treasure', font='small')}
An adventurer is looking for treasure in a mysterious dungeon.
Will they succeed or be dinner for the troll that lurks there?
"""


class Game:
    def __init__(self, dungeon):
        self.dungeon = dungeon

    def preamble(self):
        print(
            preamble
            + f"""
\nThe map of the dungeon is below:
o : an empty room
o - o : connected rooms
{self.dungeon.troll.symbol} : {self.dungeon.troll.name}
{self.dungeon.adventurer.symbol} : {self.dungeon.adventurer.name}
{self.dungeon.treasure.symbol} : the treasure
            """
        )

    def run(self, max_steps=1000, verbose=True, start_prompt=False):
        dungeon = copy.deepcopy(self.dungeon)
        dungeon.set_verbose(verbose)
        if verbose:
            self.preamble()
            dungeon.draw()
            if start_prompt:
                input("\nPress enter to continue...")
            else:
                print("\nLet the hunt begin!")

        for turn in range(max_steps):
            result = dungeon.outcome()
            if result != 0:
                if verbose:
                    if result == 1:
                        print(
                            f"\n{self.dungeon.adventurer.name} gets the treasure and returns a hero!"
                        )
                        tprint("WINNER", font="small")
                    elif result == -1:
                        print(f"\n{self.dungeon.troll.name} will eat tonight!")
                        tprint("GAME OVER", font="small")
                return result
            if verbose:
                print(f"\nTurn {turn + 1}")
            dungeon.update()
        # no outcome in max steps (e.g. no treasure and troll can't reach adventurer)
        if verbose:
            print(
                f"\nNo one saw {self.dungeon.adventurer.name} or {self.dungeon.troll.name} again."
            )
            tprint("STALEMATE", font="small")

        return result

    def probability(self, trials=10000, max_steps=1000, verbose=False):
        outcomes = {-1: 0, 0: 0, 1: 0}
        for _ in range(trials):
            result = self.run(max_steps=max_steps, verbose=False)
            outcomes[result] += 1
        for result in outcomes:
            outcomes[result] = outcomes[result] / trials
        return outcomes
