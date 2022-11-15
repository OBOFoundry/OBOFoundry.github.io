---
layout: ontology_detail
id: wbphenotype
title: C. elegans phenotype
build:
  checkout: git clone https://github.com/obophenotype/c-elegans-phenotype-ontology.git
  path: .
  system: git
contact:
  email: cgrove@caltech.edu
  github: chris-grove
  label: Chris Grove
  orcid: 0000-0001-9076-6015
description: A structured controlled vocabulary of <i>Caenorhabditis elegans</i> phenotypes
domain: phenotype
github_date_added: 2015-07-28
homepage: https://github.com/obophenotype/c-elegans-phenotype-ontology
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
preferredPrefix: WBPhenotype
products:
- id: wbphenotype.owl
- id: wbphenotype.obo
- id: wbphenotype/wbphenotype-base.owl
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/21261995
  title: 'Worm Phenotype Ontology: integrating phenotype data within and beyond the C. elegans community.'
repository: https://github.com/obophenotype/c-elegans-phenotype-ontology
taxon:
  id: NCBITaxon:6237
  label: Caenorhabditis
tracker: https://github.com/obophenotype/c-elegans-phenotype-ontology/issues
usages:
- description: WormBase uses WBPhenotype to curate worm phenotypes, and to allow search and indexing on the WormBase site
  examples:
  - description: Expression for daf-16 gene with WormBase ID WBGene00000912.
    url: http://www.wormbase.org/db/get?name=WBGene00000912;class=Gene;widget=expression
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/31642470
    title: 'WormBase: a modern Model Organism Information Resource'
  type: annotation
  user: https://www.wormbase.org/
- description: Monarch integrates phenotype annotations from sources such as WormBase, and allows for querying using the WBPhenotype ontology.
  examples:
  - description: 'Egg long: The fertilized oocytes have a greater than standard length measured end to end compared to control.'
    url: https://monarchinitiative.org/phenotype/WBPhenotype%3A0000370
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/27899636
    title: 'The Monarch Initiative: an integrative data and analytic platform connecting phenotypes to genotypes across species '
  type: annotation
  user: https://monarchinitiative.org/
activity_status: active
---
