---
layout: ontology_detail
id: slso
title: Space Life Sciences Ontology
browsers:
- title: BioPortal Ontology Browser
  label: BioPortal
  url: https://bioportal.bioontology.org/ontologies/SLSO
contact:
  email: daniel.c.berrios@nasa.gov
  label: Dan Berrios
  orcid: 0000-0003-4312-9552
  github: DanBerrios
description: The Space Life Sciences Ontology is an application ontology and is intended to support the operation of NASA's Life Sciences Data Archive and other systems that contain space life science research data.
domain: investigations
homepage: https://github.com/nasa/LSDAO
in_foundry_order: 1
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: SLSO
products:
- id: slso.owl
- id: slso.obo
- id: slso.json
- id: slso-base.owl
  description: Includes axioms linking to other ontologies, but no imports of those ontologies
repository: https://github.com/nasa/LSDAO
tracker: https://github.com/nasa/LSDAO/issues
activity_status: active
---

The Space Life Sciences Ontology is an application ontology and is intended to support the operation of NASA's Life Sciences Data Archive and other systems that contain space life science research data. Many kinds of scientific research in space involve specialized equipment, experimental procedures, specimens and specimen collection apparatus, supporting operational structures, and references to specific space environments and their characteristics. Often such research is extremely costly compared with planetary/terrestrial investigations, and the community supporting space life sciences is accustomed to the use of various specialized concepts and terminologies when dealing with this kind of research and data. However, the underlying conceptual models (and especially the specific labeled relationships in these models) have never been made explicit. The SLSO attempts to provide definition and organization of these models for the space research community.  The SLSO was developed ab inicio using the Ontology Development Kit and imports an extends many concepts from the Basic Formal Ontology (BFO), the Ontology of Biomedical Investigations (OBI), the Environmental Ontology (ENVO), and other OBO Foundry ontologies. Projects at NASA such as the Open Science Data Repository (https://osdr.nasa.gov/) are already using many OBO ontologies, including the Radiation Biology Ontology (https://github.com/Radiobiology-Informatics-Consortium/RBO) and OBI, to index space biology investigation data. With the development of the SLSO, this practice can be extended to include all life science research in space or addressing space effects. Furthermore, the SLSO has a component that imports concepts from the Science Data Discovery Ontology, which was developed to support NASA's Science Discovery Engine (https://sciencediscoveryengine.nasa.gov). These links in the imported SDDO to concepts underlying a broad spectrum of space research (astrophysics, heliophysics, etc.) can ultimately be used to provide key capabilities for discovering and analyzing space life science data and how they relate to other kinds of scientific data regarding space environments.
