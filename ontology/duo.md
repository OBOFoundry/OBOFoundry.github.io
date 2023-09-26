---
layout: ontology_detail
id: duo
title: Data Use Ontology
contact:
  email: mcourtot@gmail.com
  github: mcourtot
  label: Melanie Courtot
  orcid: 0000-0002-9551-6370
dependencies:
- id: bfo
- id: iao
description: DUO is an ontology which represent data use conditions.
domain: information
homepage: https://github.com/EBISPOT/DUO
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
preferredPrefix: DUO
products:
- id: duo.owl
repository: https://github.com/EBISPOT/DUO
tracker: https://github.com/EBISPOT/DUO/issues
activity_status: active
---

DUO allows to semantically tag datasets with restriction about their usage, making them discoverable automatically based on the authorization level of users, or intended usage.
 
Human subjects datasets often have restrictions such as “only available for cancer use” or “only available for the study of pediatric diseases,” based on the original participant consent, which must be respected when sharing and studying these datasets.
The goal of DUO is to allow large genomics and health data repositories to share the same terminology when describing data use conditions. In addition, we envision a future where web services would submit queries to these repositories such as “return all datasets that can be used to study melanoma by a commercial entity” that will help researchers find relevant data that is compatible with their research purpose. DUO includes ontology terms needed to represent such queries as well as the ontology hierarchy necessary for algorithms to determine whether a research purpose is compatible with the dataset restrictions. A further goal is to encourage the authors of new consent forms to align consent language with the terms used by DUO; this would eliminate the need for subsequent review of consent forms to classify data use and speed the availability of data for secondary use.
