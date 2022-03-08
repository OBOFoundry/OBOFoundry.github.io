---
layout: ontology_detail
id: mod
contact:
  email: pierre-alain.binz@chuv.ch
  label: Pierre-Alain Binz
  github: pabinz
  orcid: 0000-0002-0045-7698
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
publications:
  - id: https://pubmed.ncbi.nlm.nih.gov/18688235/
    title: "The PSI-MOD community standard for representation of protein modification data"
description: PSI-MOD is an ontology consisting of terms that describe protein chemical modifications
domain: biochemistry
tags:
 - proteins
homepage: http://www.psidev.info/MOD
tracker: https://github.com/HUPO-PSI/psi-mod-CV/issues
products:
  - id: mod.owl
    title: PSI-MOD.owl
    description: PSI-MOD Ontology, OWL format
  - id: mod.obo
    title: PSI-MOD.obo
    description: PSI-MOD Ontology, OBO format
title: Protein modification
build:
  source_url: https://raw.githubusercontent.com/HUPO-PSI/psi-mod-CV/master/PSI-MOD.obo
  insert_ontology_id: true
  method: obo2owl
activity_status: active
repository: https://github.com/HUPO-PSI/psi-mod-CV
preferredPrefix: MOD
---

PSI-MOD is an ontology consisting of terms that describe protein chemical modifications, logically linked by an is_a relationship in such a way as to form a direct acyclic graph (DAG). The PSI-MOD ontology has more than 45 top-level nodes, and provides alternative hierarchical paths for classifying protein modifications either by the molecular structure of the modification, or by the amino acid residue that is modified.
