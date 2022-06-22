"""This script bulk renames a given key in all ontologies' metadata.

Run with: ``python bulk_field_rename.py <old> <new>``.

Author: `Charles Tapley Hoyt <https://cthoyt.com>`_.
"""

import pathlib

import click

HERE = pathlib.Path(__file__).parent.resolve()
ONTOLOGY_DIRECTORY = HERE.parent.joinpath("ontology").resolve()


@click.command()
@click.argument("old_key")
@click.argument("new_key")
def main(old_key: str, new_key: str):
    """Rename keys across all ontologies."""
    for path in ONTOLOGY_DIRECTORY.glob("*.md"):
        with path.open() as file:
            lines = [line.rstrip("\n") for line in file]

        with path.open("w") as file:
            for line in lines:
                prefix = f"{old_key}:"
                if line.startswith(prefix):
                    line = line.removeprefix(prefix).lstrip()
                    line = f"{new_key}: {line}"
                    print(line, file=file)
                else:
                    print(line, file=file)


if __name__ == "__main__":
    main()
