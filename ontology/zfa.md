---
layout: ontology_detail
id: zfa
title: Zebrafish anatomy and development ontology
build:
  infallible: 1
  method: obo2owl
  notes: may be ready to switch to vcs soon
  source_url: https://raw.githubusercontent.com/cerivs/zebrafish-anatomical-ontology/master/src/zebrafish_anatomy.obo
contact:
  email: van_slyke@zfin.org
  github: cerivs
  label: Ceri Van Slyke
  orcid: 0000-0002-2244-7917
description: A structured controlled vocabulary of the anatomy and development of the Zebrafish
domain: anatomy and development
homepage: https://wiki.zfin.org/display/general/Anatomy+Atlases+and+Resources
in_foundry_order: 1
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: ZFA
products:
- id: zfa.owl
- id: zfa.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/24568621
  title: 'The zebrafish anatomy and stage ontologies: representing the anatomy and development of Danio rerio.'
repository: https://github.com/cerivs/zebrafish-anatomical-ontology
review:
  date: 2010
taxon:
  id: NCBITaxon:7954
  label: Danio
tracker: https://github.com/cerivs/zebrafish-anatomical-ontology/issues
usages:
- description: ZFIN uses ZFA to annotate gene expression and phenotype
  examples:
  - description: zebrafish genes expressed in hindbrain and genotypes with hindbrain phenotype
    url: http://zfin.org/ZFA:0000029
  user: http://zfin.org
activity_status: active
---

A structured controlled vocabulary of the anatomy and development of the Zebrafish (<i>Danio rerio</i>).
