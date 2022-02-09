---
layout: ontology_detail
id: upa
title: Unipathway
jobs:
  - id: https://travis-ci.org/geneontology/unipathway
    type: travis-ci
build:
  checkout: git clone https://github.com/geneontology/unipathway.git
  system: git
  path: "."
publications:
  - id: http://www.ncbi.nlm.nih.gov/pubmed/22102589
    title: "UniPathway: a resource for the exploration and annotation of metabolic pathways"
contact:
  email: "Anne.Morgat@sib.swiss"
  label: "Anne Morgat"
  github: amorgat
  orcid: 0000-0002-1216-2969
description: "A manually curated resource for the representation and annotation of metabolic pathways"
domain: pathways
homepage: https://github.com/geneontology/unipathway
products:
  - id: upa.owl
  - id: upa.obo
activity_status: inactive
dependencies:
  - id: ro
tracker: https://github.com/geneontology/unipathway/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
repository: https://github.com/geneontology/unipathway
---

UniPathway (http://www.unipathway.org) is a fully manually curated resource for the representation and annotation of metabolic pathways. UniPathway provides explicit representations of enzyme-catalyzed and spontaneous chemical reactions, as well as a hierarchical representation of metabolic pathways. This hierarchy uses linear subpathways as the basic building block for the assembly of larger and more complex pathways, including species-specific pathway variants. All of the pathway data in UniPathway has been extensively cross-linked to existing pathway resources such as KEGG and MetaCyc, as well as sequence resources such as the UniProt KnowledgeBase (UniProtKB), for which UniPathway provides a controlled vocabulary for pathway annotation. We introduce here the basic concepts underlying the UniPathway resource, with the aim of allowing users to fully exploit the information provided by UniPathway.
