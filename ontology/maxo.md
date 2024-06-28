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
- id: hp
- id: iao
- id: nbo
- id: obi
- id: ro
- id: uberon
depicted_by: https://raw.githubusercontent.com/jmcmurry/closed-illustrations/master/logos/maxo-logos/maxo_logo_black-banner.png
description: The Medical Action Ontology (MAxO) provides a broad view of medical actions and includes terms for medical procedures, interventions, therapies, treatments, and recommendations.
domain: health
homepage: https://github.com/monarch-initiative/MAxO
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
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
usages:
- description: MAxO is used to capture disease-treatment relations from the scientific literature.
  examples:
  - description: 'Bardet-biedl Syndrome 1 (MONDO:0008854) is treated through dietary interventions (MAXO:0000088) according to Forsyth et al 2003 (PMID:20301537)'
    url: https://hpo.jax.org/data/annotations
  type: annotation
  user: https://hpo.jax.org/
activity_status: active
---
