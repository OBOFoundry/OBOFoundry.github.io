---
layout: ontology_detail
id: maxo
title: Medical Action Ontology
build:
  checkout: git clone https://github.com/monarch-initiative/MAxO.git
  path: .
  system: git
contact:
  email: Leigh.Carmody@jax.org
  github: LCCarmody
  label: Leigh Carmody
  orcid: 0000-0001-7941-2961
dependencies:
- id: chebi
- id: foodon
- id: go
- id: iao
- id: ro
- id: uberon
depicted_by: https://raw.githubusercontent.com/jmcmurry/closed-illustrations/master/logos/maxo-logos/maxo_logo_black-banner.png
description: Medical Action Ontology is an ontology...
domain: health
homepage: https://github.com/monarch-initiative/MAxO
jobs:
- id: https://travis-ci.org/monarch-initiative/MAxO
  type: travis-ci
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: MAXO
products:
- id: maxo.owl
  name: Medical Action Ontology main release in OWL format
- id: maxo.obo
  name: Medical Action Ontology additional release in OBO format
- id: maxo.json
  name: Medical Action Ontology additional release in OBOJSon format
- id: maxo/maxo-base.owl
  name: Medical Action Ontology main release in OWL format
- id: maxo/maxo-base.obo
  name: Medical Action Ontology additional release in OBO format
- id: maxo/maxo-base.json
  name: Medical Action Ontology additional release in OBOJSon format
repository: https://github.com/monarch-initiative/MAxO
tags:
- medical
tracker: https://github.com/monarch-initiative/MAxO/issues
activity_status: active
---

The Medical Action Ontology (MAxO) provides a structured vocabulary for medical procedures, interventions, therapies, and treatments for disease with an emphasis on rare disease (RD). It is often difficult to find relevant clinical literature about strategies to manage RD patients. Responding to this need, MAxO provides a vocabulary to annotate diseases and phenotypes with recommended treatments and interventions.
