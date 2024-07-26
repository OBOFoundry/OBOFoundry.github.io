---
layout: ontology_detail
id: stato
title: The Statistical Methods Ontology
contact:
  email: proccaserra@gmail.com
  github: proccaserra
  label: Philippe Rocca-Serra
  orcid: 0000-0001-9853-5668
depicted_by: https://raw.githubusercontent.com/ISA-tools/stato/dev/images/stato-logo-3.png
description: STATO is a general-purpose STATistics Ontology. Its aim is to provide coverage for processes such as statistical tests, their conditions of application, and information needed or resulting from statistical methods, such as probability distributions, variables, spread and variation metrics. STATO also covers aspects of experimental design and description of plots and graphical representations commonly used to provide visual cues of data distribution or layout and to assist review of the results.
domain: information technology
homepage: http://stato-ontology.org/
in_foundry: false
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: STATO
products:
- id: stato.owl
publications:
- id: https://doi.org/10.1038/s41597-019-0286-0
  title: 'Experiment design driven FAIRification of omics data matrices, an exemplar'
- id: https://doi.org/10.1038/s41597-020-0409-7
  title: 'Semantic concept schema of the linear mixed model of experimental observations'
repository: https://github.com/ISA-tools/stato
tags:
- statistics
tracker: https://github.com/ISA-tools/stato/issues
usages:
- description: an R/Bioconductor package, named struct (Statistics in R using Class-based Templates), which defines a suite of class-based templates that allows users to develop and implement highly standardized and readable statistical analysis workflows. Struct integrates with the STATistics Ontology to ensure consistent reporting and maximizes semantic interoperability
  publications:
  - id: https://doi.org/10.1101/2021.10.10.463703
    title: 'struct: an R/Bioconductor-based framework for standardized metabolomics data analysis and beyond'
  type: annotation
  user: https://bioconductor.org/packages/release/bioc/html/struct.html
- description: Scientific Evidence Code System (SEVCO) on the FEvIR platform. The FEvIR Platform includes many Builder Tools to create FHIR Resources without requiring expertise in FHIR or JSON, and Converter Tools to convert structured data to FHIR Resources
  publications:
  - id: https://doi.org/10.1016/j.jbi.2021.103685
    title: 'Making science computable: Developing code systems for statistics, study design, and risk of bias'
  type: annotation
  user: https://fevir.net/resources/CodeSystem/27270#STATO:0000039
- description: PSI-MS CV
  publications:
  - id: https://doi.org/10.1093/database/bat009
    title: 'The HUPO proteomics standards initiative- mass spectrometry controlled vocabulary.'
  type: annotation
  user: https://github.com/HUPO-PSI/psi-ms-CV
- description: OBCS
  publications:
  - id: https://doi.org/10.1186/s13326-016-0100-2
    title: 'The Ontology of Biological and Clinical Statistics (OBCS) for standardized and reproducible statistical analysis'
  type: annotation
  user: https://github.com/obcs/obcs
activity_status: active
---

The STATistics Ontology (STATO) project started in early 2012, as part of the requirement of the community-driven ISA Commons to represent the results of data analysis. STATO is a standalone project since Nov 2012. STATO is driven and funded by several ISA-based projects and their user community, but also by collaborations with data publication platforms. STATO is applicable to, but not limited, the broad life, natural and biomedical science domain with documented applications for factorial design, association studies, differential expression, hit selection and meta-analysis. STATO has been developed to interoperate with other OBO Foundry ontologies, hence relies on the Basics Formal Ontology (BFO) as a top level ontology and uses the Ontology for Biomedical Investigations (OBI) as mid-level ontology.

 * To refer to the most current  information on the STATO project, please visit [STATO website](http://stato-ontology.org/)
 * The latest version of the ontology file (.owl) will always be available from [STATO Github repository]()
 * To use STATO, remember the licensing terms: STATO is released under [CC-by 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/)
