---
layout: ontology_detail
id: mp
title: Mammalian phenotype
build:
  source_url: ftp://ftp.informatics.jax.org/pub/reports/MPheno_OBO.ontology
  method: obo2owl
  infallible: 1
description: Standard terms for annotating mammalian phenotypic data.
homepage: http://www.informatics.jax.org/searches/MP_form.shtml
page: https://github.com/obophenotype/mammalian-phenotype-ontology
contact:
  email: pheno@jax.org
  label: JAX phenotype list
domain: phenotype
products:
  - id: mp.owl
  - id: mp.obo
browsers:
  - label: MGI
    title: MGI MP Browser
    url: http://www.informatics.jax.org/searches/MP_form.shtml
  - label: Monarch
    title: Monarch Phenotype Page
    url: http://monarchinitiative.org/phenotype/MP:0000001
jobs:
  - id: http://build.berkeleybop.org/job/build-mp-edit
    type: DryRunBuild
taxon:
  id: NCBITaxon:10088
  label: Mus
tracker: https://github.com/obophenotype/mammalian-phenotype-ontology/issues
termgenie: http://mp.termgenie.org
---

The Mammalian Phenotype Ontology is under development as a community effort to provide standard terms for annotating mammalian phenotypic data.
