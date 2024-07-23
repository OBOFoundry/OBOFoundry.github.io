---
layout: ontology_detail
id: iao
title: Information Artifact Ontology
build:
  method: owl2obo
  source_url: http://purl.obolibrary.org/obo/iao.owl
contact:
  email: zhengj2007@gmail.com
  github: zhengj2007
  label: Jie Zheng
  orcid: 0000-0002-2999-0103
depicted_by: https://avatars0.githubusercontent.com/u/13591168?v=3&s=200
description: An ontology of information entities.
domain: information
homepage: https://github.com/information-artifact-ontology/IAO/
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
preferredPrefix: IAO
products:
- id: iao.owl
- id: iao/ontology-metadata.owl
  title: IAO ontology metadata
  page: https://github.com/information-artifact-ontology/IAO/wiki/OntologyMetadata
- id: iao/dev/iao.owl
  title: IAO dev
- id: iao/d-acts.owl
  title: ontology of document acts
  contact:
    email: mbrochhausen@gmail.com
    label: Mathias Brochhausen
  description: An ontology based on a theory of document acts describing what people can do with documents
repository: https://github.com/information-artifact-ontology/IAO
tracker: https://github.com/information-artifact-ontology/IAO/issues
usages:
- description: IAO is used widely by multiple OBO ontologies for information representation.
  type: owl_import
  user: http://obofoundry.org
activity_status: active
---

The Information Artifact Ontology (IAO) is a new ontology of information entities, originally driven by work by the OBI digital entity and realizable information entity branch.
