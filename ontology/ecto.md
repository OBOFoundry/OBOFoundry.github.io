---
layout: ontology_detail
id: ecto
title: Environmental conditions, treatments and exposures ontology
build:
  checkout: git clone https://github.com/EnvironmentOntology/environmental-exposure-ontology.git
  path: .
  system: git
contact:
  email: annethessen@gmail.com
  github: diatomsRcool
  label: Anne Thessen
  orcid: 0000-0002-2908-3327
dependencies:
- id: chebi
- id: envo
- id: exo
- id: go
- id: iao
- id: maxo
- id: nbo
- id: ncbitaxon
- id: ncit
- id: pato
- id: ro
- id: uberon
- id: xco
depicted_by: https://raw.githubusercontent.com/jmcmurry/closed-illustrations/master/logos/ecto-logos/ecto-logo_black-banner.png
description: ECTO describes exposures to experimental treatments of plants and model organisms (e.g. exposures to modification of diet, lighting levels, temperature); exposures of humans or any other organisms to stressors through a variety of routes, for purposes of public health, environmental monitoring etc, stimuli, natural and experimental, any kind of environmental condition or change in condition that can be experienced by an organism or population of organisms on earth. The scope is very general and can include for example plant treatment regimens, as well as human clinical exposures (although these may better be handled by a more specialized ontology).
domain: environment
github_date_added: 2019-09-24
homepage: https://github.com/EnvironmentOntology/environmental-exposure-ontology
jobs:
- id: https://travis-ci.org/EnvironmentOntology/environmental-exposure-ontology
  type: travis-ci
license:
  label: CC0 1.0
  url: https://creativecommons.org/publicdomain/zero/1.0/
preferredPrefix: ECTO
products:
- id: ecto.owl
  name: Environmental conditions, treatments and exposures ontology main release in OWL format
- id: ecto.obo
  name: Environmental conditions, treatments and exposures ontology additional release in OBO format
- id: ecto.json
  name: Environmental conditions, treatments and exposures ontology additional release in OBOJSon format
- id: ecto/ecto-base.owl
  name: Environmental conditions, treatments and exposures ontology main release in OWL format
- id: ecto/ecto-base.obo
  name: Environmental conditions, treatments and exposures ontology additional release in OBO format
- id: ecto/ecto-base.json
  name: Environmental conditions, treatments and exposures ontology additional release in OBOJSon format
repository: https://github.com/EnvironmentOntology/environmental-exposure-ontology
tracker: https://github.com/EnvironmentOntology/environmental-exposure-ontology/issues
activity_status: active
---
