---
layout: principle
id: fp-002-format
title: Common Format (principle 2)
---

## Summary

The ontology is made available in a common formal language in an accepted concrete syntax.

[This check is automatically validated.](checks/fp_002)

## Purpose

A common format allows the maximum number of people to access and reuse an ontology.

## Implementation

### Requirements and Recommendations

We make a distinction between how an ontology is developed and how it is presented for release. Developers are free to use whatever combination of technologies and formats is appropriate for development. However, the official OWL PURL for the ontology must resolve to a syntactically valid OWL file using the [RDF-XML](https://www.w3.org/TR/rdf-syntax-grammar/) syntax.

Note: some groups publish an .obo version, and the OBO Foundry pipeline takes care of making the valid .owl file. See the FAQ for details. You may also submit the ontology for review as OBO, see 'criteria for review' below.

Note also that previously we recommended that ontologies may be available in Manchester syntax or OWL-XML, but we have revised this in order to make the official OWL release consumable by a wider variety of tools.

### Examples

- The [Gene Ontology](http://geneontology.org) is maintained as OBO-Format. It is automatically converted to OWL and is available in both OBO and OWL via the OBO Foundry.

- The [ChEBI ontology](https://www.ebi.ac.uk/chebi/) is maintained in a relational database using a custom schema, but makes an OBO-Format file available that is automatically converted to OWL. It is available in both OBO and OWL via the OBO Foundry.

- [OBI](http://obi-ontology.org) is maintained as an OWL ontology.

### Counter-examples

An ontology that is in Frames format, OWL/XML, or OWL Manchester Syntax.

## Criteria for review

The ontology is available in at least one of the following formats:

- OBO Format
- OWL or OWL2 RDF/XML

## History

Revised wording for principle accepted March 3, 2015.

### Original formulation

The ontology is in, or can be expressed in, a common shared syntax. This may be either the OBO syntax, extensions of this syntax, or OWL.

The reason for this is that the same tools can then be usefully applied. This facilitates shared software implementations. This criterion is not met in all of the ontologies currently listed, but we are working with the ontology developers to have them available in a common OBO syntax.
