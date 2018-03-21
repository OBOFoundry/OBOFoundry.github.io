---
layout: ontology_detail
id: pato
in_foundry_order: 1
title: Phenotype And Trait Ontology
build:
  source_url: https://raw.githubusercontent.com/pato-ontology/pato/master/pato.obo
  method: obo2owl
  infallible: 1
description: An ontology of phenotypic qualities (properties, attributes or characteristics)
contact:
  email: g.gkoutos@gmail.com
  label: George Gkoutos
domain: phenotype
homepage: https://github.com/pato-ontology/pato/
repository: https://github.com/pato-ontology/pato/
browsers:
  - label: BioPortal
    title: BioPortal Ontology Browser
    url: https://bioportal.bioontology.org/ontologies/PATO
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
tracker: https://github.com/pato-ontology/pato/issues
jobs:
  - id: https://travis-ci.org/pato-ontology/pato
    type: travis-ci
products:
  - id: pato.owl
  - id: pato.obo
---

Phenotypic qualities (properties). This ontology can be used in conjunction with other ontologies such as GO or anatomical ontologies to refer to phenotypes. Examples of qualities are red, ectopic, high temperature, fused, small, edematous and arrested.
