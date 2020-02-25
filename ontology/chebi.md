---
layout: ontology_detail
id: chebi
in_foundry_order: 1
alternatePrefix: ChEBI
title: Chemical Entities of Biological Interest
build:
  source_url: ftp://ftp.ebi.ac.uk/pub/databases/chebi/ontology/chebi.obo
  method: obo2owl
  infallible: 1
description: A structured classification of molecular entities of biological interest focusing on 'small' chemical compounds.
twitter: chebit
contact:
  email: gowen@ebi.ac.uk
  label: Gareth Owen
  github: "G-Owen"
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY 4.0
domain: biochemistry
homepage: http://www.ebi.ac.uk/chebi
page: http://www.ebi.ac.uk/chebi/init.do?toolBarForward=userManual
browsers:
  - label: CHEBI
    title: EBI CHEBI Browser
    url: http://www.ebi.ac.uk/chebi/chebiOntology.do?treeView=true&chebiId=CHEBI:24431#graphView
products:
  - id: chebi.owl
  - id: chebi.obo
  - id: chebi.owl.gz
    title: "chebi, compressed owl"
  - id: chebi/chebi_lite.obo
    title: "chebi_lite, no syns or xrefs"
  - id: chebi/chebi_core.obo
    title: "chebi_core, no xrefs"
tracker: https://github.com/ebi-chebi/ChEBI/issues
activity_status: active
---

A structured classification of chemical compounds of biological relevance.
