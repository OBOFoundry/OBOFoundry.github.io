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
  github: seger
description: XPO represents anatomical, cellular, and gene function phenotypes occurring throughout the development of the African frogs Xenopus laevis and tropicalis.
domain: phenotype
homepage: https://github.com/obophenotype/xenopus-phenotype-ontology
products:
  - id: xpo.owl
  - id: xpo.obo
taxon:
  id: NCBITaxon:8353
  label: Xenopus
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
activity_status: active
---

The Xenopus Phenotype Ontology represents and standardizes phenotypes occurring throughout the development of the African frogs Xenopus laevis and tropicalis. It supports the annotation of phenotypes in Xenbase and is designed to integrate Xenopus data with genotype, phenotype, and disease data across species.
