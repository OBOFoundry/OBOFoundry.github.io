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

MonDO (Monarch Disease Ontology) is a semi-automatically constructed ontology that merges in multiple disease resources to yield a coherent merged ontology. Original versions of MonDO were constructed entirely automatically. Later additional manually curated cross-ontology axioms were added. Currently construction also involves a significant amount of manual curation on merged classes.

There are currently 4 versions available, a combination of two criteria:

 - the `pre` version uses MONDO IDs as primary. This will likely be the shape of future versions
 - the main version uses clique leaders from source ontologies as primary
 - the .owl version of the main version uses equivalence axioms to connect clique leaders to equivalent classes in other ontologies/sources
 - the .owl version of the pre version uses equivalence axioms to connect MONDO classes to equivalent classes in other ontologies/sources.
  - the owl versions also have additional axiomatization following standard design patterns
  - the .obo versions are simpler, lack full axiomatization, and lack equivalence axioms to other diseases; instead xrefs are used as the linking mechanism.
  
Trackers

 - https://github.com/monarch-initiative/monarch-disease-ontology/issues - original tracker, primarily for examining kboom output and for feeding back changes to sources
 - https://github.com/monarch-initiative/mondo-build/issues - new tracker primarily for curating the grouped classes
