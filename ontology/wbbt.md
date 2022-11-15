---
layout: ontology_detail
id: wbbt
title: C. elegans Gross Anatomy Ontology
build:
  checkout: git clone https://github.com/obophenotype/c-elegans-gross-anatomy-ontology.git
  path: .
  system: git
contact:
  email: raymond@caltech.edu
  github: raymond91125
  label: Raymond Lee
  orcid: 0000-0002-8151-7479
description: A structured controlled vocabulary of the anatomy of <i>Caenorhabditis elegans</i>.
domain: anatomy and development
github_date_added: 2015-07-28
homepage: https://github.com/obophenotype/c-elegans-gross-anatomy-ontology
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: WBbt
products:
- id: wbbt.owl
- id: wbbt.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/18629098
  title: Building a cell and anatomy ontology of Caenorhabditis elegans
repository: https://github.com/obophenotype/c-elegans-gross-anatomy-ontology
taxon:
  id: NCBITaxon:6237
  label: Caenorhabditis
tracker: https://github.com/obophenotype/c-elegans-gross-anatomy-ontology/issues
usages:
- description: WormBase uses WBbt to curate anatomical expression patterns and anatomy function annotations, and to allow search and indexing on the WormBase site
  examples:
  - description: Expression for gene daf-16 with WormBase ID WBGene00000912
    url: http://www.wormbase.org/db/get?name=WBGene00000912;class=Gene;widget=expression
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/31642470
    title: 'WormBase: a modern Model Organism Information Resource'
  type: annotation
  user: https://www.wormbase.org/
activity_status: active
---
