---
layout: ontology_detail
id: pdro
title: The Prescription of Drugs Ontology
build:
  method: owl2obo
  source_url: http://purl.obolibrary.org/obo/pdro.owl
contact:
  email: paul.fabry@usherbrooke.ca
  github: pfabry
  label: Paul Fabry
  orcid: 0000-0002-3336-2476
description: An ontology to describe entities related to prescription of drugs
domain: information
homepage: https://github.com/OpenLHS/PDRO
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: PDRO
products:
- id: pdro.owl
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/34831777
  title: 'The Prescription of Drug Ontology 2.0 (PDRO): More Than the Sum of Its Parts'
repository: https://github.com/OpenLHS/PDRO
tags:
- clinical documentation
tracker: https://github.com/OpenLHS/PDRO/issues
activity_status: active
---

PDRO is a realist ontology that aims to represent the domain of drug prescriptions. Such an ontology is currently missing in the OBOFoundry and is highly relevant to the domains of existing ontologies like DRON, OMRSE and OAE. PDRO's central focus is the structure of a drug prescription, which is represented as a mereology of informational entities. Our current use cases are (1) refining this structure (e.g., adding closure axioms, cardinality, datatype bindings, etc) for prospectively standardizing local electronic prescriptions and (2) annotating prescription data of differing EHRs for detecting inappropriate prescriptions using a central semantic framework. Future ontological work will include aligning PDRO more closely with the Document Acts Ontology.
