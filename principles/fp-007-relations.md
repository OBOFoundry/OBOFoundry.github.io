---
layout: principle
id: fp-007-relations
title: Relations (principle 7)
---

## NOTE

The content of this page is scheduled to be reviewed. Improved wording will be posted as it becomes available.

## Summary

Relations should be reused from the Relations Ontology (RO).

[This check is automatically validated.](checks/fp_007)

## Purpose

To facilitate interoperability between multiple ontologies, especially with respect to logical inference. That is, a reasoner can only detect logical inconsistencies between ontologies and infer new axioms if the ontologies use the same object properties.

## Recommendations and Requirements

Each OBO ontology MUST reuse existing relations (aka object properties) that have already been declared in the Relations Ontology (RO),
rather than declaring relations that mean the same as an existing RO relation. Where it makes sense for an ontology to declare a new relation in
its own ID space and there is a RO relation that is logically a super-property of the new relation, the new relation MUST be asserted to be
a sub-property of the RO relation. In such cases, it is requested that there still be coordination with RO, for example in the form of an issue
submitted to the [RO tracker](https://github.com/oborel/obo-relations/issues).

## Implementation

Reuse means that the actual relations PURLs are used. Ontology developers should be aware that RO relations (in rare instances) can evolve over time and previous relations might become obsolete. This means developers should monitor the state of the RO relations they use.

## Examples

## Counter-Examples

<Category:Principles> <Category:Accepted> <Category:Definitions>
