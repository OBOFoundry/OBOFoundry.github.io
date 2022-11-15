---
layout: ontology_detail
id: rbo
title: Radiation Biology Ontology
build:
  checkout: git clone https://github.com/Radiobiology-Informatics-Consortium/RBO.git
  path: .
  system: git
contact:
  email: daniel.c.berrios@nasa.gov
  github: DanBerrios
  label: Daniel C. Berrios
  orcid: 0000-0003-4312-9552
dependencies:
- id: bfo
- id: chmo
- id: envo
- id: obi
- id: pato
- id: ro
- id: uo
description: RBO is an ontology for the effects of radiation on biota in terrestrial and space environments.
domain: environment
github_date_added: 2021-01-28
homepage: https://github.com/Radiobiology-Informatics-Consortium/RBO
jobs:
- id: https://travis-ci.org/DanBerrios/RBO
  type: travis-ci
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: RBO
products:
- id: rbo.owl
  name: Radiation Biology Ontology main release in OWL format
- id: rbo.obo
  name: Radiation Biology Ontology additional release in OBO format
- id: rbo.json
  name: Radiation Biology Ontology additional release in OBOJSon format
- id: rbo/rbo-base.owl
  name: Radiation Biology Ontology main release in OWL format
- id: rbo/rbo-base.obo
  name: Radiation Biology Ontology additional release in OBO format
- id: rbo/rbo-base.json
  name: Radiation Biology Ontology additional release in OBOJSon format
repository: https://github.com/Radiobiology-Informatics-Consortium/RBO
tags:
- radiation biology
tracker: https://github.com/Radiobiology-Informatics-Consortium/RBO/issues
activity_status: active
---

The effects of all kinds of radiation on biological systems is the subject of much research, both on earth and in space environments.  This ontology is designed to support the needs of these investigators, particularly for organizing, describing and archiving data from experiments and observations examining these effects.  

See [Radiation Research](https://meridian.allenpress.com/radiation-research), [International Journal of Radiation Oncology, Biology, Physics](https://www.redjournal.org/) 

