---
layout: ontology_detail
id: pdro
contact:
  email: paul.fabry@usherbrooke.ca
  label: Paul Fabry
  github: pfabry
  orcid: 0000-0002-3336-2476
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
description: An ontology to describe entities related to prescription of drugs
domain: information
tags:
  - clinical documentation
homepage: https://github.com/OpenLHS/PDRO
products:
  - id: pdro.owl
title: The Prescription of Drugs Ontology
build:
  source_url: http://purl.obolibrary.org/obo/pdro.owl
  method: owl2obo
publications:
  - id: https://pubmed.ncbi.nlm.nih.gov/34831777
    title: "The Prescription of Drug Ontology 2.0 (PDRO): More Than the Sum of Its Parts"
tracker: https://github.com/OpenLHS/PDRO/issues
activity_status: active
repository: https://github.com/OpenLHS/PDRO
preferredPrefix: PDRO
---

PDRO is a realist ontology that aims to represent the domain of drug prescriptions. Such an ontology is currently missing in the OBOFoundry and is highly relevant to the domains of existing ontologies like DRON, OMRSE and OAE. PDRO's central focus is the structure of a drug prescription, which is represented as a mereology of informational entities. Our current use cases are (1) refining this structure (e.g., adding closure axioms, cardinality, datatype bindings, etc) for prospectively standardizing local electronic prescriptions and (2) annotating prescription data of differing EHRs for detecting inappropriate prescriptions using a central semantic framework. Future ontological work will include aligning PDRO more closely with the Document Acts Ontology.
