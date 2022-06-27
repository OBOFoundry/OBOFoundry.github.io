#!/usr/bin/env python3

import csv
import sys
from argparse import ArgumentParser

import yaml


def main(args):
    """
    Takes ontologies.yml file and makes a triple file with SHACL prefixes.

    For example, for uberon it will generate:

        [ sh:prefix "UBERON" ; sh:namespace "http://purl.obolibrary.org/obo/UBERON_"]

    We always assume the CURIE prefix is uppercase, unless 'preferred_prefix' is specified
    (for mixed-case prefixes, e.g. FBbt)

    This can be useful for converting an OBO class PURL to a prefix without assumption-embedding string conversions.
    It can be used to interconvert PURLs to CURIEs.

    Note that while prefixes can sometimes be seen in RDF files, this is part of the syntax and not part of the data,
    the prefixes are expanded at parse time. The obo_prefixes.ttl file makes these explicit.

    We use the SHACL vocabulary since it provides convenient predicates for putting prefixes in the domain of discourse;
    however, it does not entail any use of SHACL

    """
    parser = ArgumentParser(
        description="""
  Takes ontologies.yml file and makes a triple file with shacl prefixes"""
    )
    parser.add_argument("input")
    args = parser.parse_args()
    stream = open(args.input, "r")
    data = yaml.load(stream, Loader=yaml.SafeLoader)

    print("@prefix sh:	<http://www.w3.org/ns/shacl#> .")
    print("@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .")
    print("[")
    print(" sh:declare")
    sep = ""
    for ont in data["ontologies"]:
        # if ont.get("is_obsolete", False):
        #    continue
        # See https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1976
        prefix = ont.get("preferredPrefix", ont["id"].upper())
        print(
            f'{sep}[ sh:prefix "{prefix}" ; sh:namespace "http://purl.obolibrary.org/obo/{prefix}_"]'
        )
        sep = ","
    print("] .")


if __name__ == "__main__":
    main(sys.argv)
