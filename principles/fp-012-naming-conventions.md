---
layout: principle
id: fp-012-naming-conventions
title: Naming Conventions (principle 12)
---

## NOTE

The content of this page is scheduled to be reviewed. Improved wording will be posted as it becomes available.

## Details

For full details, see this paper: <http://www.biomedcentral.com/1471-2105/10/125>

Briefly, some important things to remember:

- use rdfs:label for the primary label
- include exactly one rdfs:label for every declared entity (e.g. class, property)
- write labels, synonyms, etc as if writing in plain English text. ie use spaces to separate words, only capitalize proper names (e.g. Parkinson disease). Do not use CamelCase, do_not_use_underscores
- avoid extra spaces between words, or at the beginning or end of the term label
- spell out abbreviations. Abbreviations can be included as a separate property.
- make the primary labels to be as unambiguous as possible. Remember, your ontology may be used in a different context than that for which it was originally intended. Remember also of course that the label should be unambiguous without looking at parent terms
- labels should be unique within an ontology
- use the IAO property 'obo foundry unique label' [http://purl.obolibrary.org/obo/IAO_0000589](http://purl.obolibrary.org/obo/IAO_0000589) to declare a pan-OBO unique label if required

[This check is automatically validated.](checks/fp_012)

## Examples

## Counter-Examples

<Category:Principles> <Category:Accepted>
