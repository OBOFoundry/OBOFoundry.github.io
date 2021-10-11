---
layout: ontology_detail
id: agro
title: Agronomy Ontology
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY 4.0
domain: agronomy
build:
  checkout: git clone  https://github.com/AgriculturalSemantics/agro.git
  system: git
  path: "."
description: Ontology of agronomic practices, agronomic techniques, and agronomic variables used in agronomic experiments
homepage: https://github.com/AgriculturalSemantics/agro
contact:
  email: m.a.laporte@cgiar.org
  label: Marie-Angélique Laporte
  github: "marieALaporte"
products:
  - id: agro.owl
    title: "AgrO"
    description: "Contains all AgrO terms and links to other relavent ontologies."
    page: https://github.com/AgriculturalSemantics/agro/releases/tag/v2021-07-01
publications:
  - id: http://ceur-ws.org/Vol-1747/IT205_ICBO2016.pdf
    title: "Data-driven Agricultural Research for Development: A Need for Data Harmonization Via Semantics."
usages:
  - user: https://agrofims.org/about
    description: AgroFIMS enables digital collection of agronomic data that is semantically described a priori with agronomic terms from AgrO.
  - user: https://gardian.bigdata.cgiar.org/
    decription: AgrO is being used by GARDIAN to facilitate data search within publications and datasets for use in quantitative analyses.
jobs:
  - id: https://travis-ci.org/AgriculturalSemantics/agro
    type: travis-ci
tracker: https://github.com/AgriculturalSemantics/agro/issues/
activity_status: active
repository: https://github.com/AgriculturalSemantics/agro
dependencies:
  - id: envo
  - id: go
  - id: foodon
  - id: ncbitaxon
  - id: pato
  - id: peco
  - id: po
  - id: to
  - id: ro
  - id: bfo
  - id: iao
  - id: obi
  - id: uo
  - id: xco
---

AgrO, the Agronomy Ontology, describes agronomic practices, techniques, and variables used in agronomic experiments. AgrO is being built using traits identified by agronomists, the ICASA variables, and other existing ontologies such as ENVO, UO, PATO, IAO, and CHEBI. Further, AgrO powers AgroFIMS, the Agronomy Fieldbook and Information Management System modeled on a CGIAR Breeding Management System to capture agronomic data.
