---
layout: ontology_detail
id: dpo
title: Drosophila Phenotype Ontology
browsers:
- title: FlyBase Browser
  label: FB
  url: http://flybase.org/.bin/cvreport.html?cvterm=FBcv:0000347
build:
  checkout: git clone https://github.com/FlyBase/drosophila-phenotype-ontolog.git
  path: .
  system: git
contact:
  email: cp390@cam.ac.uk
  github: Clare72
  label: Clare Pilgrim
  orcid: 0000-0002-1373-1705
description: An ontology of commonly encountered and/or high level Drosophila phenotypes.
domain: phenotype
homepage: http://purl.obolibrary.org/obo/fbcv
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
preferredPrefix: FBcv
products:
- id: dpo.owl
- id: dpo.obo
- id: dpo.json
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/24138933
  title: The Drosophila phenotype ontology.
repository: https://github.com/FlyBase/drosophila-phenotype-ontology
taxon:
  id: NCBITaxon:7227
  label: Drosophila
tracker: https://github.com/FlyBase/drosophila-phenotype-ontology/issues
usages:
- description: FlyBase uses dpo for phenotype data annotation in Drosophila
  examples:
  - description: alleles and constructs annotated to pupal lethal in FlyBase
    url: http://flybase.org/cgi-bin/cvreport.html?rel=is_a&id=FBcv:0002030
  user: http://flybase.org
activity_status: active
---

An ontology of commonly encountered and/or high level Drosophila phenotypes.  It has significant formalisation - utilising terms from GO, CL, PATO and the Drosophila anatomy ontology.  It has been used by FlyBase for > 159000 annotations of phenotype.
