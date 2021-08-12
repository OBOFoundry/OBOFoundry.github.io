---
layout: ontology_detail
id: po
in_foundry_order: 1
title: Plant Ontology
review:
  date: 2013
  document:
    label: PDF
    link: https://drive.google.com/open?id=0B8vqEgF1N0NIV1o0N21UOHlLSmc
jobs:
  - id: https://travis-ci.org/Planteome/plant-ontology
    type: travis-ci
build:
  checkout: git clone https://github.com/Planteome/plant-ontology.git
  system: git
  method: vcs
  infallible: 1
contact:
  email: jaiswalp@science.oregonstate.edu
  label: Pankaj Jaiswal
  github: jaiswalp
description: "The Plant Ontology is a structured vocabulary and database resource that links plant anatomy, morphology and growth and development to plant genomics data."
domain: anatomy and development
homepage: http://browser.planteome.org/amigo
page: https://github.com/Planteome/plant-ontology
twitter: planteome
tracker: https://github.com/Planteome/plant-ontology/issues
publications:
  - id: http://www.ncbi.nlm.nih.gov/pubmed/23220694
    title: "The plant ontology as a tool for comparative plant anatomy and genomic analyses."
  - id: https://doi.org/10.1093/nar/gkx1152
    title: "The Planteome database: an integrated resource for reference ontologies, plant genomics and phenomics."
products:
  - id: po.owl
  - id: po.obo
browsers:
  - label: Planteome
    title: Planteome browser
    url: http://browser.planteome.org/amigo
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY 4.0
taxon:
  id: NCBITaxon:33090
  label: Viridiplantae
usages:
  - user: http://planteome.org/
    description: Planteome uses PO to describe location of tissue expression for genes in viridiplantae
    examples:
      - url: http://browser.planteome.org/amigo/term/PO:0025034
        description: Genes and proteins annotate to leaf
  - user: http://maize.jcvi.org/
    description: Maize CELL genomics DB uses PO to annotate images
    examples:
      - url: http://maize.jcvi.org/cellgenomics/geneDB_list.php?filter=3
        description: LhG4 Promoter Drivers
  - user: http://maizegdb.org/
    description: MaizeGDB uses PO for annotation of genes
    examples:
      - url: http://maizegdb.org/gene_center/gene/GRMZM5G863962
        description: Introduced in gene model set 5b in assembly version RefGen_v2.
  - user: http://gramene.org/
    description: Gramene uses PO for the annotation of plant genes
    examples:
      - url: http://archive.gramene.org/db/ontology/search?id=PO:0025034
        description: Gramene annotations to leaf from Arabidopsis
activity_status: active
repository: https://github.com/Planteome/plant-ontology
---

The Plant Ontology is a structured vocabulary and database resource that links plant anatomy, morphology and growth and development to plant genomics data. The PO is under active development to expand to encompass terms and annotations from all plants.

<img alt="Planteome logo" src="http://planteome.org/sites/default/files/garland_logo.PNG"/>
