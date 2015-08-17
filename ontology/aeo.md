---
layout: ontology_detail
id: aeo
contact:
  email: J.Bard@ed.ac.uk
  label: Jonathan Bard
description: AEO is an ontology of anatomical structures that expands CARO, the Common Anatomy Reference Ontology
domain: anatomy
homepage: http://www.obofoundry.org/wiki/index.php/AEO:Main_Page
products:
  - id: aeo.owl
title: Anatomical Entity Ontology
build:
  checkout: git clone https://github.com/obophenotype/human-developmental-anatomy-ontology.git
  system: git
  path: src/ontology
  method: vcs
---

AEO is an ontology of anatomical structures that expands CARO, the Common Anatomy Reference Ontology, to about 200 classes using the is_a relationship; it thus provides a detailed type classification for tissues. The new classes were chosen for their use in categorizing the major vertebrate and invertebrate anatomy ontologies at a granularity adequate for tissues of a single cell type. The ontology should be useful in increasing the amount of knowledge in anatomy ontologies, facilitating annotation and enabling interoperability across anatomy ontologies
