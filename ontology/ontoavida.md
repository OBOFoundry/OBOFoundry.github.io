---
layout: ontology_detail
id: ontoavida
title: 'OntoAvida: ontology for Avida digital evolution platform'
browsers:
- title: Ontoavida HTML Browser
  label: Human-readable (HTML)
  url: https://owl.fortunalab.org/ontoavida/
contact:
  email: fortuna@ebd.csic.es
  github: fortunalab
  label: Miguel A. Fortuna
  orcid: 0000-0002-8374-1941
dependencies:
- id: fbcv
- id: gsso
- id: ncit
- id: ro
- id: stato
description: OntoAvida develops an integrated vocabulary for the description of the most widely-used computational approach for studying evolution using digital organisms (i.e., self-replicating computer programs that evolve within a user-defined computational environment).
domain: simulation
homepage: https://gitlab.com/fortunalab/ontoavida
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: ONTOAVIDA
products:
  - id: ontoavida.owl
    title: OWL
    description: The main ontology in OWL
    page: https://gitlab.com/fortunalab/ontoavida/-/raw/master/ontoavida.owl
  - id: ontoavida.obo
    title: OBO
    description: Equivalent to ontoavida.owl, in obo format
    page: https://gitlab.com/fortunalab/ontoavida/-/raw/master/ontoavida.obo

publications:
  - id: https://doi.org/10.1038/s41597-023-02514-3
    title: "Ontology for the Avida digital evolution platform"
repository: https://gitlab.com/fortunalab/ontoavida
tags:
- digital evolution
- artificial life
tracker: https://gitlab.com/fortunalab/ontoavida/-/issues
activity_status: active
usages:
  - user: https://cran.r-project.org/package=avidaR
    description: An R package—avidaR—uses OntoAvida to perform complex queries on an RDF database—avidaDB—containing the genomes, transcriptomes, and phenotypes of more than a million digital organisms
    examples:
      - url: http://doi.org/10.7717/peerj-cs.1568
        description: "avidaR: an R library to perform complex queries on an ontology-based database of digital organisms"
---
<img  src="https://fortunalab.org/images/alife_bacteria.jpg" style="padding-right:20px; padding-bottom:10px;" height="150px" align="left"/>The **Ontology for Avida ([OntoAvida](https://owl.fortunalab.org/ontoavida/))** aims to develop an integrated vocabulary for the description of [Avida](https://github.com/devosoft/avida), the most widely used computational approach for performing experimental evolution using digital organisms–self-replicating computer programs that evolve within a user-defined computational environment. The lack of a clearly defined vocabulary makes some biologists feel reluctant to embrace the field of digital evolution. This integrated framework empowers biologists by equipping them with the necessary tools to explore and analyze the field of digital evolution more effectively. By leveraging the vocabulary of Avida, researchers can gain deeper insights into the evolutionary processes and dynamics of digital organisms. In addition, OntoAvida allows researchers to make inference based on certain rules and constraints, facilitate the reproducibility of [in silico evolution experiments](https://gitlab.com/fortunalab/ontoavida#references) and trace the provenance of the data stored in avidaDB–an RDF database containing the genomes, transcriptomes, and phenotypes of more than a million digital organisms.
