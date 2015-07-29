---
layout: ont
id: ncbitaxon
preferredPrefix: NCBITaxon
title: NCBI organismal classification
contact: 
  email: obo-taxonomy@lists.sourceforge.net
  label: obo-taxonomy-list
description: The NCBITaxon ontology is an automatic translation of the NCBI taxonomy (a taxonomic classification of living organisms and associated artifacts) database into obo/owl.
source: http://www.ncbi.nlm.nih.gov/taxonomy
wasDerivedFrom: ftp://ftp.ebi.ac.uk/pub/databases/taxonomy/taxonomy.dat
createdWith: http://owltools.googlecode.com/
domain: taxonomy
homepage: http://www.obofoundry.org/wiki/index.php/NCBITaxon:Main_Page
page: http://www.ncbi.nlm.nih.gov/taxonomy
jobs:
  - id: http://build.berkeleybop.org/job/build-ncbitaxon/
    type: ReleaseBuild
products: 
  - id: ncbitaxon.owl
  - id: ncbitaxon/subsets/taxslim.owl
---

The NCBITaxon ontology is an automatic translation of the NCBI taxonomy (a taxonomic classification of living organisms and associated artifacts) database into obo/owl.