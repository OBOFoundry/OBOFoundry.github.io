---
layout: doc
title: Ontology Review Process
---

This page deals with the process, policies, and guidelines for manually reviewing newly-submitted ontologies, with particular focus on operational aspects such as:

- which ontologies are reviewed, and in what order?
- how are reviewers chosen?
- what is the workflow for conducting a review?
- what are the criteria used?

Newly-submitted ontologies are reviewed manually after passing the automated evaluation. Though the automated evaluation checks for adherence to [OBO Foundry principles](http://www.obofoundry.org/principles/fp-000-summary.html), it cannot capture certain nuances outlined in the principles nor evaluate ontology quality. The purpose of the manual review is to check the ontology for issues that the NOR Dashboard does not cover.

# Steps prior to manual review

Once an ontology is submitted to the OBO Foundry, it is added to the New Ontology Dashboard for automated evaluation. The steps involved in ontology submission and subsequent dashboard evaluation are described in detail in this [FAQ answer](http://obofoundry.org/faq/how-do-i-register-my-ontology.html) and links therein.

# Review priority

All submitted ontologies will be manually reviewed based on the order in which the ontology becomes compliant with the automated evaluation (that is, when the [New Ontology Request (NOR) Dashboard](http://obofoundry.org/obo-nor.github.io/dashboard/index.html) status is 'pass').

# Choosing reviewers

Reviewers are chosen on a rotating basis from the members of the [OBO Foundry Operations Committee](http://obofoundry.org/docs/Membership.html).

# Ontology review workflow

The manual process begins once a reviewer is assigned. The reviewer will assess key aspects of the ontology (see below) and report the findings both to the submitter (via the issue tracker ticket used for submission) and to the OBO Operations Committee. The latter will discuss the findings and make a recommendation for acceptance, revision, or rejection.

# Manual review criteria

For the list below, yes/no questions include the expected answers in square brackets after the question. Criteria for review minimally include:

1. Ontology scope
   - Do the terms fall within the ontology's stated target domain of knowledge? [yes]
   - Was the ontology developed for a very specific purpose or community?
2. Terms with the new ontology prefix
   - Do the terms follow the OBO identifier scheme? [yes]
   - Are there terms with the same <i>meaning</i> available in another OBO Foundry ontology? [no]
   - Is there another OBO Foundry ontology whose scope covers any of the new terms? [no]
3. Correct use of imported terms
   - If the ontology reuses terms from other OBO ontologies, are they used accurately? [yes] 
   - Are imported terms in appropriate hierarchies, and do they preserve the term's upper-level alignment? [yes]
   - Are any additional axioms used for these terms correct in both a technical (e.g. passes reasoning) and substantive sense? [yes]
4. Basic review of axiomatic patterns
   - Are axioms generally stated simply or are they highly complex? (Highly complex axioms will require extra scrutiny.)
   - Are existential restrictions used correctly? [yes] (Typical mistakes include “R some (A and B and C)” to mean “(R some A and R some B and R some C)”).
5. Appropriate use of object properties - 
   - Are object properties used in a manner consistent with their definitions, domain, and range? [yes] (Examples of incorrect usage include those based on some interpretation of the label of the object property but not actually fitting the property definition or domain and range.)
6. Responsiveness to suggested changes - 
   - Have the developers been willing to fix any identified issues during the review? [yes]


