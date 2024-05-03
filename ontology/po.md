---
layout: ontology_detail
id: po
title: Plant Ontology
browsers:
- title: Planteome browser
  label: Planteome
  url: http://browser.planteome.org/amigo
contact:
  email: jaiswalp@science.oregonstate.edu
  github: jaiswalp
  label: Pankaj Jaiswal
  orcid: 0000-0002-1005-8383
depicted_by: https://github.com/Planteome/plant-ontology/blob/master/Planteome_profile.jpg
description: The Plant Ontology is a structured vocabulary and database resource that links plant anatomy, morphology and growth and development to plant genomics data.
domain: anatomy and development
homepage: http://browser.planteome.org/amigo
in_foundry_order: 1
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
page: https://github.com/Planteome/plant-ontology
preferredPrefix: PO
products:
- id: po.owl
- id: po.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/23220694
  title: The plant ontology as a tool for comparative plant anatomy and genomic analyses.
- id: https://www.ncbi.nlm.nih.gov/pubmed/29186578
  title: 'The Planteome database: an integrated resource for reference ontologies, plant genomics and phenomics.'
repository: https://github.com/Planteome/plant-ontology
taxon:
  id: NCBITaxon:33090
  label: Viridiplantae
tracker: https://github.com/Planteome/plant-ontology/issues
twitter: planteome
usages:
- description: Planteome uses PO to describe location of tissue expression for genes in viridiplantae
  examples:
  - description: Genes and proteins annotate to leaf
    url: http://browser.planteome.org/amigo/term/PO:0025034
  user: http://planteome.org/
- description: Maize CELL genomics DB uses PO to annotate images
  examples:
  - description: LhG4 Promoter Drivers
    url: http://maize.jcvi.org/cellgenomics/geneDB_list.php?filter=3
  user: http://maize.jcvi.org/
- description: MaizeGDB uses PO for annotation of genes
  examples:
  - description: Introduced in gene model set 5b in assembly version RefGen_v2.
    url: http://maizegdb.org/gene_center/gene/GRMZM5G863962
  user: http://maizegdb.org/
- description: Gramene uses PO for the annotation of plant genes
  examples:
  - description: Gramene annotations to leaf from Arabidopsis
    url: http://archive.gramene.org/db/ontology/search?id=PO:0025034
  user: http://gramene.org/
activity_status: active
---

The Plant Ontology is a structured vocabulary and database resource that links plant anatomy, morphology and growth and development to plant genomics data. The PO is under active development to expand to encompass terms and annotations from all plants.
