"""This script annotates an ORCID identifier to each ontology's contact person.

Run with: ``python annotate_orcid.py``. However, it makes sense to update the mapping at
https://github.com/cthoyt/obo-community-health first in case there are new mappings available.

Author: `Charles Tapley Hoyt <https://cthoyt.com>`_.
"""

import pathlib
from functools import cache
from io import StringIO
from typing import Union

import click
import pandas as pd
import yaml
from tqdm import tqdm

HERE = pathlib.Path(__file__).parent.resolve()
ONTOLOGY_DIRECTORY = HERE.parent.joinpath("ontology").resolve()


def update_orcid(path: Union[str, pathlib.Path]) -> None:
    """Update the given markdown file."""
    with open(path) as file:
        lines = [line.rstrip("\n") for line in file]

    assert lines[0] == "---"
    idx = min(i for i, line in enumerate(lines[1:], start=1) if line == "---")

    # Load the data like it is YAML
    data = yaml.safe_load(StringIO("\n".join(lines[1:idx])))

    contact = data.get("contact", {})
    if "orcid" in contact:
        return  # already available!

    github_handle = contact.get("github")
    if github_handle is None:
        tqdm.write(
            f"Issue getting GitHub handle for {data['id']} for {contact.get('label')} ({contact.get('email')})"
        )
        return

    orcid = get_github_to_orcid().get(github_handle)
    if orcid is None:
        tqdm.write(
            f"Issue getting ORCID for {data['id']} with GitHub handle @{github_handle}"
        )
        return

    with open(path, "w") as file:
        print("---", file=file)
        for line in lines[1:idx]:
            print(line, file=file)
            if line.startswith("  github:"):
                print(f"  orcid: {orcid}", file=file)
        print("---", file=file)
        for line in lines[idx + 1 :]:
            print(line, file=file)


@cache
def get_github_to_orcid() -> dict[str, str]:
    """Get a mapping from GitHub to ORCID identifiers."""
    url = "https://raw.githubusercontent.com/cthoyt/obo-community-health/main/data/contacts_table.tsv"
    df = pd.read_csv(url, sep="\t")
    return dict(df[["github", "orcid"]].values)


@click.command()
def main():
    for path in tqdm(ONTOLOGY_DIRECTORY.glob("*.md")):
        update_orcid(path)


if __name__ == "__main__":
    main()
