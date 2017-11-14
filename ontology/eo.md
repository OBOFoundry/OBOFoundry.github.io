---
layout: ontology_detail
id: eo
title: Plant Environment Ontology
build:
  source_url: https://github.com/Planteome/plant-environment-ontology/blob/master/plant-environment-ontology.obo.owl
  method: obo2owl
contact:
  email: jaiswalp@science.oregonstate.edu
  label: Pankaj Jaiswal
description: A structured, controlled vocabulary which describes the treatments, growing conditions, and/or study types used in plant biology experiments.
domain: environment
homepage: http://planteome.org/
page: http://browser.planteome.org/amigo/term/EO:0007359
products:
  - id: eo.owl
  - id: eo.obo
tracker: https://github.com/Planteome/plant-environment-ontology/issues
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY 4.0
publications:
  - id: http://www.ncbi.nlm.nih.gov/pubmed/22847540
    title: "Ontologies as integrative tools for plant science."
usages:
  - user: http://planteome.org/
    description: Planteome uses EO to describe traits for genes and germplasm
    examples:
      - url: http://browser.planteome.org/amigo/term/EO:0007174
        description: Genes and proteins annotated to cold temperature regiment
  - user: http://gramene.org/
    description: Gramene uses EO for the annotation of plant genes and QTLs
    examples:
      - url: http://archive.gramene.org/db/ontology/search?id=EO:0007174
        description: Gramene annotations to cold temperature regiment
---

A structured, controlled vocabulary for the representation of plant environmental conditions.

<img alt="Planteome logo" src="http://planteome.org/sites/default/files/garland_logo.PNG"/>

Note this ontology is being replaced by [PECO](peco.html)
