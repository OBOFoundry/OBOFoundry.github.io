---
layout: ontology_detail
id: kisao
title: Kinetic Simulation Algorithm Ontology
browsers:
- title: Ontology Lookup Service
  label: OLS
  url: https://www.ebi.ac.uk/ols/ontologies/kisao
- title: BioPortal
  label: BioPortal
  url: https://bioportal.bioontology.org/ontologies/KISAO
- title: OntoBee
  label: OntoBee
  url: https://www.ontobee.org/ontology/KISAO
build:
  method: owl2obo
  source_url: https://raw.githubusercontent.com/SED-ML/KiSAO/deploy/kisao.owl
contact:
  email: jonrkarr@gmail.com
  github: jonrkarr
  label: Jonathan Karr
  orcid: 0000-0002-2605-5080
description: A classification of algorithms for simulating biology, their parameters, and their outputs
domain: simulation
funded_by:
- id: https://grantome.com/search?q=P41EB023912
  title: NIH P41EB023912
- id: https://grantome.com/search?q=R35GM119771
  title: NIH R35GM119771
homepage: https://github.com/SED-ML/KiSAO
license:
  label: Artistic License 2.0
  url: http://opensource.org/licenses/Artistic-2.0
preferredPrefix: KISAO
products:
- id: kisao.owl
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/22027554
  title: Controlled vocabularies and semantics in systems biology
releases: https://github.com/SED-ML/KiSAO/releases
repository: https://github.com/SED-ML/KiSAO
tags:
- systems biology
- computational biology
- mathematical modeling
- numerical simulation
- simulation algorithms
tracker: https://github.com/SED-ML/KiSAO/issues
usages:
- description: The Simulation Experiment Description Markup Language (SED-ML) is a language for describing simulations and visualizations of their results.
  examples:
  - description: Several examples of simulations encoded in SED-ML
    url: https://sed-ml.org/examples.html
  type: annotation
  user: https://sed-ml.org/
- description: BioSimulations is a repository of biosimulation projects.
  examples:
  - description: Simulation of a synthetic oscillatory biochemical network
    url: https://biosimulations.org/projects/Repressilator-Elowitz-Nature-2000
  type: annotation
  user: https://biosimulations.org/
- description: runBioSimulations is a web application for execution biological simulations.
  examples:
  - description: Example simulation runs
    url: https://run.biosimulations.org/runs?try=1
  type: annotation
  user: https://run.biosimulations.org/
- description: BioSimulators is a registry of biosimulation tools.
  examples:
  - description: tellurium is a software tool for kinetic simulation of biochemical networks
    url: https://biosimulators.org/simulators/tellurium/latest#tab=algorithms
  seeAlso: https://arxiv.org/abs/2203.06732
  type: annotation
  user: https://biosimulators.org/
activity_status: active
---

The Kinetic Simulation Algorithm Ontology (KiSAO) describes algorithms for simulating models in biology, their parameters, and their outputs.
