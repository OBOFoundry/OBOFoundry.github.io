---
layout: ontology_detail
id: mco
title: Microbial Conditions Ontology
build:
  checkout: git clone https://github.com/microbial-conditions-ontology/microbial-conditions-ontology.git
  path: .
  system: git
contact:
  email: citlalli.mejiaalmonte@gmail.com
  github: citmejia
  label: Citlalli Mejía-Almonte
  orcid: 0000-0002-0142-5591
dependencies:
- id: bfo
- id: chebi
- id: cl
- id: clo
- id: micro
- id: ncbitaxon
- id: ncit
- id: obi
- id: omit
- id: omp
- id: pato
- id: peco
- id: uberon
- id: zeco
description: Microbial Conditions Ontology is an ontology...
domain: investigations
github_date_added: 2019-02-15
homepage: https://github.com/microbial-conditions-ontology/microbial-conditions-ontology
jobs:
- id: https://travis-ci.org/microbial-conditions-ontology/microbial-conditions-ontology
  type: travis-ci
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: MCO
products:
- id: mco.owl
- id: mco.obo
repository: https://github.com/microbial-conditions-ontology/microbial-conditions-ontology
tags:
- experimental conditions
tracker: https://github.com/microbial-conditions-ontology/microbial-conditions-ontology/issues
activity_status: active
---

Microbial Conditions Ontology contains terms to describe growth conditions in microbiological experiments. The first version is based on gene regulation experiments in Escherichia coli K-12. It is being used in RegulonDB to link growth conditions to gene regulation data.
