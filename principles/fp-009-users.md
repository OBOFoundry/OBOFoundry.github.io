---
layout: principle
id: fp-009-users
title: Documented Plurality of Users (principle 9)
---

## Summary

The ontology developers should document that the ontology is used by
multiple independent people or organizations.

## Purpose

This principle aims to ensure that the ontology tackles a relevant
scientific area and does so in a usable and sustainable fashion.

## Recommendations and Requirements

It is important to be able to illustrate usage outside of the immediate circle of ontology developers and stakeholders. Note that the ontology can still be listed on
the OBO Foundry website while publicising your resource in appropriate channels and searching for users with needs you can meet.

## Implementation

The ontology developers should provide links/citations to evidence of
use (publication, external ontology; see examples below for additional types) within your ontology [metadata file](https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/ontology) (replacing with the correct group name, link, and description):

```
usages:
- user: http://www.informatics.jax.org/disease (link to group)
  description: MGI disease model annotations use DO (description of group)
  examples:
   - url: http://www.informatics.jax.org/disease/DOID:4123 (link to specific example)
     description: Human genes and mouse homology associated with nail diseases (description of specific example)
```

You may have multiple examples for each user, and mulitple users under the `usages` tag.

## Examples

- Use of the target ontology's term IRIs in other ontologies. This can
  be evidenced by linking to the other ontology that uses an ontology
  term IRI from this ontology

- Imports in other ontologies, again, evidenced through a link to the
  importing ontology

- A documentation page with links to databases using the ontology for
  annotation

- Use in semantic web projects (e.g., Open PHACTS usage)

- Use in diverse software applications, including text mining or
  analysis pipelines

- Publications showing the ontology being used in research (evidenced
  by citation details for the publications; if behind paywall it may
  be necessary to provide a PDF for the paper)

- Citations to the ontology publication(s); such citations are only
  relevant if the authors indicate actual use of the cited ontology
  within some community (mere mention of the existence is not enough
  to warrant inclusion)

- Documentation of requests from multiple users, e.g., via an issue
  tracker (provide a link to the issue tracker online)

- Use of the terms from the ontology to structure or annotate
  experimental or derived data (e.g. GOA; provide details of how to
  review the annotations)

## Counter-Examples

Mere mention of the existence of an ontology in a publication is not
enough to count as evidence of usage

## Criteria for Review

An ontology that has not been used by other than the developer(s) is not
yet ready for review. To pass review, the ontology developers must demonstrate at least three
external users specified within. External users are defined either as researchers not
significantly overlapping in personnel with the developers or three
independent groups with three independent artefacts (db, etc) that use
the ontology.

[This check is automatically validated.](checks/fp_009)

## Feedback and Discussion

To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%239+%22Users%22+%3CENTER+ISSUE+TITLE%3E).

To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Technical+WG,automated+validation+of+principles&title=Principle+%239+%22Users%22+-+automated+validation+%3CENTER+ISSUE+TITLE%3E).
