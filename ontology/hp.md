---
layout: ontology_detail
id: hp
title: Human Phenotype Ontology
browsers:
- title: JAX HPO Browser
  label: HPO
  url: https://hpo.jax.org/app/
- title: Monarch Phenotype Page
  label: Monarch
  url: http://monarchinitiative.org/phenotype/HP:0000118
build:
  infallible: 1
  method: archive
  path: archive/hp
  source_url: http://compbio.charite.de/hudson/job/hpo/lastSuccessfulBuild/artifact/*zip*/archive.zip
contact:
  email: dr.sebastian.koehler@gmail.com
  github: drseb
  label: Sebastian Koehler
  orcid: 0000-0002-5316-1399
depicted_by: https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/logo/HPO-logo-black_small.png
description: A structured and controlled vocabulary for the phenotypic features encountered in human hereditary and other disease.
domain: phenotype
github_date_added: 2015-07-28
homepage: http://www.human-phenotype-ontology.org/
jobs:
- id: https://travis-ci.org/obophenotype/human-phenotype-ontology
  type: travis-ci
license:
  label: hpo
  url: https://hpo.jax.org/app/license
mailing_list: https://groups.io/g/human-phenotype-ontology
preferredPrefix: HP
products:
- id: hp.owl
- id: hp.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/18950739
  title: 'The Human Phenotype Ontology: a tool for annotating and analyzing human hereditary disease.'
- id: https://www.ncbi.nlm.nih.gov/pubmed/26119816
  title: 'The Human Phenotype Ontology: Semantic Unification of Common and Rare Disease.'
- id: https://www.ncbi.nlm.nih.gov/pubmed/24217912
  title: 'The Human Phenotype Ontology project: linking molecular biology and disease through phenotype data.'
- id: https://www.ncbi.nlm.nih.gov/pubmed/30476213
  title: Expansion of the Human Phenotype Ontology (HPO) knowledge base and resources.
repository: https://github.com/obophenotype/human-phenotype-ontology
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
tracker: https://github.com/obophenotype/human-phenotype-ontology/issues/
twitter: hp_ontology
usages:
- description: HPO is used by the Monarch Initiative for phenotype annotations.
  examples:
  - url: https://monarchinitiative.org/phenotype/HP:0001300
  reference: https://academic.oup.com/nar/article/45/D1/D712/2605791
  type: annotation
  user: https://monarchinitiative.org/
activity_status: active
---

An ontology is a computational representation of a domain of knowledge based upon a controlled, standardized vocabulary for describing entities and the semantic relationships between them.

The Human Phenotype Ontology (HPO) aims to provide a standardized vocabulary of phenotypic abnormalities encountered in human disease. Each term in the HPO describes a phenotypic abnormality, such as atrial septal defect. The HPO is currently being developed using the medical literature, Orphanet, DECIPHER, and OMIM.

The HPO can be browsed using:

 * [Main Browser](https://hpo.jax.org/)
 * [Monarch Browser](https://monarchinitiative.org/phenotype/HP:0000118)
