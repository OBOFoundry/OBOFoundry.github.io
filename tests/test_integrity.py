"""Test data integrity, beyond what's possible with the JSON schema."""

import json
import unittest
from functools import lru_cache
from io import StringIO
from pathlib import Path
from typing import Set

import requests
import yaml

from obofoundry.standardize_metadata import ModifiedDumper
from obofoundry.utils import ONTOLOGY_DIRECTORY, get_data, get_new_data

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent
SCHEMA_PATH = ROOT.joinpath("util", "schema", "registry_schema.json")

PUBMED_PREFIX = "https://www.ncbi.nlm.nih.gov/pubmed/"
ARXIV_PREFIX = "https://arxiv.org/abs/"
BIORXIV_PREFIX = "https://www.biorxiv.org/content/"
MEDRXIV_PREFIX = "https://www.medrxiv.org/content/"
ZENODO_PREFIX = "https://zenodo.org/record/"
DOI_PREFIX = "https://doi.org/"
CHEMRXIV_DOI_PREFIX = "https://doi.org/10.26434/chemrxiv"
ALLOWED_SPDX = {
    "CC0-1.0",  # see https://bioregistry.io/spdx:CC0-1.0
    "CC-BY-3.0",  # see https://bioregistry.io/spdx:CC-BY-3.0
    "CC-BY-4.0",  # see https://bioregistry.io/spdx:CC-BY-4.0
}
OBO_TO_SPDX = {
    "CC BY 4.0": "CC-BY-4.0",
    "CC BY 3.0": "CC-BY-3.0",
    "CC0": "CC0-1.0",
}
NOR_DASHBOARD_RESULTS = "https://raw.githubusercontent.com/OBOFoundry/obo-nor.github.io/master/dashboard/dashboard-results.yml"


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
                dependency_ids = [d["id"] for d in dependencies]
                self.assertEqual(
                    sorted(dependency_ids),
                    dependency_ids,
                    msg="dependencies should be sorted by ID",
                )
                self.assertEqual(
                    sorted(set(dependency_ids)),
                    dependency_ids,
                    msg="dependencies should be unique",
                )

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
            self.assertIn(
                sum(
                    publication.get("preferred", False)
                    for publication in data.get("publications", [])
                ),
                {0, 1},
                msg=f"Only one publication can be marked as preferred for {ontology}.",
            )

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
                    self.assertIn(
                        "user",
                        usage,
                        msg=f"Malformed usage missing a user in {ontology}",
                    )
                    with self.subTest(
                        ontology=ontology, user=usage["user"], id=publication["id"]
                    ):
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

        is_pubmed = (
            identifier.startswith(PUBMED_PREFIX)
            and identifier[len(PUBMED_PREFIX) :].isnumeric()
        )
        is_zenodo = (
            identifier.startswith(ZENODO_PREFIX)
            and identifier[len(ZENODO_PREFIX) :].isnumeric()
        )
        # TODO add regular expression validation
        is_doi = identifier.startswith(DOI_PREFIX)
        is_arxiv = identifier.startswith(ARXIV_PREFIX)
        is_biorxiv = identifier.startswith(BIORXIV_PREFIX)
        is_medrxiv = identifier.startswith(MEDRXIV_PREFIX)

        self.assertTrue(
            any(
                (
                    is_pubmed,
                    is_zenodo,
                    is_doi,
                    is_arxiv,
                    is_biorxiv,
                    is_medrxiv,
                )
            ),
            msg=msg,
        )

        # Make sure that the unversioned DOI is used
        if (
            is_arxiv
            or is_biorxiv
            or is_medrxiv
            or identifier.startswith(CHEMRXIV_DOI_PREFIX)
        ):
            for v in range(1, 100):
                self.assertFalse(
                    identifier.endswith(f".v{v}"), msg="Please use an unversioned DOI"
                )

    def test_schema_mandatory(self):
        """Test all things in schema marked as error are also in the required list."""
        """Test all things in schema marked as error/warning are also in the required list."""
        # why is there a mismatch between their levels and required status?
        skip_keys = {"in_foundry", "products", "usages"}
        schema = json.loads(SCHEMA_PATH.read_text())
        required: Set[str] = set(schema["required"])
        high_level: Set[str] = {
            key
            for key, configuration in schema["properties"].items()
            if configuration.get("level") in {"warning", "error"}
        }
        self.assertEqual(required - skip_keys, high_level - skip_keys)

    @staticmethod
    def skip_inactive(record) -> bool:
        """Check if should skip for inactive records."""
        return record.get("activity_status") != "active"

    def test_preferred_prefix(self):
        """Test all preferred prefixes."""
        for prefix, record in self.ontologies.items():
            with self.subTest(prefix=prefix):
                if self.skip_inactive(record):
                    continue
                preferred_prefix = record.get("preferredPrefix")
                self.assertIsNotNone(preferred_prefix)
                self.assertLessEqual(2, len(preferred_prefix))
                self.assertNotIn(" ", preferred_prefix)
                if prefix != "dpo":
                    self.assertEqual(preferred_prefix.casefold(), prefix.casefold())

    def test_redundant_descriptions(self):
        """Test that the description field is not redundant of the long form description."""
        for prefix, record in self.ontologies.items():
            if self.skip_inactive(record):
                continue
            description = record.get("description")
            long_description = record["long_description"]
            if description is None:
                continue
            with self.subTest(prefix=prefix):
                self.assertNotEqual(
                    _string_norm(description),
                    _string_norm(long_description),
                    msg=f"Effectively the same description was reused in the short and long-form field for {prefix}",
                )

    def test_has_purl_config(self):
        """Tests that OBO PURL configuration is available."""
        for prefix, record in self.ontologies.items():
            if self.skip_inactive(record):
                continue
            with self.subTest(prefix=prefix):
                url = f"https://raw.githubusercontent.com/OBOFoundry/purl.obolibrary.org/master/config/{prefix}.yml"
                res = requests.get(url)
                self.assertEqual(
                    200,
                    res.status_code,
                    msg=f"PURL configuration is missing for {prefix}",
                )


class TestStandardizedYaml(unittest.TestCase):
    """Test the YAML is standard."""

    def test_standardized(self):
        """Test the YAML is standardized."""
        for path in ONTOLOGY_DIRECTORY.glob("*.md"):
            with self.subTest(prefix=path.stem):
                with path.open() as file:
                    lines = [line.rstrip("\n") for line in file]

                self.assertEqual(lines[0], "---")
                idx = min(
                    i for i, line in enumerate(lines[1:], start=1) if line == "---"
                )

                # Load the data like it is YAML
                chunked = "\n".join(lines[1:idx])
                data = yaml.safe_load(StringIO(chunked))
                # These settings should match the standardize_metadata.py dumping sequence
                dumped = ModifiedDumper.dump(data)
                self.assertEqual(
                    dumped,
                    chunked,
                    msg="\n\n\tPlease run `tox -e lint` to standardize the ontology metadata.",
                )


def _string_norm(s: str) -> str:
    return (
        s.strip()
        .lower()
        .replace("\n", "")
        .replace(" ", "")
        .replace(".", "")
        .replace("-", "")
    )


class TestModernIntegrity(unittest.TestCase):
    """A test case for data integrity exclusively for new ontologies.

    Specifically, tests implemented in this integrity test are only
    "going-forwards" and don't need to be retroactively applied. This works
    since it only looks at ontologies that appear in the /ontologies folder
    with a markdown file but do not already appear in the published registry
    build.
    """

    def setUp(self) -> None:
        """Set up the test case."""
        self.ontologies = get_new_data()

    def test_github_references(self):
        """Test that new ontologies reference the pull request where they were added."""
        for prefix, data in self.ontologies.items():
            with self.subTest(prefix=prefix):
                self.assertIn("pull_request_added", data)
                self.assertIn("issue_requested", data)

    @lru_cache
    def _get_github_data(self, prefix: str):
        data = self.ontologies[prefix]
        repository = data["repository"]
        if not repository.startswith("https://github.com"):
            return None
        r = repository.removeprefix("https://github.com/").rstrip("/")
        url = f"https://api.github.com/repos/{r}"
        res = requests.get(url)
        res.raise_for_status()
        return res.json()

    def test_repository_license(self):
        """Test that the repository has a license that's correct."""
        for prefix, data in self.ontologies.items():
            repository = data["repository"]
            if not repository.startswith("https://github.com"):
                continue
            with self.subTest(prefix=prefix):
                github_data = self._get_github_data(prefix)
                self.assertIn("license", github_data)
                self.assertIn("spdx_id", github_data["license"])
                spdx = github_data["license"]["spdx_id"]
                self.assertIsNotNone(
                    spdx, msg="No LICENSE file found in the repository"
                )
                self.assertNotEqual(
                    "NOASSERTION",
                    spdx,
                    msg="Either no LICENSE file was found or the LICENSE file does not have a standard format that "
                    "GitHub can parse. See https://docs.github.com/en/repositories/managing-your-"
                    "repositorys-settings-and-features/customizing-your-repository/licensing-a-"
                    "repository#detecting-a-license for information on how GitHub does this.",
                )
                self.assertIn(
                    spdx,
                    ALLOWED_SPDX,
                    msg=f"LICENSE file does not follow a standard format for"
                    f" one of the allowed license types ({ALLOWED_SPDX})",
                )

                obo_license = data["license"]["label"]
                self.assertEqual(
                    spdx,
                    OBO_TO_SPDX[obo_license],
                    msg="FORCING FAILURE",
                )

    def test_nor_dashboard(self):
        """Test that the ontology is in and passes the NOR dashboard."""
        nor_data = yaml.safe_load(requests.get(NOR_DASHBOARD_RESULTS).content)
        nor_ontologies = {
            record["namespace"]: record for record in nor_data["ontologies"]
        }
        for prefix, data in self.ontologies.items():
            with self.subTest(prefix=prefix):
                self.assertIn(
                    prefix,
                    set(nor_ontologies),
                    msg=f"Need to add `{prefix}` to the New Ontlogy Request Dashboard "
                    f"(https://github.com/OBOFoundry/obo-nor.github.io)",
                )

                failures = set()
                for key, record in nor_ontologies[prefix]["results"].items():
                    if key in {
                        "ROBOT Report",
                        "FP09 Plurality of Users",
                    }:
                        continue
                    if record["status"] != "PASS":
                        failures.add(key)

                self.assertEqual(
                    set(),
                    failures,
                    msg="Passing the NOR Dashboard outright is required for "
                    "new ontologies, with the exception of FP09 (usages, for now)",
                )

    def test_contribution_guidelines(self):
        """Test that a contribution guidelines document is available in an expected location/format."""
        for prefix, data in self.ontologies.items():
            repository = data["repository"]
            if not repository.startswith("https://github.com"):
                continue
            r = repository.removeprefix("https://github.com/").rstrip("/")
            github_data = self._get_github_data(prefix)
            default_branch = github_data["default_branch"]
            paths = [
                # Markdown
                f"https://github.com/{r}/blob/{default_branch}/CONTRIBUTING.md",
                f"https://github.com/{r}/blob/{default_branch}/docs/CONTRIBUTING.md",
                f"https://github.com/{r}/blob/{default_branch}/.github/CONTRIBUTING.md",
                # RST
                f"https://github.com/{r}/blob/{default_branch}/CONTRIBUTING.rst",
                f"https://github.com/{r}/blob/{default_branch}/docs/CONTRIBUTING.rst",
                f"https://github.com/{r}/blob/{default_branch}/.github/CONTRIBUTING.rst",
            ]
            self.assertTrue(
                any(requests.get(path).status_code == 200 for path in paths),
                msg=f"Could not find a CONTRIBUTING.md file in the repository for {prefix} ({repository}) in any of "
                "the standard locations defined by GitHub in https://docs.github.com/en/communities/setting-up-"
                "your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors.",
            )
