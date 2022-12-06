---
layout: ontology_detail
id: agro
title: Agronomy Ontology
build:
  checkout: git clone  https://github.com/AgriculturalSemantics/agro.git
  path: .
  system: git
contact:
  email: m.a.laporte@cgiar.org
  github: marieALaporte
  label: Marie-Angélique Laporte
  orcid: 0000-0002-8461-9745
dependencies:
- id: bfo
- id: envo
- id: foodon
- id: go
- id: iao
- id: ncbitaxon
- id: obi
- id: pato
- id: peco
- id: po
- id: ro
- id: to
- id: uo
- id: xco
description: Ontology of agronomic practices, agronomic techniques, and agronomic variables used in agronomic experiments
domain: agriculture
homepage: https://github.com/AgriculturalSemantics/agro
jobs:
- id: https://travis-ci.org/AgriculturalSemantics/agro
  type: travis-ci
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: AGRO
products:
- id: agro.owl
  title: AgrO
  description: Contains all AgrO terms and links to other relavent ontologies.
publications:
- id: http://ceur-ws.org/Vol-1747/IT205_ICBO2016.pdf
  title: 'Data-driven Agricultural Research for Development: A Need for Data Harmonization Via Semantics.'
repository: https://github.com/AgriculturalSemantics/agro
tags:
- agronomy
tracker: https://github.com/AgriculturalSemantics/agro/issues/
usages:
- description: AgroFIMS enables digital collection of agronomic data that is semantically described a priori with agronomic terms from AgrO.
  user: https://agrofims.org/about
- description: AgrO is being used by GARDIAN to facilitate data search within publications and datasets for use in quantitative analyses.
  user: https://gardian.bigdata.cgiar.org/
activity_status: active
---

AgrO, the Agronomy Ontology, describes agronomic practices, techniques, and variables used in agronomic experiments. AgrO is being built using traits identified by agronomists, the ICASA variables, and other existing ontologies such as ENVO, UO, PATO, IAO, and CHEBI. Further, AgrO powers AgroFIMS, the Agronomy Fieldbook and Information Management System modeled on a CGIAR Breeding Management System to capture agronomic data.
