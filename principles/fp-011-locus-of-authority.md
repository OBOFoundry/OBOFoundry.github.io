---
layout: principle
id: fp-011-locus-of-authority
title: Locus of Authority (principle 11)
---
GO TO: [Recommendations/Requirements](#recommendations-and-requirements) &#124; [Implementation](#implementation) &#124; [Examples/Counter&#8209;Examples](#examples) &#124; [Criteria&nbsp;for&nbsp;Review](#criteria-for-review) &#124; [Feedback/Discussion](#feedback-and-discussion) 

## Summary

There should be a person who is responsible for communications between the
community and the ontology developers, for communicating with the Foundry on all
Foundry-related matters, for mediating discussions involving maintenance in the
light of scientific advance, and for ensuring that all user feedback is addressed.

## Purpose

It is important that there is a person responsible for communication rather than a group of people or a list. Often in communications to a list, the responsibility for responding can be diffused and it is likely that in some scenarios no response will be given. It may also, from time to time, be necessary to engage in strategic communications (e.g. relating to funding or collaboration possibilities) that are not able to be made public, and these should not be conducted on public mailing lists. The designation of a contact person is not to be interpreted as a designation for credit. Note that alternative contacts can be designated in case the primary contact is unavailable. However, as for the primary contact, each alternative contact must be an individual.

## Recommendations and Requirements

A primary contact person MUST be assigned.
The name, email address and GitHub username of the contact person MUST be provided when requesting to register with [OBO](http://obofoundry.org). The contact person MUST be subscribed to obo-discuss in order to be kept abreast of community developments of relevance to
participating ontology projects, but the primary contact person can, of course, delegate
these responsibilities for the project as necessary. The email address of the person who is the locus of the
authority MUST be kept up-to-date, and before that person ceases to have responsibility
for the project, they should identify a replacement and update the metadata accordingly
(via the [OBO Foundry issue tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues)) before they move on.

## Implementation

First, read the [FAQ](http://obofoundry.github.io/faq/how-do-i-edit-metadata.html) on how to edit the metadata for your ontology.

The contact email MUST NOT be a mailing list. The GitHub account MUST be for the individual designated as the locus of authority. If this person does not already have a GitHub account, we request that they [create one](https://github.com/join). Then, add the following to your [metadata file](https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/ontology) (replacing with the correct email, name, and GitHub username):

`contact: email: foo@bar.com label: John Smith github: jsmith123`

## Examples:

For Mondo, the primary contact person is Nicole Vasilevsky (nicole {at} tislab.org) and her GitHub handle is: nicolevasilevsky.

## Counter-Examples:

- Mailing list; such as go-discuss {at} geneontology.org
- Help desk; such as chebi-help {at} ebi.ac.uk
- Group email; such as ontologygroup {at} resource.org (where it is unclear precisely who receives the email and who is responsible for responding)
- Issue tracker;
- Email address of responsible person's assistant or admin; the responsible person must be <i>directly</i> reachable

## Criteria for Review

Email address will be checked to ensure it is for an individual and that it is written in a standard format.

[This check is automatically validated.](checks/fp_011)

## Feedback and Discussion

To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%2311+%22Contact%22+%3CENTER+ISSUE+TITLE%3E).

To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Technical+WG,automated+validation+of+principles&title=Principle+%2311+%22Contact%22+-+automated+validation+%3CENTER+ISSUE+TITLE%3E).
