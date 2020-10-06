---
layout: ontology_detail
id: upheno
title: Unified phenotype ontology (uPheno)
description: The uPheno ontology integrates multiple phenotype ontologies into a unified cross-species phenotype ontology. 
homepage: https://github.com/obophenotype/upheno
tracker: https://github.com/obophenotype/upheno/issues
license:
  url: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0
contact:
  label: Nicole Vasilevsky
  email: vasilevs@ohsu.edu
  github: nicolevasilevsky
mailing_list: https://groups.google.com/forum/#!forum/phenotype-ontologies-editors
jobs:
  - id: https://travis-ci.org/obophenotype/upheno
    type: travis-ci
products:
  - id: upheno.owl
  - id: upheno/mp-hp-view.owl
usages:
  - user: https://monarchinitiative.org/
    type: analysis
    description: uPheno is used by the Monarch Initiative for cross-species inference.
    examples:
      - url: https://monarchinitiative.org/phenotype/HP:0001300#diseases
    reference: https://academic.oup.com/nar/article/45/D1/D712/2605791
build:
  source_url: http://build.berkeleybop.org/job/build-pheno-ontologies/lastSuccessfulBuild/artifact/*zip*/archive.zip
  path: archive/ontology
  method: archive
activity_status: active
---
