---
layout: ontology_detail
id: fbbt
preferredPrefix: FBbt
contact:
  email: temj2@cam.ac.uk
  label: Tamsin Jones
description: An ontology representing the gross anatomy of Drosophila melanogaster.
domain: anatomy
homepage: http://purl.obolibrary.org/obo/fbbt
products:
  - id: fbbt.owl
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
  source_url: https://raw.githubusercontent.com/FlyBase/drosophila-anatomy-developmental-ontology/master/fbbt/releases/fbbt.owl
  method: owl2obo
  infallible: 1
tracker: http://purl.obolibrary.org/obo/fbbt/tracker
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
  - id: http://dx.doi.org/10.1186/2041-1480-4-32
    title: "The Drosophila anatomy ontology. [Journal of Biomedical Semantics"
  - id: http://dx.doi.org/10.1093/bioinformatics/bts113
    title: "A strategy for building neuroanatomy ontologies"
  - id: http://dx.doi.org/10.1093/bioinformatics/btr677
    title: "The Virtual Fly Brain Browser and Query Interface"
  - id: http://dx.doi.org/10.1093/nar/gkj068
    title: "FlyBase: anatomical data, images and queries"
usages:
  - user: http://www.virtualflybrain.org/
    description: VFB uses FBbt to annotate brain images
    example:
      - url: http://www.virtualflybrain.org/site/stacks/index.htm?id=FBbt_00003651
        description: "Ring neuron R2 in VFB"
    example:
      - url: http://www.virtualflybrain.org/do/gene_list.html?action=geneex&id=FBbt:00003651
        description: "genes expressed in ring neuron R2 in VFB"
  - user: http://flybase.org
    description: VFB uses FBbt for expression and phenotype data annotation in Drosophila
---

An ontology representing the gross anatomy of Drosophila melanogaster.

FBbt can be cited as:
_Costa M., Reeve S., Grumbling G., Osumi-Sutherland D._ (2013) The Drosophila anatomy ontology. [Journal of Biomedical Semantics __4__(32).](http://dx.doi.org/10.1186/2041-1480-4-32)

