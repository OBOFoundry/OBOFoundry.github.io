---
layout: ontology_detail
id: to
title: Plant Trait Ontology
browsers:
- title: Planteome browser
  label: Planteome
  url: http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab
build:
  checkout: git clone https://github.com/Planteome/plant-trait-ontology.git
  infallible: 1
  method: vcs
  path: .
  system: git
contact:
  email: jaiswalp@science.oregonstate.edu
  github: jaiswalp
  label: Pankaj Jaiswal
  orcid: 0000-0002-1005-8383
depicted_by: http://planteome.org/sites/default/files/garland_logo.PNG
description: A controlled vocabulary to describe phenotypic traits in plants.
domain: phenotype
github_date_added: 2015-07-28
homepage: http://browser.planteome.org/amigo
jobs:
- id: https://travis-ci.org/Planteome/plant-trait-ontology
  type: travis-ci
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
page: http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab
preferredPrefix: TO
products:
- id: to.owl
- id: to.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/29186578
  title: 'The Planteome database: an integrated resource for reference ontologies, plant genomics and phenomics.'
repository: https://github.com/Planteome/plant-trait-ontology
taxon:
  id: NCBITaxon:33090
  label: Viridiplantae
tracker: https://github.com/Planteome/plant-trait-ontology/issues
usages:
- description: Planteome uses TO to describe traits for genes and germplasm
  examples:
  - description: Genes and proteins annotated to submergence tolerance, including SUB1
    url: http://browser.planteome.org/amigo/term/TO:0000286
  user: http://planteome.org/
- description: Gramene uses PO for the annotation of plant genes and QTLs
  examples:
  - description: Gramene annotations to submergence tolerance
    url: http://archive.gramene.org/db/ontology/search?id=TO:0000286
  user: http://gramene.org/
activity_status: active
---

A controlled vocabulary of describe phenotypic traits in plants. Each trait is a distinguishable feature, characteristic, quality or phenotypic feature of a developing or mature plant.
