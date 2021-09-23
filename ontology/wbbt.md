---
layout: ontology_detail
id: wbbt
preferredPrefix: WBbt
contact:
  email: raymond@caltech.edu
  label: Raymond Lee
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY 4.0
description: A structured controlled vocabulary of the anatomy of <i>Caenorhabditis elegans</i>.
domain: anatomy
homepage: https://github.com/obophenotype/c-elegans-gross-anatomy-ontology
tracker: https://github.com/obophenotype/c-elegans-gross-anatomy-ontology/issues
products:
  - id: wbbt.owl
  - id: wbbt.obo
taxon:
  id: NCBITaxon:6237
  label: Caenorhabditis
title: C. elegans Gross Anatomy Ontology
build:
  checkout: git clone https://github.com/obophenotype/c-elegans-gross-anatomy-ontology.git
  system: git
  path: "."
publications:
  - id: https://pubmed.ncbi.nlm.nih.gov/18629098/
    title: "Building a cell and anatomy ontology of Caenorhabditis elegans"
usages:
  - user: https://www.wormbase.org/
    type: annotation
    description: WormBase uses WBbt to curate anatomical expression patterns and anatomy function annotations, and to allow search and indexing on the WormBase site
    examples:
      - url: http://www.wormbase.org/db/get?name=WBGene00000912;class=Gene;widget=expression
        description: "Expression for gene daf-16 with WormBase ID WBGene00000912"
    publications:
      - id: https://academic.oup.com/nar/article/48/D1/D762/5603222
        title: "WormBase: a modern Model Organism Information Resource"
activity_status: active
repository: https://github.com/obophenotype/c-elegans-gross-anatomy-ontology
---

A structured controlled vocabulary of the anatomy of <i>Caenorhabditis elegans</i>.
