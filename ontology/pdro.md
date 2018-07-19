---
layout: ontology_detail
id: pdro
contact:
  email: info@griis.ca
  label: Ryeyan Taseen
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
description: An ontology to describe entities related to prescription of drugs
domain: health
homepage: https://github.com/OpenLHS/PDRO
products:
  - id: pdro.owl
title: The Prescription of Drugs Ontology
build:
  source_url: http://purl.obolibrary.org/obo/pdro.owl
  method: owl2obo
tracker: https://github.com/OpenLHS/PDRO/issues
---

PDRO is a realist ontology that aims to represent the domain of drug prescriptions. Such an ontology is currently missing in the OBOFoundry and is highly relevant to the domains of existing ontologies like DRON, OMRSE and OAE. PDRO's central focus is the structure of a drug prescription, which is represented as a mereology of informational entities. Our current use cases are (1) refining this structure (e.g., adding closure axioms, cardinality, datatype bindings, etc) for prospectively standardizing local electronic prescriptions and (2) annotating prescription data of differing EHRs for detecting inappropriate prescriptions using a central semantic framework. Future ontological work will include aligning PDRO more closely with the Document Acts Ontology.
