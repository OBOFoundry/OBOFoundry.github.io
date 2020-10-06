---
layout: ontology_detail
id: fbcv
preferredPrefix: FBcv
contact:
  email: cp390@cam.ac.uk
  label: Clare Pilgrim
description: A structured controlled vocabulary used for various aspects of annotation by FlyBase.
domain: organisms
homepage: http://purl.obolibrary.org/obo/fbcv
products:
  - id: fbcv.owl
  - id: fbcv.obo
  - id: fbcv.json
title: FlyBase Controlled Vocabulary
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
build:
  checkout: git clone https://github.com/FlyBase/flybase-controlled-vocabulary.git
  system: git
  path: "."
tracker: https://github.com/FlyBase/flybase-controlled-vocabulary/issues
browsers:
  - label: FB
    title: FlyBase Browser
    url: http://flybase.org/.bin/cvreport.html?cvterm=FBcv:0000013
usages:
  - user: http://flybase.org
    description: FlyBase uses FBcv for phenotype data annotation in Drosophila
    example:
      - url: "http://flybase.org/cgi-bin/cvreport.html?rel=is_a&id=FBcv:0000391"
        description: "alleles and constructs annotated to bang sensitive in FlyBase"
activity_status: active
---
A structured controlled vocabulary used for various aspects of annotation by FlyBase. It includes the Drosophila Phenotype Ontology (dpo) which is also released separately.

This ontology is maintained by FlyBase for various aspects of annotation not covered, or not yet covered, by other OBO ontologies.  If and when community ontologies are available for the domains here covered FlyBase will use them.
