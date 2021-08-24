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

## OBO Foundry pre-release checklist

 - [ ] There is no other ontology in the OBO foundry which would be an appropriate place for my terms. If there was, I have contacted the editors, and we decided in mutual agreement that a separate ontology is more appropriate.
- [ ] My ontology has a specific release file with a version IRI and a dc:license annotation, serialised in RDF/XML
- [ ] All the higher-level terms in my ontology (excluding those from upper ontologies such as BFO) have definitions using the [IAO:0000115](http://www.ontobee.org/ontology/IAO?iri=http://purl.obolibrary.org/obo/IAO_0000115) property. For example, if my ontology is about diseases, treatments and symptoms, the terms "disease", "treatment" and "symptom" have a definition (note that if you use the term "disease", you will have important it from another suitable OBO ontology). Note that definitions are key to understanding the intentions of a term - and I understand that _all_ terms in the ontology, not just the high-level ones, _SHOULD_ have a textual definition.
 - [ ] For every term in my ontology, I checked whether another OBO foundry ontology has it. If so, I re-used that term directly (not by cross-reference, by directly using the IRI).
 - [ ] For all relationship properties (Object and Data Property) I checked whether [RO](http://www.ontobee.org/ontology/catalog/RO?iri=http://www.w3.org/2002/07/owl%23ObjectProperty) includes an appropriate one. I understand that aligning with RO is an essential part of the overall alignment between OBO ontologies!
 - [ ] For the selection of appropriate annotation properties, I looked at [OMO](http://www.ontobee.org/ontology/catalog/OMO?iri=http://www.w3.org/2002/07/owl%23AnnotationProperty) first. I understand that aligning ontology metadata and term-level metadata is essential for cross-integration of OBO ontologies. 
 - [ ] If I was not sure about the meaning of any of the checkboxes above, I have consulted with a member of the OBO Foundry for advice.


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
usages:
  - user: http://website.of.the.project.using.my.ontology.com
    description: A short description of how the project above is using my ontology
```
