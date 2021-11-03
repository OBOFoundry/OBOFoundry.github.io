---
layout: ontology_detail
id: pco
title: Population and Community Ontology
jobs:
  - id: https://travis-ci.org/PopulationAndCommunityOntology/pco
    type: travis-ci
build:
  checkout: git clone https://github.com/PopulationAndCommunityOntology/pco.git
  system: git
  path: "."
contact:
  email: rlwalls2008@gmail.com
  label: Ramona Walls
description: An ontology about groups of interacting organisms such as populations and communities
domain: collections of organisms
homepage: https://github.com/PopulationAndCommunityOntology/pco
products:
  - id: pco.owl
dependencies:
  - id: ro
  - id: bfo
  - id: pato
  - id: envo
  - id: go
  - id: iao
  - id: bfo
  - id: ncbi_taxon
  - id: caro
tracker: https://github.com/PopulationAndCommunityOntology/pco/issues
license:
  url: http://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
activity_status: active
repository: https://github.com/PopulationAndCommunityOntology/pco
preferredPrefix: PCO
---

The Population and Community Ontology (PCO) describes material entities, qualities, and processes related to collections of interacting organisms such as populations and communities. It is taxon neutral, and can be used for any species, including humans.
