---
layout: ontology_detail
id: xao
description: XAO represents the anatomy and development of the African frogs Xenopus laevis and tropicalis.
domain: anatomy and development
homepage: http://www.xenbase.org/anatomy/xao.do?method=display
contact:
  label: Erik Segerdell
  email: Erik.Segerdell@cchmc.org
  github: seger
  orcid: 0000-0002-9611-1279
in_foundry_order: 1
products:
  - id: xao.owl
  - id: xao.obo
taxon:
  id: NCBITaxon:8353
  label: Xenopus
title: Xenopus Anatomy Ontology
review:
  date: 2010
build:
  source_url: https://raw.githubusercontent.com/xenopus-anatomy/xao/master/xenopus_anatomy.obo
  method: obo2owl
  infallible: 0
tracker: https://github.com/xenopus-anatomy/xao/issues
publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/18817563
    title: "An ontology for Xenopus anatomy and development."
  - id: https://www.ncbi.nlm.nih.gov/pubmed/24139024
    title: "Enhanced XAO: the ontology of Xenopus anatomy and development underpins more accurate annotation of gene expression and queries on Xenbase."
usages:
  - user: http://www.xenbase.org
    description: Xenbase uses XAO to annotate gene expression.
    examples:
      - url: http://www.xenbase.org/anatomy/showanatomy.do?method=displayAnatomySummary&anatomyId=463
        description: Xenopus genes expressed in the pronephric kidney.
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
activity_status: active
repository: https://github.com/xenopus-anatomy/xao
preferredPrefix: XAO
---

The Xenopus Anatomy Ontology represents and standardizes the anatomy and development of the African frogs Xenopus laevis and tropicalis. It supports the annotation of gene expression data in Xenbase and is designed to facilitate cross-taxa comparisons.
