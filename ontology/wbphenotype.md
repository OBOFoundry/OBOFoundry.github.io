---
layout: ontology_detail
id: wbphenotype
preferredPrefix: WBPhenotype
contact:
  email: cgrove@caltech.edu
  label: Chris Grove
  github: chris-grove
  orcid: 0000-0001-9076-6015
license:
  url: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
description: A structured controlled vocabulary of <i>Caenorhabditis elegans</i> phenotypes
domain: phenotype
homepage: https://github.com/obophenotype/c-elegans-phenotype-ontology
tracker: https://github.com/obophenotype/c-elegans-phenotype-ontology/issues
products:
  - id: wbphenotype.owl
  - id: wbphenotype.obo
  - id: wbphenotype/wbphenotype-base.owl
taxon:
  id: NCBITaxon:6237
  label: Caenorhabditis
title: C. elegans phenotype
build:
  checkout: git clone https://github.com/obophenotype/c-elegans-phenotype-ontology.git
  system: git
  path: "."
publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/21261995
    title: "Worm Phenotype Ontology: integrating phenotype data within and beyond the C. elegans community."
usages:
  - user: https://www.wormbase.org/
    type: annotation
    description: WormBase uses WBPhenotype to curate worm phenotypes, and to allow search and indexing on the WormBase site
    examples:
      - url: http://www.wormbase.org/db/get?name=WBGene00000912;class=Gene;widget=expression
        description: Expression for daf-16 gene with WormBase ID WBGene00000912.
    publications:
      - id: https://www.ncbi.nlm.nih.gov/pubmed/31642470
        title: "WormBase: a modern Model Organism Information Resource"
  - user: https://monarchinitiative.org/
    type: annotation
    description: Monarch integrates phenotype annotations from sources such as WormBase, and allows for querying using the WBPhenotype ontology.
    examples:
      - url: https://monarchinitiative.org/phenotype/WBPhenotype%3A0000370
        description: "Egg long: The fertilized oocytes have a greater than standard length measured end to end compared to control."
    publications:
      - id: https://www.ncbi.nlm.nih.gov/pubmed/27899636
        title: "The Monarch Initiative: an integrative data and analytic platform connecting phenotypes to genotypes across species "
activity_status: active
repository: https://github.com/obophenotype/c-elegans-phenotype-ontology
---

A structured controlled vocabulary of <i>Caenorhabditis elegans</i> phenotypes
