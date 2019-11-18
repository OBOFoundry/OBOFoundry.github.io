---
layout: ontology_detail
id: bto
contact:
  email: a.chang@tu-bs.de
  label: Antje Chang
description: A structured controlled vocabulary for the source of an enzyme comprising tissues, cell lines, cell types and cell cultures.
domain: anatomy
homepage: http://www.brenda-enzymes.info
tracker: https://github.com/BRENDA-Enzymes/BTO/issues
page: https://en.wikipedia.org/wiki/BRENDA_tissue_ontology
publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/21030441
    title: "The BRENDA Tissue Ontology (BTO): the first all-integrating ontology of all organisms for enzyme sources"
products:
  - id: bto.owl
  - id: bto.obo
  - id: bto.json
license:
  url: https://creativecommons.org/licenses/by-nd/4.0/
  label: CC BY-ND 4.0
title: BRENDA tissue / enzyme source
build:
  checkout: git clone https://github.com/BRENDA-Enzymes/BTO.git
  system: git
  path: "."
activity_status: active
---

A structured controlled vocabulary for the source of an enzyme. It comprises terms for tissues, cell lines, cell types and cell cultures from uni- and multicellular organisms.
