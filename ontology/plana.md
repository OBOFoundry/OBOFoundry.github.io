---
layout: ontology_detail
id: plana
title: planaria-ontology
build:
  checkout: git clone https://github.com/obophenotype/planaria-ontology.git
  path: .
  system: git
contact:
  email: smr@stowers.org
  github: srobb1
  label: Sofia Robb
  orcid: 0000-0002-3528-5267
dependencies:
- id: ro
- id: uberon
description: PLANA, the planarian anatomy ontology, encompasses the anatomy and life cycle stages for both __Schmidtea mediterranea__ biotypes.
domain: anatomy and development
homepage: https://github.com/obophenotype/planaria-ontology
jobs:
- id: https://travis-ci.org/obophenotype/planaria-ontology
  type: travis-ci
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: PLANA
products:
- id: plana.owl
- id: plana.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/34318308
  title: 'Planarian Anatomy Ontology: a resource to connect data within and across experimental platforms'
repository: https://github.com/obophenotype/planaria-ontology
tracker: https://github.com/obophenotype/planaria-ontology/issues
usages:
- description: Planosphere's PAGE database uses PLANA to annotate gene expression locations
  examples:
  - description: The user can get an overview of the genes expressed in the planarian epidermis
    url: https://planosphere.stowers.org/ontology/PLANA_0000034
  user: https://planosphere.stowers.org/
activity_status: active
---

Anatomy ontology for planaria and terms specific to the developmental stages of the planarian __Schmidtea mediterranea__
