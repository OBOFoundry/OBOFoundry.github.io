---
layout: principle
id: fp-010-collaboration
title: Commitment To Collaboration (principle 10)
---

## Summary

OBO Foundry ontology development, in common with many other standards-oriented scientific
activities, should be carried out in a collaborative fashion.

## Purpose
The benefits of collaboration are threefold: (1) Avoid duplication of work; (2) Increase interoperability; and (3) Ensure that ontology content is both scientifically sound and meets community needs.

## Implementation
### Recommendation:
It is expected that Foundry ontologies will collaborate with other Foundry ontologies, particularly in ensuring orthogonality of distinct ontologies, in re-using content from other ontologies in cross-product definitions where appropriate, and in establishing and evolving Foundry principles to advance the Foundry suite of ontologies to better serve the joint users. Where there are multiple ontology providers in a particular domain, they are particularly encouraged to get together and determine how the domain should be divided between the ontologies, or whether the ontologies should be merged into a single artifact. Should it be determined that there is a competing ontology in the same domain, the Foundry ontology should invite the developers of the external ontology to collaborate and should strive to negotiate an arrangement that is beneficial to both projects. If necessary, conflicts can be mediated in dedicated workshops or using the [obo-discuss mailing list](https://groups.google.com/forum/#!forum/obo-discuss) where Foundry advisors and members of the editorial board can help the parties negotiate to a mutually agreeable solution. 

Additionally, ontologies should have mechanisms in place to alert and announce changes in the ontology to relevant stakeholders and collaborators. This includes obsoletion of terms, and changes in classification that move multiple terms from one branch to another. The granularity of announcements should be decided with relevant stakeholders. For example, for some ontologies, curators need to know well in advance of proposed obsoletion changes to be able to migrate data and avoid stale annotations to obsolete terms. For ontologies that are leveraged for classification of other ontologies such as CHEBI, changes in classification criteria for high level terms can have wide-ranging impacts. There should be mechanisms to allow stakeholders to engage in discussions about major changes before they happen. 

### Examples:
* _Collaborative workshop_: http://ncorwiki.buffalo.edu/index.php/Protein_Ontology_Workshop 
* _Conflict resolution_: The Statistical Methods Ontology (STATO) and Ontology of Biological and Clinical Statistics (OBCS) both cover statistics. The developers of each have posted to the OBO Foundry discussion list to work out how to collaborate.
* _Contribution to external ontology_: Plant Ontology (PO) curators contribute definitions to Gene Ontology (GO) for biological processes and cell components in plants. PO then uses the GO terms in their definition of corresponding structures and stages.
*_Documentation of collaboration_: Cell Line Ontology (CLO), Cell Ontology (CL), and Ontology of Biomedical Investigations (OBI) published a paper sorting out their overlap and documented working together. Sarntivjiai et al., "CLO: The cell line ontology", J. Biomed. Sem., 2014, 5, 37. http://www.ncbi.nlm.nih.gov/pubmed/25852852
* _Providing terms upon request_: The Disease Ontology (DO) responded to a request from the PRotein Ontology for curation of certain disease terms.

### Counter-examples: 
Interactions between ontologies developed by the same entity (person, consortium) are not evidence of collaboration.

## Criteria for Review
To pass review, the ontology developers must document their attempts at an open dialog with OBO Foundry members, for example by attempting to ascertain if there are other possible ontologies in (or overlapping) the domain of interest. Such documentation can be a simple pointer to an e-mail thread on the OBO discuss list. If there are other ontologies that might need to be aligned or have boundaries determined, evidence of coordination or cooperation should be provided. Further evidence of collaboration may include examples of terms that have been provided to other ontologies in the OBO Foundry community. Finally, hosting or participating in collaborative workshops or meetings attended by OBO Foundry community members is considered evidence of collaboration.

<Category:Principles> <Category:Accepted>
