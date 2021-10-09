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
usages: 
  - user: AgroFIMS
    description: A key use case for AgrO is the Agronomy Field Information Management System (AgroFIMS). AgroFIMS enables digital collection of agronomic data that is semantically described a priori with agronomic terms from AgrO.
      - url: https://agrofims.org/about
  - user: Agricultural Model Intercomparison and Improvement Project (AgMIP)
    decription: AgrO is being used by the University of Florida (UF), and researchers associated with the Agricultural Model Intercomparison and Improvement Project (AgMIP) and IFPRI as a standard reference terminology to enable the generation and reuse of model-ready data. The goal of this effort is to facilitate data queries in GARDIAN that include a measure of the appropriateness of each dataset for use in quantitative analyses. Each dataset will include metadata that fully describe the terminology used in that dataset with links to AgrO definitions and units.
      - url: https://bigdata.cgiar.org/resources/gardian/
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
repository: https://github.com/AgriculturalSemantics/agro
---

AgrO, the Agronomy Ontology, describes agronomic practices, techniques, and variables used in agronomic experiments. AgrO is being built using traits identified by agronomists, the ICASA variables, and other existing ontologies such as ENVO, UO, PATO, IAO, and CHEBI. Further, AgrO powers AgroFIMS, the Agronomy Fieldbook and Information Management System modeled on a CGIAR Breeding Management System to capture agronomic data.
