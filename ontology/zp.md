---
layout: ontology_detail
id: zp
title: Zebrafish Phenotype Ontology
jobs:
  - id: https://travis-ci.org/obophenotype/zebrafish-phenotype-ontology
    type: travis-ci
build:
  checkout: git clone https://github.com/obophenotype/zebrafish-phenotype-ontology.git
  system: git
  path: "."
contact:
  email: ybradford@zfin.org
  label: Yvonne Bradford
description: The Zebrafish Phenotype Ontology formally defines all phenotypes of the Zebrafish model organism.
domain: phenotype
homepage: https://github.com/obophenotype/zebrafish-phenotype-ontology
products:
  - id: zp.owl
  - id: zp.obo
dependencies:
  - id: go
  - id: ro
  - id: pato
  - id: bspo
  - id: zfa
  - id: bfo
  - id: uberon
tracker: https://github.com/obophenotype/zebrafish-phenotype-ontology/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
usages:
  - user: https://monarchinitiative.org/
    type: annotation
    description: Monarch integrates phenotype annotations from sources such as ZFIIN, and allows for querying using the ZP ontology.
    examples:
      - url: https://monarchinitiative.org/phenotype/ZP:0005692
        description: "adaxial cell absent, abnormal: Abnormal(ly) absent (of) adaxial cell."
    publications:
      - id: https://academic.oup.com/nar/article/45/D1/D712/2605791
        title: "The Monarch Initiative: an integrative data and analytic platform connecting phenotypes to genotypes across species"
activity_status: active
---
