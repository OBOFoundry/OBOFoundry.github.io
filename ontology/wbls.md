---
layout: ontology_detail
id: wbls
preferredPrefix: WBls
contact:
  email: cgrove@caltech.edu
  label: Chris Grove
  github: chris-grove
  orcid: 0000-0001-9076-6015
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
description: A structured controlled vocabulary of the development of <i>Caenorhabditis elegans</i>.
domain: anatomy and development
tags:
  - developemental life stage
homepage: https://github.com/obophenotype/c-elegans-development-ontology
tracker: https://github.com/obophenotype/c-elegans-development-ontology/issues
products:
  - id: wbls.owl
  - id: wbls.obo
taxon:
  id: NCBITaxon:6237
  label: Caenorhabditis
title: C. elegans development ontology
build:
  checkout: git clone https://github.com/obophenotype/c-elegans-development-ontology.git
  system: git
  path: "."
publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/31642470
    title: "WormBase: a modern Model Organism Information Resource"
usages:
  - user: https://www.wormbase.org/
    type: annotation
    description: WormBase uses WBls to curate temporal expression patterns, and to allow search and indexing on the WormBase site
    examples:
      - url: http://www.wormbase.org/db/get?name=WBGene00000912;class=Gene;widget=expression
        description: Expression for daf-16 gene with WormBase ID WBGene00000912.
    publications:
      - id: https://www.ncbi.nlm.nih.gov/pubmed/31642470
        title: "WormBase: a modern Model Organism Information Resource"
activity_status: active
repository: https://github.com/obophenotype/c-elegans-development-ontology
---
