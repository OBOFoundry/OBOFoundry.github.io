"""A workflow for removing a field from all ontology markdown files' metadata."""

import json
from io import StringIO
from pathlib import Path

import click
import yaml

from obofoundry.constants import ONTOLOGY_DIRECTORY, ROOT
from obofoundry.standardize_metadata import ModifiedDumper


def remove_field(name: str) -> None:
    """Remove the metadata key from all ontologies' metadata."""
    for path in ONTOLOGY_DIRECTORY.glob("*.md"):
        remove_field_from_file(path, name)

    schema_path = ROOT.joinpath("util", "schema", "registry_schema.json")
    schema = json.loads(schema_path.read_text())
    if name in schema['properties']:
        del schema['properties'][name]
    schema_path.write_text(json.dumps(schema, indent=2) + "\n")


def remove_field_from_file(path: Path, name: str) -> None:
    """Update the given markdown file."""
    with open(path) as file:
        lines = [line.rstrip("\n") for line in file]

    assert lines[0] == "---"
    idx = min(i for i, line in enumerate(lines[1:], start=1) if line == "---")

    # Load the data like it is YAML
    data = yaml.safe_load(StringIO("\n".join(lines[1:idx])))

    if name in data:
        del data[name]

    dumped = ModifiedDumper.dump(data)

    with open(path, "w") as file:
        print("---", file=file)
        print(dumped, file=file)
        print("---", file=file)
        for line in lines[idx + 1 :]:
            print(line, file=file)


@click.command()
@click.argument("names", nargs=-1)
def main(names: list[str]) -> None:
    """Remove the metadata key from all ontologies' metadata."""
    for name in names:
        remove_field(name)


if __name__ == "__main__":
    main()
