---
layout: ontology_detail
id: ogms
title: Ontology for General Medical Science
contact:
  email: baeverma@jcvi.org
  github: BAevermann
  label: Brian Aevermann
  orcid: 0000-0003-1346-1327
depicted_by: https://avatars2.githubusercontent.com/u/12973154?s=200&v=4
description: An ontology for representing treatment of disease and diagnosis and on carcinomas and other pathological entities
domain: health
homepage: https://github.com/OGMS/ogms
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
preferredPrefix: OGMS
products:
- id: ogms.owl
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/21347182
  title: Toward an ontological treatment of disease and diagnosis
  preferred: true
- id: https://www.ncbi.nlm.nih.gov/pubmed/25991121
  title: Biomarkers in the Ontology for General Medical Science
repository: https://github.com/OGMS/ogms
tags:
- medicine
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
tracker: https://github.com/OGMS/ogms/issues
usages:
- description: Multiple ontologies using OGMS terms, such as the Ontology for Biomedical Investigations (OBI), Relation Ontology (RO), Infectious Disease Ontology (IDO), Representation of Social Entities (OMRSE), and Mental Disease Ontology (MFOMD). OGMS has been extended to create various OBO ontologies, including the IDO and its extensions, as well as the OMRSE, MFOMD, Oral Health and Disease ontology (OHD), and Cardiovascular Disease Ontology (CVDO).
  examples:
  - description: List of ontologies using at least one OGMS term
    url: http://dashboard.obofoundry.org/dashboard/ogms/dashboard.html
  - description: List of ontologies using the term "disease"
    url: https://ontobee.org/ontology/OGMS?iri=http://purl.obolibrary.org/obo/OGMS_0000031
  user: (multiple)
activity_status: active
---

The Ontology for General Medical Science (OGMS) is based on the papers Toward an Ontological Treatment of Disease and Diagnosis and On Carcinomas and Other Pathological Entities. The ontology attempts to address some of the issues raised at the Workshop on Ontology of Diseases (Dallas, TX) and the Signs, Symptoms, and Findings Workshop(Milan, Italy). OGMS was formerly called the clinical phenotype ontology. Terms from OGMS hang from the Basic Formal Ontology. See http://ontology.buffalo.edu/medo/Disease_and_Diagnosis.pdf
