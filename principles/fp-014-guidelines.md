---
layout: principle
id: fp-014-guidelines
title: Guidelines (principle 14)
---

# Draft Draft Draft Draft Draft Draft

GO TO: [Recommendations/Requirements](#recommendations-and-requirements) &#124; [Implementation](#implementation) &#124; [Examples/Counter&#8209;Examples](#examples) &#124; [Criteria&nbsp;for&nbsp;Review](#criteria-for-review) &#124; [Feedback/Discussion](#feedback-and-discussion)

## Summary

In addition to the principles, each ontology MUST follow gen  eral OBO guidelines.

## Purpose

rev. A unique namespace within the OBO Foundry Library allows the source of an element or term (e.g., class, property) from any ontology to be identified immediately by the prefix of the identifier. It also allows ontology element IRIs to be shortened to a compact URI or CURIE, which allows developers to use CURIES for working with ontologies. OWL syntax allows for ontologies and their elements to have identifiers in the form of an IRI. The OBO Foundry uses IRIs in the form of PURLs to allow an ontology and its elements to be resolvable (findable on the web). PURLs are URLs (and thus locate the resource) that are permanent or redirectable, allowing the URL to point to a new location when the resource moves. OBO Foundry PURLs use a standard format that includes the ontology namespace so that they can be easily maintained by a group of volunteers, and so ontology maintainers can update the location their PURL points to using a GitHub pull request.

## Recommendations and Requirements

rev. Each ontology MUST have a unique IRI in the form of an OBO Foundry permanent URL (PURL). The PURL must include the ontology namespace, which is a short string of letters (usually 2-5) that represents the ontology. Namespaces MUST be approved by the OBO Foundry Operations Committee. Every element (class, property, etc.) created by the ontology MUST use the namespace in the identifier of each element, as specified in the OBO Foundry [ID policy](http://www.obofoundry.org/id-policy).

## Implementation

### Ontology Namespace:

rev. The ontology namespace MUST be unique; that is, it MUST NOT be in current use or have been used in the past. When used as part of the ontology IRI, the namespace is in lower case. When used as part of a CURIE, on its own, or as part of a term ID, the namespace MUST be capitalized (<i>Note: this applies to ontologies submitted after 1st June 2024; mixed-case prefixes for ontologies submitted before this date may be retained</i>).

rev. To request a new namespace, ontology developers MUST follow the guidelines outlined here. Note that very short namespaces (2-3 characters) are reserved for ontologies that cover a general domain and are likely to be frequently used.

### Ontology IRI:

rev. For guidelines on how to create IRIs for ontology elements/terms, see the OBO Foundry [ID policy](http://www.obofoundry.org/id-policy).

## Examples

## Counter Examples

## Criteria for Review

rev. The ontology namespace MUST be registered following the procedures outlined within the [OBO Foundry membership requirements and technical details](http://www.obofoundry.org/docs/Policy_for_OBO_namespace_and_associated_PURL_requests.html) document. In addition, the ontology IRI MUST follow the format given above.

rev. [This check is automatically validated.](checks/fp_003) The automatic check fully covers the requirements for this principle.

## Feedback and Discussion

rev. To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%233+%22URIs%22+%3CENTER+ISSUE+TITLE%3E).

rev. To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Technical+WG,automated+validation+of+principles&title=Principle+%233+%22URIs%22+-+automated+validation+%3CENTER+ISSUE+TITLE%3E).

rev. See also [this discussion](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2596) of URI capitalization by the OBO Foundry Operations Committee.
