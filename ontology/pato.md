---
layout: ontology_detail
id: pato
title: Phenotype And Trait Ontology
browsers:
- title: BioPortal Ontology Browser
  label: BioPortal
  url: https://bioportal.bioontology.org/ontologies/PATO
contact:
  email: g.gkoutos@gmail.com
  github: gkoutos
  label: George Gkoutos
  orcid: 0000-0002-2061-091X
description: An ontology of phenotypic qualities (properties, attributes or characteristics)
domain: phenotype
homepage: https://github.com/pato-ontology/pato/
in_foundry_order: 1
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: PATO
products:
- id: pato.owl
- id: pato.obo
- id: pato.json
- id: pato/pato-base.owl
  description: Includes axioms linking to other ontologies, but no imports of those ontologies
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/28387809
  title: 'The anatomy of phenotype ontologies: principles, properties and applications'
- id: https://www.ncbi.nlm.nih.gov/pubmed/15642100
  title: Using ontologies to describe mouse phenotypes
repository: https://github.com/pato-ontology/pato
tracker: https://github.com/pato-ontology/pato/issues
usages:
- description: PATO is used by the Human Phenotype Ontology (HPO) for logical definitions of phenotypes that facilitate cross-species integration.
  examples:
  - description: An abnormality in a cellular process.
    url: https://www.ebi.ac.uk/ols/ontologies/hp/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FHP_0011017&viewMode=All&siblings=false
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/30476213
    title: Expansion of the Human Phenotype Ontology (HPO) knowledge base and resources
  type: annotation
  user: https://hpo.jax.org/app/
activity_status: active
---

Phenotypic qualities (properties). This ontology can be used in conjunction with other ontologies such as GO or anatomical ontologies to refer to phenotypes. Examples of qualities are red, ectopic, high temperature, fused, small, edematous and arrested.
