---
layout: ontology_detail
id: ontoavida
title: 'OntoAvida: ontology for Avida digital evolution platform'
contact:
  email: fortuna@ebd.csic.es
  github: miguelfortuna
  label: Miguel A. Fortuna
  orcid: 0000-0002-8374-1941
dependencies:
- id: fbcv
- id: gsso
- id: ncit
- id: ro
- id: stato
description: OntoAvida develops an integrated vocabulary for the description of the most widely-used computational approach for studying evolution using digital organisms (i.e., self-replicating computer programs that evolve within a user-defined computational environment).
domain: simulation
homepage: https://gitlab.com/fortunalab/ontoavida
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: ONTOAVIDA
products:
- id: ontoavida.owl
- id: ontoavida.obo
repository: https://gitlab.com/fortunalab/ontoavida
tags:
- digital evolution
- artificial life
tracker: https://gitlab.com/fortunalab/ontoavida/-/issues
activity_status: active
---
<img  src="https://fortunalab.org/images/alife_bacteria.jpg" style="padding-right:20px; padding-bottom:10px;" height="150px" align="left"/>The **Ontology for Avida ([OntoAvida](https://gitlab.com/fortunalab/ontoavida))** project aims to develop an integrated vocabulary for the description of [Avida](https://github.com/devosoft/avida), the most widely used computational approach for performing experimental evolution. The lack of a clearly defined vocabulary makes biologists feel reluctant to embrace the field of digital evolution. This unique ontology has the potential to change this picture overnight. In addition, OntoAvida will allow researchers to make inference (e.g., on phenotypic plasticity) based on certain rules and constraints, facilitate the reproducibility of the *in silico* evolution experiments reported in the [scientific literature](https://gitlab.com/fortunalab/ontoavida#references), and trace the provenance of the data stored in AvidaDB, a semantic database that stores genomes and transcriptomes of more than a million digital organisms.
