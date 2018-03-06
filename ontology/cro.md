---
layout: ontology_detail
id: cro
title: Contributor Role Ontology
description: A classification of the diverse roles performed in the work leading to a published research output in the sciences. Its purpose to provide transparency in contributions to scholarly published work, to enable improved systems of attribution, credit, and accountability.
domain: scholarly contribution roles
homepage: https://github.com/openrif/contributor-role-ontology
tracker: https://github.com/openrif/contributor-role-ontology/issues
contact:
  email: whimar@ohsu.edu
  label: Marijane White
license:
  url: https://creativecommons.org/licenses/by/2.0/
  label: CC-BY
build:
  checkout: git clone https://github.com/openrif/contributor-role-ontology.git
  system: git
  path: src/ontology
products:
  - id: cro.owl
    title: CRO
---

The Contributor Role Ontology is an OWL implementation of and eventual expansion of the CASRAI Contributor Roles Taxonomy (CRediT), which is a high-level classification of the diverse roles performed in the work leading to a published research output in the sciences. Its purpose to provide transparency in contributions to scholarly published work, to enable improved systems of attribution, credit, and accountability.