---
layout: principle
id: fp-002-format
title: format
---

Principle Name
--------------

common format

Summary
-------

The ontology is made available in a common formal language in an
accepted concrete syntax.

Purpose
-------

A common format allows the maximum number of people to access and reuse
an ontology.

Implementation
--------------

### Recommendations

The ontology should be available in at least one of the following
formats:

-   OBO Format
-   OWL or OWL2 concrete syntax
    -   RDF/XML
    -   OWL2-XML
    -   OWL2-Manchester Syntax

If you intend to use your ontology for semantic web applications, it
should be in OWL. OWL is part of the W3C's Semantic Web technology
stack, which includes RDF [RDF Concepts] and SPARQL [SPARQL].

### Examples

-   The Gene Ontology is maintained as OBO-Format. It is automatically
    converted to OWL and is available in both OBO and OWL via the OBO
    Foundry.

-   The ChEBI ontology is maintained in a relational database using a
    custom schema, but makes an OBO-Format file available that is
    automatically converted to OWL. It is available in both OBO and OWL
    via the OBO Foundry.

OBI is maintained as an OWL ontology.

### Counter examples

An ontology that is in Frames format.

Criteria for Review
-------------------

The ontology is available in at least one of the following formats:

-   OBO Format
-   OWL or OWL2 concrete syntax
    -   RDF/XML
    -   OWL2-XML
    -   OWL2-Manchester Syntax

History
-------

Revised wording for principle accepted March 3, 2015

### Original Formulation

\<blockquote\>

The ontology is in, or can be expressed in, a common shared syntax. This
may be either the OBO syntax, extensions of this syntax, or OWL.

The reason for this is that the same tools can then be usefully applied.
This facilitates shared software implementations. This criterion is not
met in all of the ontologies currently listed, but we are working with
the ontology developers to have them available in a common OBO syntax.
\</blockquote\>

<Category:Principles> <Category:Accepted>
