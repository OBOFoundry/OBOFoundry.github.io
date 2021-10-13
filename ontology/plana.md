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
description: PLANA, the planarian anatomy ontology, encompasses the anatomy and life cycle stages for both __Schmidtea mediterranea__ biotypes.
domain: anatomy
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
  label: CC-BY
activity_status: active
repository: https://github.com/obophenotype/planaria-ontology
preferredPrefix: PLANA
---

Anatomy ontology for planaria and terms specific to the developmental stages of the planarian __Schmidtea mediterranea__
