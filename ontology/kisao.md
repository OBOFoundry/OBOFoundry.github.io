---
layout: ontology_detail
id: kisao
contact:
  email: jonrkarr@gmail.com
  label: Jonathan Karr
  github: jonrkarr
  orcid: 0000-0002-2605-5080
description: A classification of algorithms for simulating biology, their parameters, and their outputs
domain: simulation
tags:
  - systems biology
  - computational biology
  - mathematical modeling
  - numerical simulation
  - simulation algorithms
homepage: https://github.com/SED-ML/KiSAO
releases: https://github.com/SED-ML/KiSAO/releases
tracker: https://github.com/SED-ML/KiSAO/issues
products:
  - id: kisao.owl
title: Kinetic Simulation Algorithm Ontology
build:
  source_url: https://raw.githubusercontent.com/SED-ML/KiSAO/deploy/kisao.owl
  method: owl2obo
license:
  url: http://opensource.org/licenses/Artistic-2.0
  label: Artistic License 2.0
activity_status: active
repository: https://github.com/SED-ML/KiSAO
preferredPrefix: KISAO
usages:
  - user: https://sed-ml.org/
    type: annotation
    description: The Simulation Experiment Description Markup Language (SED-ML) is a language for describing simulations and visualizations of their results.
    examples:
      - url: https://sed-ml.org/examples.html
        description: "Several examples of simulations encoded in SED-ML"
  - user: https://biosimulations.org/
    type: annotation
    description: BioSimulations is a repository of biosimulation projects.
    examples:
      - url: https://biosimulations.org/projects/Repressilator-Elowitz-Nature-2000
        description: "Simulation of a synthetic oscillatory biochemical network"
  - user: https://run.biosimulations.org/
    type: annotation
    description: runBioSimulations is a web application for execution biological simulations.
    examples:
      - url: https://run.biosimulations.org/runs?try=1
        description: "Example simulation runs"
  - user: https://biosimulators.org/
    seeAlso: https://arxiv.org/abs/2203.06732
    type: annotation
    description: BioSimulators is a registry of biosimulation tools.
    examples:
      - url: https://biosimulators.org/simulators/tellurium
        description: "tellurium is a software tool for kinetic simulation of biochemical networks"
browsers:
  - label: OLS
    title: Ontology Lookup Service
    url: https://www.ebi.ac.uk/ols/ontologies/kisao
  - label: BioPortal
    title: BioPortal
    url: https://bioportal.bioontology.org/ontologies/KISAO
  - label: OntoBee
    title: OntoBee
    url: https://www.ontobee.org/ontology/KISAO
publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/22027554
    title: "Controlled vocabularies and semantics in systems biology"
funded_by:
  - "NIH P41EB023912"
  - "NIH R35GM119771"
---

The Kinetic Simulation Algorithm Ontology (KiSAO) describes algorithms for simulating models in biology, their parameters, and their outputs.
