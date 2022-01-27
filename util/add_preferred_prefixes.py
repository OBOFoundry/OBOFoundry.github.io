# -*- coding: utf-8 -*-

"""This script adds preferred prefixes to any file that doesn't have one.

Run with: ``python add_preferred_prefixes.py``.

Author: `Charles Tapley Hoyt <https://cthoyt.com>`_.
"""

import pathlib
from io import StringIO
from typing import Union

import click
import yaml

HERE = pathlib.Path(__file__).parent.resolve()
ONTOLOGY_DIRECTORY = HERE.parent.joinpath("ontology").resolve()


def update_markdown(path: Union[str, pathlib.Path]) -> None:
    """Update the given markdown file."""
    with open(path) as file:
        lines = [line.rstrip("\n") for line in file]

    assert lines[0] == "---"
    idx = min(i for i, line in enumerate(lines[1:], start=1) if line == "---")

    # Load the data like it is YAML
    data = yaml.safe_load(StringIO("\n".join(lines[1:idx])))

    # For first pass, let's only update ontologies that don't have
    # an explicit entry, and also aren't marked as inactive/obsolete/orphaned
    if "preferredPrefix" in data:
        return
    if "is_obsolete" in data and data["is_obsolete"]:
        return
    if "activity_status" in data and data["activity_status"] in {
        "inactive",
        "orphaned",
    }:
        return

    with open(path, "w") as file:
        print("---", file=file)
        for line in lines[1:idx]:
            print(line, file=file)
        print("preferredPrefix:", data["id"].upper(), file=file)
        print("---", file=file)
        for line in lines[idx + 1 :]:
            print(line, file=file)


@click.command()
def main():
    for path in ONTOLOGY_DIRECTORY.glob("*.md"):
        update_markdown(path)


if __name__ == "__main__":
    main()
