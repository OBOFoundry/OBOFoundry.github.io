---
layout: ontology_detail
id: hp
alternativePrefix: HPO
description: A structured and controlled vocabulary for the phenotypic features encountered in human hereditary and other disease.
domain: phenotype
twitter: hp_ontology
homepage: http://www.human-phenotype-ontology.org/
contact:
  email: dr.sebastian.koehler@gmail.com
  label: Sebastian Koehler
  github: drseb
license:
  url: https://hpo.jax.org/app/license
  label: hpo
products:
  - id: hp.owl
  - id: hp.obo
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
title: Human Phenotype Ontology
jobs:
  - id: https://travis-ci.org/obophenotype/human-phenotype-ontology
    type: travis-ci
build:
  source_url: http://compbio.charite.de/hudson/job/hpo/lastSuccessfulBuild/artifact/*zip*/archive.zip
  path: archive/hp
  method: archive
  infallible: 1
tracker: https://github.com/obophenotype/human-phenotype-ontology/issues/
mailing_list: https://groups.google.com/forum/#!forum/phenotype-ontologies-editors
browsers:
  - label: HPO
    title: Charite HPO Browser
    url: http://www.human-phenotype-ontology.org/hpoweb/showterm?id=HP:0000118
  - label: Monarch
    title: Monarch Phenotype Page
    url: http://monarchinitiative.org/phenotype/HP:0000118
publications:
  - id: http://www.ncbi.nlm.nih.gov/pubmed/18950739
    title: "The Human Phenotype Ontology: a tool for annotating and analyzing human hereditary disease."
  - id: http://www.ncbi.nlm.nih.gov/pubmed/26119816
    title: "The Human Phenotype Ontology: Semantic Unification of Common and Rare Disease."
  - id: http://www.ncbi.nlm.nih.gov/pubmed/24217912
    title: "The Human Phenotype Ontology project: linking molecular biology and disease through phenotype data."
  - id: http://www.ncbi.nlm.nih.gov/pubmed/30476213
    title: "Expansion of the Human Phenotype Ontology (HPO) knowledge base and resources."
usages:
 - user: https://monarchinitiative.org/
   type: annotation
   description: HPO is used by the Monarch Initiative for phenotype annotations.
   examples:
    - url: https://monarchinitiative.org/phenotype/HP:0001300
   reference: https://academic.oup.com/nar/article/45/D1/D712/2605791
activity_status: active
---

<img src="http://human-phenotype-ontology.github.io/img/HPO-logo-stacked-black.png"/>

An ontology is a computational representation of a domain of knowledge based upon a controlled, standardized vocabulary for describing entities and the semantic relationships between them.

The Human Phenotype Ontology (HPO) aims to provide a standardized vocabulary of phenotypic abnormalities encountered in human disease. Each term in the HPO describes a phenotypic abnormality, such as atrial septal defect. The HPO is currently being developed using the medical literature, Orphanet, DECIPHER, and OMIM.

The HPO can be browsed using:

 * [Main Browser](https://hpo.jax.org/)
 * [HPO Browser](http://www.human-phenotype-ontology.org/hpoweb/showterm?id=HP:0000118)
 * [Monarch Browser](https://monarchinitiative.org/phenotype/HP:0000118)
