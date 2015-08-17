---
layout: ontology_detail
id: clo
contact:
  email: Sirarat.Sarntivijai@fda.hhs.gov
  label: Sirarat Sarntivijai
description: An ontology to standardize and integrate cell line information and to support computer-assisted reasoning.
homepage: http://www.clo-ontology.org
products:
  - id: clo.owl
title: Cell Line Ontology
build:
  checkout: svn --ignore-externals co http://clo-ontology.googlecode.com/svn/trunk/src/ontology
  system: svn
  method: vcs
  post_processing_command: owltools --use-catalog clo.owl --merge-imports-closure --ni -o -f obo --no-check clo.obo


---
The Cell Line Ontology (CLO) is a community-driven ontology that is developed to standardize and integrate cell line information and support computer-assisted reasoning.
