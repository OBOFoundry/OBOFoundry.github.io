---
layout: ontology_detail
id: prefer
title: Precision Fermentation Ontology
browsers:
- title: Ontology Lookup Service Browser
  label: OLS
  url: https://www.ebi.ac.uk/ols4/ontologies/prefer
contact:
  email: txellmgsol@gmail.com
  github: txellext
  label: Txell Amigó
  orcid: 0009-0009-0018-4253
description: PREFER is an ontology designed to integrate high-throughput bioprocess data, covering operational, environmental and process parameters across different scales of a precision fermentation process, to accelerate the development and scaling of biosustainable production processes.
domain: investigations
homepage: https://github.com/Multiomics-Analytics-Group/prefer_ontology
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
preferredPrefix: PREFER
products:
- id: prefer.owl
  title: Main PREFER OWL edition
  description: Complete ontology, plus inter-ontology axioms, and imports modules
  format: owl-rdf/xml
  is_canonical: true
  uses:
  - iao
  - cl
  - omo
  - ro
  - chebi
  - pat
  - go
  - obi
  - uberon
  - cob
  - ncbitaxon
- id: prefer.obo
  title: prefer obo format edition
  derived_from: prefer.owl
  description: Complete ontology, plus inter-ontology axioms, and imports modules merged in
  format: obo
- id: prefer.json
  title: PREFER OBOGraph-JSON format edition
  derived_from: prefer.owl
  description: Complete ontology, plus inter-ontology axioms, and imports modules merged in
  format: json
- id: prefer/prefer-basic.owl
  title: Basic prefer
  description: Basic version, no inter-ontology axioms
  format: owl-rdf/xml
- id: prefer/prefer-basic.obo
  title: Basic PREFER (OBO version)
  description: Basic version, no inter-ontology axioms
  format: obo
- id: prefer/prefer-basic.json
  title: Basic PREFER (OBOGraph-JSON version)
  description: Basic version, no inter-ontology axioms
  format: json
- id: prefer/prefer-base.owl
  title: PREFER base module
  description: complete PREFER but with no imports or external axioms
  format: owl-rdf/xml
- id: prefer/prefer-base.obo
  title: PREFER base module (OBO version)
  description: complete PREFER but with no imports or external axioms
  format: obo
- id: prefer/prefer-base.json
  title: PREFER base module (OBOGraph-JSON version)
  description: complete PREFER but with no imports or external axioms
  format: json
publications:
- id: https://arxiv.org/abs/2602.16755
  title: 'PREFER: An Ontology for the PREcision FERmentation Community'
repository: https://github.com/Multiomics-Analytics-Group/prefer_ontology/
tracker: https://github.com/Multiomics-Analytics-Group/prefer_ontology/issues
usages:
- description: PREFER is used for the integration of data for biofoundry precision fermentation data.
  publications:
  - id: https://arxiv.org/abs/2602.16755
    title: 'PREFER: An Ontology for the PREcision FERmentation Community'
  type: annotation
  user: http://bright.dtu.dk/
activity_status: active
---
