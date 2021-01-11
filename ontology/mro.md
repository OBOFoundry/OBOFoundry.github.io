---
layout: ontology_detail
id: mro
title: MHC Restriction Ontology
description: An ontology for Major Histocompatibility Complex (MHC) restriction in experiments
tracker: https://github.com/IEDB/MRO/issues
homepage: https://github.com/IEDB/MRO
domain: Major Histocompatibility Complex
contact:
  label: Bjoern Peters
  email: bpeters@lji.org
  github: bpeters42
license:
  url: https://creativecommons.org/licenses/by/3.0/
  label: CC-BY
products:
  - id: mro.owl
usages:
  - user: https://www.iedb.org/
    type: annotation
    description: MRO is used by the The Immune Epitope Database (IEDB) annotations
    examples:
      - url: https://www.iedb.org/assay/1357035
        description: "Epitope ID: 59611 based on reference 1003499"
    publications:
      - id: https://doi.org/10.1093/nar/gky1006
        title: "The Immune Epitope Database (IEDB): 2018 update"
activity_status: active
---

The MHC Restriction Ontology (MRO) is an application ontology capturing how Major Histocompatibility Complex (MHC) restriction is defined in experiments, spanning exact protein complexes, individual protein chains, serotypes, haplotypes and mutant molecules, as well as evidence for MHC restrictions.
