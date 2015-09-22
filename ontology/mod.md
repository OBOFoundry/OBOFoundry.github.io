---
layout: ontology_detail
id: mod
contact:
  email: hhe@ebi.ac.uk
  label: Henning Hermjakob
description: PSI-MOD is an ontology consisting of terms that describe protein chemical modifications
domain: proteins
homepage: http://www.psidev.info/MOD
products:
  - id: mod.owl
title: Protein modification
build:
  source_url: http://psidev.cvs.sourceforge.net/viewvc/psidev/psi/mod/data/PSI-MOD.obo
  method: obo2owl
---

PSI-MOD is an ontology consisting of terms that describe protein chemical modifications, logically linked by an is_a relationship in such a way as to form a direct acyclic graph (DAG). The PSI-MOD ontology has more than 45 top-level nodes, and provides alternative hierarchical paths for classifying protein modifications either by the molecular structure of the modification, or by the amino acid residue that is modified.
