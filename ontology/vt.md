---
layout: ontology_detail
id: vt
title: Vertebrate trait ontology
build:
  checkout: svn co http://phenotype-ontologies.googlecode.com/svn/trunk/src/ontology/vt
  method: vcs
  system: svn
contact:
  email: caripark@iastate.edu
  github: caripark
  label: Carissa Park
  orcid: 0000-0002-2346-5201
description: An ontology of traits covering vertebrates
domain: phenotype
github_date_added: 2015-08-21
homepage: https://github.com/AnimalGenome/vertebrate-trait-ontology
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: VT
products:
- id: vt.owl
repository: https://github.com/AnimalGenome/vertebrate-trait-ontology
tracker: https://github.com/AnimalGenome/vertebrate-trait-ontology/issues
usages:
- description: The Animal Quantitative Trait Loci (QTL) Database (Animal QTLdb) annotates trait mapping data for livestock animals using the VTO
  examples:
  - description: Links to cattle QTL associated with the VTO term gastrointestinal system morphology trait or its descendants
    url: https://www.animalgenome.org/cgi-bin/QTLdb/BT/traitsrch?tword=Gastrointestinal%20tract%20weight
  user: https://www.animalgenome.org/cgi-bin/QTLdb/index
- description: The Rat Genome Database (RGD) uses the VTO to annotate rat QTL
  examples:
  - description: Annotations of rat QTL associated with the VTO term cholesterol amount or its descendants
    url: https://rgd.mcw.edu/rgdweb/ontology/annot.html?acc_id=VT:0003947&species=Rat
  user: https://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=VT:0000001
- description: The Mouse Phenome Database (MPD) uses the VTO to annotate mouse strain traits
  examples:
  - description: Studies in the MPD database that have measurements related to the VTO term spleen size trait or its descendants
    url: https://phenome.jax.org/ontologies/VT:0002224
  user: https://phenome.jax.org/ontologies/navigate/VT:0000001
activity_status: active
---
