---
layout: ontology_detail
id: rbo
title: Radiation Biology Ontology
jobs:
  - id: https://travis-ci.org/DanBerrios/RBO
    type: travis-ci
build:
  checkout: git clone https://github.com/Radiobiology-Informatics-Consortium/RBO.git
  system: git
  path: "."
contact:
  email: daniel.c.berrios@nasa.gov
  label: Daniel C. Berrios
  github: DanBerrios
description: RBO is an ontology for the effects of radiation on biota in terrestrial and space environments.
domain: radiation biology, the study of the effects of radiation on biological systems
homepage: https://github.com/Radiobiology-Informatics-Consortium/RBO
products:
  - id: rbo.owl
    name: "Radiation Biology Ontology main release in OWL format"
  - id: rbo.obo
    name: "Radiation Biology Ontology additional release in OBO format"
  - id: rbo.json
    name: "Radiation Biology Ontology additional release in OBOJSon format"
  - id: rbo/rbo-base.owl
    name: "Radiation Biology Ontology main release in OWL format"
  - id: rbo/rbo-base.obo
    name: "Radiation Biology Ontology additional release in OBO format"
  - id: rbo/rbo-base.json
    name: "Radiation Biology Ontology additional release in OBOJSon format"
dependencies:
  - id: ro
  - id: bfo
  - id: pato
  - id: chmo
  - id: envo
  - id: obi
  - id: uo

tracker: https://github.com/Radiobiology-Informatics-Consortium/RBO/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
activity_status: active
repository: https://github.com/Radiobiology-Informatics-Consortium/RBO
---

The effects of all kinds of radiation on biological systems is the subject of much research, both on earth and in space environments.  This ontology is designed to support the needs of these investigators, particularly for organizing, describing and archiving data from experiments and observations examining these effects.  

See [Radiation Research](https://meridian.allenpress.com/radiation-research), [International Journal of Radiation Oncology, Biology, Physics](https://www.redjournal.org/) 

