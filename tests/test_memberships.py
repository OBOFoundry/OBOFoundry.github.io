"""Tests for working group membership data."""

import unittest
from pathlib import Path

import yaml
from pydantic import BaseModel

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
DATA = ROOT.joinpath("_data")


class Member(BaseModel):
    """Representation of a member in a working group."""

    name: str
    orcid: str
    affiliation: str


class Group(BaseModel):
    """Representation of a working group."""

    members: list[Member]


class TestMembershipData(unittest.TestCase):
    """Test membership data."""

    def test_technical(self):
        """Test the technical working group data is clean."""
        path = DATA.joinpath("technical.yml")
        self.assert_data(path)

    def assert_data(self, path: Path):
        """Assert the data is good."""
        res = Group.parse_obj(yaml.safe_load(path.read_text()))
        self.assertIsNotNone(res)
