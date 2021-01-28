---
layout: ontology_detail
id: rbo
title: Radiation Biology Ontology
build:
  checkout: git clone https://github.com/DanBerrios/RBO.git
  system: git
  path: "."
contact:
  email: daniel.c.berrios@nasa.gov
  label: Daniel C. Berrios
  github: https://github.com/DanBerrios
description: The RBO is an ontology about Radiation Biology, with emphasis on Space Biology.
domain: radiation biology, the study of the effects of radiation on biological systems
homepage: https://github.com/DanBerrios/RBO
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

tracker: https://github.com/DanBerrios/RBO/issues
license:
  url: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0
activity_status: active
---

The effects of all kinds of radiation on biological systems is the subject of much research, both on earth and in space environments.  This ontology is designed to support the needs of these investigators, particularly for organizing, describing and archiving data from experiments and observations examining these effects.  

See [Radiation Research](https://meridian.allenpress.com/radiation-research), [International Journal of Radiation Oncology, Biology, Physics](https://www.redjournal.org/) 

