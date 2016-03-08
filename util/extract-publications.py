#!/usr/bin/env python3

# Read the ontologies.yml file
# collect the first 'publications' entry from each project,
# and write as Markdown.

__author__ = 'James A. Overton'

import argparse, yaml

template = '- {ontology} ({id}): [{title}]({link})\n'

def main():
    parser = argparse.ArgumentParser(
        description='Extract publication data')
    parser.add_argument('ontologies',
        type=argparse.FileType('r'),
        help='the ontologies YAML file to read')
    parser.add_argument('publications_path',
        type=str,
        help='the path to the output file')
    args = parser.parse_args()

    data = yaml.load(args.ontologies)
    publications = []
    for ontology in data['ontologies']:
      result = {}
      if 'title' in ontology:
        result['ontology'] = ontology['title']
      if 'id' in ontology:
        result['id'] = ontology['id']
      if 'publications' in ontology:
        for publication in ontology['publications']:
          if 'id' in publication and 'title' in publication:
            result['link'] = publication['id']
            result['title'] = publication['title']
            break
      if 'ontology' in result and 'id' in result \
          and 'link' in result and 'title' in result:
        publications.append(result)

    publications = sorted(publications, key=lambda k: k['ontology'])
    with open(args.publications_path, 'w') as output:
      output.write('---\nlayout: default\ntitle: OBO-Related Publications\n---\n\n')
      for publication in publications:
        output.write(template.format(**publication))

if __name__ == "__main__":
    main()
