"""Test data integrity, beyond what's possible with the JSON schema."""

import json
import unittest
from io import StringIO
from pathlib import Path
from typing import List, Literal, Optional, Set

import yaml
from pydantic import BaseModel, Field

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
DATA = ROOT.joinpath("_data")
ROLES = DATA.joinpath("roles.yml")


class Person(BaseModel):
    """A model for a person."""

    name: str
    orcid: str
    status: Literal["lead", "support"]
    start: Optional[str]


class Role(BaseModel):
    """A model for a role in the OBO Foundry community."""

    name: str
    description: str
    open: Optional[bool]
    commitment: Optional[str]
    requirements: List[str] = Field(default_factory=list)
    people: List[Person]


class TestRoles(unittest.TestCase):
    """Test data integrity of roles."""

    def test_data(self):
        """Test the working group data is clean."""
        roles = yaml.safe_load(ROLES.read_text())
        for role_dict in roles:
            name = role_dict.get("name")
            with self.subTest(name=name):
                self.assertIsNotNone(name)
                Role.parse_obj(role_dict)
