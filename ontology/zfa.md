---
layout: ontology_detail
id: zfa
in_foundry_order: 1
contact:
  email: van_slyke@zfin.org
  label: Ceri Van Slyke
  github: cerivs
description: A structured controlled vocabulary of the anatomy and development of the Zebrafish
domain: anatomy
homepage: https://wiki.zfin.org/display/general/Anatomy+Atlases+and+Resources
products:
  - id: zfa.owl
  - id: zfa.obo
taxon:
  id: NCBITaxon:7954
  label: Danio
title: Zebrafish anatomy and development ontology
review:
  date: 2010
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
build:
  notes: may be ready to switch to vcs soon
  source_url: https://raw.githubusercontent.com/cerivs/zebrafish-anatomical-ontology/master/src/zebrafish_anatomy.obo
  method: obo2owl
  infallible: 1
tracker: https://github.com/cerivs/zebrafish-anatomical-ontology/issues
publications:
  - id: http://www.ncbi.nlm.nih.gov/pubmed/24568621
    title: "The zebrafish anatomy and stage ontologies: representing the anatomy and development of Danio rerio."
usages:
  - user: http://zfin.org
    description: ZFIN uses ZFA to annotate gene expression and phenotype
    examples:
      - url: http://zfin.org/ZFA:0000029
        description: zebrafish genes expressed in hindbrain and genotypes with hindbrain phenotype
activity_status: active
---

A structured controlled vocabulary of the anatomy and development of the Zebrafish (<i>Danio rerio</i>).
