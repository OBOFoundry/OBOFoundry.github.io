---
layout: ontology_detail
id: duo
title: Data Use Ontology
jobs:
  - id: https://travis-ci.org/EBISPOT/DUO
    type: travis-ci
build:
  checkout: git clone https://github.com/EBISPOT/duo.git
  system: git
  path: "."
contact:
  email: mcourtot@gmail.com
  label: Melanie Courtot
  github: mcourtot
  orcid: 0000-0002-9551-6370
description: DUO is an ontology which represent data use conditions.
homepage: https://github.com/EBISPOT/DUO
products:
  - id: duo.owl
dependencies:
  - id: iao
  - id: bfo
tracker: https://github.com/EBISPOT/DUO/issues
license:
  url: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
activity_status: active
repository: https://github.com/EBISPOT/DUO
preferredPrefix: DUO
domain: information
---

DUO allows to semantically tag datasets with restriction about their usage, making them discoverable automatically based on the authorization level of users, or intended usage.
 
Human subjects datasets often have restrictions such as “only available for cancer use” or “only available for the study of pediatric diseases,” based on the original participant consent, which must be respected when sharing and studying these datasets.
The goal of DUO is to allow large genomics and health data repositories to share the same terminology when describing data use conditions. In addition, we envision a future where web services would submit queries to these repositories such as “return all datasets that can be used to study melanoma by a commercial entity” that will help researchers find relevant data that is compatible with their research purpose. DUO includes ontology terms needed to represent such queries as well as the ontology hierarchy necessary for algorithms to determine whether a research purpose is compatible with the dataset restrictions. A further goal is to encourage the authors of new consent forms to align consent language with the terms used by DUO; this would eliminate the need for subsequent review of consent forms to classify data use and speed the availability of data for secondary use.
