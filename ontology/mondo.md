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
browsers:
  - label: Monarch
    title: Monarch Initiative Disease Browser
    url: https://monarchinitiative.org/disease/DOID:14330
products:
 - id: mondo.owl
   title: Main OWL edition
   description: Complete ontology, plus inter-ontology equivalence axioms. Uses identifiers of contributing ontologies.
   format: owl-rdf/xml
   is_canonical: true
 - id: mondo.obo
   title: obo-format edition
   description: As OWL, but omits equivalence axioms. xrefs can be used as proxy for equivalence. Uses identifiers of contributing ontologies.
   format: obo
   derived_from: mondo.owl
 - id: pre/mondo.owl
   title: Preview of new OWL edition
   description: Complete ontology, plus inter-ontology equivalence axioms. Uses MONDO identifiers.
   format: owl-rdf/xml
 - id: pre/mondo.obo
   title: Preview of new OBO edition
   description: Complete ontology, but omits inter-ontology equivalence axioms. Uses MONDO identifiers.
   format: obo
---

MonDO (Monarch Disease Ontology) is a semi-automatically constructed ontology that merges in multiple disease resources to yield a coherent merged ontology.
