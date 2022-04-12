---
layout: ontology_detail
id: fobi
contact:
  email: polcaes@gmail.com
  label: Pol Castellano Escuder
  github: pcastellanoescuder
  orcid: 0000-0001-6466-877X
description: FOBI (Food-Biomarker Ontology) is an ontology to represent food intake data and associate it with metabolomic data
domain: diet, metabolomics, and nutrition
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
products:
  - id: fobi.owl
    title: FOBI is an ontology to represent food intake data and associate it with metabolomic data
    format: owl-rdf/xml
title: Food-Biomarker Ontology
dependencies:
  - id: chebi
  - id: foodon
publications:
   - id: https://www.ncbi.nlm.nih.gov/pubmed/32556148
     title: "FOBI: an ontology to represent food intake data and associate it with metabolomic data"
   - id: https://www.ncbi.nlm.nih.gov/pubmed/34601570
     title: "The fobitools framework: the first steps towards food enrichment analysis"
tracker: https://github.com/pcastellanoescuder/FoodBiomarkerOntology/issues
homepage: https://github.com/pcastellanoescuder/FoodBiomarkerOntology
activity_status: active
repository: https://github.com/pcastellanoescuder/FoodBiomarkerOntology
preferredPrefix: FOBI
---

FOBI (Food-Biomarker Ontology) is composed of two interconnected sub-ontologies. One is a ”Food Ontology” consisting of raw foods and multi-ingredient foods while the second is a ”Biomarker Ontology” containing food intake biomarkers classified by their chemical classes. These two sub-ontologies are conceptually independent but interconnected by different properties.
