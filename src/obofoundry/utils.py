"""Test data integrity, beyond what's possible with the JSON schema."""

from pathlib import Path

import yaml

from obofoundry.constants import ONTOLOGY_DIRECTORY

__all__ = [
    "get_data",
]


def get_data():
    """Get ontology data."""
    ontologies = {}
    for path in ONTOLOGY_DIRECTORY.glob("*.md"):
        with open(path) as file:
            lines = [line.rstrip("\n") for line in file]

        assert lines[0] == "---"
        idx = min(i for i, line in enumerate(lines[1:], start=1) if line == "---")

        # Load the data like it is YAML
        data = yaml.safe_load("\n".join(lines[1:idx]))
        data["long_description"] = "".join(lines[idx:])
        ontologies[data["id"]] = data
    return ontologies
