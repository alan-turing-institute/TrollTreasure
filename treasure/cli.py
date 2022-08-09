from argparse import ArgumentParser, RawTextHelpFormatter

from treasure.dungeon import Dungeon
from treasure.game import Game, preamble


def main():
    parser = ArgumentParser(
        description=f"\n{preamble}\n", formatter_class=RawTextHelpFormatter
    )

    parser.add_argument("path", help="Path to dungeon specification YAML file")
    parser.add_argument(
        "-n",
        type=int,
        help=(
            "Number of times to play the dungeon "
            "(if greater than 1 estimate outcome probabilities)"
        ),
        default=1,
    )
    parser.add_argument(
        "--max_steps",
        type=int,
        help="Number of game turns before declaring a draw",
        default=1000,
    )

    args = parser.parse_args()

    d = Dungeon.from_file(args.path)
    g = Game(d)
    if args.n > 1:
        print(f"Computing outcomes for {args.path}")
        prob = g.probability(trials=args.n, max_steps=args.max_steps)
        print(f"Win: {prob[1]}")
        print(f"Lose: {prob[-1]}")
        print(f"Draw: {prob[0]}")
    else:
        g.run(max_steps=args.max_steps)
