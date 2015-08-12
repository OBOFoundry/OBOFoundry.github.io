---
layout: ontology_detail
id: bspo
contact: 
  email: cjmungall@lbl.gov
  label: Chris Mungall
description: An ontology for respresenting spatial concepts, anatomical axes, gradients, regions, planes, sides, and surfaces
domain: anatomy
homepage: https://github.com/obophenotype/biological-spatial-ontology 
products: 
  - id: bspo.owl
title: Biological Spatial Ontology
build:
  checkout: git clone https://github.com/obophenotype/biological-spatial-ontology.git
  system: git
  path: src/ontology
  method: vcs
  infallible: 1
tracker: https://github.com/obophenotype/biological-spatial-ontology/issues
publications:
  - id: http://www.ncbi.nlm.nih.gov/pubmed/25140222
    title: "Nose to tail, roots to shoots: spatial descriptors for phenotypic diversity in the Biological Spatial Ontology."
---

An ontology for respresenting spatial concepts, anatomical axes, gradients, regions, planes, sides, and surfaces. These concepts can be used at multiple biological scales and in a diversity of taxa, including plants, animals and fungi. The BSPO is used to provide a source of anatomical location descriptors for logically defining anatomical entity classes in anatomy ontologies. 
