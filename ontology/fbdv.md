---
layout: ontology_detail
id: fbdv
preferredPrefix: FBdv
contact:
  email: cp390@cam.ac.uk
  label: Clare Pilgrim
description: A structured controlled vocabulary of the development of Drosophila melanogaster.
domain: development
homepage: http://purl.obolibrary.org/obo/fbdv
products:
  - id: fbdv.owl
  - id: fbdv.obo
  - id: fbdv.json
  - id: fbdv/fbdv-simple.owl
  - id: fbdv/fbdv-simple.obo
taxon:
  id: NCBITaxon:7227
  label: Drosophila
title: Drosophila development
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
build:
  checkout: git clone https://github.com/FlyBase/drosophila-developmental-ontology.git
  system: git
  path: "."
tracker: https://github.com/FlyBase/drosophila-developmental-ontology/issues
browsers:
  - label: FB
    title: FlyBase Browser
    url: http://flybase.org/.bin/cvreport.html?cvterm=FBdv:00007008
activity_status: active
---

A structured controlled vocabulary of the development of <i>Drosophila melanogaster</i>.
