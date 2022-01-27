# -*- coding: utf-8 -*-

"""Standardize the license labels using the Bioregistry.

Run with: ``python standardize_license_labels.py``.

Author: `Charles Tapley Hoyt <https://cthoyt.com>`_.
"""

import pathlib
from typing import Union

import click
from bioregistry.license_standardizer import LICENSES
from tqdm import tqdm

HERE = pathlib.Path(__file__).parent.resolve()
ONTOLOGY_DIRECTORY = HERE.parent.joinpath("ontology").resolve()


def update_markdown(path: Union[str, pathlib.Path]) -> None:
    """Update the given markdown file."""
    with open(path) as file:
        lines = [line.rstrip("\n") for line in file]

    try:
        idx = min(i for i, line in enumerate(lines) if line.startswith("license:"))
    except ValueError:
        # no license
        return

    license_url = None
    for i in range(1, 3):
        line = lines[idx + i].strip()
        if "url:" in line:
            _, license_url = line.split(":", 1)

    if license_url is None:
        tqdm.write(f"no license URL in {path}")
        return

    new_label = LICENSES.get(license_url.strip())
    if new_label is None:
        tqdm.write(f"could not standardize license URL {license_url} in {path}")
        return

    license_label, license_label_idx = None, None
    for i in range(1, 3):
        line = lines[idx + i].strip()
        if "label:" in line:
            license_label_idx = idx + i
            _, license_label = line.split(":", 1)

    if license_label.replace("-", "") == new_label.replace("-", ""):
        return

    if license_label_idx is None:
        tqdm.write(f"no license label in {path}")
        return

    with open(path, "w") as file:
        for i, line in enumerate(lines):
            if i == license_label_idx:
                print(f"  label: {new_label}", file=file)
            else:
                print(line, file=file)


@click.command()
def main():
    for path in ONTOLOGY_DIRECTORY.glob("*.md"):
        update_markdown(path)


if __name__ == "__main__":
    main()
