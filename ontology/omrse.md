---
layout: ontology_detail
id: omrse
title: Ontology for Modeling and Representation of Social Entities
build:
  method: owl2obo
  source_url: https://github.com/mcwdsi/OMRSE
contact:
  email: hoganwr@gmail.com
  github: hoganwr
  label: Bill Hogan
  orcid: 0000-0002-9881-1017
description: The Ontology for Modeling and Representation of Social Entities (OMRSE) is an OBO Foundry ontology that represents the various entities that arise from human social interactions, such as social acts, social roles, social groups, and organizations.
domain: health
homepage: https://github.com/mcwdsi/OMRSE/wiki/OMRSE-Overview
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: OMRSE
products:
- id: omrse.owl
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/27406187
  title: 'The ontology of medically related social entities: recent developments'
repository: https://github.com/mcwdsi/OMRSE
tags:
- social
- behavior
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
tracker: https://github.com/mcwdsi/OMRSE/issues
usages:
- description: OMRSE is used by the CAFÊ and TIPTOE projects
  examples:
  - description: The project creates and maintains the Ontology of Organizational Structures of Trauma centers and Trauma systems or OOSTT, which reuses OMRSE terms
    url: https://www.ebi.ac.uk/ols4/ontologies/oostt/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FOOSTT_00000089
  publications:
  - id: https://pubmed.ncbi.nlm.nih.gov/28217041
    title: 'OOSTT: a Resource for Analyzing the Organizational Structures of Trauma Centers and Trauma Systems'
  type: owl:Ontology
  user: https://boar.uams.edu/projects/comparative-assessment-framework-for-environments-of-trauma-care
- description: OMRSE is used by the Intervention Setting Ontology component of the Behavior Change Intervention Ontology
  examples:
  - description: Several facility classes extend OMRSE's 'facility'
    url: https://www.ebi.ac.uk/ols4/ontologies/bcio/classes/http%253A%252F%252Fhumanbehaviourchange.org%252Fontology%252FBCIO_026022
  publications:
  - id: https://doi.org/10.12688/wellcomeopenres.15904.1
    title: 'Development of an Intervention Setting Ontology for behaviour change: Specifying where interventions take place'
  type: owl:Ontology
  user: https://www.humanbehaviourchange.org
activity_status: active
---

For more information on the social entities represented in OMRSE, please visit our wiki page or list of publications. OMRSE is designed to be a mid-level ontology that bridges the gap between BFO, which it reuses for its top-level hierarchy, and more specific domain or application ontologies. For this reason, we are always open to working with ontology developers who want to build interoperability between their projects and OMRSE.
