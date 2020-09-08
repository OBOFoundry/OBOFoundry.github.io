---
layout: ontology_detail
id: obib
title: Ontology for Biobanking
contact:
  email: jiezheng@pennmedicine.upenn.edu
  label: Jie Zheng
description: An ontology built for annotation and modeling of biobank repository and biobanking administration
domain: biobanking, specimens, bio-repository, biocuration
homepage: https://github.com/biobanking/biobanking
products:
  - id: obib.owl
tracker: https://github.com/biobanking/biobanking/issues
usages:
 - user: https://github.com/PennTURBO/turbo-ontology
   description: TURBO ontology supporting the PennTURBO project.
   examples:
    - url: http://purl.obolibrary.org/obo/OBIB_0000079
      description: Blood draw time
 - user: https://github.com/MIABIS/miabis
   description: The Minimum Information About BIobank data Sharing (MIABIS) aims to standardize data elements used to describe biobanks, research on samples and associated data. General attributes to describe biobanks, sample collections and studies at an aggregated/metadata level are defined in MIABIS Core 2.0 (Merino-Martinez et al., 2016).
 - user: https://biospecimens.cancer.gov/resources/vocabularies.asp
   description: The National Cancer Institute Biorepositories and Biospecimen Research Branch (BBRB) is an international leader in research and policy activities related to biospecimen collection, processing, and storage, also known as biobanking.
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY  
activity_status: active
---

The Ontology for Biobanking (OBIB) is an ontology for the annotation and modeling of the activities, contents, and administration of a biobank. Biobanks are facilities that store specimens, such as bodily fluids and tissues, typically along with specimen annotation and clinical data. OBIB is based on a subset of the Ontology for Biomedical Investigation (OBI), has the Basic Formal Ontology (BFO) as its upper ontology, and is developed following OBO Foundry principles. The first version of OBIB resulted from the merging of two existing biobank-related ontologies, OMIABIS and biobank ontology.
