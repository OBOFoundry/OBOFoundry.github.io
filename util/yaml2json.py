#!/usr/bin/env python3

import json
from argparse import ArgumentParser

import yaml

__author__ = "cjm"


parser = ArgumentParser(
    description="Converts a YAML file to JSON, writing the result to STDOUT"
)
parser.add_argument("yaml_file", type=str, help="YAML file to convert")
args = parser.parse_args()

with open(args.yaml_file, "r") as stream:
    data = yaml.load(stream, Loader=yaml.SafeLoader)
data["@context"] = "http://obofoundry.github.io/registry/context.jsonld"
json = json.dumps(
    data, sort_keys=True, indent=4, ensure_ascii=False, separators=(",", ": ")
)
print(json)
