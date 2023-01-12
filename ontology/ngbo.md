---
layout: ontology_detail
id: ngbo
title: Next Generation Biobanking Ontology
contact:
  email: dal.alghamdi92@gmail.com
  github: dalalghamdi
  label: Dalia Alghamdi
  orcid: 0000-0002-2801-0767
description: 'The Next Generation Biobanking Ontology (NGBO) is an open application ontology representing contextual data about omics digital assets in biobank. The ontology focuses on capturing the information about three main activities: wet bench analysis used to generate omics data, bioinformatics analysis used to analyze and interpret data, and data management.'
domain: investigations
homepage: https://github.com/Dalalghamdi/NGBO
issue_requested: 1819
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: NGBO
products:
- id: ngbo.owl
pull_request_added: 2214
repository: https://github.com/Dalalghamdi/NGBO
tracker: https://github.com/Dalalghamdi/NGBO/issues
activity_status: active
---
NGBO is developed to represent omics contextual data to support experts in specimen-derivative data  discovery and reuse stages, it includes real-world physical objects such as specimens, computerized objects such as datasets, and planned processes and related specifications. The intended end-users are biobanking organizations, data collectors, omics researchers, and decision-makers. 
NGBO is used to build a federated query platform for the Saudi Human Genome Project (SHGP). SHGP is a genetic database for the Saudi population; the project collects data sets from seven different sites. The federated query platform is freely available and licensed under the Apache License 2.0 at: https://github.com/Dalalghamdi/NGBOProject.
The ontology is maintained in GitHub, and improvement will continue based on community input and feedback from users; also, Since NGBO is an application ontology, NGBO-defined terms will be submitted to relevant domain ontologies. In our future work, we will continue the data curation efforts by completing the metadata management proposal for the Saudi Human Genome Project.
NGBO is built based on Open Biological and Biomedical Ontologies (OBO) Foundry principles. The basic formal ontology (BFO) is used as a top-level ontology for NGBO development. Pre-existing terms from other appropriately maintained ontologies, annotated with proper PURLs, labels, and textual and logical definitions, are imported, preventing multiple representations of the same entity. Examples Include OBI terms that describe entities involved in biomedical investigations, such as, but not limited to, material entities, processes, and protocols, through OWL import. From the ontology for biobanking (OBIB; https://github.com/biobanking/biobanking), terms to describe specimens, donors, and specimen management are imported. Information artifact ontology (IAO; https://github.com/information-artifact-ontology/IAO) is another relevant ontology used as a mid-level ontology and includes terms that describe identifiers, software solutions, and documents. 
