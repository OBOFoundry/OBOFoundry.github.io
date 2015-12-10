---
layout: principle
id: fp-011-locus-of-authority
title: locus of authority / contact person
---

## Principle Name

contact person

## Summary
There should be a single person who is responsible for communications between the 
community and the ontology developers, for communicating with the Foundry on all 
Foundry-related matters, for mediating discussions involving  maintenance in the 
light of scientific advance, and for ensuring that all user feedback is addressed.

## Purpose
It is important that there is a single person responsible for communication rather 
than a group of people or a list. Often in communications to a list, the responsibility 
for responding can be diffused and it is likely that in some scenarios no response will 
be given. It may also, from time to time, be necessary to engage in strategic 
communications (e.g. relating to funding or collaboration possibilities) that are not 
able to be made public, and these should not be conducted on public mailing lists. The 
designation of a single contact person is not to be interpreted as a designation for credit.
 
## Implementation
    
### Recommendation: 
The name and email address of this person should be provided when requesting to include 
an ontology in the OBO Foundry (or, better yet, when requesting inclusion in the OBO 
Library), and should be listed in the [OBO Registry] 
(http://obofoundry.org). 
This person must be subscribed to 
obo-discuss in order to be kept abreast of community developments of relevance to 
participating ontology projects. The email address of the person who is the locus of the 
authority must be kept up-to-date, and before that person ceases to have responsibility 
for the project, they should identify a replacement and update the metadata accordingly 
(via the [OBO Foundry issue tracker] (https://github.com/OBOFoundry/OBOFoundry.github.io/issues)) before they move on. The contact person can, of course, delegate 
these responsibilities as necessary.

### Examples: 

For ChEBI, the primary contact person is Janna Hastings (hastings@ebi.ac.uk). 

This can be seen in the [chebi.md](https://github.com/OBOFoundry/OBOFoundry.github.io/blob/master/ontology/chebi.md) file

```
contact:
  email: hastings@ebi.ac.uk
  label: Janna Hastings
```

### Counterexamples: 

Do not use a mailing list

for ChEBI, chebi-help@ebi.ac.uk

## History

### Original Formulation

```
 (Name: Locus of Authority) There should be a single person who is responsible for the 
 ontology, for ensuring continued maintenance in light of scientific advance and prompt 
 response to user feedback, Contact information for this person should be provided on the 
 ontology website, and listed in the OBO Library Metadata File.
 
 There should be a single person (perhaps the same person) who is responsible for liaison 
 between the ontology developers and the OBO Foundry coordinating editors. 

```

<Category:Principles> <Category:Accepted>
