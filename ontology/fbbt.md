---
layout: ontology_detail
id: fbbt
preferredPrefix: FBbt
contact:
  email: cp390@cam.ac.uk
  label: Clare Pilgrim
description: An ontology representing the gross anatomy of Drosophila melanogaster.
domain: Drosophilid anatomy
homepage: http://purl.obolibrary.org/obo/fbbt
products:
  - id: fbbt.owl
  - id: fbbt.obo
  - id: fbbt.json
  - id: fbbt/fbbt-simple.owl
  - id: fbbt/fbbt-simple.obo
taxon:
  id: NCBITaxon:7227
  label: Drosophila
title: Drosophila gross anatomy
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
build:
  checkout: git clone https://github.com/FlyBase/drosophila-anatomy-developmental-ontology.git
  system: git
  path: "."
tracker: https://github.com/FlyBase/drosophila-anatomy-developmental-ontology/issues
browsers:
  - label: FB
    title: FlyBase Browser
    url: http://flybase.org/.bin/cvreport.html?cvterm=FBbt:10000000
  - label: VFB
    title: Virtual Fly Brain
    url: http://www.virtualflybrain.org/site/stacks/index.htm?add=FBbt:00007401
  - label: BioPortal
    title: BioPortal Browser
    url: http://bioportal.bioontology.org/ontologies/FB-BT?p=classes
publications:
  - id: https://doi.org/10.1186/2041-1480-4-32
    title: "The Drosophila anatomy ontology. [Journal of Biomedical Semantics"
  - id: https://doi.org/10.1093/bioinformatics/bts113
    title: "A strategy for building neuroanatomy ontologies"
  - id: https://doi.org/10.1093/bioinformatics/btr677
    title: "The Virtual Fly Brain Browser and Query Interface"
  - id: https://doi.org/10.1093/nar/gkj068
    title: "FlyBase: anatomical data, images and queries"
usages:
  - user: http://www.virtualflybrain.org/
    description: VFB uses FBbt to annotate brain images
    examples:
      - url: http://www.virtualflybrain.org/site/stacks/index.htm?id=FBbt_00003651
        description: "Ring neuron R2 in VFB"
      - url: http://www.virtualflybrain.org/do/gene_list.html?action=geneex&id=FBbt:00003651
        description: "genes expressed in ring neuron R2 in VFB"
  - user: http://flybase.org
    description: Flybase uses FBbt for expression and phenotype data annotation in Drosophila
    examples:
      - url: "http://flybase.org/cgi-bin/cvreport.html?rel=is_a&id=FBbt:00005106"
        description: "alleles, constructs and insertions annotated to neuron in FlyBase"
activity_status: active
---

An ontology representing the gross anatomy of Drosophila melanogaster.

FBbt can be cited as:
_Costa M., Reeve S., Grumbling G., Osumi-Sutherland D._ (2013) The Drosophila anatomy ontology. [Journal of Biomedical Semantics __4__(32).](https://doi.org/10.1186/2041-1480-4-32)
