---
layout: doc
permalink: /roles/metadata-steward
title: Registry Metadata Steward
---

You are responsible for shepherding our registry metadata according to our principles and SOPs, merge changes and generally protect and guard them. This involves also facilitating the implementation of QC checks.

## Responsibilities

- Checking OBOFoundry.github.io at least weekly for metadata related issues and pull requests. This involves changes to files in the following paths:
  - https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/util/schema (the metadata schema)
  - https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/ontology (the ontology metadata)
  - https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/_data (the OBO Foundry member metadata)
  - https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/registry (the OBO Foundry registry metadata)
  - https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/_config.yml (the OBO Foundry website config YAML)
- Tagging metadata related issues and pull requests with 'attn: OFOC call' if they need to be discussed by the Operations Committee. Provide instructions what needs to be discussed.
- Assessing pull requests to be in line with [OBO SOPs on Ontology Metadata](https://obofoundry.org/docs/SOP.html#META). Unless covered by an explicit exception, metadata changes must be signed off by registered ontology contacts.
  - When evaluating `usage`, take special notice of the level of evidence required by [Principle 9](https://obofoundry.org/principles/fp-009-users.html)
- When metadata records are updated, all downstream files, including the registry, are regenerated using [Build derived files](https://github.com/OBOFoundry/OBOFoundry.github.io/actions/workflows/build.yml) GitHub Action. The Metadata Steward should sanity check the diff for any oddities, in particular changes to the file `registry/ontologies.yml`.  This PR serves as a second line of defence and should not be automatically merged into master as part of the GitHub action.
- Providing guidance for metadata-related issues and pull requests.
- Implement additional checks for metadata integrity if necessary.
- The Registry Metadata Steward is not required to fix issues with the metadata proactively, but may choose to do so at their own discretion.
- Provide monthly summary to Technical Working Group OBO Operations liaison for report to OBO Operations Committee.
