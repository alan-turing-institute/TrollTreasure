# TrollTreasure

Sample solution for the packaging exercise in the RSE course

## Installation

To install in a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
pip install .
```

## Run Example

Run a single game:

```bash
treasure examples/dungeon.yml
```

Compute outcome probabilities:

```bash
treasure dungeons/example.yml -n 1000
```

Check `treasure --help` for other options.

## Development

Install development dependencies and run tests:

```bash
pip install '.[dev]'
pytest
```
