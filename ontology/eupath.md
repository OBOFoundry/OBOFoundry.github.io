---
layout: ontology_detail
id: eupath
contact:
  email: stoeckrt@pennmedicine.upenn.edu
  label: Chris Stoeckert
  github: cstoeckert
license:
  url: http://creativecommons.org/licenses/by/4.0/
  label: CC-BY
depicted_by: https://raw.githubusercontent.com/EuPathDB/communitysite/master/assets/images/VEuPathDB-logo-s.png
domain: functional genomics, population biology, clinical epidemiology, and microbiomes
description: An ontology is developed to support Eukaryotic Pathogen, Host & Vector Genomics Resource (VEuPathDB; https://veupathdb.org). 
homepage: https://github.com/VEuPathDB-ontology/VEuPathDB-ontology
products:
  - id: eupath.owl
title: VEuPathDB ontology
tracker: https://github.com/VEuPathDB-ontology/VEuPathDB-ontology/issues
usages:
 - user: https://veupathdb.org
   type: annotation and query
   description: The VEuPathDB ontology is used in the VEuPathDB (Eukaryotic Pathogen, Vector & Host Informatics Resources) covers both functional genomics and population biology.
 - user: https://clinepidb.org
   type: annotation and query
   description: The VEuPathDB ontology is used in the clinical epidemiology resources.
 - user: https://microbiomedb.org
   type: annotation and query
   description: The VEuPathDB ontology is used in the MicrobiomeDB, a systems biology platform for integrating, mining and analyzing microbiome experiments.

activity_status: active
---

The VEuPathDB ontology is an application ontology developed to encode our understanding of what data is about in the public resources developed and maintained by the Eukaryotic Pathogen, Host & Vector Genomics Resource (VEuPathDB; https://veupathdb.org). The VEuPathDB ontology was previously named the EuPathDB ontology prior to EuPathDB joining with VectorBase.The ontology was built based on the Ontology of Biomedical Investigations (OBI) with integration of other OBO ontologies such as PATO, OGMS, DO, etc. as needed for coverage. Currently the VEuPath ontology is primarily intended to be used for support of the VEuPathDB sites. Terms with VEuPathDB ontology IDs that are not specific to VEuPathDB will be submitted to OBO Foundry ontologies for subsequent import and replacement of those terms when they are available.
