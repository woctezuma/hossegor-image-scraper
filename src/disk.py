import json
from pathlib import Path


def save(data: set, fname: str) -> None:
    with Path(fname).open("w", encoding="utf8 ") as f:
        json.dump(sorted(data), f, indent=2)


def load(fname: str) -> set[str]:
    try:
        with Path(fname).open(encoding="utf8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    return set(data)
