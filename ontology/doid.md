---
layout: ontology_detail
id: doid
in_foundry_order: 1
contact:
  email: lynn.schriml@gmail.com
  label: Lynn Schriml
description: An ontology for describing the classification of human diseases organized by etiology.
twitter: diseaseontology
facebook: https://www.facebook.com/diseaseontology
domain: disease
homepage: http://www.disease-ontology.org
DO wiki: http://diseaseontology.sourceforge.net/
products:
  - id: doid.owl  
    title: Disease Ontology inferred hierarchy that includes anatomy, cell of origin, infectious agent and phenotype axioms
  - id: doid.obo  
    title: Disease Ontology asserted is_a hierarchy (this file is equivalent to DO's previous HumanDO.obo file)
taxon:
  id: NCBITaxon:9606 
  label: Homo sapiens
title: Human Disease Ontology
build:
  source_url: https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/master/src/ontology/doid-non-classified.obo
  method: obo2owl
  infallible: 1
tracker: https://github.com/DiseaseOntology/HumanDiseaseOntology/issues
publications:
  - id: http://www.ncbi.nlm.nih.gov/pubmed/?term=25348409
    title: "Disease Ontology 2015 update: an expanded and updated database of human diseases for linking biomedical knowledge through disease data"
license:
  url: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0 Universal
---

Creating a comprehensive classification of human diseases organized by etiology.

<img src="http://www.disease-ontology.org/media/images/DO_logo.jpg"/>
