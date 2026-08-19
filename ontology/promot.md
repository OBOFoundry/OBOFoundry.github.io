---
layout: ontology_detail
id: promot
title: PROMOT Ontology
jobs:
  - id: https://travis-ci.org/JuPoIm/promot
    type: travis-ci
build:
  checkout: git clone https://github.com/JuPoIm/promot.git
  system: git
  path: "."
contact:
  email: juliette.potier@institutimagine.org
  label: 
  github: https://github.com/JuPoIm/
description: PROMOT Ontology is an ontology that describes three groups of neuromuscular diseases, their related gene variants, phenotypes, and affected anatomical entities, body structures, body functions and activities.
domain: health
homepage: https://github.com/JuPoIm/promot
products:
  - id: promot-en.owl
    name: "PROMOT Ontology main release in OWL format (english version)"
  - id: promot-en.obo
    name: "PROMOT Ontology additional release in OBO format (english version)"
  - id: promot-en.json
    name: "PROMOT Ontology additional release in OBOJSon format (english version)"
  - id: promot-int.owl
    name: "PROMOT Ontology main release in OWL format (international version)"
  - id: promot-int.obo
    name: "PROMOT Ontology additional release in OBO format (international version)"
  - id: promot-int.json
    name: "PROMOT Ontology additional release in OBOJSon format (international version)"
  - id: promot/promot-base.owl
    name: "PROMOT Ontology main release in OWL format (english version)"
  - id: promot/promot-base.obo
    name: "PROMOT Ontology additional release in OBO format (english version)"
  - id: promot/promot-base.json
    name: "PROMOT Ontology additional release in OBOJSon format (english version)"
dependencies:
- id: bfo
- id: ordo
- id: fma
- id: hp
- id: icf
- id: snomed
- id: ro
- id: ncit
- id: obi
- id: eco
- id: iao
- id: so

tracker: https://github.com/JuPoIm/promot/issues
license:
  url: http://creativecommons.org/licenses/by/4.0/
  label: CC-BY-SA
activity_status: active
---

The PROMOT ontology represents three groups of neuromuscular diseases related to the 13 genes the PROMOT Master Observational Trial focuses on:

* Oculopharyngeal Muscular Dystrophy (_PABPN1_)
* Congenital Myasthenic Syndromes (_CHRNE_, _DOK7_, _COLQ_, _RAPSN_, _GFPT1_, _GMPPB_)
* Congenital Myopathies (_RYR1_, _TTN_, _NEB_, _MTM1_, _ACTA1_, _SELENON_)

This ontology describes the phenotypes associated to the diseases and genes. It also describes the affected anatomical entities, body structures, body functions, and activities.

Intended users are the experts from the PROMOT project but also anyone interested in neuromuscular diseases and their impacts on functioning and activities, such as the newly created NMDO project consortium.

The ontology relates to the following OBO ontologies: BFO, ECO, HP, IAO, NCIT, OBI, RO and SO.

The PROMOT ontology was built in the context of the "Performing a Rare Disease-Oriented Master Observational Trial" initiative (PROMOT initiative). It aims to be the conceptual schema for the PROMOT initiative common data model. This common data model is intended to collect and share in a federated infrastructure patient data scattered between the different sites involved in the master observational trial.

The international version of the ontology is available on [Bioportal](https://bioportal.bioontology.org/ontologies/PROMOT) under the same name.

