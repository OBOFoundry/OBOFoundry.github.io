---
layout: ontology_detail
id: zp
title: Zebrafish Phenotype Ontology
build:
  checkout: git clone https://github.com/obophenotype/zebrafish-phenotype-ontology.git
  path: .
  system: git
contact:
  email: ybradford@zfin.org
  github: ybradford
  label: Yvonne Bradford
  orcid: 0000-0002-9900-7880
dependencies:
- id: bfo
- id: bspo
- id: go
- id: pato
- id: ro
- id: uberon
- id: zfa
description: The Zebrafish Phenotype Ontology formally defines all phenotypes of the Zebrafish model organism.
domain: phenotype
github_date_added: 2019-01-02
homepage: https://github.com/obophenotype/zebrafish-phenotype-ontology
jobs:
- id: https://travis-ci.org/obophenotype/zebrafish-phenotype-ontology
  type: travis-ci
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: ZP
products:
- id: zp.owl
- id: zp.obo
repository: https://github.com/obophenotype/zebrafish-phenotype-ontology
tracker: https://github.com/obophenotype/zebrafish-phenotype-ontology/issues
usages:
- description: Monarch integrates phenotype annotations from sources such as ZFIIN, and allows for querying using the ZP ontology.
  examples:
  - description: 'adaxial cell absent, abnormal: Abnormal(ly) absent (of) adaxial cell.'
    url: https://monarchinitiative.org/phenotype/ZP:0005692
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/27899636
    title: 'The Monarch Initiative: an integrative data and analytic platform connecting phenotypes to genotypes across species'
  type: annotation
  user: https://monarchinitiative.org/
activity_status: active
---
