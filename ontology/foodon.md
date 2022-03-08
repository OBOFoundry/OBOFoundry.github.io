---
layout: ontology_detail
id: foodon
contact:
  email: damion_dooley@sfu.ca
  label: Damion Dooley
  github: ddooley
  orcid: 0000-0002-8844-9165
description: A broadly scoped ontology representing entities which bear a “food role”. It encompasses materials in natural ecosystems and agriculture that are consumed by humans and domesticated animals. This includes any generic (unbranded) raw or processed food material found in processing plants, markets, stores or food distribution points. FoodOn also imports nutritional component and dietary pattern terms from other OBO Foundry ontologies to support interoperability in diet and nutrition research
domain: diet, metabolomics and nutrition
tags:
 - food
homepage: https://foodon.org/
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
products:
  - id: foodon.owl
    title: FoodOn ontology with import file references and over 9,000 food products
    format: owl-rdf/xml
  - id: foodon_core.owl
    title: FoodOn core ontology (currently the same as foodon.owl)
    format: owl-rdf/xml
title: Food Ontology
dependencies:
  - id: uberon
  - id: ro
  - id: eo
  - id: chebi
  - id: ncbitaxon
  - id: bfo
  - id: envo
  - id: obi
tracker: https://github.com/FoodOntology/foodon/issues/
activity_status: active
repository: https://github.com/FoodOntology/foodon
preferredPrefix: FOODON
---

A broadly scoped ontology representing entities which bear a “food role”.  It encompasses materials in natural ecosystems and food webs as well as human-centric categorization and handling of food.
