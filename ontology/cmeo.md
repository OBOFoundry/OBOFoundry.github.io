---
layout: ontology_detail
id: cmeo
title: Clinical Metadata Exploration Ontology
contact:
  email: komalsyeda29@gmail.com
  github: komi786
  label: Komal Gilani
  orcid: 0000-0001-7292-1026
description: CMEO (Clinical Metadata Exploration Ontology) is a semantic model for representing and querying clinical cohort study metadata to support cross-study discovery and metadata-driven harmonization.
domain: health
homepage: https://komi786.github.io/cmeo/
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: CMEO
products:
- id: cmeo.owl
  title: CMEO main release
publications:
- id: https://doi.org/10.1186/s12911-025-03272-5
  title: 'CMEO: a metadata-centric ontology for clinical studies exploration and harmonization assessment'
repository: https://github.com/komi786/cmeo
tracker: https://github.com/komi786/cmeo/issues
activity_status: active
---

CMEO describes the metadata of clinical studies: study design and protocol, eligibility criteria, outcomes, the variables collected and how they are specified (data type, units, codes, visits, missing values), and data access and use conditions. Each study can be represented as a knowledge graph, so that variables and study designs can be compared and harmonized across studies. CMEO reuses BFO, IAO, OBI, OBCS, STATO, RO, DUO and other OBO ontologies.
