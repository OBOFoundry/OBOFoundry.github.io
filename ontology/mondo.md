---
layout: ontology_detail
id: mondo
label: MonDO
title: Monarch Disease Ontology
description: a semi-automatically constructed ontology that merges in multiple disease resources to yield a coherent merged ontology
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
taxon:
  id: NCBITaxon:33208
  label: Metazoa
domain: disease
tracker: https://github.com/monarch-initiative/monarch-disease-ontology/issues
canonical: mondo.owl
products:
 - id: mondo.owl
   title: Main OWL edition
   description: Complete ontology, plus inter-ontology equivalence axioms
   format: owl-rdf/xml
   is_canonical: true
 - id: mondo.obo
   title: obo-format edition
   description: As OWL, but omits equivalence axioms
   format: obo
   derived_from: mondo.owl
---

MonDO (Monarch Disease Ontology) is a semi-automatically constructed ontology that merges in multiple disease resources to yield a coherent merged ontology.
