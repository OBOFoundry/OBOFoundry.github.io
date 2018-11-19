---
layout: ontology_detail
id: planp
title: Planarian Phenotype Ontology
jobs:
  - id: https://travis-ci.org/srobb1/planarian-phenotype-ontology
    type: travis-ci
build:
  checkout: git clone https://github.com/srobb1/planarian-phenotype-ontology.git
  system: git
  path: "."
contact:
  email: smr@stowers.org
  label: Sofia Robb
description: Planarian Phenotype Ontology is an ontology of phenotypes
domain: stuff
homepage: https://github.com/srobb1/planarian-phenotype-ontology
products:
  - id: planp.owl
  - id: planp.obo
dependencies:
 - id: ro
 - id: pato
 - id: plana
 - id: go
tracker: https://github.com/srobb1/planarian-phenotype-ontology/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
---

Planarian phenotype ontology.
