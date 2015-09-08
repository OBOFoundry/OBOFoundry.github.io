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
license:
  url: https://creativecommons.org/licenses/by/3.0/
  label: CC-BY
taxon:
  id: NCBITaxon:33208
  label: Metazoa
domain: cells
tracker: https://github.com/obophenotype/cell-ontology/issues
termgenie: http://cl.termgenie.org
mailing_list: https://lists.sourceforge.net/lists/listinfo/obo-cell-type
dependencies:
 - id: uberon
 - id: go
canonical: cl.owl
products:
 - id: cl.owl
   title: Main CL OWL edition
   description: Complete ontology, plus inter-ontology axioms, and imports modules
   format: owl-rdf/xml
   is_canonical: true
   uses: [uberon, chebi, go, pr, pato]
 - id: cl.obo
   title: CL obo format edition
   description: Complete ontology, plus inter-ontology axioms, and imports modules merged in
   format: obo
   derived_from: cl.owl
 - id: cl/cl-basic.obo
   title: Basic CL
   description: Basic version, no inter-ontology axioms
   format: obo
---

The Cell Ontology is designed as a structured controlled vocabulary for cell types. This ontology was constructed for use by the model organism and other bioinformatics databases, where there is a need for a controlled vocabulary of cell types. This ontology is not organism specific it covers cell types from prokaryotes to mammals. However, it excludes plant cell types, which are covered by PO.
