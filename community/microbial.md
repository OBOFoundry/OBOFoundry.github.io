---
layout: community
id: microbial
title: OBO Microbial Community
description: Coordination of OBO efforts for annotating microbes and the microbiome
homepage: http://obofoundry.org/community/microbial
# mailist TODO
#members:
# - cmungall
# - pbuttigieg
# - todo
ontologies:
  - id: envo
    description: "For annotating microbial habitats"
    role: ""
  - id: micro
    description: "traits and phenotypes"
    role: ""
  - id: mco
    description: "microbial conditions"
    role: ""
  - id: ohmi
    description: "host-microbiome interactions"
    role: ""
  - id: omp
    description: "phenotypes"
    role: ""
  - id: phipo
    description: "pathogen-host phenotypes"
    role: ""
  - id: go
    description: "For annotating microbial function"
    role: ""
---

This OBO community group is for coordinating the efforts of different ontologies for annotating traits and functions of microbes, either in isolation or in the host of host-microbiome interactions, or microbial communities.

## Background

Microorganisms such as bacteria, fungi and viruses play a major role in the health of humans and the health of the planet. Microbiomes are communities of microorganisms, and are found everywhere, living in or around organisms, in the oceans, in the athmosphere, in the soil and deep in the earth's crust.

Microbiology and microbiome science is generating huge amounts of data, including sequences of microbial communities (metagenomes) as well as other kinds of omics data. In order to make sense of this data, it's necessary to ensure that sample data is associated with structured metadata, describing the environment of the microbial community. A key ontology here is the environment ontology [ENVO](https://obofoundry.org/ontology/envo), which provides hierarchical descriptors at multiple scales for describing microbioal samples and the environments in which microbial communities can be found. ENVO can also be used to analyze microbiome data, for example, connecting environments to the kinds of gene families and gene functions that are enriched.

There are a number of ontologies for describing microbial phenotypes, such as [MICRO](https://obofoundry.org/ontology/micro) and [OMP](https://obofoundry.org/ontology/omp)

For functional annotation of microbial genes, the [GO](https://obofoundry.org/ontology/go) is the recommended OBO ontology.

The [Genome Standards Consortium](http://gensc.org/) (GSC) coordinates the usage of many of these ontologies through minimal information standards such as the [MIxS](http://gensc.org/mixs/)
