---
layout: ontology_detail
id: scdo
title: Sickle Cell Disease Ontology
build:
  checkout: git clone https://github.com/scdodev/scdo-ontology.git
  system: git
  path: "."
contact:
  email: giant.plankton@gmail.com
  label: Jade Hotchkiss
  github: JadeHotchkiss
  orcid: 0000-0002-2193-0704
description: An ontology for the standardization of terminology and integration of knowledge about Sickle Cell Disease.
domain: health
tags:
  - disease
homepage: https://scdontology.h3abionet.org/
products:
  - id: scdo.owl
  - id: scdo.obo
publications: 
  - id: https://www.ncbi.nlm.nih.gov/pubmed/35363306
     title: "The Sickle Cell Disease Ontology: recent development and expansion of the universal sickle cell knowledge representation."
  - id: https://www.ncbi.nlm.nih.gov/pubmed/33021900
     title: "The Sickle Cell Disease Ontology: Enabling Collaborative Research and Co-Designing of New Planetary Health Applications."
  - id: https://www.ncbi.nlm.nih.gov/pubmed/31769834
     title: "The Sickle Cell Disease Ontology: enabling universal sickle cell-based knowledge representation."
tracker: https://github.com/scdodev/scdo-ontology/issues
license:
  url: https://www.gnu.org/licenses/gpl-3.0.en.html
  label: GPL-3.0
activity_status: active
repository: https://github.com/scdodev/scdo-ontology
dependencies:
  - id: apollo_sv
  - id: aro
  - id: chebi
  - id: chmo
  - id: cmo
  - id: doid
  - id: dron
  - id: duo
  - id: envo
  - id: eupath
  - id: exo
  - id: gaz
  - id: gsso
  - id: hp
  - id: hsapdv
  - id: ico
  - id: ido
  - id: idomal
  - id: mp
  - id: nbo
  - id: ncit
  - id: obi
  - id: ogms
  - id: opmi
  - id: pr
  - id: sbo
  - id: stato
  - id: symp
  - id: uo
  - id: vo
  - id: vt
preferredPrefix: SCDO
---

The Sickle Cell Disease Ontology (SCDO) project is a collaboration between H3ABioNet (Pan African Bioinformatics Network) and SPAN (Sickle Cell Disease Pan African Network). The SCDO is currently under development and its purpose is to: 1) establish community standardized SCD terms and descriptions, 2) establish canonical and hierarchical representation of knowledge on SCD, 3) links to other ontologies and bodies of work such as DO, PhenX, MeSH, ICD, NCI’s thesaurus, SNOMED and OMIM. Once complete, we anticipate that the ontology will: 1) be the most comprehensive collection of knowledge on SCD, 2) facilitate exploration of new scientific questions and ideas, 3) facilitate seamless data sharing and collaborations including meta-analysis within the SCD community, 4) support the building of databasing and clinical informatics in SCD.
