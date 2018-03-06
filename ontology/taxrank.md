---
layout: ontology_detail
id: taxrank
contact:
  email: peteremidford@yahoo.com
  label: Peter Midford
description: A vocabulary of taxonomic ranks (species, family, phylum, etc)
domain: taxonomy
homepage: https://www.phenoscape.org/wiki/Taxonomic_Rank_Vocabulary
products:
  - id: taxrank.owl
  - id: taxrank.obo
title: Taxonomic rank vocabulary
jobs:
  - id: https://travis-ci.org/phenoscape/taxrank
    type: travis-ci
build:
  checkout: git clone https://github.com/phenoscape/taxrank.git
  system: git
  path: "."
tracker: https://github.com/phenoscape/taxrank/issues
license:
  url: http://creativecommons.org/publicdomain/zero/1.0/
  label: CC-0
---

A vocabulary of taxonomic ranks intended to replace the sets of rank terms found in the Teleost Taxonomy Ontology, the OBO translation of the NCBI taxonomy and similar OBO taxonomy ontologies.  It provides terms for taxonomic ranks drawn from both the NCBI taxonomy database and from a rank vocabulary developed for the TDWG biodiversity information standards group.  Cross references to appearances of each term in each source are provided.  Consistent with its intended use as a vocabulary of labels, there is no relation specifying an ordering of the rank terms.
