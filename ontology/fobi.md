---
layout: ontology_detail
id: fobi
title: Food-Biomarker Ontology
contact:
  email: polcaes@gmail.com
  github: pcastellanoescuder
  label: Pol Castellano Escuder
  orcid: 0000-0001-6466-877X
dependencies:
- id: chebi
- id: foodon
description: FOBI (Food-Biomarker Ontology) is an ontology to represent food intake data and associate it with metabolomic data
domain: diet, metabolomics, and nutrition
github_date_added: 2019-12-04
homepage: https://github.com/pcastellanoescuder/FoodBiomarkerOntology
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: FOBI
products:
- id: fobi.owl
  title: FOBI is an ontology to represent food intake data and associate it with metabolomic data
  format: owl-rdf/xml
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/32556148
  title: 'FOBI: an ontology to represent food intake data and associate it with metabolomic data'
- id: https://www.ncbi.nlm.nih.gov/pubmed/34601570
  title: 'The fobitools framework: the first steps towards food enrichment analysis'
repository: https://github.com/pcastellanoescuder/FoodBiomarkerOntology
tracker: https://github.com/pcastellanoescuder/FoodBiomarkerOntology/issues
activity_status: active
---

FOBI (Food-Biomarker Ontology) is composed of two interconnected sub-ontologies. One is a ”Food Ontology” consisting of raw foods and multi-ingredient foods while the second is a ”Biomarker Ontology” containing food intake biomarkers classified by their chemical classes. These two sub-ontologies are conceptually independent but interconnected by different properties.
