---
layout: ontology_detail
id: pso
title: Plant Stress Ontology
build:
  checkout: git clone https://github.com/Planteome/plant-stress-ontology.git
  path: .
  system: git
contact:
  email: cooperl@oregonstate.edu
  github: cooperl09
  label: Laurel Cooper
  orcid: 0000-0002-6379-8932
dependencies:
- id: ro
description: The Plant Stress Ontology describes biotic and abiotic stresses that a plant may encounter.
domain: agriculture
homepage: https://github.com/Planteome/plant-stress-ontology
jobs:
- id: https://travis-ci.org/Planteome/plant-stress-ontology
  type: travis-ci
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: PSO
products:
- id: pso.owl
- id: pso.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/29186578
  title: 'The Planteome database: an integrated resource for reference ontologies, plant genomics and phenomics.'
repository: https://github.com/Planteome/plant-stress-ontology
tags:
- plant disease
- abiotic stress
tracker: https://github.com/Planteome/plant-stress-ontology/issues
activity_status: active
---
