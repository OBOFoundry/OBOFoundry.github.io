---
layout: ontology_detail
id: phipo
title: Pathogen Host Interaction Phenotype Ontology
jobs:
  - id: https://travis-ci.org/PHI-base/phipo
    type: travis-ci
build:
  checkout: git clone https://github.com/PHI-base/phipo.git
  system: git
  path: "."
contact:
  email: alayne.cuzick@rothamsted.ac.uk
  label: Alayne Cuzick
description: PHIPO is a formal ontology of species-neutral phenotypes observed in pathogen-host interactions.
domain: phenotype
homepage: https://github.com/PHI-base/phipo
products:
  - id: phipo.owl
  - id: phipo.obo
dependencies:
  - id: pato
tracker: https://github.com/PHI-base/phipo/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
activity_status: active
repository: https://github.com/PHI-base/phipo
preferredPrefix: PHIPO
---

PHIPO is being developed to support the comprehensive and detailed representation of phenotypes in PHI-base, the multi-species Pathogen-Host Interactions database available online at <http://www.phi-base.org>. PHIPO is pre-composed and logically defined.
