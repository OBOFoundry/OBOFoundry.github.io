---
layout: ontology_detail
id: poro
title: Porifera Ontology
build:
  checkout: git clone https://github.com/obophenotype/porifera-ontology.git
  infallible: 1
  method: vcs
  path: .
  system: git
contact:
  email: robert.thacker@stonybrook.edu
  github: bobthacker
  label: Bob Thacker
  orcid: 0000-0002-9654-0073
dependencies:
- id: ro
- id: uberon
description: An ontology covering the anatomy of the taxon Porifera (sponges)
domain: anatomy and development
homepage: https://github.com/obophenotype/porifera-ontology
jobs:
- id: https://travis-ci.org/obophenotype/porifera-ontology
  type: travis-ci
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: PORO
products:
- id: poro.owl
- id: poro.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/25276334
  title: 'The Porifera Ontology (PORO): enhancing sponge systematics with an anatomy ontology'
repository: https://github.com/obophenotype/porifera-ontology
taxon:
  id: NCBITaxon:6040
  label: Porifera
tracker: https://github.com/obophenotype/porifera-ontology/issues
activity_status: active
---

An ontology covering the anatomy of Porifera (sponges)

![fig1](http://www.jbiomedsem.com/content/5/1/39/figure/F1?highres=y)
(figure from Boury-Esnault N, Rützler K: Thesaurus of Sponge Morphology. Washington: Smithsonian Institution Press; 1997)

## Browse ##

The ontology can be browsed in [OntoBee](http://www.ontobee.org/browser/index.php?o=PORO)

Example entry points:

  * http://purl.obolibrary.org/obo/PORO_0000017 spicule
  * http://purl.obolibrary.org/obo/PORO_0000029 spongin

## Download ##

This ontology is available from

  * http://purl.obolibrary.org/obo/poro.owl
  * http://purl.obolibrary.org/obo/poro.obo
