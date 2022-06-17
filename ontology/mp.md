---
layout: ontology_detail
id: mp
title: Mammalian Phenotype Ontology
license:
  url: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
build:
  checkout: git clone https://github.com/mgijax/mammalian-phenotype-ontology.git
  system: git
  path: "."
description: Standard terms for annotating mammalian phenotypic data.
homepage: http://www.informatics.jax.org/searches/MP_form.shtml
page: https://github.com/mgijax/mammalian-phenotype-ontology
contact:
  email: drsbello@gmail.com
  label: Sue Bello
  github: sbello
  orcid: 0000-0003-4606-0597
domain: phenotype
products:
  - id: mp.owl
    title: "MP (OWL edition)"
    description: "The main ontology in OWL. Contains all MP terms and links to other OBO ontologies."
    page: https://github.com/mgijax/mammalian-phenotype-ontology/releases/tag/current
  - id: mp.obo
    title: "MP (OBO edition)"
    description: "A direct translation of the MP (OWL edition) into OBO format."
    page: https://github.com/mgijax/mammalian-phenotype-ontology/releases/tag/current
  - id: mp.json
    title: MP (obographs JSON edition)
    description: "For a description of the format see https://github.com/geneontology/obographs."
    page: https://github.com/mgijax/mammalian-phenotype-ontology/releases/tag/current
  - id: mp/mp-base.owl
    title: MP Base Module
    description: "The main ontology plus axioms connecting to select external ontologies, excluding axioms from the the external ontologies themselves."
    page: https://github.com/mgijax/mammalian-phenotype-ontology/releases/tag/current
publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/22961259
    title: "The Mammalian Phenotype Ontology as a unifying standard for experimental and high-throughput phenotyping data"
browsers:
  - label: MGI
    title: MGI MP Browser
    url: http://www.informatics.jax.org/searches/MP_form.shtml
  - label: RGD
    title: RGD MP Browser
    url: https://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=MP:0000001
  - label: Monarch
    title: Monarch Phenotype Page
    url: http://monarchinitiative.org/phenotype/MP:0000001
usages:
  - user: http://www.informatics.jax.org/vocab/mp_ontology
    description: MGI annotates phenotypes of mouse models using the MP
    examples:
      - url: http://www.informatics.jax.org/vocab/mp_ontology/MP:0008762
        description: "Term browser page for embryonic lethality showing information about the term including definition, placement in the MP hierarchy, and link to mouse models annotated to this term or any of its decendants"
  - user: https://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=MP:0000001
    description: RGD annotates phenotypes associated with rat genes and alleles using the MP
    examples:
      - url: https://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=MP:0008762
        description: "Term browser page for embryonic lethality showing information about the term including definition, placement in the MP hierarchy, and link to annotations to this term or any of its decendants"
  - user: https://www.mousephenotype.org/
    description: "IMPC annotates abnormal phenotypes of mice carrying null alleles found following the application of a standardised set of physiological tests"
    examples:
      - url: https://www.mousephenotype.org/data/phenotypes/MP:0013522
        description: "All IMPC alleles that have been annotated to the MP term 'decreased memory-marker CD4-positive NK T cell number'."
jobs:
  - id: http://build.berkeleybop.org/job/build-mp-edit
    type: DryRunBuild
taxon:
  id: NCBITaxon:40674
  label: Mammalia
tracker: https://github.com/mgijax/mammalian-phenotype-ontology/issues
mailing_list: https://groups.google.com/forum/#!forum/phenotype-ontologies-editors
activity_status: active
repository: https://github.com/mgijax/mammalian-phenotype-ontology
preferredPrefix: MP
added: 2015-07-28
---

The Mammalian Phenotype Ontology is under development as a community effort to provide standard terms for annotating mammalian phenotypic data.
