---
layout: ontology_detail
id: chiro
title: CHEBI Integrated Role Ontology
jobs:
  - id: https://travis-ci.org/obophenotype/chiro
    type: travis-ci
build:
  checkout: git clone https://github.com/obophenotype/chiro.git
  system: git
  path: "."
contact:
  email: vasilevs@ohsu.edu
  label: Nicole Vasilevsky
  github: nicolevasilevsky
description: CHEBI provides a distinct role hierarchy. Chemicals in the structural hierarchy are connected via a 'has role' relation. CHIRO provides links from these roles to useful other classes in other ontologies. This will allow direct connection between chemical structures (small molecules, drugs) and what they do. This could be formalized using 'capable of', in the same way Uberon and the Cell Ontology link structures to processes.
domain: biochemistry
homepage: https://github.com/obophenotype/chiro
products:
  - id: chiro.owl
    name: "CHEBI Integrated Role Ontology main release in OWL format"
  - id: chiro.obo
    name: "CHEBI Integrated Role Ontology additional release in OBO format"
dependencies:
- id: chebi
- id: mp
- id: hp
- id: go
- id: pr
- id: uberon
- id: ncbitaxon

tracker: https://github.com/obophenotype/chiro/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
activity_status: active
---
