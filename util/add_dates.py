"""Add date added annotations to all ontologies."""

import datetime
import itertools as itt
import os
import pathlib

import pystow
from dateutil.parser import parse

HERE = pathlib.Path(__file__).parent.resolve()
ONTOLOGY_DIRECTORY = HERE.parent.joinpath("ontology").resolve()

DATA_PATH = pystow.join("obo", name="commits.txt")


def main():
    """Add date added annotations to all ontologies."""
    if not DATA_PATH.is_file():
        command = f'git log --format="format:%ci" --name-only --diff-filter=A > {str(DATA_PATH)}'
        print("running command:", command)
        os.system(command)

    with DATA_PATH.open() as file:
        lines = [line.strip() for line in file]

    ontology_to_time = {}
    for flag, sublines in itt.groupby(lines, key=lambda line: not line.strip()):
        if flag:
            continue
        time = parse(next(sublines))
        ontologies = [
            subline.removeprefix("ontology/").removesuffix(".md")
            for subline in sublines
            if subline.startswith("ontology/") and subline.endswith(".md")
        ]
        if not ontologies:
            continue
        for ontology in ontologies:
            ontology_to_time[ontology] = time

    for ontology, time in ontology_to_time.items():
        path = ONTOLOGY_DIRECTORY.joinpath(ontology).with_suffix(".md")
        if not path.is_file():
            print(f"File no longer exists: {path} added on {time}")
            continue
        update_markdown(path, time)


def update_markdown(path: pathlib.Path, date: datetime.datetime) -> None:
    """Update the given markdown file."""
    with path.open() as file:
        lines = [line.rstrip("\n") for line in file]

    if any(line.startswith("github_date_added:") for line in lines):
        # No need to add duplicates
        return

    assert lines[0] == "---"
    idx = min(i for i, line in enumerate(lines[1:], start=1) if line == "---")

    with path.open("w") as file:
        print("---", file=file)
        for line in lines[1:idx]:
            print(line, file=file)
        print("github_date_added:", date.strftime("%Y-%m-%d"), file=file)
        print("---", file=file)
        for line in lines[idx + 1 :]:
            print(line, file=file)


if __name__ == "__main__":
    main()
