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
  orcid: 0000-0001-5208-3432
description: CHEBI provides a distinct role hierarchy. Chemicals in the structural hierarchy are connected via a 'has role' relation. CHIRO provides links from these roles to useful other classes in other ontologies. This will allow direct connection between chemical structures (small molecules, drugs) and what they do. This could be formalized using 'capable of', in the same way Uberon and the Cell Ontology link structures to processes.
domain: chemistry and biochemistry
homepage: https://github.com/obophenotype/chiro
products:
  - id: chiro.owl
    name: "CHEBI Integrated Role Ontology main release in OWL format"
  - id: chiro.obo
    name: "CHEBI Integrated Role Ontology additional release in OBO format"
publications:
  - id: https://doi.org/10.26434/chemrxiv.12591221
    title: "Extension of Roles in the ChEBI Ontology"
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
  url: http://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
activity_status: active
repository: https://github.com/obophenotype/chiro
preferredPrefix: CHIRO
github_date_added: 2019-09-26
---
