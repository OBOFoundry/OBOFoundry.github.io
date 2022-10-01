"""Tests for working group membership data."""

import unittest
from pathlib import Path
from typing import List

import yaml
from pydantic import BaseModel
from collections import Counter

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
DATA = ROOT.joinpath("_data")


class Member(BaseModel):
    """Representation of a member in a working group."""

    name: str
    orcid: str
    affiliation: str
    country: str
    groups: List[str]


class Group(BaseModel):
    """Representation of a working group."""

    members: List[Member]


class TestMembershipData(unittest.TestCase):
    """Test membership data."""

    def test_data(self):
        """Test the working group data is clean."""
        path = DATA.joinpath("operations").with_suffix(".yml")
        res = Group.parse_obj(yaml.safe_load(path.read_text()))
        self.assertIsNotNone(res)
        counter = Counter(
            member.orcid
            for member in res.members
            if member.orcid
        )
        counter = {
            orcid
            for orcid, count in counter.items()
            if count > 1
        }
        self.assertEqual(0, len(counter), msg=f"Duplicate: {counter}")
