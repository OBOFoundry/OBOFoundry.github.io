---
layout: ontology_detail
id: plana
title: planaria-ontology
jobs:
  - id: https://travis-ci.org/obophenotype/planaria-ontology
    type: travis-ci
build:
  checkout: git clone https://github.com/obophenotype/planaria-ontology.git
  system: git
  path: "."
contact:
  email: smr@stowers.org
  label: Sofia Robb
  github: srobb1
  orcid: 0000-0002-3528-5267
publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/34318308
    title: "Planarian Anatomy Ontology: a resource to connect data within and across experimental platforms"
description: PLANA, the planarian anatomy ontology, encompasses the anatomy and life cycle stages for both __Schmidtea mediterranea__ biotypes.
domain: anatomy and development
homepage: https://github.com/obophenotype/planaria-ontology
products:
  - id: plana.owl
  - id: plana.obo
dependencies:
  - id: ro
  - id: uberon
usages:
  - user: https://planosphere.stowers.org/
    description: Planosphere's PAGE database uses PLANA to annotate gene expression locations
    examples:
      - url: https://planosphere.stowers.org/ontology/PLANA_0000034
        description: "The user can get an overview of the genes expressed in the planarian epidermis"
tracker: https://github.com/obophenotype/planaria-ontology/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
activity_status: active
repository: https://github.com/obophenotype/planaria-ontology
preferredPrefix: PLANA
github_date_added: 2017-02-07
---

Anatomy ontology for planaria and terms specific to the developmental stages of the planarian __Schmidtea mediterranea__
