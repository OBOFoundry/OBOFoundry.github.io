# -*- coding: utf-8 -*-

"""Unit tests for metadata integrity.

Run from the root of the repository using ``tox`` with:

.. code-block:: sh

    $ pip install tox
    $ tox
"""

import json
import os
import unittest
from io import StringIO
from pathlib import Path
from typing import Union

import yaml

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()

SCHEMA_PATH = ROOT.joinpath("util", "schema", "registry_schema.json")
SCHEMA = json.loads(SCHEMA_PATH.read_text())

#: These are the valid licenses listed in the registry schema file
VALID_LICENSE_LABELS = {
    value
    for entry in SCHEMA["properties"]["license"]["anyOf"]
    for value in entry["properties"]["label"]["enum"]
}
VALID_LICENSE_URLS = {
    value
    for entry in SCHEMA["properties"]["license"]["anyOf"]
    for value in entry["properties"]["url"]["enum"]
}
#: These ontologies have invalid licenses, but they're grandfathered in
LEGACY_LICENSE_PREFIXES = {
    "GSSO",
    "HP",
    "KISAO",
    "MAMO",
    "SBO",
    "SCDO",
    "TXPO",
}


def load_all():
    """Load all metadata files in a dictionary from lowercased OBO Foundry IDs to metadata."""
    rv = {}
    for path in ROOT.joinpath("ontology").glob("*.md"):
        data = load(path)
        rv[data["id"]] = data
    return rv


def load(path: Union[str, os.PathLike]):
    """Load metadata from a single markdown file."""
    with open(path) as file:
        lines = [line.rstrip("\n") for line in file]
    idx = min(i for i, line in enumerate(lines[1:], start=1) if line == "---")
    return yaml.safe_load(StringIO("\n".join(lines[1:idx])))


class TestIntegrity(unittest.TestCase):
    """A test case for checking metadata integrity."""

    @classmethod
    def setUpClass(cls):
        """Set up the test case by loading metadata for various tests."""
        cls.metadata = load_all()

    def test_license(self):
        """Test that licenses are present and valid, based on the JSON schema.

        - Ontologies marked as obsolete, orphaned, and inactive are skipped.
        - Ontologies that had invalid licenses at the time of writing the test are skipped.
          Future ontologies should conform to this based on OBO Foundry's
          `openness principle <http://www.obofoundry.org/principles/fp-001-open.html>`_.
        """
        for prefix, data in self.metadata.items():
            if data.get("is_obsolete") or data.get("activity_status") in {
                "orphaned",
                "inactive",
            }:
                continue
            if prefix.upper() in LEGACY_LICENSE_PREFIXES:
                continue
            with self.subTest(prefix=prefix):
                self.assertIn("license", set(data), msg=f"Failed on {prefix}")
                self.assertIn("label", data["license"])
                self.assertIn(data["license"]["label"], VALID_LICENSE_LABELS)
                self.assertIn("url", data["license"])
                self.assertIn(data["license"]["url"], VALID_LICENSE_URLS)
