---
layout: ontology_detail
id: ecocore
title: An ontology of core ecological entities
jobs:
  - id: https://travis-ci.org/EcologicalSemantics/ecocore
    type: travis-ci
build:
  checkout: git clone https://github.com/EcologicalSemantics/ecocore.git
  system: git
  path: "."
contact:
  email: p.buttigieg@gmail.com
  label: Pier Luigi Buttigieg
  github: pbuttigieg
description: Ecocore is a community ontology for the concise and controlled description of ecological traits of organisms.
domain: ecological functions, ecological interactions
homepage: https://github.com/EcologicalSemantics/ecocore
products:
  - id: ecocore.owl
  - id: ecocore.obo
dependencies:
  - id: pco
  - id: ro
  - id: bfo
  - id: pato
  - id: envo
  - id: chebi
  - id: go
  - id: uberon
  - id: po
  - id: iao
tracker: https://github.com/EcologicalSemantics/ecocore/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
activity_status: active
repository: https://github.com/EcologicalSemantics/ecocore
---

This ontology aims to provide core semantics for ecological entities, such as ecological functions (for predators, prey, etc), food webs, and ecological interactions. The ontology, closely interoperates with existing OBO ontologies such as the Environment Ontology, the Population and Community Ontology (PCO), the Relations Ontology (RO), the Gene Ontology (for biological processes etc), the Phenotype and Quality Ontology (PATO), the Plant Ontology (PO), and many others. Ecocore is under active development.
