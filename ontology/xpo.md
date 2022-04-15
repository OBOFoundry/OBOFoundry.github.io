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
  email: Erik.Segerdell@cchmc.org
  label: Erik Segerdell
  github: seger
  orcid: 0000-0002-9611-1279
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
publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/35317743
    title: "The Xenopus phenotype ontology: bridging model organism phenotype data to human health and development."
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
activity_status: active
repository: https://github.com/obophenotype/xenopus-phenotype-ontology
preferredPrefix: XPO
---

The Xenopus Phenotype Ontology represents and standardizes phenotypes occurring throughout the development of the African frogs Xenopus laevis and tropicalis. It supports the annotation of phenotypes in Xenbase and is designed to integrate Xenopus data with genotype, phenotype, and disease data across species.
