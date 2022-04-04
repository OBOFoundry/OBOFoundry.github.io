---
layout: ontology_detail
id: to
contact:
  email: jaiswalp@science.oregonstate.edu
  label: Pankaj Jaiswal
  github: jaiswalp
  orcid: 0000-0002-1005-8383
description: A controlled vocabulary to describe phenotypic traits in plants.
domain: phenotype
homepage: http://browser.planteome.org/amigo
page: http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab
products:
  - id: to.owl
  - id: to.obo
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
taxon:
  id: NCBITaxon:33090
  label: Viridiplantae
title: Plant Trait Ontology
browsers:
  - label: Planteome
    title: Planteome browser
    url: http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab
jobs:
  - id: https://travis-ci.org/Planteome/plant-trait-ontology
    type: travis-ci
build:
  checkout: git clone https://github.com/Planteome/plant-trait-ontology.git
  system: git
  path: "."
  method: vcs
  infallible: 1
tracker: https://github.com/Planteome/plant-trait-ontology/issues
publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/29186578
    title: "The Planteome database: an integrated resource for reference ontologies, plant genomics and phenomics."
usages:
  - user: http://planteome.org/
    description: Planteome uses TO to describe traits for genes and germplasm
    examples:
      - url: http://browser.planteome.org/amigo/term/TO:0000286
        description: Genes and proteins annotated to submergence tolerance, including SUB1
  - user: http://gramene.org/
    description: Gramene uses PO for the annotation of plant genes and QTLs
    examples:
      - url: http://archive.gramene.org/db/ontology/search?id=TO:0000286
        description: Gramene annotations to submergence tolerance
activity_status: active
repository: https://github.com/Planteome/plant-trait-ontology
preferredPrefix: TO
depicted_by: http://planteome.org/sites/default/files/garland_logo.PNG
---

A controlled vocabulary of describe phenotypic traits in plants. Each trait is a distinguishable feature, characteristic, quality or phenotypic feature of a developing or mature plant.
