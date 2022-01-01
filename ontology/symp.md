---
layout: ontology_detail
id: symp
contact:
  email: lynn.schriml@gmail.com
  label: Lynn Schriml
  github: lschriml
description: An ontology of disease symptoms, with symptoms encompasing perceived changes in function, sensations or appearance reported by a patient indicative of a disease.
domain: disease
homepage: http://symptomontologywiki.igs.umaryland.edu/mediawiki/index.php/Main_Page
products:
  - id: symp.owl
  - id: symp.obo
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
title: Symptom Ontology
build:
  source_url: https://raw.githubusercontent.com/DiseaseOntology/SymptomOntology/master/symp.obo
  method: obo2owl
  infallible: 1
tracker: https://github.com/DiseaseOntology/SymptomOntology/issues
license:
  url: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
usages:
  - user: http://www.disease-ontology.org
    description: Symptoms of human diseases in the DO
    examples:
      - url: http://www.disease-ontology.org/?id=DOID:0060164
        description: symptoms of human diseases
activity_status: active
repository: https://github.com/DiseaseOntology/SymptomOntology
preferredPrefix: SYMP
---

The symptom ontology was designed around the guiding concept of a symptom being: "A perceived change in function, sensation or appearance reported by a patient indicative of a disease". Understanding the close relationship of Signs and Symptoms, where Signs are the objective observation of an illness, the Symptom Ontology will work to broaden it's scope to capture and document in a more robust manor these two sets of terms. Understanding that at times, the same term may be both a Sign and a Symptom.
