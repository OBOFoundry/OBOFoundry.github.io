---
layout: principle
id: fp-008-documented
title: Documentation (principle 8)
---

## NOTE

The wording of this principle is still in progress, with some issues still to be addressed (see Issues To Be Addressed below).

## Summary

The owners of the ontology should strive to provide as much documentation as possible. The documentation should detail the different processes specific to an ontology life cycle and target various audiences (users or developers).

[This check is automatically validated.](checks/fp_008)

## Purpose

Central to the issue of ontology documentation is ensuring transparency and traceability of artefact development. For each of the development steps, clear procedures should be made available. Documentation availability will be used to assess the quality of the resource. The following itemized list provides a core checklist, distinguishing general ontology documentation (general information about the resource) and local ontology documentation (documentation at artefact level itself and representational unit level (class and relations)). Documentation assessment with the purpose of assessing Ontology soundness, will cover updates and revision to the documentation. As ontology evolve, so should the documentation, for example by including a release documentation file.

## Recommendations and Requirements

## Implementation
### Term adoption
If a term that was previously defined in an identifier space belonging to ontology A (e.g. http://purl.obolibrary.org/obo/A_123) is adopted by ontology B (with a different identifier scheme, e.g. http://purl.obolibrary.org/obo/B_123) the following annotation assertion MUST be added to that term:

OWL format:
`<http://purl.obolibrary.org/obo/A_123> rdfs:isDefinedBy <http://purl.obolibrary.org/obo/b.owl>`

OBO format:
`property_value: isDefinedBy http://purl.obolibrary.org/obo/b.owl`

## Examples

_Embedded or 'in-situ' documentation_:
  Namely any specific metadata available from the ontology artefact itself providing information about the resource in its entirety or parts of it.
  global ontology description (about the ontology as a whole):
- creator(s)
- maintainer(s)
- license
- version

_local ontology documentation (about each term):_
  documentation for individual representational unit annotation
- justify the different elements of class metadata
- justify class axiomatization
  documentation about the textual definition: is it manually created or generated with software assistance by relying on patterns and class axioms.

_User documentation:_
  A documentation detailing the ontology's raison d'etre, its coverage, the use cases and query cases (including translation into SPARQL queries) it is intended to support
  documentation about how to access the resource
  documentation about how to produce semantic web document compatible with the representation intended by the developers (OWL examples, OWL coding patterns)
- availability of peer-reviewed publication about the resource
- availability of training material and tutorial
- availability of presentations (e.g. on slideshare)
- availability of web seminars (e.g. on a youtube channel)

_Developer documentation:_

- documentation about collaborating and submitting issues by creating a [CONTRIBUTING.md file](http://mozillascience.github.io/working-open-workshop/contributing/) as described [here](http://obofoundry.org/principles/fp-020-responsiveness.html#implementation).
- documentation about authors contributions
- documentation about licensing terms, rights of use.
- documentation about version control
- documentation about release process
- documentation about changes in ontology between release version
- continuous integration
- documentation about the methodology used for developing the resource
- documentation about interaction with orthogonal resources
- documentation about resource acknowledgement
- documentation about term submission/term requests
- documentation about batch submission
- documentation about term deprecation and deprecation policy (aka retirement policy)
- documentation about conflict resolution
- a documentation detailing the use of software agent devised or exploited to develop, maintain, enhance, perform quality control and ensure high availability of the resource
- documentation about how the ontology is being used

## Issues To Be Addressed (partial list):

1. What minimal metadata is needed?

2. What minimal documentation is needed?

3. Clarification of the role of publications

the ontology is well-documented (e.g. in a published paper describing the ontology or in manuals for developers and users)

<Category:Principles> <Category:Accepted>
