---
layout: ontology_detail
id: taxrank
title: Taxonomic rank vocabulary
build:
  checkout: git clone https://github.com/phenoscape/taxrank.git
  path: .
  system: git
contact:
  email: balhoff@renci.org
  github: balhoff
  label: Jim Balhoff
  orcid: 0000-0002-8688-6599
description: A vocabulary of taxonomic ranks (species, family, phylum, etc)
domain: organisms
homepage: https://github.com/phenoscape/taxrank
jobs:
- id: https://travis-ci.org/phenoscape/taxrank
  type: travis-ci
license:
  label: CC0 1.0
  url: http://creativecommons.org/publicdomain/zero/1.0/
preferredPrefix: TAXRANK
products:
- id: taxrank.owl
- id: taxrank.obo
publications:
- id: https://doi.org/10.1186/2041-1480-4-34
  title: 'The vertebrate taxonomy ontology: a framework for reasoning across model organism and species phenotypes'
repository: https://github.com/phenoscape/taxrank
tags:
- taxonomy
tracker: https://github.com/phenoscape/taxrank/issues
activity_status: active
---

A vocabulary of taxonomic ranks intended to replace the sets of rank terms found in the Teleost Taxonomy Ontology, the OBO translation of the NCBI taxonomy and similar OBO taxonomy ontologies.  It provides terms for taxonomic ranks drawn from both the NCBI taxonomy database and from a rank vocabulary developed for the TDWG biodiversity information standards group.  Cross references to appearances of each term in each source are provided.  Consistent with its intended use as a vocabulary of labels, there is no relation specifying an ordering of the rank terms.
