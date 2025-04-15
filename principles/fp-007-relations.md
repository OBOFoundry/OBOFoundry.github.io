---
layout: principle
id: fp-007-relations
title: Relations (principle 7)
---
GO TO: [Recommendations/Requirements](#recommendations-and-requirements) &#124; [Implementation](#implementation) &#124; [Examples/Counter&#8209;Examples](#examples) &#124; [Criteria&nbsp;for&nbsp;Review](#criteria-for-review) &#124; [Feedback/Discussion](#feedback-and-discussion)

## Summary

Existing relations MUST be reused from the Relations Ontology (RO). New relations SHOULD be submitted to RO.

[This check is automatically validated.](checks/fp_007)

## Purpose

To facilitate interoperability between multiple ontologies, especially with respect to logical inference. That is, a reasoner can only detect logical inconsistencies between ontologies and infer new axioms if the ontologies use the same relations (aka object properties).

## Recommendations and Requirements

For any given relation need, each OBO ontology MUST reuse a relation from the Relations Ontology (RO) if the appropriate relation already exists,
rather than declaring new relations that hold the same meaning. Where it makes sense for an ontology to declare a new relation in
its own ID space and there is a RO relation that is logically a super-property of the new relation, the new relation MUST be asserted to be
a sub-property of the RO relation. In such cases, it is requested that there still be coordination with RO, for example in the form of an issue
submitted to the [RO tracker](https://github.com/oborel/obo-relations/issues).

Note: 'Reuse' means that the actual RO relations PURLs are used. Ontology developers should be aware that RO relations (in rare instances) can evolve over time and previous relations might become obsolete. This means developers should monitor the state of the RO relations they use.

## Implementation

- If the domain of the proposed relation is a class in the same ontology as that relation, it is fine to keep in the ontology; if a suitable RO parent exists, the new relation MUST be declared a sub-property of that parent.
- If the domain of the proposed relation is a class outside of the ontology defining that relation, the relation MUST be added to RO.
- If the relation seems generally usable (that is, could potentially be used by other ontologies), the relation MUST be added to RO.
- If there are any doubts about how to proceed based on the above, there SHOULD be an attempt to add to RO.
- It is never a bad idea to add to RO, even for those relations that are 'self-contained' (as described in the first bullet point).

Note regarding property chains: If a proposed property chain makes use of relations that are themselves in RO, the property chain SHOULD be submitted to RO.

## Examples

## Counter-Examples

## Criteria for Review

Each relation in the ontology that does not use an RO IRI will be checked to see if there is an exact label match in RO. If so, this will be flagged as an ERROR. Any other non-RO properties will be flagged with an INFO message.

[This check is automatically validated.](checks/fp_007)

## Feedback and Discussion

To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%237+%22Relations%22+%3CENTER+ISSUE+TITLE%3E).

To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Technical+WG,automated+validation+of+principles&title=Principle+%237+%22Relations%22+-+automated+validation+%3CENTER+ISSUE+TITLE%3E).
