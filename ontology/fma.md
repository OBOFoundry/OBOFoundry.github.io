---
layout: ontology_detail
id: fma
contact:
  email: mejino@u.washington.edu
  label: Onard Mejino
license:
  url: https://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
description: This is currently a slimmed down version of FMA
domain: anatomy
homepage: http://si.washington.edu/projects/fma
page: http://en.wikipedia.org/wiki/Foundational_Model_of_Anatomy
publications:
  - id: http://www.ncbi.nlm.nih.gov/pubmed/18688289
    title: Translating the Foundational Model of Anatomy into OWL
  - id: http://www.ncbi.nlm.nih.gov/pubmed/18360535
    title: "The foundational model of anatomy in OWL: Experience and perspectives"
  - id: http://www.ncbi.nlm.nih.gov/pubmed/16779026
    title: "Challenges in converting frame-based ontology into OWL: the Foundational Model of Anatomy case-study"
products:
  - id: fma.owl
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
title: Foundational Model of Anatomy Ontology (subset)
build:
  source_url: http://svn.code.sf.net/p/obo/svn/fma-conversion/trunk/fma2_obo.obo
  insert_ontology_id: true
  method: obo2owl
tracker: https://sourceforge.net/p/obo/foundational-model-of-anatomy-fma-requests/
activity_status: active
preferredPrefix: FMA
---

Obo format translation of the FMA, omitting all relationships other than is_a, part_of and has_part. Future versions of fma_obo will include more relationships
