---
layout: ontology_detail
id: to
contact:
  email: jaiswalp@science.oregonstate.edu
  label: Pankaj Jaiswal
description: A controlled vocabulary of describe phenotypic traits in plants.
domain: phenotype
homepage: http://planteome.org
page: http://browser.planteome.org/amigo/term/TO:0000387#display-lineage-tab
products:
  - id: to.owl
  - id: to.obo
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY 4.0
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
  - id: http://www.ncbi.nlm.nih.gov/pubmed/22847540
    title: "Ontologies as integrative tools for plant science."
---

A controlled vocabulary of describe phenotypic traits in plants. Each trait is a distinguishable feature, characteristic, quality or phenotypic feature of a developing or mature plant.

<img alt="Planteome logo" src="http://planteome.org/sites/default/files/garland_logo.PNG"/>
