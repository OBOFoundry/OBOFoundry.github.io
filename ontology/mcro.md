---
layout: ontology_detail
id: mcro
title: Model Card Report Ontology
contact:
  email: muamith@utmb.edu
  github: ProfTuan
  label: Tuan Amith
  orcid: 0000-0003-4333-1857
dependencies:
- id: iao
- id: swo
description: An ontology representing the structure of model card reports - reports that describe basic characteristics of machine learning models for the public and consumers.
domain: information technology
homepage: https://github.com/UTHealth-Ontology/MCRO
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: MCRO
products:
- id: mcro.owl
repository: https://github.com/UTHealth-Ontology/MCRO
tracker: https://github.com/UTHealth-Ontology/MCRO/issues
activity_status: active
---

Model card reports are documents detailing transparent metadata information relating to machine learning models. Analogous with drug labels and nutritional labels, the goal of model cards are to communicate relevant information on all aspects of a machine learning model that have undergone any experimentation. However, these reports of the machine learning models are presented in static documents. 

This work encodes the various structures of model card reports and align them to standard OBO Foundry ontologies (specifically the Information Artifact Ontology and the Software Ontology) to help formalize and enrich these documents, and essentially make these reports computable for indexing, searching and aggregation.


