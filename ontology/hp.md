---
layout: ontology_detail
id: hp
alternativePrefix: HPO
description: A structured and controlled vocabulary for the phenotypic features encountered in human hereditary and other disease.
domain: phenotype
twitter: hp_ontology
homepage: http://www.human-phenotype-ontology.org/
contact:
  email: sebastian.koehler@charite.de
  label: Sebastian Koehler
products:
  - id: hp.owl
  - id: hp.obo
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
title: human phenotype ontology
jobs:
  - id: https://travis-ci.org/obophenotype/human-phenotype-ontology
    type: travis-ci
build:
  source_url: http://compbio.charite.de/hudson/job/hpo/lastSuccessfulBuild/artifact/*zip*/archive.zip
  path: archive/hp
  method: archive
  infallible: 1
tracker: https://github.com/obophenotype/human-phenotype-ontology/issues/
termgenie: http://hp.termgenie.org
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
---

<img src="http://www.human-phenotype-ontology.org/contao/tl_files/simplifyblue/images/HPO-logo.png"/>

The Human Phenotype Ontology is being developed to provide a structured and controlled vocabulary for the phenotypic features encountered in human hereditary and other disease. Our goal is to provide resource for the computational analysis of the human phenome, with a current focus on monogenic diseases listed in the Online Mendelian Inheritance in Man (OMIM) database, for which annotations are also provided.

The HPO can be browsed using:

 * [HPO Browser](http://www.human-phenotype-ontology.org/hpoweb/showterm?id=HP:0000118)
