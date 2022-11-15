---
layout: ontology_detail
id: sbo
title: Systems Biology Ontology
build:
  insert_ontology_id: true
  method: obo2owl
  source_url: http://www.ebi.ac.uk/sbo/exports/Main/SBO_OBO.obo
contact:
  email: sheriff@ebi.ac.uk
  github: rsmsheriff
  label: Rahuman Sheriff
  orcid: 0000-0003-0705-9809
description: Terms commonly used in Systems Biology, and in particular in computational modeling.
domain: chemistry and biochemistry
github_date_added: 2015-07-28
homepage: http://www.ebi.ac.uk/sbo/
license:
  label: Artistic License 2.0
  url: http://opensource.org/licenses/Artistic-2.0
preferredPrefix: SBO
products:
- id: sbo.owl
repository: https://github.com/EBI-BioModels/SBO
tracker: https://github.com/EBI-BioModels/SBO/issues
activity_status: active
---

The Systems Biology Ontology is a set of controlled, relational vocabularies of terms commonly used in Systems Biology, and in particular in computational modeling. The ontology consists of six orthogonal vocabularies defining: the roles of reaction participants (eg. "substrate"), quantitative parameters (eg. "Michaelis constant"), a precise classification of mathematical expressions that describe the system (eg. "mass action rate law"), the modeling framework used (eg. "logical framework"), and a branch each to describe entity (eg. "macromolecule") and interaction (eg. "process") types. SBO terms can be used to introduce a layer of semantic information into the standard description of a model, or to annotate the results of biochemical experiments in order to facilitate their efficient reuse. SBO is an Open Biomedical Ontologies (OBO) candidate ontology, and is free for use. More information about SBO can be found from the project FAQ, at http://www.ebi.ac.uk/sbo/ SBO is a project of the BioModels.net effort and is developed through community collaboration
