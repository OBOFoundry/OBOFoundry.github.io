---
layout: ontology_detail
id: oae
title: Ontology of Adverse Events
contact:
  email: yongqunh@med.umich.edu
  github: yongqunh
  label: Yongqunh He
  orcid: 0000-0001-9189-9661
description: A biomedical ontology in the domain of adverse events
domain: health
homepage: https://github.com/OAE-ontology/OAE/
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
preferredPrefix: OAE
products:
- id: oae.owl
repository: https://github.com/OAE-ontology/OAE
tags:
- adverse events
tracker: https://github.com/OAE-ontology/OAE/issues
activity_status: active

publications:
- id: https://pubmed.ncbi.nlm.nih.gov/25093068/
  title: OAE - The Ontology of Adverse Events
- id: https://pubmed.ncbi.nlm.nih.gov/41526409/
  title: The Ontology of Adverse Events in 2025

usages:
- description: Using OAE to support the classification and analysis of VAERS vaccine adverse event reporting system data analysis.
  examples:
  - description: OAE was used to analyze and differentiate adverse events associated with inactivated and live attenuated influenza vaccines reported in VAERS
    url: https://pubmed.ncbi.nlm.nih.gov/23209624/
  - description: OAE was used to analyze COVID-19 vaccine adverse events reported in VAERS
    url: https://pubmed.ncbi.nlm.nih.gov/35814246/
  - description: OAE was used to analyze adverse events associated with monovalent and combination vaccines against Hepatitis A and B diseases reported in VAERS
    url: https://pubmed.ncbi.nlm.nih.gov/27694888/
  user: biomedical researchers
- description: Using OAE to analyze vaccine adverse event using FDA vaccine package insert documents
  examples:
  - description: OAE was used to unveil differential vaccine adverse events via LLM text embeddings of FDA vaccine package insert documents
    url: https://pubmed.ncbi.nlm.nih.gov/40410898/
  user: biomedical researchers
- description: Using OAE to analyze vaccine adverse events reported in PubMed papers
  examples:
  - description: OAE was used to classify human and animal adverse events associated with different Brucella animal vaccines as reported in PubMed literature
    url: https://pubmed.ncbi.nlm.nih.gov/40410898/
  user: biomedical researchers
- description: VIOLIN vaccine resource uses OAE to represent vaccine adverse event information.
  examples:
  - description: The VIOLIN vaccine safety database (Vaxafe) uses OAE to map adverse event information in vaccine adverse event case reports, for example, Vaxafe uses OAE to represent many adverse events (such as Convulsion, Cough) reported in a VAERS case ID - 204308.
    url: https://violinet.org/vaxafe/case.php?vaers_id=204308
  user: https://violinet.org/  
---

The Ontology of Adverse Events (OAE) is a biomedical ontology in the domain of adverse events. OAE aims to standardize adverse event annotation, integrate various adverse event data, and support computer-assisted reasoning.  OAE is a community-based ontology. Its development follows the OBO Foundry principles.
