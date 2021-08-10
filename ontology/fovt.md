---
layout: ontology_detail
id: fovt
title: FuTRES Ontology of Vertebrate Traits
jobs:
  - id: https://travis-ci.org/futres/fovt
    type: travis-ci
build:
  checkout: git clone https://github.com/futres/fovt.git
  system: git
  path: "."
contact:
  email: rlwalls2008@gmail.com
  label: FuTRES Ontology of Vertebrate Traits
  github: https://github.com/futres/fovt
description: FuTRES Ontology of Vertebrate Traits is an application ontology used to convert vertebrate trait data in spreadsheet to triples. FOVT leverages the BioCollections Ontology (BCO) to link observations of individual specimens to their trait values. Traits are defined in the Ontology of Biological Attributes (OBA).
domain: vertebrate traits
homepage: https://github.com/futres/fovt
products:
  - id: fovt.owl
    name: "FuTRES Ontology of Vertebrate Traits main release in OWL format"
  - id: fovt.obo
    name: "FuTRES Ontology of Vertebrate Traits additional release in OBO format"
  - id: fovt/fovt-base.owl
    name: "FuTRES Ontology of Vertebrate Traits main release in OWL format"
  - id: fovt/fovt-base.obo
    name: "FuTRES Ontology of Vertebrate Traits additional release in OBO format"
dependencies:
  - id: bco
  - id: oba
  - id: ro
  - id: bfo
  - id: pato
  - id: bspo
  - id: iao
  - id: uberon

tracker: https://github.com/futres/fovt/issues
license:
  url: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0
activity_status: active
repository: https://github.com/futres/fovt
---

The FuTRES Ontology of Vertebrate Traits is an application ontology used to convert vertebrate trait data in spreadsheets to triples, using the [Ontology Data Pipeline](https://github.com/biocodellc/ontology-data-pipeline) from Biocode LLC. FOVT leverages the BioCollections Ontology (BCO) to link observations of individual specimens to their trait values. Traits are defined in the Ontology of Biological Attributes (OBA).

For more details on FOVT, see https://futres.org/.
