"""Test data integrity, beyond what's possible with the JSON schema."""

import unittest
from pathlib import Path

import yaml

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent
ONTOLOGY_DIRECTORY = ROOT.joinpath("ontology").resolve()

uri_prefix = "https://www.ncbi.nlm.nih.gov/pubmed/"


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
                    self.assert_valid_publication_id(
                        publication,
                        msg=f"{ontology} publication {i} has unexpected identifier: {identifier}",
                    )

            for i, usage in enumerate(data.get("usages", [])):
                for j, publication in enumerate(usage.get("publications", [])):
                    self.assertIn("user", usage, msg=f"Malformed usage missing a user in {ontology}")
                    with self.subTest(ontology=ontology, user=usage["user"], id=publication["id"]):
                        self.assert_valid_publication_id(
                            publication,
                            msg=f"{ontology} usage {i} publication {j} has unexpected identifier: {publication['id']}",
                        )

    def assert_valid_publication_id(self, publication, msg=None):
        """Assert that the publication is annotated properly."""
        self.assertIn("title", publication)
        self.assertIn("id", publication)
        identifier = publication["id"]
        self.assertIsInstance(identifier, str)
        self.assertFalse(identifier.endswith("/"))
