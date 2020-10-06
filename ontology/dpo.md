---
layout: ontology_detail
id: dpo
preferredPrefix: FBcv
contact:
  email: cp390@cam.ac.uk
  label: Clare Pilgrim
description: An ontology of commonly encountered and/or high level Drosophila phenotypes.
domain: phenotype
homepage: http://purl.obolibrary.org/obo/fbcv
products:
  - id: dpo.owl
  - id: dpo.obo
  - id: dpo.json
taxon:
  id: NCBITaxon:7227
  label: Drosophila
title: Drosophila Phenotype Ontology
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
build:
  checkout: git clone https://github.com/FlyBase/drosophila-phenotype-ontolog.git
  system: git
  path: "."
tracker: https://github.com/FlyBase/drosophila-phenotype-ontology/issues
browsers:
  - label: FB
    title: FlyBase Browser
    url: http://flybase.org/.bin/cvreport.html?cvterm=FBcv:0000347
publications:
  - id: https://doi.org/10.1186/2041-1480-4-30
    title: "The Drosophila phenotype ontology."
usages:
  - user: http://flybase.org
    description: FlyBase uses dpo for phenotype data annotation in Drosophila
    example:
      - url: "http://flybase.org/cgi-bin/cvreport.html?rel=is_a&id=FBcv:0002030"
        description: "alleles and constructs annotated to pupal lethal in FlyBase"
activity_status: active
---

An ontology of commonly encountered and/or high level Drosophila phenotypes.  It has significant formalisation - utilising terms from GO, CL, PATO and the Drosophila anatomy ontology.  It has been used by FlyBase for > 159000 annotations of phenotype.
