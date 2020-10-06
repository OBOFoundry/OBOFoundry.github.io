---
layout: ontology_detail
id: ecao
title: The Echinoderm Anatomy and Development Ontology
build:
  checkout: git clone https://github.com/echinoderm-ontology/ecao_ontology.git
  system: git
  path: "."
contact:
  email: ettensohn@cmu.edu
  label: Charles Ettensohn
  github: ettensohn
description: An ontology for the development and anatomy of the different species of the phylum Echinodermata (NCBITaxon:7586).
domain: anatomy
homepage: https://github.com/echinoderm-ontology/ecao_ontology
products:
  - id: ecao.owl
  - id: ecao.obo
dependencies:
 - id: uberon
 - id: ro
 - id: cl
tracker: https://github.com/echinoderm-ontology/ecao_ontology/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
activity_status: active
---

This ontology is intended to be used for the description and curation of information related to gene regulatory processes in echinoderms (e.g., expression patterns of endogenous genes and reporter DNA constructs, phenotypic effects of gene perturbations, etc.). 
The ontology was developed as a collaborativie work between MARIMBA (http://marimba.obs-vlfr.fr/home), a database of marine invertebrate models genomics created in the context of the European project CORBEL (https://www.corbel-project.eu/home.html) and Echinobase (http://www.echinobase.org/Echinobase/), a database of echinoderm genomics. 
The ontology will be used in both MARIMBA and Echinobase.

For further information contact:
- Jenifer Croce (jenifer.croce@obs-vlfr.fr)
  GitHub: @Jenicroce
- Charles Ettensohn (ettensohn@cmu.edu)
  GitHub: @ettensohn
