"""Tests for working group membership data."""

import unittest
from collections import Counter
from pathlib import Path
from textwrap import dedent
from typing import List, Literal, Optional

import yaml
from pydantic import BaseModel

from obofoundry.constants import ALUMNI_METADATA_PATH, OPERATIONS_METADATA_PATH

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
DATA = ROOT.joinpath("_data")
OFOC_IMAGS = ROOT.joinpath("images", "ofoc")


class Affiliation(BaseModel):
    """Represents an affiliation."""

    name: str
    ror: Optional[str]
    wikidata: Optional[str]


class Member(BaseModel):
    """Representation of a member in a working group."""

    name: str
    orcid: str
    wikidata: str
    github: str
    affiliation: Affiliation
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
        counter = Counter(member.orcid for member in res.members)
        counter = {orcid for orcid, count in counter.items() if count > 1}
        self.assertEqual(0, len(counter), msg=f"Duplicate: {counter}")
        for person in res.members:
            with self.subTest(name=person.name):
                self.assertFalse(
                    person.affiliation.ror is None and person.affiliation.wikidata is None,
                    msg=dedent(
                        f"""\
                        No ROR nor Wikidata identifier was curated for {person.name}.
                        Please search https://ror.org for their affiliation. If none exists, please
                        submit a new ROR ID request (linked from bottom of homepage). If the request
                        is rejected, create a Wikidata entry and annotate in the `affiliation_wikidata` field.
                    """.rstrip()
                    ),
                )
                stub = OFOC_IMAGS.joinpath(person.github)
                self.assertTrue(
                    any(
                        stub.with_suffix(suffix).is_file()
                        for suffix in [".png", ".jpg"]
                    ),
                    msg=f"{person.name} is missing a photo in {OFOC_IMAGS} that matches their github handle",
                )

    def test_encoding(self):
        """Test correct encoding."""
        t = OPERATIONS_METADATA_PATH.read_text()
        self.assertEqual(yaml.safe_dump(yaml.safe_load(t), allow_unicode=True), t)

    def test_alumni(self):
        """Test the alumni data."""
        data = yaml.safe_load(ALUMNI_METADATA_PATH.read_text())["members"]
        for i, member in enumerate(data):
            with self.subTest(row=i):
                self.assertIn("name", member)
                self.assertIn("orcid", member)
