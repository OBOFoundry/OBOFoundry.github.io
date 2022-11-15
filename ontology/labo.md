---
layout: ontology_detail
id: labo
title: clinical LABoratory Ontology
contact:
  email: paul.fabry@usherbrooke.ca
  github: pfabry
  label: Paul Fabry
  orcid: 0000-0002-3336-2476
dependencies:
- id: iao
- id: obi
- id: ogms
- id: omiabis
- id: omrse
- id: opmi
description: LABO is an ontology of informational entities formalizing clinical laboratory tests prescriptions and reporting documents.
domain: information
github_date_added: 2019-08-29
homepage: https://github.com/OpenLHS/LABO
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: LABO
products:
- id: labo.owl
publications:
- id: https://doi.org/10.5281/zenodo.6522019
  title: 'LABO: An Ontology for Laboratory Test Prescription and Reporting'
releases: https://github.com/OpenLHS/LABO/releases/
repository: https://github.com/OpenLHS/LABO
tags:
- clinical documentation
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
tracker: https://github.com/OpenLHS/LABO/issues
usages:
- description: LABO is a part of a core ontological model of medical knowledge in the PARS3 data platform.
  type: database architecture
  user: https://griis.ca/
activity_status: active
---

LABO is an ontology of informational entities describing laboratory tests prescriptions and reporting documents. LABO is a component of a core ontological model, along with the ontology of drug prescriptions PDRO, that aims to enable interoperability between various clinical data sources in the context of a Learning Health System.
