---
layout: ontology_detail
id: ro
title: Relations Ontology
build:
  checkout: svn co http://obo-relations.googlecode.com/svn/trunk/src/ontology
  system: svn
  method: vcs
  infallible: 1
canonical: ro.owl
description: Relationship types shared across multiple ontologies
homepage: https://github.com/oborel/obo-relations/
tracker: https://github.com/oborel/obo-relations/issues
mailing_list: https://lists.sourceforge.net/lists/listinfo/obo-relations
domain: relations
contact:
  email: cjmungall@lbl.gov
  label: Chris Mungall
jobs:
  - id: http://build.berkeleybop.org/job/build-ro
    type: DryRunBuild
products:
 - id: ro.owl
   title: Relation Ontology
 - id: ro.obo
   title: Relation Ontology in obo format
 - id: ro/core.owl
   title: Core relations
   description: Minimal subset intended to work with BFO-classes
 - id: ro/subsets/ro-interaction.owl
   title: Interaction relations
 - id: ro/subsets/ro-eco.owl
   title: Ecology subset
 - id: ro/subsets/ro-neuro.owl
   title: Neuroscience subset
license:
  url: https://creativecommons.org/licenses/by/3.0/
  label: CC-BY
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
