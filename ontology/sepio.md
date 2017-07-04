---
layout: ontology_detail
id: sepio
title: Scientific Evidence and Provenance Information Ontology
description: An ontology for representing the provenance of scientific claims and the evidence that supports them.
domain: scientific claims, evidence
homepage: https://github.com/monarch-initiative/SEPIO-ontology
tracker: https://github.com/monarch-initiative/SEPIO-ontology/issues
contact:
  email: mhb120@gmail.com
  label: Matthew Brush
license:
  url: https://creativecommons.org/licenses/by-sa/2.0/
  label: CC-BY-SA
build:
  checkout: git clone https://github.com/monarch-initiative/SEPIO-ontology.git
  system: git
  path: src/ontology
products:
  - id: sepio.owl
    title: SEPIO


---

The Scientific Evidence and Provenance Information Ontology (SEPIO) was developed to support description of evidence and provenance information for scientific claims. The core model represents the relationships between claims, their evidence lines, the information items that comprise these lines of evidence, and the methods, tools, and agents involved in the creation of these entities.  Use cases driving SEPIO development include integration of scientific claims and their associated evidence/provenance metadata, and support for the discovery, analysis, and evaluation of claims based on this metadata.


