---
name: New Ontology Request
about: Request to register a new ontology with the OBO Foundry
title: ''
labels: new ontology
assignees: ''

---

Use this form to register a new ontology with the OBO Foundry. Please read the instructions provided here:
http://obofoundry.org/docs/NewOntologyRegistrationInstructions.html

## Ontology title


## Requested ID space


## Ontology location


## Contact person
Name:
Email address:
GitHub username: 

## Issue tracker


## Ontology license

- [ ] CC0 (public domain)
- [ ] CC-BY (version 3 or later)
- [ ] Other: *please specify*

## Available ontology formats


## What domain is the ontology intended to cover?


## Related OBO Foundry ontologies


## Intended use/related projects


## Data source


## Additional comments or remarks

## Metadata

Please fill in the following metadata record which will be used by the OBO Foundry website. Note that the values shown are just examples, for example `yourfourletterid` could be something like `aism`, `cohm`, `mondo` (it does not have to be four letters). `your_domain_like_for_example_anatomy` could be simply `anatomy`, and the license should be whatever your actual license is. An example can be found [here](https://github.com/OBOFoundry/OBOFoundry.github.io/edit/master/ontology/amphx.md), but you really only need to fill in the metadata mentioned here.

```
id: yourfourletterid
title: The Title Of Your Ontology
contact:
  email: email@example.com
  label: Your Name
description: Some one sentence description of your ontology.
domain: your_domain_like_for_example_anatomy
homepage: https://github.com/YOURORG/your_repo
products:
  - id: yourfourletterid.owl
  - id: yourfourletterid.obo
dependencies:
  - id: ro
  - id: otheroboontology
tracker: https://github.com/YOURORG/your_repo/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
```
