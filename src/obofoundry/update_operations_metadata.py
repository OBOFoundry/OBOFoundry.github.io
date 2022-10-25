"""Run this script to update the operations metadata."""

from pathlib import Path
from textwrap import dedent

import click
import yaml
from tqdm import tqdm

from obofoundry.constants import ALUMNI_METADATA_PATH, OPERATIONS_METADATA_PATH
from obofoundry.utils import query_wikidata


@click.command(name="update-operations-metadata")
def main():
    """Update the operations committee members metadata file by querying Wikidata."""
    _main(ALUMNI_METADATA_PATH)
    _main(OPERATIONS_METADATA_PATH)


def _main(path: Path):
    operations_metadata = yaml.safe_load(path.read_text())
    for member in tqdm(operations_metadata["members"]):
        orcid = member["orcid"]
        if "wikidata" not in member or "github" not in member:
            tqdm.write(f"{member['name']} ({orcid}) missing wikidata or github")
            sparql = dedent(
                f"""\
                SELECT DISTINCT ?item ?github
                WHERE
                {{
                    ?item wdt:P496 "{orcid}" .
                    OPTIONAL {{ ?item wdt:P2037 ?github }} .
                }}
                LIMIT 1
                """
            )
            res = query_wikidata(sparql)
            if res:
                member["wikidata"] = res[0]["item"]["value"].removeprefix(
                    "http://www.wikidata.org/entity/"
                )
                github = res[0].get("github")
                if github:
                    member["github"] = github["value"]
            path.write_text(
                yaml.safe_dump(
                    operations_metadata,
                    sort_keys=True,
                    width=float("inf"),
                    allow_unicode=True,
                )
            )


if __name__ == "__main__":
    main()
