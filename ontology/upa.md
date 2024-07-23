---
layout: ontology_detail
id: upa
title: Unipathway
contact:
  email: Anne.Morgat@sib.swiss
  github: amorgat
  label: Anne Morgat
  orcid: 0000-0002-1216-2969
dependencies:
- id: ro
description: A manually curated resource for the representation and annotation of metabolic pathways
domain: biological systems
homepage: https://github.com/geneontology/unipathway
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
products:
- id: upa.owl
- id: upa.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/22102589
  title: 'UniPathway: a resource for the exploration and annotation of metabolic pathways'
repository: https://github.com/geneontology/unipathway
tags:
- pathways
tracker: https://github.com/geneontology/unipathway/issues
activity_status: inactive
---

UniPathway (http://www.unipathway.org) is a fully manually curated resource for the representation and annotation of metabolic pathways. UniPathway provides explicit representations of enzyme-catalyzed and spontaneous chemical reactions, as well as a hierarchical representation of metabolic pathways. This hierarchy uses linear subpathways as the basic building block for the assembly of larger and more complex pathways, including species-specific pathway variants. All of the pathway data in UniPathway has been extensively cross-linked to existing pathway resources such as KEGG and MetaCyc, as well as sequence resources such as the UniProt KnowledgeBase (UniProtKB), for which UniPathway provides a controlled vocabulary for pathway annotation. We introduce here the basic concepts underlying the UniPathway resource, with the aim of allowing users to fully exploit the information provided by UniPathway.
