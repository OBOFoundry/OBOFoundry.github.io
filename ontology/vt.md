---
layout: ontology_detail
id: vt
products:
  - id: vt.owl
title: Vertebrate trait ontology
homepage: https://github.com/AnimalGenome/vertebrate-trait-ontology
tracker: https://github.com/AnimalGenome/vertebrate-trait-ontology/issues
contact:
  label: Carissa Park
  email: caripark@iastate.edu
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
build:
  checkout: svn co http://phenotype-ontologies.googlecode.com/svn/trunk/src/ontology/vt
  system: svn
  method: vcs
description: An ontology of traits covering vertebrates
activity_status: active
usages:
  - user: https://www.animalgenome.org/cgi-bin/QTLdb/index
    description: The Animal Quantitative Trait Loci (QTL) Database (Animal QTLdb) annotates trait mapping data for livestock animals using the VTO
    examples:
      - url: https://www.animalgenome.org/cgi-bin/QTLdb/BT/traitsrch?tword=Gastrointestinal%20tract%20weight
        description: "Links to cattle QTL associated with the VTO term gastrointestinal system morphology trait or its descendants"
  - user: https://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=VT:0000001
    description: The Rat Genome Database (RGD) uses the VTO to annotate rat QTL
    examples:
      - url: https://rgd.mcw.edu/rgdweb/ontology/annot.html?acc_id=VT:0003947&species=Rat
        description: "Annotations of rat QTL associated with the VTO term cholesterol amount or its descendants"        
repository: https://github.com/AnimalGenome/vertebrate-trait-ontology
---
