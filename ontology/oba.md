---
layout: ontology_detail
id: oba
title: Ontology of Biological Attributes
build:
  checkout: git clone https://github.com/obophenotype/bio-attribute-ontology.git
  method: vcs
  path: .
  system: git
contact:
  email: cjmungall@lbl.gov
  github: cmungall
  label: Chris Mungall
  orcid: 0000-0002-6601-2165
description: A collection of biological attributes (traits) covering all kingdoms of life.
domain: phenotype
github_date_added: 2015-07-28
homepage: https://github.com/obophenotype/bio-attribute-ontology
jobs:
- id: https://travis-ci.org/obophenotype/bio-attribute-ontology
  type: travis-ci
license:
  label: CC0 1.0
  url: http://creativecommons.org/publicdomain/zero/1.0/
page: http://wiki.geneontology.org/index.php/Extensions/x-attribute
preferredPrefix: OBA
products:
- id: oba.owl
- id: oba.obo
- id: oba/subsets/oba-basic.obo
repository: https://github.com/obophenotype/bio-attribute-ontology
tracker: https://github.com/obophenotype/bio-attribute-ontology/issues
activity_status: active
---

A collection of biological attributes (traits) covering all kingdoms of life. Interoperable with
VT (vertebrate trait ontology) and TO (plant trait ontology). Extends PATO.
