---
layout: ontology_detail
id: fbdv
title: Drosophila development
browsers:
- title: FlyBase Browser
  label: FB
  url: http://flybase.org/.bin/cvreport.html?cvterm=FBdv:00007008
build:
  checkout: git clone https://github.com/FlyBase/drosophila-developmental-ontology.git
  path: .
  system: git
contact:
  email: cp390@cam.ac.uk
  github: Clare72
  label: Clare Pilgrim
  orcid: 0000-0002-1373-1705
description: A structured controlled vocabulary of the development of Drosophila melanogaster.
domain: anatomy and development
homepage: http://purl.obolibrary.org/obo/fbdv
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
preferredPrefix: FBdv
products:
- id: fbdv.owl
- id: fbdv.obo
- id: fbdv.json
- id: fbdv/fbdv-simple.owl
- id: fbdv/fbdv-simple.obo
publications: []
repository: https://github.com/FlyBase/drosophila-developmental-ontology
taxon:
  id: NCBITaxon:7227
  label: Drosophila
tracker: http://purl.obolibrary.org/obo/fbdv/tracker
usages:
- description: Used to record stages in expression and phenotype curation
  examples:
  - description: Expression of DLP in embryonic/larval midgut primordium at embryonic stage 13 (http://purl.obolibrary.org/obo/FBdv_00005328) (Khare and Baumgartner, 2000)
    url: https://flybase.org/reports/FBgn0041604#expression
  user: http://flybase.org
activity_status: active
---

A structured controlled vocabulary of the development of <i>Drosophila melanogaster</i>.
