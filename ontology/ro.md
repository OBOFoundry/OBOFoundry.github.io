---
layout: ontology_detail
id: ro
title: Relation Ontology
build:
  checkout: git clone https://github.com/oborel/obo-relations.git
  infallible: 1
  method: vcs
  system: git
canonical: ro.owl
contact:
  email: cjmungall@lbl.gov
  github: cmungall
  label: Chris Mungall
  orcid: 0000-0002-6601-2165
description: Relationship types shared across multiple ontologies
documentation: https://oborel.github.io/obo-relations/
domain: upper
homepage: https://oborel.github.io/
jobs:
- id: https://travis-ci.org/oborel/obo-relations
  type: travis-ci
license:
  label: CC0 1.0
  url: http://creativecommons.org/publicdomain/zero/1.0/
mailing_list: https://groups.google.com/forum/#!forum/obo-relations
preferredPrefix: RO
products:
- id: ro.owl
  title: Relation Ontology
  description: Canonical edition
- id: ro.obo
  title: Relation Ontology in obo format
  description: The obo edition is less expressive than the OWL, and has imports merged in
- id: ro.json
  title: Relation Ontology in obojson format
- id: ro/core.owl
  title: RO Core relations
  description: Minimal subset intended to work with BFO-classes
  page: https://github.com/oborel/obo-relations/wiki/ROCore
- id: ro/ro-base.owl
  title: RO base ontology
  description: Axioms defined within RO and to be used in imports for other ontologies
  page: https://github.com/INCATools/ontology-development-kit/issues/50
- id: ro/subsets/ro-interaction.owl
  title: Interaction relations
  description: For use in ecology and environmental science
- id: ro/subsets/ro-eco.owl
  title: Ecology subset
- id: ro/subsets/ro-neuro.owl
  title: Neuroscience subset
  description: For use in neuroscience
  page: http://bioinformatics.oxfordjournals.org/content/28/9/1262.long
repository: https://github.com/oborel/obo-relations
tags:
- relations
tracker: https://github.com/oborel/obo-relations/issues
usages:
- description: RO is used for annotation extensions in the GO and GO Causal Activity Models.
  examples:
  - description: wg_biogenesis_FlyBase
    url: http://model.geneontology.org/56d1143000003402
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/24885854
    title: A method for increasing expressivity of Gene Ontology annotations using a compositional approach
  type: annotation
  user: http://geneontology.org
activity_status: active
---

![logo](/images/ro_logo.png)

# Summary

RO is a collection of relations intended primarily for standardization across ontologies in the [OBO Foundry](http://obofoundry.org) and wider OBO library. It incorporates [ROCore](https://github.com/oborel/obo-relations/wiki/ROCore) upper-level relations such as [part of](http://purl.obolibrary.org/obo/BFO_0000050) as well as biology-specific relationship types such as [develops from](http://purl.obolibrary.org/obo/RO_0002202).

See the site [Menu](https://github.com/oborel/obo-relations/wiki/Menu) for more info

# Download

Use the following URIs to download this ontology:

 * http://purl.obolibrary.org/obo/ro.owl
 * http://purl.obolibrary.org/obo/ro.obo

Note that the source ontology is OWL - the [OBO](https://github.com/oborel/obo-relations/wiki/OBOFormatUsersGuide) version may have less axioms. Another difference between the two formats is that the OWL makes use of imports, whereas everything is combined into one with the obo file.
