---
layout: principle
id: fp-002-format
title: Common Format (principle 2)
---
GO TO: [Recommendations/Requirements](#recommendations-and-requirements) &#124; [Implementation](#implementation) &#124; [Examples/Counter&#8209;Examples](#examples) &#124; [Criteria&nbsp;for&nbsp;Review](#criteria-for-review) &#124; [Feedback/Discussion](#feedback-and-discussion)

## Summary

The ontology is made available in a common formal language in an accepted concrete syntax.

## Purpose

A common format allows the maximum number of people to access and reuse an ontology.

## Recommendations and Requirements

All ontologies MUST have at least one OWL product whose name corresponds to the registered prefix (e.g., 'GO' --> go.owl, 'OBI' --> obi.owl). Thus the ontology whose IRI is http://purl.obolibrary.org/obo/ro.owl (known to the OBO Foundry as 'RO'), must have at least the product ro.owl. Developers are free to use whatever combination of technologies and formats is appropriate for development. However, the official OWL PURL (see [Principle 3](https://obofoundry.org/principles/fp-003-uris.html)) for the ontology MUST resolve to a syntactically valid OWL file using the [RDF-XML](https://www.w3.org/TR/rdf-syntax-grammar/) syntax.

Developers can OPTIONALLY produce ontologies in other formats. These are conventionally the same IRI as the owl, but with .owl changed to the relevant extension (e.g., '.obo', '.json'). Note that such products are not listed by default. If you produce an additional format product, you should register it under the 'products' field in the appropriate metadata file found in this [folder](https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/ontology).

## Implementation

ROBOT offers functionality to convert a variety of formats, including OBO, to RDF/XML. Protégé allows you to save ontologies in RDF/XML, as well. The [Ontology 101 Tutorial](https://ontology101tutorial.readthedocs.io/en/latest/StartingProtege.html) has directions on starting and saving in Protégé.

## Examples

- The [Gene Ontology](http://geneontology.org) is maintained as OBO-Format. It is automatically converted to OWL and is available in both OBO and OWL via the OBO Foundry.

- The [ChEBI ontology](https://www.ebi.ac.uk/chebi/) is maintained in a relational database using a custom schema, but makes an OBO-Format file available that is automatically converted to OWL. It is available in both OBO and OWL via the OBO Foundry.

- [OBI](http://obi-ontology.org) is maintained as an OWL ontology.

## Counter-Examples

An ontology that is in Frames format, OWL/XML, or OWL Manchester Syntax.

## Criteria for Review

The ontology MUST be available in RDF/XML format.

[This check is automatically validated.](checks/fp_002) The automatic check fully covers the requirements for this principle.

## Feedback and Discussion

To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%232+%22Format%22+%3CENTER+ISSUE+TITLE%3E).

To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Technical+WG,automated+validation+of+principles&title=Principle+%232+%22Format%22+-+automated+validation+%3CENTER+ISSUE+TITLE%3E).
