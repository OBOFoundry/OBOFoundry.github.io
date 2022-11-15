---
layout: ontology_detail
id: eo
title: Plant Environment Ontology
build:
  method: obo2owl
  source_url: https://github.com/Planteome/plant-environment-ontology/blob/master/plant-environment-ontology.obo.owl
contact:
  email: jaiswalp@science.oregonstate.edu
  github: jaiswalp
  label: Pankaj Jaiswal
  orcid: 0000-0002-1005-8383
depicted_by: http://planteome.org/sites/default/files/garland_logo.PNG
description: A structured, controlled vocabulary which describes the treatments, growing conditions, and/or study types used in plant biology experiments.
domain: environment
github_date_added: 2015-07-29
homepage: http://planteome.org/
is_obsolete: true
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
page: http://browser.planteome.org/amigo/term/EO:0007359
products:
- id: eo.owl
- id: eo.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/22847540
  title: Ontologies as integrative tools for plant science.
replaced_by: peco
repository: https://github.com/Planteome/plant-environment-ontology
tracker: https://github.com/Planteome/plant-environment-ontology/issues
usages:
- description: Planteome uses EO to describe traits for genes and germplasm
  examples:
  - description: Genes and proteins annotated to cold temperature regiment
    url: http://browser.planteome.org/amigo/term/EO:0007174
  user: http://planteome.org/
- description: Gramene uses EO for the annotation of plant genes and QTLs
  examples:
  - description: Gramene annotations to cold temperature regiment
    url: http://archive.gramene.org/db/ontology/search?id=EO:0007174
  user: http://gramene.org/
activity_status: inactive
---

A structured, controlled vocabulary for the representation of plant environmental conditions.

## Migration Guide from EO to PECO

If you are using classes like EO:nnnnnn then you should be able to substitute this for PECO:nnnnnn, as all of the numeric parts of the ID are preserved.

For a more robust mechanism, peco.obo contains alt_ids, and peco.owl contains the equivalent replaced_by assertions, which point from an obsoleted EO class to the corresponding PECO class.

If you have any issues you can report them here:

https://github.com/Planteome/plant-experimental-conditions-ontology/issues/95
