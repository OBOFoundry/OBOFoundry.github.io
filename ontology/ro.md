---
layout: ontology_detail
id: ro
title: Relation Ontology
build:
  checkout:  git clone https://github.com/oborel/obo-relations.git
  system: git
  method: vcs
  infallible: 1
canonical: ro.owl
aberowl_id: relo
description: Relationship types shared across multiple ontologies
homepage: https://github.com/oborel/obo-relations/
documentation: https://github.com/oborel/obo-relations/wiki/ROGuide
tracker: https://github.com/oborel/obo-relations/issues
mailing_list: "https://groups.google.com/forum/#!forum/obo-relations"
domain: relations
contact:
  email: cjmungall@lbl.gov
  label: Chris Mungall
jobs:
  - id: http://build.berkeleybop.org/job/build-ro
    type: DryRunBuild
  - id: https://travis-ci.org/oborel/obo-relations
    type: travis-ci
products:
 - id: ro.owl
   title: Relation Ontology
   description: Canonical edition
 - id: ro.obo
   title: Relation Ontology in obo format
   description: Has imports merged in
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
license:
  url: http://creativecommons.org/publicdomain/zero/1.0/
  label: CC-0
usages:
 - user: http://geneontology.org
   type: annotation
   description: RO is used for annotation extensions in the GO
   reference: https://doi.org/10.1186/1471-2105-15-155
 - user: http://geneontology.org
   type: annotation
   description: RO is used for GO Causal Activity Models
   examples:
    - http://model.geneontology.org/56d1143000003402
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
