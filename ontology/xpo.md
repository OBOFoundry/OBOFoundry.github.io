---
layout: ontology_detail
id: xpo
title: Xenopus Phenotype Ontology
jobs:
  - id: https://travis-ci.org/obophenotype/xenopus-phenotype-ontology
    type: travis-ci
build:
  checkout: git clone https://github.com/obophenotype/xenopus-phenotype-ontology.git
  system: git
  path: "."
contact:
  email: esegerd3@gmail.com
  label: Erik Segerdell
description: An ontology of anatomical, cellular, and gene function phenotypes in Xenopus, the African clawed frogs.
domain: phenotype
homepage: https://github.com/obophenotype/xenopus-phenotype-ontology
products:
  - id: xpo.owl
  - id: xpo.obo
dependencies:
 - id: iao
 - id: go
 - id: ro
 - id: pato
 - id: bfo
 - id: chebi
 - id: cl
 - id: xao
tracker: https://github.com/obophenotype/xenopus-phenotype-ontology/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
---

The Xenopus Phenotype Ontology represents and standardizes anatomical, cellular, and gene function phenotypes in Xenopus, the African clawed frogs. The XPO is being designed primarily to support phenotype curation in Xenbase, the model organism database for Xenopus, and to facilitate mappings between frog phenotypes and human disease.
