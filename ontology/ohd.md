---
layout: ontology_detail
id: ohd
title: Oral Health and Disease Ontology
build:
  method: owl2obo
  source_url: http://purl.obolibrary.org/obo/ohd.owl
contact:
  email: wdduncan@gmail.com
  github: wdduncan
  label: Bill Duncan
  orcid: 0000-0001-9625-1899
description: The Oral Health and Disease Ontology is used for representing the diagnosis and treatment of dental maladies.
domain: health
homepage: https://purl.obolibrary.org/obo/ohd/home
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
preferredPrefix: OHD
products:
- id: ohd.owl
- id: ohd/dev/ohd.owl
  title: OHD dev
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/32819435
  title: Structuring, reuse and analysis of electronic dental data using the Oral Health and Disease Ontology
repository: https://github.com/oral-health-and-disease-ontologies/ohd-ontology
tracker: https://github.com/oral-health-and-disease-ontologies/ohd-ontology/issues
activity_status: active
---

The Oral Health and Disease Ontology is intended as a BFO and OBO
Foundry compliant ontology for the oral health domain. It is currently
used to represent the content of dental practice health records and is
intended to be further developed for use in translation medicine.  It
demonstrates a principled split between billing codes as information
entities and what the codes are about, such as dental procedures,
materials, and patients.

OHD is structured using BFO uses terms from OGMS, OBI, IAO and FMA. In
addition it uses terms from CARO, OMRSE, NCBITaxon, and a subset of
terms from the Current Dental Terminology (CDT)

OHD is in early development and subject to change without notice. 

The current developers of OHD are Alan Ruttenberg(alanruttenberg@gmail.com) and Bill Duncan
(wdduncan@gmail.com).

Initial work on OHD was funded by the University of Buffalo School of
Dental Medicine and NIDCR grants 5R21DE021178-02 and 5R03DE023358-02,
PI: Titus Schleyer (schleyer@regenstrief.org)
