---
layout: principle
id: fp-012-naming-conventions
title: Naming Conventions (principle 12)
---

## NOTE

The content of this page is scheduled to be reviewed. Improved wording will be posted as it becomes available.

GO TO: [Recommendations/Requirements](#recommendations-and-requirements) &#124; [Implementation](#implementation) &#124; [Examples/Counter&#8209;Examples](#examples) &#124; [Criteria&nbsp;for&nbsp;Review](#criteria-for-review) &#124; [Feedback/Discussion](#feedback-and-discussion)

## Summary

The names (primary labels) for elements (classes, properties, etc.) in an ontology must be intelligible to scientists and amenable to natural language processing. Each primary label SHOULD be unique among OBO Library ontologies, and MUST be unique within its own ontology.

## Purpose

Text to be added.

## Recommendations and Requirements

Text to be added.
For full details, see this paper: <http://www.biomedcentral.com/1471-2105/10/125>

Briefly, some important things to remember:

- use rdfs:label for the primary label
- include exactly one rdfs:label for every declared entity (e.g. class, property)
- write labels, synonyms, etc as if writing in plain English text. ie use spaces to separate words, only capitalize proper names (e.g. Parkinson disease). Do not use CamelCase, do_not_use_underscores
- avoid extra spaces between words, or at the beginning or end of the term label
- spell out abbreviations. Abbreviations can be included as a separate property.
- make the primary labels to be as unambiguous as possible. Remember, your ontology may be used in a different context than that for which it was originally intended. Remember also of course that the label should be unambiguous without looking at parent terms
- labels MUST be unique within an ontology
- use the IAO property 'obo foundry unique label' [http://purl.obolibrary.org/obo/IAO_0000589](http://purl.obolibrary.org/obo/IAO_0000589) to declare a pan-OBO unique label if required

## Implementation

Text to be added.

## Examples

Text to be added.

## Counter Examples

Text to be added.

## Criteria for Review

Text to be added.

[This check is automatically validated.](checks/fp_012)

## Feedback and Discussion

<!-- rev. To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%2314+%22Guidelines).

rev. To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Technical+WG,automated+validation+of+principles&title=Principle+%2314+%22Guidelines).

rev. See also [this discussion](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/????) ??? by the OBO Foundry Operations Committee. -->

<Category:Principles> <Category:Accepted>
