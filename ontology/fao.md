---
layout: ontology_detail
id: fao
contact:
  email: dinglis@stanford.edu
  label: Diane Inglis
description: A structured controlled vocabulary for the anatomy of fungi.
domain: anatomy
tracker: https://github.com/obophenotype/fungal-anatomy-ontology/issues
homepage: http://www.yeastgenome.org/fungi/fungal_anatomy_ontology/
page: http://www.yeastgenome.org/fungi/fungal_anatomy_ontology/#description
products:
  - id: fao.owl
  - id: fao.obo
taxon:
  id: NCBITaxon:4751
  label: Fungal
title: Fungal gross anatomy
build:
  checkout: git clone https://github.com/obophenotype/fungal-anatomy-ontology.git
  system: git
  method: vcs
  infallible: 1
---

A structured controlled vocabulary for the anatomy of fungi.
