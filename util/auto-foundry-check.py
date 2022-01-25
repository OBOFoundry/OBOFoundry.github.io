#!/usr/bin/env python3

# Read the ontologies.yml file
# check foundry criteria

__author__ = "Chris Mungall"

import argparse

import yaml

header = """---
layout: doc
title: OBO Foundry Criteria Checker
---

[The OBO Foundry: coordinated evolution of ontologies to support biomedical data integration](http://www.nature.com/nbt/journal/v25/n11/abs/nbt1346.html)

Barry Smith, Michael Ashburner, Cornelius Rosse, Jonathan Bard, William Bug, Werner Ceusters, Louis J Goldberg, Karen Eilbeck, Amelia Ireland, Christopher J Mungall, The OBI Consortium, Neocles Leontis, Philippe Rocca-Serra, Alan Ruttenberg, Susanna-Assunta Sansone, Richard H Scheuermann, Nigam Shah, Patricia L Whetzel, and Suzanna Lewis

*Nature Biotechnology* **25**, 1251 - 1255 (2007)

[Google Scholar list of papers citing The OBO Foundry.](https://scholar.google.ca/scholar?cites=13806088078865650870&as_sdt=2005&sciodt=0,5&hl=en)

### Ontology Project Publications

"""

template = "- {ontology} ({id}): [{title}]({link})\n"

IN_FOUNDRY_ORDER = "in_foundry_order"


def main():
    parser = argparse.ArgumentParser(description="Extract foundry data")
    parser.add_argument(
        "-i",
        "--ontologies",
        type=argparse.FileType("r"),
        help="the ontologies YAML file to read",
    )
    # parser.add_argument(-'r','--review_path',
    #    type=str,
    #    help='the path to the review file')
    args = parser.parse_args()

    data = yaml.load(args.ontologies, Loader=yaml.SafeLoader)
    reviews = []
    for ontology in data["ontologies"]:
        if "is_obsolete" in ontology:
            continue
        reviews.append(review_ontology(ontology))

    print("## SUCCESS")
    for r in reviews:
        if r["fails"] == []:
            print(" * {}".format(r["id"]))
    print("## FAILS")
    for r in reviews:
        if len(r["fails"]) > 0:
            conflict = ""
            if r["conflict"]:
                conflict = "*CONFLICT*"
            print(" * {} FAILS: {} {}".format(r["id"], r["fails"], conflict))


FAIL_LICENSE = "license not CC-BY or CC-0"
FAIL_TRACKER = "No tracker for community requests"
FAIL_USERS = "No real users"


def review_ontology(ont):
    inject(ont)
    fails = []
    is_foundry = IN_FOUNDRY_ORDER in ont
    open_license = False
    if "license" in ont:
        lurl = ont["license"]["url"]
        if (
            "creativecommons.org/licenses/by/" in lurl
            or "creativecommons.org/publicdomain/zero" in lurl
        ):
            open_license = True
    if not open_license:
        fails.append(FAIL_LICENSE)
    if "tracker" not in ont:
        fails.append(FAIL_TRACKER)
    if "usages" not in ont:
        fails.append(FAIL_USERS)
    conflict = is_foundry and len(fails) > 0
    return dict(id=ont["id"], fails=fails, conflict=conflict)


def inject(ont):
    pass


if __name__ == "__main__":
    main()
