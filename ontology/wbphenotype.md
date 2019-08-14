---
layout: ontology_detail
id: wbphenotype
preferredPrefix: WBPhenotype
contact:
  email: cgrove@caltech.edu
  label: Chris Grove
license:
  url: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
description: A structured controlled vocabulary of <i>Caenorhabditis elegans</i> phenotypes
domain: phenotype
homepage: https://github.com/obophenotype/c-elegans-phenotype-ontology
products:
  - id: wbphenotype.owl
  - id: wbphenotype.obo
  - id: wbphenotype-base.owl
taxon:
  id: NCBITaxon:6237
  label: Caenorhabditis
title: C. elegans phenotype
build:
  checkout: git clone https://github.com/obophenotype/c-elegans-phenotype-ontology.git
  system: git
  path: "."
publications:
- id: http://www.ncbi.nlm.nih.gov/pubmed/?term=21261995
  title: "Worm Phenotype Ontology: integrating phenotype data within and beyond the C. elegans community."
usages:
 - user: https://monarchinitiative.org/
   type: annotation
   description: WBPhenotype is used by the Monarch Initiative for phenotype annotations.
   examples:
    - url: https://monarchinitiative.org/phenotype/WBPhenotype%3A0000370
   reference: https://academic.oup.com/nar/article/45/D1/D712/2605791
activity_status: active
---

A structured controlled vocabulary of <i>Caenorhabditis elegans</i> phenotypes
