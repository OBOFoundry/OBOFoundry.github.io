---
layout: ontology_detail
id: psdo
title: Performance Summary Display Ontology
build:
  checkout: https://github.com/Display-Lab/psdo.git
  system: git
  path: "."
contact:
  email: zachll@umich.edu
  label: Zach Landis-Lewis
description: Ontology to reproducibly study visualizations of clinical performance
domain: learning systems
homepage: https://github.com/Display-Lab/psdo
products:
  - id: psdo.owl
dependencies:
 - id: stato
 - id: iao
 - id: bfo
 - id: ro
tracker: https://github.com/Display-Lab/psdo/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
activity_status: active
---

The Performance Summary Display Ontology (PSDO) is a lightweight application ontology used to
reproducibly study visualizations of clinical performance and their associated outcomes in 
healthcare quality improvement settings. 
PSDO extends boundaries of visual representation artifacts by the IAO in the domain of distributed
representations. 
PSDO describes dimensional representations of relational information displays that can be used to
study the influence of feedback interventions on clinical practice.
