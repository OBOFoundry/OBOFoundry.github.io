---
layout: ontology_detail
id: mcro
title: Model Card Report Ontology
contact:
  email: muamith@utmb.edu
  github: ProfTuan
  label: Tuan Amith
  orcid: 0000-0003-4333-1857
dependencies:
- id: iao
- id: swo
description: An ontology representing the structure of model card reports - reports that describe basic characteristics of machine learning models for the public and consumers.
domain: information technology
homepage: https://github.com/UTHealth-Ontology/MCRO
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: MCRO
products:
- id: mcro.owl
publications:
- id: https://doi.org/10.1186/s12859-022-04797-6
  title: Toward a standard formal semantic representation of the model card report
repository: https://github.com/UTHealth-Ontology/MCRO
tracker: https://github.com/UTHealth-Ontology/MCRO/issues
usages:
- description: MCRO used for publishing model cards
  examples:
  - description: Demonstration of Java-based library utilizing MCRO to output RDF-based model card reports
    url: https://github.com/UTHealth-Ontology/MCRO-Software
  publications:
  - id: https://doi.org/10.1145/3543873.3587601
    title: Application of an ontology for model cards to generate computable artifacts for linking machine learning information from biomedical research
  user: https://github.com/UTHealth-Ontology/MCRO-Software
activity_status: active
---

Model card reports are documents detailing transparent metadata information relating to machine learning models [Mitchell, et al., 2019](https://dl.acm.org/doi/10.1145/3287560.3287596). Analogous with drug labels and nutritional labels, the goal of model cards are to communicate relevant information on all aspects of a machine learning model that have undergone any experimentation to stakeholders, developers, end-users, policy makers, etc. Typically they are short static documents that outline the machine learning models' meta information (e.g.,name of the model, creators, licensing, versioning), performance and limitation information (e.g., evaluation metrics, datasets evaluated, training data), ethical particulars (e.g., risks, sensitive data, harm reduction), potential users (e.g., impacted users, primary users), etc. 

The National Institutes of Health, through their Bridge2AI initiative, expressed interest in model cards as an artifact to communicate specifics and promote transparency for AI-based machine learning models in biomedical research. However, these reports are presented in static documents, and have the potential to impede any possible retrieval, analysis, and aggregation of these reports. Model card reports translated as RDF-based formats could help in this effort, including supplementing application tools to analyze AI-based machine learning models.

This work encodes the various structures of model card reports and align them to standard OBO Foundry ontologies (specifically the Information Artifact Ontology and the Software Ontology) to help formalize and enrich these documents, and essentially make these reports computable for indexing, searching and aggregation.


