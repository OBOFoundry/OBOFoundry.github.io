---
layout: ontology_detail
id: poro
contact:
  email: robert.thacker@stonybrook.edu
  label: Bob Thacker
description: An ontology covering the anatomy of the taxon Porifera (sponges)
domain: anatomy
homepage: https://github.com/obophenotype/porifera-ontology
products:
  - id: poro.owl
taxon:
  id: NCBITaxon:6040
  label: Porifera
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
title: Porifera Ontology
dependencies:
 - id: uberon
 - id: ro
jobs:
  - id: https://travis-ci.org/obophenotype/porifera-ontology
    type: travis-ci
build:
  checkout: git clone https://github.com/obophenotype/porifera-ontology.git
  system: git
  path: .
  infallible: 1
  method: vcs
tracker: https://github.com/obophenotype/porifera-ontology/issues
---

An ontology covering the anatomy of Porifera (sponges)

![fig1](http://www.jbiomedsem.com/content/5/1/39/figure/F1?highres=y)
(figure from Boury-Esnault N, Rützler K: Thesaurus of Sponge Morphology. Washington: Smithsonian Institution Press; 1997)

## Citing ##

Thacker, R. W., Díaz, M. C., Kerner, A., Vignes-Lebbe, R., Segerdell, E., Haendel, M. a, & Mungall, C. J. (2014). [The Porifera Ontology (PORO): enhancing sponge systematics with an anatomy ontology](http://www.jbiomedsem.com/content/5/1/39/abstract). _Journal of Biomedical Semantics_, 5(1), 39. doi:10.1186/2041-1480-5-39

## Browse ##

The ontology can be browsed in [OntoBee](http://www.ontobee.org/browser/index.php?o=PORO)

Example entry points:

  * http://purl.obolibrary.org/obo/PORO_0000017 spicule
  * http://purl.obolibrary.org/obo/PORO_0000029 spongin

## Download ##

This ontology is available from

  * http://purl.obolibrary.org/obo/poro.owl
  * http://purl.obolibrary.org/obo/poro.obo
