# -*- coding: utf-8 -*-

"""This script sorts the ordering of the metadata in each ontology markdown file.

Run with: ``python standardize_metadata.py``.

Author: `Charles Tapley Hoyt <https://cthoyt.com>`_.
"""

import pathlib
from io import StringIO
from typing import Union

import click
import yaml

HERE = pathlib.Path(__file__).parent.resolve()
ONTOLOGY_DIRECTORY = HERE.parent.joinpath("ontology").resolve()


def update_markdown(path: pathlib.Path) -> None:
    """Update the given markdown file."""
    with path.open() as file:
        lines = [line.rstrip("\n") for line in file]

    assert lines[0] == "---"
    idx = min(i for i, line in enumerate(lines[1:], start=1) if line == "---")

    # Load the data like it is YAML
    data = yaml.safe_load(StringIO("\n".join(lines[1:idx])))
    dumped = yaml.safe_dump(
        data,
        sort_keys=True,
        explicit_end=False,
        width=float("inf"),
    ).rstrip()

    with path.open("w") as file:
        print("---", file=file)
        print(dumped, file=file)
        print("---", file=file)
        for line in lines[idx + 1 :]:
            print(line, file=file)


@click.command()
def main():
    for path in ONTOLOGY_DIRECTORY.glob("*.md"):
        update_markdown(path)


if __name__ == "__main__":
    main()
