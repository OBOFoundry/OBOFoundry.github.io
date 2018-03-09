---
layout: principle
id: fp-005-delineated-content
title: Scope
---


NOTE
-------
The wording of this principle is still in progress, with some issues still to be addressed (see Issues To Be Addressed below).

Summary
-------
The scope of an ontology is the extent of the domain or subject matter it intends to cover. The ontology must have a clearly specified scope and content that adheres to that scope.

Purpose
-------
An in-scope ontology prevents overlaps between ontologies (duplication of terms), facilitates user searches for specific content, and enables quick selection of ontologies of interest, yet still allows for new terms to be created via combination of existing terms (cross-products).

Implementation
-------
The domain (scope) covered by the ontology should be clearly stated. The statement should be brief and free of jargon; a few sentences should suffice. The content of the ontology should stay within the confines of the stated scope.

Recommendations
-------
Ideally the scope should be fairly narrow. Required terms that are out of scope should be imported from the appropriate ontology.



Issues To Be Addressed (partial list):
-------
1.Would like a metadata tag in the ontology itself for this. TBD.

2.Possible need for controlled vocabulary for scope/domain (for example: Anatomy, Upper Level Ontology, Disease, Phenotype, Applicable taxonomy)


Date Accepted
-------------

-   original principle

History
-------

### Original Formulation

```
 The ontology has a clearly specified and clearly
delineated content.

The ontology must be orthogonal to other ontologies already lodged
within OBO.

The major reason for this principle is to allow two different
ontologies, for example anatomy and process, to be combined through
additional relationships. These relationships could then be used to
constrain when terms could be jointly applied to describe complementary
(but distinguishable) perspectives on the same biological or medical
entity.

As a corollary to this, we would strive for community acceptance of a
single ontology for one domain, rather than encouraging rivalry between
ontologies.


```

Examples
--------

Counter-Examples
----------------

<Category:Principles> <Category:Accepted>
