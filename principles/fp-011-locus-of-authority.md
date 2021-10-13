---
layout: principle
id: fp-011-locus-of-authority
title: Locus of Authority (principle 11)
---

## Summary
There should be a person who is responsible for communications between the 
community and the ontology developers, for communicating with the Foundry on all 
Foundry-related matters, for mediating discussions involving maintenance in the 
light of scientific advance, and for ensuring that all user feedback is addressed.

[This check is automatically validated.](checks/fp_011)

## Purpose
It is important that there is a person responsible for communication rather than a group of people or a list. Often in communications to a list, the responsibility for responding can be diffused and it is likely that in some scenarios no response will be given. It may also, from time to time, be necessary to engage in strategic communications (e.g. relating to funding or collaboration possibilities) that are not able to be made public, and these should not be conducted on public mailing lists. The designation of a contact person is not to be interpreted as a designation for credit. Note that alternative contacts can be designated in case the primary contact is unavailable. However, as for the primary contact, each alternative contact must be an individual.

## Recomendations and Requirements
A primary contact person MUST be assigned.
The name, email address and GitHub username of the contact person MUST be provided when requesting to register with [OBO](http://obofoundry.org), and the email address MUST NOT be a mailing list. If the person does not already have a GitHub account, we request that they [create one](https://github.com/join). The contact person MUST be subscribed to obo-discuss in order to be kept abreast of community developments of relevance to 
participating ontology projects, but the primary contact person can, of course, delegate 
these responsibilities for the project as necessary. The email address of the person who is the locus of the 
authority MUST be kept up-to-date, and before that person ceases to have responsibility 
for the project, they should identify a replacement and update the metadata accordingly. 
(via the [OBO Foundry issue tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues)) before they move on.

## Implementation

The following should be included in the metadata file for your ontology, found in this [folder](https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/ontology) (replacing with the correct email, name, and GitHub username):
<pre>
contact:
   email: foo@bar.com
   label: John Smith
   github: jsmith123</pre>
   
Instructions for direct editing of the metadata file can be found in the [FAQ](http://obofoundry.github.io/faq/how-do-i-edit-metadata.html). Alternatively, a request to change the metadata can be submitted to the [OBO Foundry issue tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues).

### Examples: 
For Mondo, the primary contact person is Nicole Vasilevsky (nicole@tislab.org) and her GitHub handle is: nicolevasilevsky. 

### Counter-Examples: 
Mailing list; for ChEBI, chebi-help@ebi.ac.uk

### Criteria for Review

Email address will be checked to ensure it is written in a standard format.

<Category:Principles> <Category:Accepted>
