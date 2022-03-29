#!/usr/bin/env python3

import csv
import sys
from argparse import ArgumentParser

import yaml


def main(args):
    parser = ArgumentParser(
        description="""
  Takes a YAML file containing information for various ontologies and a metadata file specifying
  the sorting order for ontologies, and then produces a sorted version input YAML"""
    )
    parser.add_argument(
        "unsorted_yaml",
        type=str,
        help="Unsorted YAML file containing information for ontologies",
    )
    parser.add_argument(
        "metadata_grid",
        type=str,
        help="CSV or TSV file containing metadata information for ontologies",
    )
    parser.add_argument(
        "output_yaml",
        type=str,
        help="Name of output YAML file that will contain sorted ontology information",
    )
    args = parser.parse_args()

    data_file = args.unsorted_yaml
    grid = args.metadata_grid
    output = args.output_yaml

    sort_order = get_sort_order(grid)
    data = load_data(data_file)
    data = sort_ontologies(data, sort_order)
    write_data(data, output)


def get_sort_order(grid):
    """Given the path to the metadata grid (CSV or TSV), extract the order of
    ontologies from the grid. Return the list of ontology IDs in that order."""
    sort_order = []
    if ".csv" in grid:
        separator = ","
    elif ".tsv" or ".txt" in grid:
        separator = "\t"
    else:
        print("%s must be tab- or comma-separated.", file=sys.stderr)
        sys.exit(1)
    with open(grid, "r") as f:
        reader = csv.reader(f, delimiter=separator)
        # Ignore the header row:
        next(reader)
        for row in reader:
            # Ontology IDs are in the first column of the CSV/TSV. We simply pull them out of each line
            # in the file. Their ordering in the file is the sort ordering we are looking for:
            sort_order.append(row[0])
    return sort_order


def load_data(data_file):
    """Given a YAML file, load the data into a dictionary."""
    stream = open(data_file, "r")
    data = yaml.load(stream, Loader=yaml.SafeLoader)
    return data


def sort_ontologies(data, sort_order):
    """Given the ontologies data as a dictionary and the list of ontologies in
    proper sort order, return the sorted data."""
    ontologies = []
    for ont_id in sort_order:
        # We assume that ontology ids are unique:
        ont = [ont for ont in data["ontologies"] if ont["id"] == ont_id].pop()
        ontologies.append(ont)
    data["ontologies"] = ontologies
    return data


def write_data(data, output):
    """Given the ontologies data as a dictionary and an output YAML file to
    write to, write the data to the file."""
    with open(output, "w") as f:
        yaml.safe_dump(data, f, allow_unicode=True)


if __name__ == "__main__":
    main(sys.argv)
