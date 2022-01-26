---
layout: ontology_detail
id: labo
title: clinical LABoratory Ontology
contact:
  email: paul.fabry@usherbrooke.ca
  label: Paul Fabry
  github: pfabry
description: LABO is an ontology of informational entities formalizing clinical laboratory tests prescriptions and reporting documents.
domain: clinical documentation
usages:
  - user: https://griis.ca/
    type: database architecture
    description: LABO is a part of a core ontological model of medical knowledge in the PARS3 data platform.
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
homepage: https://github.com/OpenLHS/LABO
tracker: https://github.com/OpenLHS/LABO/issues
releases: https://github.com/OpenLHS/LABO/releases/
dependencies:
  - id: iao
  - id: obi
  - id: ogms
  - id: omiabis
  - id: omrse
  - id: opmi
products:
  - id: labo.owl
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
activity_status: active
repository: https://github.com/OpenLHS/LABO
preferredPrefix: LABO
---

LABO is an ontology of informational entities describing laboratory tests prescriptions and reporting documents. LABO is a component of a core ontological model, along with the ontology of drug prescriptions PDRO, that aims to enable interoperability between various clinical data sources in the context of a Learning Health System.
