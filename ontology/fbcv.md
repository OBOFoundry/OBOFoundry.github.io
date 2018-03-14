---
layout: ontology_detail
id: fbcv
preferredPrefix: FBcv
contact:
  email: temj2@cam.ac.uk
  label: Tamsin Jones
description: A structured controlled vocabulary used for various aspects of annotation by FlyBase.
domain:
homepage: http://purl.obolibrary.org/obo/fbcv
products:
  - id: fbcv.owl
title: FlyBase Controlled Vocabulary
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
build:
  source_url: https://raw.githubusercontent.com/FlyBase/flybase-controlled-vocabulary/master/releases/fbcv.owl
  method: obo2owl
tracker: http://purl.obolibrary.org/obo/fbbt/tracker
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
---
A structured controlled vocabulary used for various aspects of annotation by FlyBase. It includes the Drosophila Phenotype Ontology (dpo) which is also released separately.

This ontology is maintained by FlyBase for various aspects of annotation not covered, or not yet covered, by other OBO ontologies.  If and when community ontologies are available for the domains here covered FlyBase will use them.
