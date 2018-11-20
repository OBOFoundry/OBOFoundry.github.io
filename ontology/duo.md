---
layout: ontology_detail
id: duo
title: The Data Use Ontology
jobs:
  - id: https://travis-ci.org/EBISPOT/DUO
    type: travis-ci
build:
  checkout: git clone https://github.com/EBISPOT/duo.git
  system: git
  path: "."
contact:
  email: mcourtot@gmail.com
  label: Melanie Courtot
  github: mcourtot
description: DUO is an ontology which represent data use conditions.
homepage: https://github.com/EBISPOT/DUO
products:
  - id: duo.owl
dependencies:
 - id: iao
 - id: bfo
tracker: https://github.com/EBISPOT/DUO/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
---

An ontology based on the consent codes decsription from the Dyke et al. paper at https://doi.org/10.1371/journal.pgen.1005772. It allows to semantically tag datasets with restriction about their usage, making them discoverable automatically based on the authorization level of users, or intended usage.
This resource is based on the OBO Foundry principles, and its use is under review by the Broad Institute ad the European Genome-phenome Archive (EGA) at EMBL-EBI.
