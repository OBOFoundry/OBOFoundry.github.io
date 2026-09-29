---
layout: principle
id: fp-007-relations
title: Relations (principle 7)
---
GO TO: [Recommendations/Requirements](#recommendations-and-requirements) &#124; [Implementation](#implementation) &#124; [Examples/Counter&#8209;Examples](#examples) &#124; [Criteria&nbsp;for&nbsp;Review](#criteria-for-review) &#124; [Feedback/Discussion](#feedback-and-discussion)

## Summary

Existing relations MUST be reused. New relations SHOULD be submitted to the Relations Ontology (RO).

## Purpose

To facilitate interoperability between multiple ontologies, especially with respect to logical inference, because a reasoner can only detect logical inconsistencies between ontologies and infer new axioms if the ontologies use the same relations (aka object properties).

## Recommendations and Requirements

For any given relation need, each OBO ontology MUST reuse a relation from the Relations Ontology (RO) or other ontology if the appropriate relation already exists,
rather than declaring new a relation that holds the same meaning. Where it makes sense for an ontology to declare a new relation in
its own ID space and there is a RO relation that is logically a super-property of the new relation, the new relation MUST be asserted to be
a sub-property of the RO relation. In such cases, it is requested that there still be coordination with RO, for example in the form of an issue
submitted to the [RO tracker](https://github.com/oborel/obo-relations/issues).

## Implementation

### Reusing relations
'Reuse' means that the actual existing-relation PURL is used. Ontology developers should be aware that (in rare instances) relations can evolve over time and previous relations might become obsolete. This means developers should monitor the state of the relations they use. The Relations Ontology MUST be the first source for appropriate relations, and ontology developers SHOULD, with due diligence, search RO for needed relations. If a necessary relation cannot be found within RO, then the developers MUST search other OBO ontologies for reasonable candidates using, for example, an ontology search engine such as [Ontobee](https://ontobee.org/) or [OLS](https://www.ebi.ac.uk/ols4/).

### Creating New Relations
An effort to specify a domain and range for the relation SHOULD be made, though caution is advised to ensure that each is neither too broad nor too specific. The appropriate home for a new relation will depend on multiple factors, including the general applicability of the relation (beyond its immediate use within the context of a given ontology), and in consideration of its domain and range:
- If both the domain and range are from the same ontology as the relation, the relation MAY be kept in that ontology;
- If either the domain or range is from a different ontology as the relation, but the relation is not general enough for use by other ontologies, the relation MAY be kept in the originating ontology;
- If the relation seems appropriate for general usage, the relation SHOULD be submitted to RO;
- For any relation not submitted to RO, if a suitable RO parent exists, then the relation MUST be declared a sub-property of that parent.

While it is never a bad idea to submit a new relation to RO, if there are any doubts about how to proceed based on the above, a discussion with RO developers SHOULD be made via the [RO issue tracker](https://github.com/oborel/obo-relations/issues) or the [OBO Community  Slack](https://obo-communitygroup.slack.com) using the #relation-ontology channel.

Note regarding property chains: If a proposed property chain makes use of relations that are themselves in RO, the property chain SHOULD be submitted to RO.

## Examples

## Counter-Examples

## Criteria for Review

Each relation in the ontology that does not use an RO IRI will be checked to see if there is an exact label match in RO. If so, this will be flagged as an ERROR. Any other non-RO properties will be flagged with an INFO message.

[This check is automatically validated.](checks/fp_007)

## Feedback and Discussion

To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%237+%22Relations%22+%3CENTER+ISSUE+TITLE%3E).

To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Technical+WG,automated+validation+of+principles&title=Principle+%237+%22Relations%22+-+automated+validation+%3CENTER+ISSUE+TITLE%3E).
