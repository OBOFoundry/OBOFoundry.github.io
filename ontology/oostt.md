---
layout: ontology_detail
id: oostt
title: Ontology of Organizational Structures of Trauma centers and Trauma systems
contact:
  email: mbrochhausen@gmail.com
  github: mbrochhausen
  label: Mathias Brochhausen
  orcid: 0000-0003-1834-3856
description: An ontology built for representating the organizational components of trauma centers and trauma systems.
domain: health
homepage: https://github.com/OOSTT/OOSTT
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
preferredPrefix: OOSTT
products:
- id: oostt.owl
repository: https://github.com/OOSTT/OOSTT
tracker: https://github.com/OOSTT/OOSTT/issues
usages:
- description: OOSTT terms, such as OOSTT_00000017 'trauma program' and OOSTT_00000021 'trauma medical director role,' are used in the CAFE questionnaire to assess trauma centers and systems.
  type: application
  user: https://cafe-trauma.com/
- description: OOSTT terms, such as OOSTT_00000002 'trauma center' and OOSTT_00000066 'emergency medicine liaison role,' are used in the TIPTOE questionnaire to relate trauma center/system structure to patient outcomes.
  type: application
  user: https://tiptoe.apps.dbmi.cloud/tiptoe
- description: OOSTT is used by OMRSE.
  examples:
  - description: academic degree
    url: http://purl.obolibrary.org/obo/OOSTT_00000074
  type: owl:Ontology
  user: http://purl.obolibrary.org/obo/omrse.owl
activity_status: active
---

The Ontology of Organizational Structures of Trauma centers and Trauma systems (OOSTT) is a representation of the components of trauma centers and trauma systems coded in Web Ontology Language (OWL2). It is developed collaboratively by domain and ontology experts in the NIH-funded CAFE (Comparative Assessment Framework for Environments of trauma care) project (1R01GM111324-01A1). It will be used as the ontology backbone of a graphical user interface comparing graphical representations of organizational structures.
