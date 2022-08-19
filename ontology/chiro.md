---
layout: ontology_detail
id: chiro
title: CHEBI Integrated Role Ontology
build:
  checkout: git clone https://github.com/obophenotype/chiro.git
  path: .
  system: git
contact:
  email: vasilevs@ohsu.edu
  github: nicolevasilevsky
  label: Nicole Vasilevsky
  orcid: 0000-0001-5208-3432
dependencies:
- id: chebi
- id: go
- id: hp
- id: mp
- id: ncbitaxon
- id: pr
- id: uberon
description: CHEBI provides a distinct role hierarchy. Chemicals in the structural hierarchy are connected via a 'has role' relation. CHIRO provides links from these roles to useful other classes in other ontologies. This will allow direct connection between chemical structures (small molecules, drugs) and what they do. This could be formalized using 'capable of', in the same way Uberon and the Cell Ontology link structures to processes.
domain: chemistry and biochemistry
homepage: https://github.com/obophenotype/chiro
jobs:
- id: https://travis-ci.org/obophenotype/chiro
  type: travis-ci
license:
  label: CC0 1.0
  url: http://creativecommons.org/publicdomain/zero/1.0/
preferredPrefix: CHIRO
products:
- id: chiro.owl
  name: CHEBI Integrated Role Ontology main release in OWL format
- id: chiro.obo
  name: CHEBI Integrated Role Ontology additional release in OBO format
publications:
- id: https://doi.org/10.26434/chemrxiv.12591221
  title: Extension of Roles in the ChEBI Ontology
repository: https://github.com/obophenotype/chiro
tracker: https://github.com/obophenotype/chiro/issues
activity_status: active
---
