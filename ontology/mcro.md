---
layout: ontology_detail
id: mcro
title: "Model Card Report Ontology: An OWL2-encoded ontology modeling the model card report for machine learning model assests."
contact:
  email: muamith@utmb.edu
  label: Tuan Amith
  orcid: 0000-0003-4333-1857
description: "Model card reports are documents detailing transparent metadata information relating to machine learning models. Similar to what we have with drug labels and nutritional labels, the goal of model cards are to communicate relevant information on all aspects of a machine learning model that have undergone any experimentation. However these important reports of the machine learning models are presented in static documents. This work encodes the structure of model card reports and align them to standard OBO Foundry ontologies to help formalize and enrich these documents. The end result is computable model of the model card that can be used to standardize reporting and be integrated in future software tooling (searching and indexing, etc.)."
domain: information technology
homepage: https://github.com/UTHealth-Ontology/MCRO
products:
  - id: mcro.owl
dependencies:
  - id: iao
  - id: swo
  - id: prov-o
tracker: https://github.com/UTHealth-Ontology/MCRO
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
activity_status: active
repository: https://github.com/UTHealth-Ontology/MCRO
preferredPrefix: MCRO
---

An OWL2-encoded ontology modeling the model card report for machine learning model assests. The aim of this work is to describe machine learning models to communicate information about specific details about the model (trade offs, intended users, licensing, etc.). As an ontology-based artifact we can semantically express, standardize, and yield computable benefits to the model card reports. 