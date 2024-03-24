---
layout: ontology_detail
id: xao
title: Xenopus Anatomy Ontology
build:
  infallible: 0
  method: obo2owl
  source_url: https://raw.githubusercontent.com/xenopus-anatomy/xao/master/xenopus_anatomy.obo
contact:
  email: Erik.Segerdell@cchmc.org
  github: seger
  label: Erik Segerdell
  orcid: 0000-0002-9611-1279
description: XAO represents the anatomy and development of the African frogs Xenopus laevis and tropicalis.
domain: anatomy and development
homepage: http://www.xenbase.org/anatomy/xao.do?method=display
in_foundry_order: 1
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: XAO
products:
- id: xao.owl
- id: xao.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/18817563
  title: An ontology for Xenopus anatomy and development.
- id: https://www.ncbi.nlm.nih.gov/pubmed/24139024
  title: 'Enhanced XAO: the ontology of Xenopus anatomy and development underpins more accurate annotation of gene expression and queries on Xenbase.'
repository: https://github.com/xenopus-anatomy/xao
taxon:
  id: NCBITaxon:8353
  label: Xenopus
tracker: https://github.com/xenopus-anatomy/xao/issues
usages:
- description: Xenbase uses XAO to annotate gene expression.
  examples:
  - description: Xenopus genes expressed in the pronephric kidney.
    url: http://www.xenbase.org/anatomy/showanatomy.do?method=displayAnatomySummary&anatomyId=463
  user: http://www.xenbase.org
activity_status: active
---

The Xenopus Anatomy Ontology represents and standardizes the anatomy and development of the African frogs Xenopus laevis and tropicalis. It supports the annotation of gene expression data in Xenbase and is designed to facilitate cross-taxa comparisons.
