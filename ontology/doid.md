---
layout: ontology_detail
id: doid
in_foundry_order: 1
contact:
  email: lynn.schriml@gmail.com
  label: Lynn Schriml
  github: lschriml
description: An ontology for describing the classification of human diseases organized by etiology.
twitter: diseaseontology
facebook: https://www.facebook.com/diseaseontology
domain: disease
homepage: http://www.disease-ontology.org
DO wiki: http://diseaseontology.sourceforge.net/
products:
  - id: doid.owl
    title: Disease Ontology, OWL format. This file contains DO's is_a asserted hierarchy plus equivalent axioms to other OBO Foundry ontologies.
  - id: doid.obo
    title: Disease Ontology, OBO format. This file omits the equivalent axioms.

browsers:
  - label: DO
    title: DO Browser
    url: http://www.disease-ontology.org/
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
title: Human Disease Ontology
review:
  date: 2015
  document:
    label: PDF
    link: https://drive.google.com/open?id=0B8vqEgF1N0NIZ082U2JETHlSTGs
build:
  source_url: https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/master/src/ontology/doid.obo
  method: obo2owl
  infallible: 1
tracker: https://github.com/DiseaseOntology/HumanDiseaseOntology/issues
publications:
  - id: http://www.ncbi.nlm.nih.gov/pubmed/?term=25348409
    title: "Disease Ontology 2015 update: an expanded and updated database of human diseases for linking biomedical knowledge through disease data"
license:
  url: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0 Universal
usages:
   - user: https://www.alliancegenome.org
    description: Alliance of Genome Resources: MGD, RGD, SGD, FlyBase, WormBase, ZFIN use DO
    examples:
      - url: https://www.alliancegenome.org/search?category=disease
       description: 10,860 DO human Diseases annotated to over 190,000 MOD genes, alleles, disease models and human genes
      - url: https://www.alliancegenome.org/disease/DOID:0080599
       description: The landing page for Coronavirus Infectious Disease
  - user: http://www.informatics.jax.org/disease
    description: MGI disease model annotations use DO
    examples:
      - url: http://www.informatics.jax.org/disease/DOID:4123
        description: Human genes and mouse homology associated with nail diseases
 - user: https://www.iedb.org
    description: Immune Epitope Database
    examples:
      - url: https://www.iedb.org
        description: Search for experimental data on antibody and T cell epitopes associated with human diseases in the DO. To search for DO disease terms, use the Disease search box on the front page.
activity_status: active
repository: https://github.com/DiseaseOntology/HumanDiseaseOntology
---

Creating a comprehensive classification of human diseases organized by etiology.

<u>Additional OBO formatted DO files</u>
- Download DO's asserted is_a OBO file [HumanDO.obo](https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/master/src/ontology/HumanDO.obo). 
This file is equivalent to doid-non-classified.obo.

- DO provides an additional OBO file, [doid-merged.obo](https://raw.githubusercontent.com/DiseaseOntology/HumanDiseaseOntology/master/src/ontology/doid-merged.obo). 
 for the [AGR](http://www.alliancegenome.org) that includes [OMIM](http://omim.org) to DO associations as xrefs plus defined  relationships between OMIM susceptibility IDs and DO terms.  

<img src="http://www.disease-ontology.org/media/images/DO_logo.jpg"/>
