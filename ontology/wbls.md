---
layout: ontology_detail
id: wbls
title: C. elegans development ontology
build:
  checkout: git clone https://github.com/obophenotype/c-elegans-development-ontology.git
  path: .
  system: git
contact:
  email: cgrove@caltech.edu
  github: chris-grove
  label: Chris Grove
  orcid: 0000-0001-9076-6015
description: A structured controlled vocabulary of the development of <i>Caenorhabditis elegans</i>.
domain: anatomy and development
github_date_added: 2015-07-28
homepage: https://github.com/obophenotype/c-elegans-development-ontology
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: WBls
products:
- id: wbls.owl
- id: wbls.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/31642470
  title: 'WormBase: a modern Model Organism Information Resource'
repository: https://github.com/obophenotype/c-elegans-development-ontology
tags:
- developemental life stage
taxon:
  id: NCBITaxon:6237
  label: Caenorhabditis
tracker: https://github.com/obophenotype/c-elegans-development-ontology/issues
usages:
- description: WormBase uses WBls to curate temporal expression patterns, and to allow search and indexing on the WormBase site
  examples:
  - description: Expression for daf-16 gene with WormBase ID WBGene00000912.
    url: http://www.wormbase.org/db/get?name=WBGene00000912;class=Gene;widget=expression
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/31642470
    title: 'WormBase: a modern Model Organism Information Resource'
  type: annotation
  user: https://www.wormbase.org/
activity_status: active
---
