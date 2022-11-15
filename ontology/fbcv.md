---
layout: ontology_detail
id: fbcv
title: FlyBase Controlled Vocabulary
browsers:
- title: FlyBase Browser
  label: FB
  url: http://flybase.org/.bin/cvreport.html?cvterm=FBcv:0000013
build:
  checkout: git clone https://github.com/FlyBase/flybase-controlled-vocabulary.git
  path: .
  system: git
contact:
  email: cp390@cam.ac.uk
  github: Clare72
  label: Clare Pilgrim
  orcid: 0000-0002-1373-1705
description: A structured controlled vocabulary used for various aspects of annotation by FlyBase.
domain: organisms
github_date_added: 2015-08-06
homepage: http://purl.obolibrary.org/obo/fbcv
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
preferredPrefix: FBcv
products:
- id: fbcv.owl
- id: fbcv.obo
- id: fbcv.json
publications: []
repository: https://github.com/FlyBase/flybase-controlled-vocabulary
tracker: https://github.com/FlyBase/flybase-controlled-vocabulary/issues
usages:
- description: FlyBase uses FBcv for phenotype data annotation in Drosophila
  examples:
  - description: alleles and constructs annotated to bang sensitive in FlyBase
    url: http://flybase.org/cgi-bin/cvreport.html?rel=is_a&id=FBcv:0000391
  user: http://flybase.org
activity_status: active
---

A structured controlled vocabulary used for various aspects of annotation by FlyBase. It includes the Drosophila Phenotype Ontology (dpo) which is also released separately.

This ontology is maintained by FlyBase for various aspects of annotation not covered, or not yet covered, by other OBO ontologies.  If and when community ontologies are available for the domains here covered FlyBase will use them.
