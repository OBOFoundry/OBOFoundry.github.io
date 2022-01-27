---
layout: ontology_detail
id: iao
contact:
  email: jiezheng@pennmedicine.upenn.edu
  label: Jie Zheng
  github: zhengj2007
description: "An ontology of information entities."
domain: information
homepage: https://github.com/information-artifact-ontology/IAO/
license:
  url: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
products:
  - id: iao.owl
  - id: iao/ontology-metadata.owl
    title: IAO ontology metadata
    page: https://github.com/information-artifact-ontology/IAO/wiki/OntologyMetadata
  - id: iao/dev/iao.owl
    title: IAO dev
  - id: iao/d-acts.owl
    title: ontology of document acts
    description: "An ontology based on a theory of document acts describing what people can do with documents"
    contact:
      email: mbrochhausen@gmail.com
      label: Mathias Brochhausen
title: Information Artifact Ontology
build:
  source_url: http://purl.obolibrary.org/obo/iao.owl
  method: owl2obo
tracker: https://github.com/information-artifact-ontology/IAO/issues
depicted_by: https://avatars0.githubusercontent.com/u/13591168?v=3&s=200
usages:
  - user: http://obofoundry.org
    type: owl_import
    description: IAO is used widely by multiple OBO ontologies for information representation.
activity_status: active
repository: https://github.com/information-artifact-ontology/IAO
preferredPrefix: IAO
---

The Information Artifact Ontology (IAO) is a new ontology of information entities, originally driven by work by the OBI digital entity and realizable information entity branch.
