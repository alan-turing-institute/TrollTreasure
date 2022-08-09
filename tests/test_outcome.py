from pathlib import Path

import pytest
import yaml

from treasure.dungeon import Dungeon
from treasure.game import Game


@pytest.mark.parametrize(
    "yml_path, abs_prec, rel_prec",
    [
        ("dungeons/test_lose100.yml", 0, 0),
        ("dungeons/test_stalemate.yml", 0, 0),
        ("dungeons/test_win100.yml", 0, 0),
        ("dungeons/test_win50.yml", 0.05, 0.05),
    ],
)
def test_outcome(yml_path, abs_prec, rel_prec):
    full_path = Path(__file__).parent / yml_path
    d = Dungeon.from_file(full_path)
    g = Game(d)
    actual_outcome = g.probability()

    with open(full_path) as f:
        expected_outcome = yaml.safe_load(f)["outcome"]
    if abs_prec == rel_prec == 0:
        assert actual_outcome == expected_outcome
    else:
        assert actual_outcome == pytest.approx(
            expected_outcome, abs=abs_prec, rel=rel_prec
        )
