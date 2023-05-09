---
layout: principle
id: fp-009-users
title: Documented Plurality of Users (principle 9)
---
GO TO: [Recommendations/Requirements](#recommendations-and-requirements) &#124; [Implementation](#implementation) &#124; [Examples/Counter&#8209;Examples](#examples) &#124; [Criteria&nbsp;for&nbsp;Review](#criteria-for-review) &#124; [Feedback/Discussion](#feedback-and-discussion)

## Summary

The ontology developers should document that the ontology is used by
multiple independent people or organizations.

## Purpose

This principle aims to ensure that the ontology tackles a relevant
scientific area and does so in a usable and sustainable fashion.

## Recommendations and Requirements

It is important to be able to illustrate usage outside of the immediate circle of ontology developers and stakeholders. Demonstrations of usage MUST be publicly available. Preferred indicators of usage are those that directly demonstrate such, including:

- Use of the target ontology's term IRIs in an external ontology. Indicators of this type MUST include one or more IRIs for a term _within the external ontology_ that uses a term from the target ontology.
  
- Documentation of requests from multiple users. Indicators of this type MUST link to specific requests in the issue tracker, OR link to an issue tracker search (for example, showing new term requests), OR link to an email thread or other mechanism _if publicly viewable_.

- Publications showing the ontology being used in research by external users. Indicators of this type MUST provide citation details for the publications (link to PubMed or full text) and MUST include a sentence demonstrating the use (preferably taken from the title, abstract, or full text of the cited reference). Note that if citing full text that is behind a paywall, it may be necessary to provide a PDF for the paper.

- Use of terms from the ontology to provide structure to or annotation of experimental or derived data. Indicators of this type MUST provide a link to a URL that shows the annotation or demonstrates the structure.

- Terms imported into external ontologies. Indicators of this type MUST link to direct evidence of import, such as the OntoBee page for the term (which includes a section indicating which ontologies have imported it), OR to the OBO Dashboard page for the target ontology (which includes a section "Which ontologies use it?"), OR to any other source of direct evidence. A link to the importing ontology as a whole does not constitute appropriate evidence, as this is too indirect (that is, it requires extra steps to verify).

- Inclusion of the target ontology on a documentation page that lists which resources are used for the project. Indicators of this type MUST include a link to the appropriate documentation page.

Other indicators are currently possible as well:

- Use in semantic web projects (e.g., Open PHACTS usage).

- Use in software applications, including text mining or analysis pipelines.

- Citations to the ontology publication(s); Note that such citations are only
  relevant if the authors indicate actual use of the cited ontology
  within some community (mere mention of the existence is not enough
  to warrant inclusion).

Note that the ontology can still be listed on the OBO Foundry website while publicising your resource in appropriate channels and searching for users with needs you can meet. 

## Implementation

The ontology developers MUST provide links/citations to publicly available evidence of
use within your ontology [metadata file](https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/ontology) as given below (replacing with the correct group name, link, and description):

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

Use of PSI-MOD term IRI (in the form of a CURIE) in the PR ontology:
```
- user: http://purl.obolibrary.org/obo/pr
  description: Protein Ontology
  examples:
   - url: https://proconsortium.org/app/export/obo/PR:000027653/
     description: OBO Format stanza showing use of PSI-MOD term in logical definition
```
Term requests to PR from multiple users:
```
- user: (multiple)
  description: Term requests made via the Protein Ontology GitHub tracker
  examples:
   - url: https://github.com/PROconsortium/PRoteinOntology/issues?q=is%3Aissue+label%3A%22Term+Request%22
     description: List of issues tagged with 'Term Request' to PRO
```
Publication showing the Disease Ontology being used in research by external users
```
- user: https://pubmed.ncbi.nlm.nih.gov/36860337/
  description: Machine learning-based prediction of candidate gene biomarkers correlated with immune infiltration in patients with idiopathic pulmonary fibrosis
  examples:
   - url: https://pubmed.ncbi.nlm.nih.gov/36860337/
     description: In abstract, "Functional annotation, pathway enrichment, Disease Ontology and gene set enrichment analyses revealed..."
```
Use of terms from GO for annotation:
```
- user: https://www.uniprot.org
  description: UniProt
  examples:
   - url: https://www.uniprot.org/uniprotkb/Q15796/entry#function
     description: Functional annotation using GO (see subsection entitled "GO annotations")
```
OBI terms imported into external ontologies
```
- user: (multiple)
  description: Ontologies using OBI terms
  examples:
   - url: http://dashboard.obofoundry.org/dashboard/obi/dashboard.html
     description: List of ontologies using at least one OBI term (See section entitled "Info: Which ontologies use it?")
   - url: https://ontobee.org/ontology/OBI?iri=http://purl.obolibrary.org/obo/OBI_0000691
     description: List of ontologies using the term 'ABI 377 automated sequencer' (See section entitled "Ontologies that use the Class")
```

## Counter-Examples

- Mere mention of the existence of an ontology in a publication is not
enough to count as evidence of usage

- Reference to any evidence that cannot be viewed publicly

## Criteria for Review

Ontology developers must demonstrate at least three external users specified within the metadata file. External users are defined either as researchers not
significantly overlapping in personnel with the developers or three independent groups with three independent artefacts (db, etc) that use
the ontology. Note that new ontologies are not expected to have a plurality of users, and thus the automatic evaluation of this criterion can be ignored.

[This check is automatically validated.](checks/fp_009)

## Feedback and Discussion

To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%239+%22Users%22+%3CENTER+ISSUE+TITLE%3E).

To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Technical+WG,automated+validation+of+principles&title=Principle+%239+%22Users%22+-+automated+validation+%3CENTER+ISSUE+TITLE%3E).
