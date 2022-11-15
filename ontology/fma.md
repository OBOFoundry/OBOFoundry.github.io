---
layout: ontology_detail
id: fma
title: Foundational Model of Anatomy Ontology (subset)
build:
  insert_ontology_id: true
  method: obo2owl
  source_url: http://svn.code.sf.net/p/obo/svn/fma-conversion/trunk/fma2_obo.obo
contact:
  email: mejino@u.washington.edu
  label: Onard Mejino
description: This is currently a slimmed down version of FMA
domain: anatomy and development
github_date_added: 2015-07-28
homepage: http://si.washington.edu/projects/fma
license:
  label: CC BY 3.0
  url: https://creativecommons.org/licenses/by/3.0/
page: http://en.wikipedia.org/wiki/Foundational_Model_of_Anatomy
preferredPrefix: FMA
products:
- id: fma.owl
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/18688289
  title: Translating the Foundational Model of Anatomy into OWL
- id: https://www.ncbi.nlm.nih.gov/pubmed/18360535
  title: 'The foundational model of anatomy in OWL: Experience and perspectives'
- id: https://www.ncbi.nlm.nih.gov/pubmed/16779026
  title: 'Challenges in converting frame-based ontology into OWL: the Foundational Model of Anatomy case-study'
repository: https://bitbucket.org/uwsig/fma
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
tracker: https://bitbucket.org/uwsig/fma/issues
activity_status: inactive
---

Obo format translation of the FMA, omitting all relationships other than is_a, part_of and has_part. Future versions of fma_obo will include more relationships
