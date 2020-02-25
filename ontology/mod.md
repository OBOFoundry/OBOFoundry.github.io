---
layout: ontology_detail
id: mod
contact:
  email: pierre-alain.binz@chuv.ch
  label: Pierre-Alain Binz
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY 4.0
description: PSI-MOD is an ontology consisting of terms that describe protein chemical modifications
domain: proteins
homepage: http://www.psidev.info/MOD
tracker: https://github.com/HUPO-PSI/psi-mod-CV/issues
products:
  - id: mod.owl
title: Protein modification
build:
  source_url: https://raw.githubusercontent.com/MICommunity/psidev/master/psi/mod/data/PSI-MOD.obo
  insert_ontology_id: true
  method: obo2owl
activity_status: active
---

PSI-MOD is an ontology consisting of terms that describe protein chemical modifications, logically linked by an is_a relationship in such a way as to form a direct acyclic graph (DAG). The PSI-MOD ontology has more than 45 top-level nodes, and provides alternative hierarchical paths for classifying protein modifications either by the molecular structure of the modification, or by the amino acid residue that is modified.
