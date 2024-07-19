---
layout: ontology_detail
id: foodon
title: Food Ontology
contact:
  email: damion_dooley@sfu.ca
  github: ddooley
  label: Damion Dooley
  orcid: 0000-0002-8844-9165
dependencies:
- id: bfo
- id: chebi
- id: envo
- id: eo
- id: ncbitaxon
- id: obi
- id: ro
- id: uberon
description: A broadly scoped ontology representing entities which bear a “food role”. It encompasses materials in natural ecosystems and agriculture that are consumed by humans and domesticated animals. This includes any generic (unbranded) raw or processed food material found in processing plants, markets, stores or food distribution points. FoodOn also imports nutritional component and dietary pattern terms from other OBO Foundry ontologies to support interoperability in diet and nutrition research
domain: diet, metabolomics, and nutrition
homepage: https://foodon.org/
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: FOODON
products:
- id: foodon.owl
  title: FoodOn ontology with import file references and over 9,000 food products
  format: owl-rdf/xml
- id: foodon_core.owl
  title: FoodOn core ontology (currently the same as foodon.owl)
  format: owl-rdf/xml
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/31304272
  title: 'FoodOn: a harmonized food ontology to increase global food traceability, quality control and data integration'
repository: https://github.com/FoodOntology/foodon
tags:
- food
tracker: https://github.com/FoodOntology/foodon/issues/
activity_status: active
usages:
- user: https://fdc.nal.usda.gov/
  description: FoodData Central nutrition database web portal provided by USDA Agricultural Research Service. E.g. https://fdc.nal.usda.gov/fdc-app.html#/food-details/1750340/attributes
- user: https://www.fda.gov/food/whole-genome-sequencing-wgs-program/genometrakr-network
  description: FDA GenomeTrackr surveillance program for reporting foodborne pathogen biosamples.  E.g. https://www.ncbi.nlm.nih.gov/biosample/SAMN03455272
- user: https://foodperiodictable.org/
  description: Periodic Table Of Food Initiative database of food biosample nutrition analytics. E.g. https://ptfidiscover.markerlab.com/detail/food/GGB100329
- user: https://wikifcd.wikibase.cloud/wiki/Main_Page
  description: Wiki database consolidating over 30 global food composition databases. E.g. https://wikifcd.wikibase.cloud/wiki/Item:Q568877
---

A broadly scoped ontology representing entities which bear a “food role”.  It encompasses materials in natural ecosystems and food webs as well as human-centric categorization and handling of food.
