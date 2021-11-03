---
layout: ontology_detail
id: pato
in_foundry_order: 1
title: Phenotype And Trait Ontology
review:
  date: 2010
build:
  source_url: https://raw.githubusercontent.com/pato-ontology/pato/master/pato.obo
  method: obo2owl
  infallible: 1
description: An ontology of phenotypic qualities (properties, attributes or characteristics)
contact:
  email: g.gkoutos@gmail.com
  label: George Gkoutos
  github: gkoutos
domain: phenotype
homepage: https://github.com/pato-ontology/pato/
repository: https://github.com/pato-ontology/pato/
browsers:
  - label: BioPortal
    title: BioPortal Ontology Browser
    url: https://bioportal.bioontology.org/ontologies/PATO
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
tracker: https://github.com/pato-ontology/pato/issues
jobs:
  - id: https://travis-ci.org/pato-ontology/pato
    type: travis-ci
products:
  - id: pato.owl
  - id: pato.obo
  - id: pato.json
  - id: pato/pato-base.owl
    description: "Includes axioms linking to other ontologies, but no imports of those ontologies"
usages:
  - user: https://hpo.jax.org/app/
    type: annotation
    description: PATO is used by the Human Phenotype Ontology (HPO) for logical definitions of phenotypes that facilitate cross-species integration.
    examples:
      - url: https://www.ebi.ac.uk/ols/ontologies/hp/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FHP_0011017&viewMode=All&siblings=false
        description: An abnormality in a cellular process.
    publications:
      - id: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6324074/
        title: "Expansion of the Human Phenotype Ontology (HPO) knowledge base and resources"
activity_status: active
preferredPrefix: PATO
---

Phenotypic qualities (properties). This ontology can be used in conjunction with other ontologies such as GO or anatomical ontologies to refer to phenotypes. Examples of qualities are red, ectopic, high temperature, fused, small, edematous and arrested.
