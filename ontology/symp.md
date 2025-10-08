---
layout: ontology_detail
id: symp
title: Symptom Ontology
build:
  infallible: 1
  method: obo2owl
  source_url: https://raw.githubusercontent.com/DiseaseOntology/SymptomOntology/master/src/ontology/symp.obo
contact:
  email: lynn.schriml@gmail.com
  github: lschriml
  label: Lynn Schriml
  orcid: 0000-0001-8910-9851
description: An ontology of disease symptoms, with symptoms encompasing perceived changes in function, sensations or appearance reported by a patient indicative of a disease.
domain: health
homepage: https://github.com/DiseaseOntology/SymptomOntology
license:
  label: CC0 1.0
  url: https://creativecommons.org/publicdomain/zero/1.0/
preferredPrefix: SYMP
products:
- id: symp.owl
- id: symp.obo
publications:
- id: https://pubmed.ncbi.nlm.nih.gov/19850722/
  title: GeMInA, Genomic Metadata for Infectious Agents, a geospatial surveillance pathogen database
- id: https://pubmed.ncbi.nlm.nih.gov/34755882/
  title: The Human Disease Ontology 2022 update
repository: https://github.com/DiseaseOntology/SymptomOntology
tags:
- disease
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
tracker: https://github.com/DiseaseOntology/SymptomOntology/issues
usages:
- description: Symptoms of human diseases in the DO
  examples:
  - description: symptoms of human diseases
    url: https://disease-ontology.org/?id=DOID:0060164
  user: https://disease-ontology.org/
activity_status: active
---

The symptom ontology was designed around the guiding concept of a symptom being: "A perceived change in function, sensation or appearance reported by a patient indicative of a disease". Understanding the close relationship of Signs and Symptoms, where Signs are the objective observation of an illness, the Symptom Ontology will work to broaden it's scope to capture and document in a more robust manor these two sets of terms. Understanding that at times, the same term may be both a Sign and a Symptom.
