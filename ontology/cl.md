---
layout: ontology_detail
id: cl
label: Cell Ontology
title: Cell Ontology
build:
  checkout: git clone https://github.com/obophenotype/cell-ontology.git
  email_cc: cl_edit@googlegroups.com
  system: git
  method: vcs
  infallible: 1
description: The Cell Ontology is a structured controlled vocabulary for cell types in animals.
integration_server: http://build.berkeleybop.org/job/build-cl/
taxon:
  id: NCBITaxon:33208
  label: Metazoa
domain: cells
tracker: https://code.google.com/p/cell-ontology/issues/list
termgenie: http://cl.termgenie.org
mailing_list: https://lists.sourceforge.net/lists/listinfo/obo-cell-type
dependencies:
 - id: uberon
 - id: go
canonical: cl.owl
products:
 - id: cl.owl
 - id: cl.obo
 - id: cl/cl-basic.obo
---

The Cell Ontology is designed as a structured controlled vocabulary for cell types. This ontology was constructed for use by the model organism and other bioinformatics databases, where there is a need for a controlled vocabulary of cell types. This ontology is not organism specific it covers cell types from prokaryotes to mammals. However, it excludes plant cell types, which are covered by PO.
