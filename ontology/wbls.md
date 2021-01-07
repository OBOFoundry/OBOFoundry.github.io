---
layout: ontology_detail
id: wbls
preferredPrefix: WBls
contact:
  email: cgrove@caltech.edu
  label: Chris Grove
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
description: A structured controlled vocabulary of the development of <i>Caenorhabditis elegans</i>.
domain: developemental life stage
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
  - id: https://academic.oup.com/nar/article/48/D1/D762/5603222
    title: "WormBase: a modern Model Organism Information Resource"
usages:
  - user: https://www.wormbase.org/
    type: annotation
    description: WormBase uses WBls to curate temporal expression patterns, and to allow search and indexing on the WormBase site
    examples:
      - url: http://www.wormbase.org/db/get?name=WBGene00000912;class=Gene;widget=expression
    reference: https://academic.oup.com/nar/article/48/D1/D762/5603222
activity_status: active
---

A structured controlled vocabulary of the development of <i>Caenorhabditis elegans</i>.
