"""This script bulk renames a given domain.

Run with: ``python bulk_domain_rename.py <old> <new>``.

Author: `Charles Tapley Hoyt <https://cthoyt.com>`_.
"""

import pathlib

import click

HERE = pathlib.Path(__file__).parent.resolve()
ONTOLOGY_DIRECTORY = HERE.parent.joinpath("ontology").resolve()


@click.command()
@click.argument("old_label")
@click.argument("new_label")
def main(old_label: str, new_label: str):
    """Rename domains across all ontologies."""
    old_line = f"domain: {old_label}"
    new_line = f"domain: {new_label}"

    for path in ONTOLOGY_DIRECTORY.glob("*.md"):
        with path.open() as file:
            lines = [line.rstrip("\n") for line in file]

        with path.open("w") as file:
            for line in lines:
                if line == old_line:
                    print(new_line, file=file)
                else:
                    print(line, file=file)


if __name__ == "__main__":
    main()
