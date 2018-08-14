---
layout: ontology_detail
id: upheno
title: Combined phenotype ontology
mailing_list: https://groups.google.com/forum/#!forum/phenotype-ontologies-editors
jobs:
  - id: https://travis-ci.org/obophenotype/upheno
    type: travis-ci
products:
  - id: upheno.owl
  - id: mp-hp-view.owl
build:
  source_url: http://build.berkeleybop.org/job/build-pheno-ontologies/lastSuccessfulBuild/artifact/*zip*/archive.zip
  path: archive/ontology
  method: archive
---
