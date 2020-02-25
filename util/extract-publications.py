#!/usr/bin/env python3

import argparse
import yaml

# Read the ontologies.yml file
# collect the first 'publications' entry from each project,
# and write as Markdown.

__author__ = 'James A. Overton'


header = '''---
layout: doc
title: Publications Related to the OBO Foundry
---

[The OBO Foundry: coordinated evolution of ontologies to support biomedical data integration](http://www.nature.com/nbt/journal/v25/n11/abs/nbt1346.html)

Barry Smith, Michael Ashburner, Cornelius Rosse, Jonathan Bard, William Bug, Werner Ceusters, Louis J Goldberg, Karen Eilbeck, Amelia Ireland, Christopher J Mungall, The OBI Consortium, Neocles Leontis, Philippe Rocca-Serra, Alan Ruttenberg, Susanna-Assunta Sansone, Richard H Scheuermann, Nigam Shah, Patricia L Whetzel, and Suzanna Lewis

*Nature Biotechnology* **25**, 1251 - 1255 (2007)

[Google Scholar list of papers citing The OBO Foundry.](https://scholar.google.ca/scholar?cites=13806088078865650870&as_sdt=2005&sciodt=0,5&hl=en)

### Ontology Project Publications

'''

template = '- {ontology} ({id}): [{title}]({link})\n'


def main():
  parser = argparse.ArgumentParser(description='Extract publication data')
  parser.add_argument('ontologies', type=argparse.FileType('r'),
                      help='the ontologies YAML file to read')
  parser.add_argument('publications_path', type=str, help='the path to the output file')
  args = parser.parse_args()

  data = yaml.load(args.ontologies, Loader=yaml.SafeLoader)
  publications = []
  for ontology in data['ontologies']:
    result = {}
    if 'title' in ontology:
      result['ontology'] = ontology['title']
    if 'id' in ontology:
      result['id'] = ontology['id']

    for publication in ontology.get('publications', []):
      if 'id' in publication and 'title' in publication:
        result['link'] = publication['id']
        result['title'] = publication['title']
        break
    if 'ontology' in result and 'id' in result \
       and 'link' in result and 'title' in result:
      publications.append(result)

  publications = sorted(publications, key=lambda k: k['ontology'])
  with open(args.publications_path, 'w') as output:
    output.write(header)
    for publication in publications:
      output.write(template.format(**publication))


if __name__ == "__main__":
  main()
