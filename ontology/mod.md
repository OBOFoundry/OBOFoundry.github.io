---
layout: ontology_detail
id: mod
title: Protein modification
build:
  insert_ontology_id: true
  method: obo2owl
  source_url: https://raw.githubusercontent.com/HUPO-PSI/psi-mod-CV/master/PSI-MOD.obo
contact:
  email: pierre-alain.binz@chuv.ch
  github: pabinz
  label: Pierre-Alain Binz
  orcid: 0000-0002-0045-7698
description: PSI-MOD is an ontology consisting of terms that describe protein chemical modifications
domain: chemistry and biochemistry
homepage: http://www.psidev.info/MOD
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: MOD
products:
- id: mod.owl
  title: PSI-MOD.owl
  description: PSI-MOD Ontology, OWL format
- id: mod.obo
  title: PSI-MOD.obo
  description: PSI-MOD Ontology, OBO format
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/18688235
  title: The PSI-MOD community standard for representation of protein modification data
repository: https://github.com/HUPO-PSI/psi-mod-CV
tags:
- proteins
tracker: https://github.com/HUPO-PSI/psi-mod-CV/issues
activity_status: active
---

PSI-MOD is an ontology consisting of terms that describe protein chemical modifications, logically linked by an is_a relationship in such a way as to form a direct acyclic graph (DAG). The PSI-MOD ontology has more than 45 top-level nodes, and provides alternative hierarchical paths for classifying protein modifications either by the molecular structure of the modification, or by the amino acid residue that is modified.
