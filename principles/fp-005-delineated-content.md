---
layout: principle
id: fp-005-delineated-content
title: Scope (principle 5)
---

## NOTE

The wording of this principle is still in progress, with some issues still to be addressed (see Issues To Be Addressed below).

## Summary

The scope of an ontology is the extent of the domain or subject matter it intends to cover. The ontology must have a clearly specified scope and content that adheres to that scope.

## Purpose

An in-scope ontology prevents overlaps between ontologies (duplication of terms), facilitates user searches for specific content, and enables quick selection of ontologies of interest, yet still allows for new terms to be created via combination of existing terms (cross-products).

## Recommendations and Requirements

Ideally the scope should be fairly narrow. Required terms that are out of scope should be imported from the appropriate ontology unless no such ontology exists and there is an immediate need for an out-of-scope term (or set thereof). We encourage the ontology maintainers to create a shareable file with such terms so that the community can access, reuse, edit, and add these new terms as new ontologies with the intended scope are developed.

## Implementation

The domain (scope) covered by the ontology should be clearly stated. The statement should be brief and free of jargon; a few sentences should suffice. The content of the ontology should stay within the confines of the stated scope. Out-of-scope terms should be placed within a separate module that can be imported/exported as a single unit.
Generic terms must be maintained with community needs in mind. Mid/upper level terms should be considered for the [Core Ontology for Biology and Biomedicine (COB)](https://obofoundry.org/ontology/cob.html).


## Examples

## Counter-Examples

## Issues To Be Addressed (partial list):

1.Would like a metadata tag in the ontology itself for this. TBD.

2.Possible need for controlled vocabulary for scope/domain (for example: Anatomy, Upper Level Ontology, Disease, Phenotype, Applicable taxonomy)

## Criteria for Review

A scope (‘domain’) MUST be declared in the registry data, and terms from the ontology have to fall within that scope.

[This check is automatically validated.](checks/fp_005)

## Feedback and Discussion

To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%235+%22Scope%22+%3CENTER+ISSUE+TITLE%3E).

To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Technical+WG,automated+validation+of+principles&title=Principle+%235+%22Scope%22+-+automated+validation+%3CENTER+ISSUE+TITLE%3E).
