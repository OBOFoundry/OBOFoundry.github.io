"""Run this script to update the operations metadata."""

from obofoundry.constants import OPS_PATH
from obofoundry.utils import load_ops
import click
import yaml
import requests
from textwrap import dedent

#: WikiData SPARQL endpoint. See https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service#Interfacing
WIKIDATA_SPARQL = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"


def query_wikidata(query: str):
    """Query the Wikidata SPARQL endpoint and return JSON."""
    res = requests.get(
        WIKIDATA_SPARQL,
        params={"query": query, "format": "json"},
    )
    res.raise_for_status()
    res_json = res.json()
    return res_json["results"]["bindings"]


@click.command()
def main():
    operations_metadata = yaml.safe_load(OPS_PATH.read_text())
    for member in operations_metadata["members"]:
        orcid = member["orcid"]
        if "wikidata" not in member:
            print(orcid, "missing ORCID")
            q = dedent(f"""\
                SELECT DISTINCT ?item ?github 
                WHERE 
                {{
                    ?item wdt:P496 "{orcid}" .
                    OPTIONAL {{ ?item wdt:P2037 ?github }} .
                }}
                LIMIT 1
                """)
            print(f"running query:\n{q}")
            res = query_wikidata(q)
            if res:
                member["wikidata"] = res[0]["item"]["value"].removeprefix("http://www.wikidata.org/entity/")
                github = res[0].get("github")
                if github:
                    member["github"] = github["value"]
            OPS_PATH.write_text(yaml.safe_dump(operations_metadata, sort_keys=True, width=float("inf")))


if __name__ == '__main__':
    main()
