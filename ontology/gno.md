---
layout: ontology_detail
id: gno
contact:
  email: nje5@georgetown.edu
  label: Nathan Edwards
  github: edwardsnj
description: An ontology for glycans based on GlyTouCan, but organized by subsumption.
domain: glycan structure
homepage: https://github.com/glygen-glycan-data/GNOme
products:
  - id: gno.owl
  - id: gno.obo
  - id: gno.json
title: Glycan Naming Ontology
build:
  checkout: git clone https://github.com/glygen-glycan-data/GNOme.git
  system: git
  path: "."
tracker: https://github.com/glygen-glycan-data/GNOme/issues
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY 4.0
activity_status: active
browsers:
  - label: GNOme
    title: GNOme Glycan Composition Browser and Subsumption Navigator
    url: https://raw.githack.com/glygen-glycan-data/GNOme/master/GNOme.browser.html
---
