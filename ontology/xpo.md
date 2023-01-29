---
layout: ontology_detail
id: xpo
title: Xenopus Phenotype Ontology
build:
  checkout: git clone https://github.com/obophenotype/xenopus-phenotype-ontology.git
  path: .
  system: git
contact:
  email: Erik.Segerdell@cchmc.org
  github: seger
  label: Erik Segerdell
  orcid: 0000-0002-9611-1279
dependencies:
- id: bfo
- id: chebi
- id: cl
- id: go
- id: iao
- id: pato
- id: ro
- id: xao
description: XPO represents anatomical, cellular, and gene function phenotypes occurring throughout the development of the African frogs Xenopus laevis and tropicalis.
domain: phenotype
homepage: https://github.com/obophenotype/xenopus-phenotype-ontology
jobs:
- id: https://travis-ci.org/obophenotype/xenopus-phenotype-ontology
  type: travis-ci
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: XPO
products:
- id: xpo.owl
- id: xpo.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/35317743
  title: 'The Xenopus phenotype ontology: bridging model organism phenotype data to human health and development.'
repository: https://github.com/obophenotype/xenopus-phenotype-ontology
taxon:
  id: NCBITaxon:8353
  label: Xenopus
tracker: https://github.com/obophenotype/xenopus-phenotype-ontology/issues
activity_status: active
---

The Xenopus Phenotype Ontology represents and standardizes phenotypes occurring throughout the development of the African frogs Xenopus laevis and tropicalis. It supports the annotation of phenotypes in Xenbase and is designed to integrate Xenopus data with genotype, phenotype, and disease data across species.
