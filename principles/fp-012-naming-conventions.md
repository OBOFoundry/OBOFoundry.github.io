---
layout: principle
id: fp-012-naming-conventions
title: Naming Conventions (principle 12)
---

## NOTE

The content of this page is scheduled to be reviewed. Improved wording will be posted as it becomes available.

GO TO: [Recommendations/Requirements](#recommendations-and-requirements) &#124; [Implementation](#implementation) &#124; [Examples/Counter&#8209;Examples](#examples) &#124; [Criteria&nbsp;for&nbsp;Review](#criteria-for-review) &#124; [Feedback/Discussion](#feedback-and-discussion)

## Summary

The names (primary labels) for elements (classes, properties, etc.) in an ontology SHOULD be unique among OBO Foundry ontologies, MUST be unique within its own ontology, and SHOULD be written in accepted format.

## Purpose

Primary labels are a major mechanism by which terms are referenced. Accordingly, it is important that labels be unique, unambiguous, and formatted for ease of reading and comprehension. Non-unique labels (sometimes for terms that mean very different things) may cause confusion for human users and may prevent some ontology editing tools from full access to terms (for example, when crafting axioms). Labels that are ambiguous cause difficulty when users are trying to identify a term that matches their intention.

## Recommendations and Requirements

Text to be added.

For full details, see this paper: <http://www.biomedcentral.com/1471-2105/10/125>

Briefly, some important things to remember:

- There MUST be exactly one rdfs:label for every declared entity (e.g. class, property)
- Labels MUST be unique within an ontology and SHOULD be unique within the wider OBO Foundry
- Format requirements
  - Write labels and synonyms using plain English text
    - Use spaces to separate words
    - Only capitalize proper names (e.g. Parkinson disease)
    - Do not use CamelCase
    - Do not use under_scores
  - Avoid extra spaces between words, or at the beginning or end of the term label
  - Spell out abbreviations. Abbreviations can be included as alternative labels (i.e., synonyms)
- Primary labels SHOULD be as unambiguous as possible. An ontology may be used in a context that differs from that for which it was originally intended, including being combined with other ontologies.
- Optimally, each label SHOULD be unambiguous even without looking at parent terms

## Implementation

Text to be added.
- Use rdfs:label for the primary label
- use the IAO property 'obo foundry unique label' [http://purl.obolibrary.org/obo/IAO_0000589](http://purl.obolibrary.org/obo/IAO_0000589) to declare a pan-OBO unique label if required


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
