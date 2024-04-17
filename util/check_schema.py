# -*- coding: utf-8 -*-

"""A script for automatically checking the schema compliance of all ontologies.

Run with: ``python check_schema.py``.

Author: `Charles Tapley Hoyt <https://cthoyt.com>`_.
"""

import json
from collections import Counter, defaultdict

import click
from tabulate import tabulate
from utils import SCHEMA_PATH, get_data

#: These keys are automatically populated during build
SKIP_KEYS = {
    "ontology_purl",
}


@click.command()
@click.option("--max-cutoff", type=int, default=3, show_default=True)
@click.option("--links", is_flag=True)
def main(max_cutoff: int, links: bool):
    """Check schema usage."""
    _check_schema(max_cutoff=max_cutoff, links=links)


def _check_schema(max_cutoff: int = 3, links: bool = True):
    ontologies = get_data()

    property_usage = Counter()
    for data in ontologies.values():
        for key in data:
            property_usage[key] += 1

    keys = {k for k, v in property_usage.items() if v <= max_cutoff}

    r = defaultdict(set)
    for prefix, data in ontologies.items():
        for key in keys:
            if key in data:
                r[key].add(prefix)

    print(f"Fields used at most {max_cutoff} times:")
    print(
        tabulate(
            [
                (
                    k,
                    ", ".join(
                        (
                            f"[{prefix}](https://obofoundry.org/ontologies/{prefix})"
                            if links
                            else prefix
                        )
                        for prefix in prefixes
                    ),
                )
                for k, prefixes in r.items()
            ],
            tablefmt="github",
            headers=["key", "ontologies"],
        )
    )

    with SCHEMA_PATH.open() as file:
        schema = json.load(file)
    unused = {
        prop
        for prop in schema["properties"]
        if prop not in property_usage and prop not in SKIP_KEYS
    }
    print("Unused properties:")
    print(*sorted(unused), sep="\n")


if __name__ == "__main__":
    main()
