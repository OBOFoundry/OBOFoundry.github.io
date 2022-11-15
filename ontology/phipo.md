---
layout: ontology_detail
id: phipo
title: Pathogen Host Interaction Phenotype Ontology
build:
  checkout: git clone https://github.com/PHI-base/phipo.git
  path: .
  system: git
contact:
  email: alayne.cuzick@rothamsted.ac.uk
  github: CuzickA
  label: Alayne Cuzick
  orcid: 0000-0001-8941-3984
dependencies:
- id: pato
description: PHIPO is a formal ontology of species-neutral phenotypes observed in pathogen-host interactions.
domain: phenotype
github_date_added: 2018-08-15
homepage: https://github.com/PHI-base/phipo
jobs:
- id: https://travis-ci.org/PHI-base/phipo
  type: travis-ci
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: PHIPO
products:
- id: phipo.owl
- id: phipo.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/34788826
  title: 'PHI-base in 2022: a multi-species phenotype database for Pathogen-Host Interactions'
repository: https://github.com/PHI-base/phipo
tracker: https://github.com/PHI-base/phipo/issues
activity_status: active
---

PHIPO is being developed to support the comprehensive and detailed representation of phenotypes in PHI-base, the multi-species Pathogen-Host Interactions database available online at <http://www.phi-base.org>. PHIPO is pre-composed and logically defined.
