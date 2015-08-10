#!/usr/bin/env python3

__author__ = 'cjm'

import yaml
import json
import optparse
     
parser = optparse.OptionParser()
(options, args) = parser.parse_args()

if (len(args) != 1):
    raise ValueError("Must pass exactly 1 yaml file")
stream = open(args[0], 'r');
data = yaml.load(stream)
json = json.dumps(data)

print(json)

# To install: sudo easy_install pyyaml 
