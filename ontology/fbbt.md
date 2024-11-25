---
layout: ontology_detail
id: fbbt
title: Drosophila gross anatomy
browsers:
- title: FlyBase Browser
  label: FB
  url: http://flybase.org/.bin/cvreport.html?cvterm=FBbt:10000000
- title: Virtual Fly Brain
  label: VFB
  url: http://www.virtualflybrain.org/site/stacks/index.htm?add=FBbt:00007401
build:
  checkout: git clone https://github.com/FlyBase/drosophila-anatomy-developmental-ontology.git
  path: .
  system: git
contact:
  email: cp390@cam.ac.uk
  github: Clare72
  label: Clare Pilgrim
  orcid: 0000-0002-1373-1705
description: An ontology representing the gross anatomy of Drosophila melanogaster.
domain: anatomy and development
homepage: http://purl.obolibrary.org/obo/fbbt
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
preferredPrefix: FBbt
products:
- id: fbbt.owl
- id: fbbt.obo
- id: fbbt.json
- id: fbbt/fbbt-simple.owl
- id: fbbt/fbbt-simple.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/24139062
  title: The Drosophila anatomy ontology
  preferred: true
- id: https://www.ncbi.nlm.nih.gov/pubmed/22402613
  title: A strategy for building neuroanatomy ontologies
- id: https://www.ncbi.nlm.nih.gov/pubmed/22180411
  title: The Virtual Fly Brain Browser and Query Interface
- id: https://www.ncbi.nlm.nih.gov/pubmed/16381917
  title: 'FlyBase: anatomical data, images and queries'
repository: https://github.com/FlyBase/drosophila-anatomy-developmental-ontology
tags:
- Drosophilid anatomy
taxon:
  id: NCBITaxon:7227
  label: Drosophila
tracker: http://purl.obolibrary.org/obo/fbbt/tracker
usages:
- description: VFB uses FBbt to annotate brain images
  examples:
  - description: Ring neuron R2 in VFB
    url: http://www.virtualflybrain.org/site/stacks/index.htm?id=FBbt_00003651
  - description: genes expressed in ring neuron R2 in VFB
    url: http://www.virtualflybrain.org/do/gene_list.html?action=geneex&id=FBbt:00003651
  user: http://www.virtualflybrain.org/
- description: Flybase uses FBbt for expression and phenotype data annotation in Drosophila
  examples:
  - description: alleles, constructs and insertions annotated to neuron in FlyBase
    url: http://flybase.org/cgi-bin/cvreport.html?rel=is_a&id=FBbt:00005106
  user: http://flybase.org
activity_status: active
---
