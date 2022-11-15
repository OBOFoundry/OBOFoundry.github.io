---
layout: ontology_detail
id: doid
title: Human Disease Ontology
browsers:
- title: DO Browser
  label: DO
  url: http://www.disease-ontology.org/
build:
  infallible: 1
  method: obo2owl
  source_url: https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/master/src/ontology/doid.obo
contact:
  email: lynn.schriml@gmail.com
  github: lschriml
  label: Lynn Schriml
  orcid: 0000-0001-8910-9851
depicted_by: http://www.disease-ontology.org/media/images/DO_logo.jpg
description: An ontology for describing the classification of human diseases organized by etiology.
domain: health
github_date_added: 2015-07-28
homepage: http://www.disease-ontology.org
in_foundry_order: 1
license:
  label: CC0 1.0
  url: https://creativecommons.org/publicdomain/zero/1.0/
preferredPrefix: DOID
products:
- id: doid.owl
  title: Disease Ontology, OWL format. This file contains DO's is_a asserted hierarchy plus equivalent axioms to other OBO Foundry ontologies.
- id: doid.obo
  title: Disease Ontology, OBO format. This file omits the equivalent axioms.
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/25348409
  title: 'Disease Ontology 2015 update: an expanded and updated database of human diseases for linking biomedical knowledge through disease data'
- id: https://www.ncbi.nlm.nih.gov/pubmed/34755882
  title: The Human Disease Ontology 2022 update
repository: https://github.com/DiseaseOntology/HumanDiseaseOntology
review:
  date: 2015
  document:
    label: PDF
    link: https://drive.google.com/open?id=0B8vqEgF1N0NIZ082U2JETHlSTGs
tags:
- disease
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
tracker: https://github.com/DiseaseOntology/HumanDiseaseOntology/issues
twitter: diseaseontology
usages:
- description: Alliance of Genome Resources - MGD, RGD, SGD, FlyBase, WormBase, ZFIN use DO
  examples:
  - description: Human diseases annotated to over 190,000 MOD genes, alleles, disease models and human genes
    url: https://www.alliancegenome.org/search?category=disease
  - description: The landing page for Coronavirus Infectious Disease
    url: https://www.alliancegenome.org/disease/DOID:0080599
  user: https://www.alliancegenome.org
- description: MGI disease model annotations use DO
  examples:
  - description: physical disorder
    url: http://www.informatics.jax.org/disease/DOID:0080015
  user: http://www.informatics.jax.org/disease
- description: Immune Epitope Database
  examples:
  - description: Antibody and T cell epitopes associated with human diseases
    url: https://www.iedb.org
  user: https://www.iedb.org
activity_status: active
---

Creating a comprehensive classification of human diseases organized by etiology.

<u>Additional OBO formatted DO files</u>
- Download DO's asserted is_a OBO file [HumanDO.obo](https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/master/src/ontology/HumanDO.obo). 
This file is equivalent to doid-non-classified.obo.

- DO provides an additional OBO file, [doid-merged.obo](https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/master/src/ontology/doid-merged.obo). 
 for the [AGR](http://www.alliancegenome.org) that includes [OMIM](http://omim.org) to DO associations as xrefs plus defined  relationships between OMIM susceptibility IDs and DO terms.  
