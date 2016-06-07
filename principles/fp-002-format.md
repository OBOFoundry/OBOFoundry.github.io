---
layout: principle
id: fp-002-format
title: common format
---

## Principle name

common format

## Summary

The ontology is made available in a common formal language in an accepted concrete syntax.

## Purpose

A common format allows the maximum number of people to access and reuse an ontology.

## Implementation

### Recommendations

The ontology should be available in at least one of the following formats:

- OBO Format
- OWL or OWL2 concrete syntax
    - RDF/XML
    - OWL2-XML
    - OWL2-Manchester Syntax

If you intend to use your ontology for semantic web applications, it should be in OWL. OWL is part of the W3C's Semantic Web technology stack, which includes RDF ([RDF Concepts](https://www.w3.org/TR/rdf11-concepts/)) and [SPARQL](https://www.w3.org/TR/sparql11-overview/).

### Examples

- The [Gene Ontology](http://geneontology.org) is maintained as OBO-Format. It is automatically converted to OWL and is available in both OBO and OWL via the OBO Foundry.

- The [ChEBI ontology](https://www.ebi.ac.uk/chebi/) is maintained in a relational database using a custom schema, but makes an OBO-Format file available that is automatically converted to OWL. It is available in both OBO and OWL via the OBO Foundry.

- [OBI](http://obi-ontology.org) is maintained as an OWL ontology.

### Counter-examples

An ontology that is in Frames format.

## Criteria for review

The ontology is available in at least one of the following formats:

- OBO Format
- OWL or OWL2 concrete syntax
    - RDF/XML
    - OWL2-XML
    - OWL2-Manchester Syntax

## History

Revised wording for principle accepted March 3, 2015.

### Original formulation

The ontology is in, or can be expressed in, a common shared syntax. This may be either the OBO syntax, extensions of this syntax, or OWL.

The reason for this is that the same tools can then be usefully applied. This facilitates shared software implementations. This criterion is not met in all of the ontologies currently listed, but we are working with the ontology developers to have them available in a common OBO syntax.

See the [wiki history](http://wiki.obofoundry.org/wiki/index.php?title=FP_002_format&action=history) for older formulations.
