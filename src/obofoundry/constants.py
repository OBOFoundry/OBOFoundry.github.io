"""Constants for the OBO Foundry."""

import pathlib

HERE = pathlib.Path(__file__).parent.resolve()
ROOT = HERE.parent.parent.resolve()
ONTOLOGY_DIRECTORY = ROOT.joinpath("ontology")
DATA_DIRECTORY = ROOT.joinpath("_data")
#: Path to the file containing metadata about members of the OBO Operations Committee
OPERATIONS_METADATA_PATH = DATA_DIRECTORY.joinpath("operations.yml")
ALUMNI_METADATA_PATH = DATA_DIRECTORY.joinpath("alumni.yml")
