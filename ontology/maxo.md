---
layout: ontology_detail
id: maxo
title: Medical Action Ontology
jobs:
  - id: https://travis-ci.org/monarch-initiative/MAxO
    type: travis-ci
build:
  checkout: git clone https://github.com/monarch-initiative/MAxO.git
  system: git
  path: "."
contact:
  email: Leigh.Carmody@jax.org
  label: Leigh Carmody
  github: LCCarmody
  orcid: 0000-0001-7941-2961
description: Medical Action Ontology is an ontology...
domain: health
tags:
  - medical
homepage: https://github.com/monarch-initiative/MAxO
products:
  - id: maxo.owl
    name: "Medical Action Ontology main release in OWL format"
  - id: maxo.obo
    name: "Medical Action Ontology additional release in OBO format"
  - id: maxo.json
    name: "Medical Action Ontology additional release in OBOJSon format"
  - id: maxo/maxo-base.owl
    name: "Medical Action Ontology main release in OWL format"
  - id: maxo/maxo-base.obo
    name: "Medical Action Ontology additional release in OBO format"
  - id: maxo/maxo-base.json
    name: "Medical Action Ontology additional release in OBOJSon format"
dependencies:
  - id: iao
  - id: go
  - id: ro
  - id: uberon
  - id: foodon
  - id: chebi

tracker: https://github.com/monarch-initiative/MAxO/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
activity_status: active
repository: https://github.com/monarch-initiative/MAxO
preferredPrefix: MAXO
depicted_by: https://raw.githubusercontent.com/jmcmurry/closed-illustrations/master/logos/maxo-logos/maxo_logo_black-banner.png
---

The Medical Action Ontology (MAxO) provides a structured vocabulary for medical procedures, interventions, therapies, and treatments for disease with an emphasis on rare disease (RD). It is often difficult to find relevant clinical literature about strategies to manage RD patients. Responding to this need, MAxO provides a vocabulary to annotate diseases and phenotypes with recommended treatments and interventions.
