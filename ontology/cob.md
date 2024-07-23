---
layout: ontology_detail
id: cob
title: Core Ontology for Biology and Biomedicine
contact:
  email: bpeters@lji.org
  github: bpeters42
  label: Bjoern Peters
  orcid: 0000-0002-8457-6693
description: COB brings together key terms from a wide range of OBO projects to improve interoperability.
domain: upper
homepage: https://obofoundry.org/COB/
license:
  label: CC0 1.0
  url: https://creativecommons.org/publicdomain/zero/1.0/
preferredPrefix: COB
products:
- id: cob.owl
  title: COB
  description: Core Ontology for Biology and Biomedicine, main ontology
- id: cob/cob-base.owl
  title: COB base module
  description: base module for COB
- id: cob/cob-native.owl
  title: COB native module
  description: COB with native IDs preserved rather than rewired to OBO IDs
- id: cob/cob-to-external.owl
  title: COB to external
  type: BridgeOntology
- id: cob/products/demo-cob.owl
  title: COB demo ontology (experimental)
  description: demo of COB including subsets of other ontologies (Experimental, for demo purposes only)
  status: alpha
repository: https://github.com/OBOFoundry/COB
tracker: https://github.com/OBOFoundry/COB/issues
activity_status: active
---

The Core Ontology for Biology and Biomedicine (COB) brings together key terms from a wide range of OBO projects into a single, small ontology. The goal is to improve interoperabilty and reuse across the OBO community through better coordination of key terms.
