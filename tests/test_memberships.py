"""Tests for working group membership data."""

import unittest
from collections import Counter
from pathlib import Path
from typing import List, Literal

import yaml
from pydantic import BaseModel

from obofoundry.constants import ALUMNI_METADATA_PATH, OPERATIONS_METADATA_PATH

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
DATA = ROOT.joinpath("_data")


class Member(BaseModel):
    """Representation of a member in a working group."""

    name: str
    orcid: str
    wikidata: str
    github: str
    affiliation: str
    country: str
    groups: List[Literal["editorial", "outreach", "technical"]]


class Group(BaseModel):
    """Representation of a working group."""

    members: List[Member]


class TestMembershipData(unittest.TestCase):
    """Test membership data."""

    def test_data(self):
        """Test the working group data is clean."""
        res = Group.parse_obj(yaml.safe_load(OPERATIONS_METADATA_PATH.read_text()))
        self.assertIsNotNone(res)
        counter = Counter(member.orcid for member in res.members if member.orcid)
        counter = {orcid for orcid, count in counter.items() if count > 1}
        self.assertEqual(0, len(counter), msg=f"Duplicate: {counter}")

    def test_alumni(self):
        """Test the alumni data."""
        data = yaml.safe_load(ALUMNI_METADATA_PATH.read_text())["members"]
        for i, member in enumerate(data):
            with self.subTest(row=i):
                self.assertIn("name", member)
                self.assertIn("orcid", member)
