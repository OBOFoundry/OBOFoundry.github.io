# -*- coding: utf-8 -*-

"""This script automatically populates the repository field based on the tracker/homepage fields.

Run with: ``python populate_repositories.py``.

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
    repository = get_repository(data)

    with open(path, "w") as file:
        print("---", file=file)
        for line in lines[1:idx]:
            print(line, file=file)
        if repository:
            print("repository:", repository, file=file)
        print("---", file=file)
        for line in lines[idx + 1 :]:
            print(line, file=file)


def get_repository(data):
    if "repository" in data:
        return
    tracker = data.get("tracker")
    if tracker and tracker.startswith("https://github.com"):
        if tracker.endswith("/issues"):
            tracker = tracker[: -len("/issues")]
        elif tracker.endswith("/issues/"):
            tracker = tracker[: -len("/issues/")]
        return tracker
    homepage = data.get("homepage")
    if homepage and homepage.startswith("https://github.com"):
        if homepage.endswith("/issues"):
            homepage = homepage[: -len("/issues")]
        elif homepage.endswith("/issues/"):
            homepage = homepage[: -len("/issues/")]
        return homepage


@click.command()
def main():
    for path in ONTOLOGY_DIRECTORY.glob("*.md"):
        update_markdown(path)


if __name__ == "__main__":
    main()
