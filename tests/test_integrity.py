"""Test data integrity, beyond what's possible with the JSON schema."""

import unittest
from pathlib import Path

import citation_url
import yaml

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent
ONTOLOGY_DIRECTORY = ROOT.joinpath("ontology").resolve()


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
        ontologies[data["id"]] = data
    return ontologies


class TestIntegrity(unittest.TestCase):
    """Test case for data integrity."""

    def setUp(self) -> None:
        """Set up the test case."""
        self.ontologies = get_data()

    def test_dependencies(self):
        """Test dependencies are valid OBO Foundry ontologies."""
        for ontology, data in self.ontologies.items():
            dependencies = data.get("dependencies")
            if not dependencies:
                continue
            with self.subTest(ontology=ontology):
                for i, dependency in enumerate(dependencies):
                    # Check that the ID is a valid OBO ontology prefix
                    dependency_id = dependency["id"]
                    dependency_type = dependency.get("type")
                    if dependency_type == "BridgeOntology":
                        self.assertTrue(dependency_id.startswith(f"{ontology}/"))
                        # TODO what else should be checked about bridge ontologies? or are these invalid?
                    else:
                        self.assertIn(
                            dependency_id,
                            set(self.ontologies),
                            msg=f"Ontology {ontology} has invalid dependency at index {i}: {dependency_id}",
                        )

    def test_publications(self):
        """Test publications information."""
        for ontology, data in sorted(self.ontologies.items()):
            for i, publication in enumerate(data.get("publications", [])):
                identifier = publication["id"]
                if ontology == "agro" and identifier.startswith("http://ceur-ws.org/"):
                    # Skip this one case since it's grandfathered in, but otherwise
                    # these aren't good enough to be considered real citations since
                    # they don't have a DOI
                    continue

                with self.subTest(ontology=ontology, id=identifier):
                    self.assertIn("title", publication)
                    self.assertIsInstance(identifier, str)
                    self.assertFalse(identifier.endswith("/"))
                    self.assertTrue(
                        identifier.startswith("https://www.ncbi.nlm.nih.gov/pubmed/"),
                        msg=f"{ontology} publication {i} has unexpected identifier: {identifier}",
                    )

                    result = citation_url.parse(identifier)
                    self.assertEqual(citation_url.Status.success, result.status)
