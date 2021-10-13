---
layout: ontology_detail
id: oba
contact:
  email: cjmungall@lbl.gov
  label: Chris Mungall
license:
  url: http://creativecommons.org/publicdomain/zero/1.0/
  label: CC-0
description: A collection of biological attributes (traits) covering all kingdoms of life.
domain: phenotype
homepage: https://github.com/obophenotype/bio-attribute-ontology
tracker: https://github.com/obophenotype/bio-attribute-ontology/issues
page: http://wiki.geneontology.org/index.php/Extensions/x-attribute
products:
  - id: oba.owl
  - id: oba.obo
  - id: oba/subsets/oba-basic.obo
title: Ontology of Biological Attributes
jobs:
  - id: https://travis-ci.org/obophenotype/bio-attribute-ontology
    type: travis-ci
build:
  checkout: git clone https://github.com/obophenotype/bio-attribute-ontology.git
  system: git
  path: "."
  method: vcs
activity_status: active
repository: https://github.com/obophenotype/bio-attribute-ontology
preferredPrefix: OBA
---

A collection of biological attributes (traits) covering all kingdoms of life. Interoperable with
VT (vertebrate trait ontology) and TO (plant trait ontology). Extends PATO.
