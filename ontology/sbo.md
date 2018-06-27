---
layout: ontology_detail
id: sbo
contact:
  email: sheriff@ebi.ac.uk
  label: Rahuman Sheriff
description: Terms commonly used in Systems Biology, and in particular in computational modeling.
domain: biochemistry
homepage: http://www.ebi.ac.uk/sbo/
products:
  - id: sbo.owl
title: Systems Biology Ontology
build:
  source_url: http://www.ebi.ac.uk/sbo/exports/Main/SBO_OBO.obo
  method: obo2owl
  insert_ontology_id: true
tracker: https://sourceforge.net/p/sbo/term-request/
license:
  url: http://opensource.org/licenses/Artistic-2.0
  label: Artistic License 2.0
---

The Systems Biology Ontology is a set of controlled, relational vocabularies of terms commonly used in Systems Biology, and in particular in computational modeling. The ontology consists of six orthogonal vocabularies defining: the roles of reaction participants (eg. "substrate"), quantitative parameters (eg. "Michaelis constant"), a precise classification of mathematical expressions that describe the system (eg. "mass action rate law"), the modeling framework used (eg. "logical framework"), and a branch each to describe entity (eg. "macromolecule") and interaction (eg. "process") types. SBO terms can be used to introduce a layer of semantic information into the standard description of a model, or to annotate the results of biochemical experiments in order to facilitate their efficient reuse. SBO is an Open Biomedical Ontologies (OBO) candidate ontology, and is free for use. More information about SBO can be found from the project FAQ, at http://www.ebi.ac.uk/sbo/ SBO is a project of the BioModels.net effort and is developed through community collaboration
