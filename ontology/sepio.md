---
layout: ontology_detail
id: sepio
title: Scientific Evidence and Provenance Information Ontology
build:
  checkout: git clone https://github.com/monarch-initiative/SEPIO-ontology.git
  path: src/ontology
  system: git
contact:
  email: mhb120@gmail.com
  github: mbrush
  label: Matthew Brush
  orcid: 0000-0002-1048-5019
depicted_by: https://raw.githubusercontent.com/jmcmurry/closed-illustrations/master/logos/SEPIO-LOGOS/sepio_logo_black-banner.png
description: An ontology for representing the provenance of scientific claims and the evidence that supports them.
domain: investigations
github_date_added: 2017-06-30
homepage: https://github.com/monarch-initiative/SEPIO-ontology
license:
  label: CC BY 3.0
  url: https://creativecommons.org/licenses/by/3.0/
preferredPrefix: SEPIO
products:
- id: sepio.owl
  title: SEPIO
repository: https://github.com/monarch-initiative/SEPIO-ontology
tags:
- scientific claims
- evidence
tracker: https://github.com/monarch-initiative/SEPIO-ontology/issues
activity_status: active
---

The Scientific Evidence and Provenance Information Ontology (SEPIO) was developed to support description of evidence and provenance information for scientific claims. The core model represents the relationships between claims, their evidence lines, the information items that comprise these lines of evidence, and the methods, tools, and agents involved in the creation of these entities.  Use cases driving SEPIO development include integration of scientific claims and their associated evidence/provenance metadata, and support for the discovery, analysis, and evaluation of claims based on this metadata.
