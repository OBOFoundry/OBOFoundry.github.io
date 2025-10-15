---
layout: ontology_detail
id: fovt
title: FuTRES Ontology of Vertebrate Traits
contact:
  email: meghan.balk@gmail.com
  github: megbalk
  label: Meghan Balk
  orcid: 0000-0003-2699-3066
dependencies:
- id: bco
- id: bfo
- id: bspo
- id: iao
- id: oba
- id: pato
- id: ro
- id: uberon
description: FuTRES Ontology of Vertebrate Traits is an application ontology used to convert vertebrate trait data in spreadsheet to triples. FOVT leverages the BioCollections Ontology (BCO) to link observations of individual specimens to their trait values. Traits are defined in the Ontology of Biological Attributes (OBA).
domain: phenotype
homepage: https://github.com/futres/fovt
license:
  label: CC0 1.0
  url: https://creativecommons.org/publicdomain/zero/1.0/
preferredPrefix: FOVT
products:
- id: fovt.owl
  name: FuTRES Ontology of Vertebrate Traits main release in OWL format
- id: fovt.obo
  name: FuTRES Ontology of Vertebrate Traits additional release in OBO format
- id: fovt/fovt-base.owl
  name: FuTRES Ontology of Vertebrate Traits main release in OWL format
- id: fovt/fovt-base.obo
  name: FuTRES Ontology of Vertebrate Traits additional release in OBO format
repository: https://github.com/futres/fovt
tags:
- vertebrate traits
tracker: https://github.com/futres/fovt/issues
activity_status: active
---

The FuTRES Ontology of Vertebrate Traits is an application ontology used to convert vertebrate trait data in spreadsheets to triples, using the [Ontology Data Pipeline](https://github.com/biocodellc/ontology-data-pipeline) from Biocode LLC. FOVT leverages the BioCollections Ontology (BCO) to link observations of individual specimens to their trait values. Traits are defined in the Ontology of Biological Attributes (OBA).

For more details on FOVT, see https://futres.org/.
