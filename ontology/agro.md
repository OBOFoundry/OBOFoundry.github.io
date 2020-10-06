---
layout: ontology_detail
id: agro
title: Agronomy Ontology
contact:
  email: m.a.laporte@cgiar.org
  label: Marie-Angélique Laporte
  github: marieALaporte
description: Ontology of agronomic practices, agronomic techniques, and agronomic variables used in agronomic experiments
domain: agronomy
homepage: https://github.com/AgriculturalSemantics/agro
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY
mailing_list: https://groups.google.com/group/agronomyOntology
products:
  - id: agro.owl
dependencies:
 - id: envo
 - id: uo
 - id: ro
 - id: pato
 - id: chebi
 - id: iao
 - id: ncbitaxon
 - id: po
 - id: peco
jobs:
  - id: https://travis-ci.org/AgriculturalSemantics/agro
    type: travis-ci
build:
  checkout: git clone  https://github.com/AgriculturalSemantics/agro.git
  system: git
  path: .
  method: vcs
  infallible: 1
tracker: https://github.com/AgriculturalSemantics/agro/issues/
activity_status: active
---

AgrO, the Agronomy Ontology, describes agronomic practices, techniques, and variables used in agronomic experiments. AgrO is being built using traits identified by agronomists, the ICASA variables, and other existing ontologies such as ENVO, UO, PATO, IAO, and CHEBI. Further, AgrO powers AgroFIMS, the Agronomy Fieldbook and Information Management System modeled on a CGIAR Breeding Management System to capture agronomic data.

