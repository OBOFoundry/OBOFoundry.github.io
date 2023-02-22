"""Test data integrity, beyond what's possible with the JSON schema."""

import requests
import yaml

from obofoundry.constants import ONTOLOGY_DIRECTORY, ROOT

__all__ = [
    "get_data",
    "query_wikidata",
    "get_new_data",
]


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
        data["long_description"] = "".join(lines[idx:])
        ontologies[data["id"]] = data
    return ontologies


#: WikiData SPARQL endpoint. See https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service#Interfacing
WIKIDATA_SPARQL = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"


def query_wikidata(query: str):
    """Query the Wikidata SPARQL endpoint and return JSON."""
    headers = {"User-Agent": "obofoundry/1.0 (https://obofoundry.org)"}
    res = requests.get(
        WIKIDATA_SPARQL, params={"query": query, "format": "json"}, headers=headers
    )
    res.raise_for_status()
    res_json = res.json()
    return res_json["results"]["bindings"]


def get_new_data():
    """Get records for ontologies that have additional checks.

    So far, this applies in the following scenarios:

    1. New ontologies, i.e., there's a markdown file for the ontology in the ``/ontologies`` directory
       but has it not yet been published and does not appear in the config.yml
    """
    data = get_data()
    config_path = ROOT.joinpath("_config.yml")
    config_data = yaml.safe_load(config_path.read_text())
    published = {record["id"] for record in config_data["ontologies"]}
    return {
        prefix: record for prefix, record in data.items() if prefix not in published
    }
