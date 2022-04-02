---
layout: ontology_detail
id: ecto
title: Environmental conditions, treatments and exposures ontology
contact:
  email: annethessen@gmail.com
  github: diatomsRcool
  orcid: 0000-0002-2908-3327
  label: Anne Thessen
description: ECTO describes exposures to experimental treatments of plants and model organisms (e.g. exposures to modification of diet, lighting levels, temperature); exposures of humans or any other organisms to stressors through a variety of routes, for purposes of public health, environmental monitoring etc, stimuli, natural and experimental, any kind of environmental condition or change in condition that can be experienced by an organism or population of organisms on earth. The scope is very general and can include for example plant treatment regimens, as well as human clinical exposures (although these may better be handled by a more specialized ontology).
domain: environment
homepage: https://github.com/EnvironmentOntology/environmental-exposure-ontology
jobs:
  - id: https://travis-ci.org/EnvironmentOntology/environmental-exposure-ontology
    type: travis-ci
build:
  checkout: git clone https://github.com/EnvironmentOntology/environmental-exposure-ontology.git
  system: git
  path: "."
products:
  - id: ecto.owl
    name: "Environmental conditions, treatments and exposures ontology main release in OWL format"
  - id: ecto.obo
    name: "Environmental conditions, treatments and exposures ontology additional release in OBO format"
  - id: ecto.json
    name: "Environmental conditions, treatments and exposures ontology additional release in OBOJSon format"
  - id: ecto/ecto-base.owl
    name: "Environmental conditions, treatments and exposures ontology main release in OWL format"
  - id: ecto/ecto-base.obo
    name: "Environmental conditions, treatments and exposures ontology additional release in OBO format"
  - id: ecto/ecto-base.json
    name: "Environmental conditions, treatments and exposures ontology additional release in OBOJSon format"
dependencies:
  - id: chebi
  - id: envo
  - id: exo
  - id: go
  - id: iao
  - id: maxo
  - id: nbo
  - id: ncit
  - id: ncbitaxon
  - id: pato
  - id: ro
  - id: uberon
  - id: xco
tracker: https://github.com/EnvironmentOntology/environmental-exposure-ontology/issues
license:
  url: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
activity_status: active
repository: https://github.com/EnvironmentOntology/environmental-exposure-ontology
preferredPrefix: ECTO
depicted_by: https://raw.githubusercontent.com/jmcmurry/closed-illustrations/master/logos/ecto-logos/ecto-logo_black-banner.png
---
