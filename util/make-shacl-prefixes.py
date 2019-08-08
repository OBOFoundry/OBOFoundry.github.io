#!/usr/bin/env python3

import csv
import sys
import yaml

from argparse import ArgumentParser


def main(args):
  parser = ArgumentParser(description='''
  Takes ontologies.yml file and makes a triple file with shacl prefixes''')
  parser.add_argument('input')
  args = parser.parse_args()
  stream = open(args.input, 'r')
  data = yaml.load(stream, Loader=yaml.SafeLoader)

  print('@prefix sh:	<http://www.w3.org/ns/shacl#> .')
  print('@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .')
  print('[')
  print(' sh:declare')
  sep = ''
  for ont in data['ontologies']:
    if ont.get('is_obsolete',False):
      continue
    prefix = ont.get('preferredPrefix', ont['id'].upper())
    print(f'{sep}[ sh:prefix "{prefix}" ; sh:namespace "http://purl.obolibrary.org/obo/{prefix}_"]')
    sep = ','
  print(']')
    
    
  

if __name__ == '__main__':
  main(sys.argv)
