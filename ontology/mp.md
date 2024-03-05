---
layout: ontology_detail
id: mp
title: Mammalian Phenotype Ontology
browsers:
- title: MGI MP Browser
  label: MGI
  url: http://www.informatics.jax.org/searches/MP_form.shtml
- title: RGD MP Browser
  label: RGD
  url: https://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=MP:0000001
- title: Monarch Phenotype Page
  label: Monarch
  url: http://monarchinitiative.org/phenotype/MP:0000001
contact:
  email: drsbello@gmail.com
  github: sbello
  label: Sue Bello
  orcid: 0000-0003-4606-0597
depicted_by: https://raw.githubusercontent.com/mgijax/mammalian-phenotype-ontology/main/logo/2024_MP_logo_RGB_ICON_color.png
description: Standard terms for annotating mammalian phenotypic data.
domain: phenotype
homepage: http://www.informatics.jax.org/searches/MP_form.shtml
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
mailing_list: https://groups.google.com/forum/#!forum/phenotype-ontologies-editors
page: https://github.com/mgijax/mammalian-phenotype-ontology
preferredPrefix: MP
products:
- id: mp.owl
  title: MP (OWL edition)
  description: The main ontology in OWL. Contains all MP terms and links to other OBO ontologies.
  page: https://github.com/mgijax/mammalian-phenotype-ontology/releases/tag/current
- id: mp.obo
  title: MP (OBO edition)
  description: A direct translation of the MP (OWL edition) into OBO format.
  page: https://github.com/mgijax/mammalian-phenotype-ontology/releases/tag/current
- id: mp.json
  title: MP (obographs JSON edition)
  description: For a description of the format see https://github.com/geneontology/obographs.
  page: https://github.com/mgijax/mammalian-phenotype-ontology/releases/tag/current
- id: mp/mp-base.owl
  title: MP Base Module
  description: The main ontology plus axioms connecting to select external ontologies, excluding axioms from the the external ontologies themselves.
  page: https://github.com/mgijax/mammalian-phenotype-ontology/releases/tag/current
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/22961259
  title: The Mammalian Phenotype Ontology as a unifying standard for experimental and high-throughput phenotyping data
repository: https://github.com/mgijax/mammalian-phenotype-ontology
taxon:
  id: NCBITaxon:40674
  label: Mammalia
tracker: https://github.com/mgijax/mammalian-phenotype-ontology/issues
usages:
- description: MGI annotates phenotypes of mouse models using the MP
  examples:
  - description: Term browser page for embryonic lethality showing information about the term including definition, placement in the MP hierarchy, and link to mouse models annotated to this term or any of its decendants
    url: http://www.informatics.jax.org/vocab/mp_ontology/MP:0008762
  user: http://www.informatics.jax.org/vocab/mp_ontology
- description: RGD annotates phenotypes associated with rat genes and alleles using the MP
  examples:
  - description: Term browser page for embryonic lethality showing information about the term including definition, placement in the MP hierarchy, and link to annotations to this term or any of its decendants
    url: https://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=MP:0008762
  user: https://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=MP:0000001
- description: IMPC annotates abnormal phenotypes of mice carrying null alleles found following the application of a standardised set of physiological tests
  examples:
  - description: All IMPC alleles that have been annotated to the MP term 'decreased memory-marker CD4-positive NK T cell number'.
    url: https://www.mousephenotype.org/data/phenotypes/MP:0013522
  user: https://www.mousephenotype.org/
activity_status: active
---

The Mammalian Phenotype Ontology is under development as a community effort to provide standard terms for annotating mammalian phenotypic data.
