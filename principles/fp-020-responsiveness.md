---
layout: principle
id: fp-020-responsiveness
title: Responsiveness (principle 20)
---

## Summary

Ontology developers MUST offer channels for community participation and SHOULD be responsive to requests.

## Purpose

Ontology development benefits from community input, which is strongly encouraged by the OBO Foundry. Accordingly, "responsiveness" is a key quality of our general collaborative spirit. This principle is intended to ensure that channels for community input are available and that responses to input are given swiftly.

Recommendations and Requirements

---

Ontology developers MUST set up a mechanism to track community requests and suggestions (collectively, “issues”), and SHOULD aim to respond within 2-5 working days. Optional: Establish a discussion forum for more general communication with and between users.

Expectations of responsiveness:

1. Issues are contributions - and should be met by a thankful attitude. When receiving an item on your issue tracker, the first thing to do is thank the contributor, even if it cannot be addressed right away.
2. If an issue cannot be addressed right away, explain when you plan to address the issue.
3. Do not close issues without responding. If an issue is out of scope for a repository, recommend moving it to a different repository.
4. It is recommended that one or more developers be designated to triage issues.

## Implementation

A discussion mailing list and issue tracker are required to obtain an OBO Foundry PURL. The OBO Foundry offers the following recommendations on the responsiveness in issue trackers (GitHub is recommended).

1. Specify the URL for an issue tracker (GitHub is recommended) in the ontology configuration file (YAML) that is used to display ontology details on the OBO Foundry web site.
2. Optional: Establish a discussion forum (For example, Google groups mailing list, Slack, Twitter).

Specification of the tracker is done using the following text (customized for your ontology) within its [metadata file](https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/ontology):

`tracker: https://github.com/geneontology/go-ontology/issues/ `

## Examples

Issue tracker: https://github.com/monarch-initiative/mondo/issues

Discussion list: mondo-users@googlegroups.com

Collaboration of this sort can be demonstrated by having an active discussion mailing list, or responsiveness to community requests on a GitHub tracker.

## Counter-Examples

Waiting until an issue is resolved before responding, if such resolution comes well after submission of a ticket.

## Criteria for Review

There is a functioning issue tracker for ontology requests specified on the OBO Foundry web site.

[This check is automatically validated.](checks/fp_020)

## Feedback and Discussion

To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%2320+%22Responsiveness%22+%3CENTER+ISSUE+TITLE%3E).

To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Technical+WG,automated+validation+of+principles&title=Principle+%2320+%22Responsiveness%22+-+automated+validation+%3CENTER+ISSUE+TITLE%3E).
