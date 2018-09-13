---
layout: ontology_detail
id: mp
title: Mammalian Phenotype
license:
  url: http://creativecommons.org/licenses/by/4.0/
  label: CC-BY 4.0
build:
  source_url: http://build.berkeleybop.org/job/build-mp-edit/lastSuccessfulBuild/artifact/*zip*/archive.zip
  path: archive/src/ontology
  method: archive
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
  - label: RGD
    title: RGD MP Browser
    url: https://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=MP:0000001
  - label: Monarch
    title: Monarch Phenotype Page
    url: http://monarchinitiative.org/phenotype/MP:0000001
jobs:
  - id: http://build.berkeleybop.org/job/build-mp-edit
    type: DryRunBuild
taxon:
  id: NCBITaxon:40674
  label: Mammalia
tracker: https://github.com/obophenotype/mammalian-phenotype-ontology/issues
mailing_list: Phenotype editors mailing list: https://groups.google.com/forum/#!forum/phenotype-ontologies-editors
---

The Mammalian Phenotype Ontology is under development as a community effort to provide standard terms for annotating mammalian phenotypic data.
