---
layout: ontology_detail
id: agro
title: Agronomy Ontology
contact:
  email: c.aubert@cgiar.org
  label: Celine Aubert
  github: celineaubert
description: Ontology of agronomic practices, agronomic techniques, and agronomic variables used in agronomic experiments
domain: agronomy
homepage: https://github.com/AgriculturalSemantics/agro
license:
  url: http://creativecommons.org/licenses/by/3.0/
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

---

AGRO, the AGRonomy Ontology, describes agronomic practices, agronomic techniques, and agronomic variables used in agronomic experiments. AGRO is being built using traits identified by agronomists, the ICASA variables, and other existing ontologies such as ENVO, UO, and PATO, IAO, and CHEBI. Further, AGRO will power an Agronomy Management System and fieldbook modeled on a CGIAR Breeding Management System to capture agronomic data. 

