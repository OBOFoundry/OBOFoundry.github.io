---
layout: ontology_detail
id: mco
title: Microbial Conditions Ontology
jobs:
  - id: https://travis-ci.org/microbial-conditions-ontology/microbial-conditions-ontology
    type: travis-ci
build:
  checkout: git clone https://github.com/microbial-conditions-ontology/microbial-conditions-ontology.git
  system: git
  path: "."
contact:
  email: citlalli.mejiaalmonte@gmail.com
  label: Citlalli Mejía-Almonte
description: Microbial Conditions Ontology is an ontology...
domain: experimental conditions
homepage: https://github.com/microbial-conditions-ontology/microbial-conditions-ontology
products:
  - id: mco.owl
  - id: mco.obo
dependencies:
 - id: bfo
 - id: chebi
 - id: cl
 - id: clo
 - id: micro
 - id: ncbitaxon
 - id: peco
 - id: ncit
 - id: obi
 - id: omit
 - id: omp
 - id: pato
 - id: uberon
 - id: zeco
tracker: https://github.com/microbial-conditions-ontology/microbial-conditions-ontology/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
activity_status: active
---

Enter a detailed description of your ontology here

Microbial Conditions Ontology contains terms to describe growth conditions in microbiological experiments. The first version is based on gene regulation experiments in Escherichia coli K-12. It is being used in RegulonDB to link growth conditions to gene regulation data. 
