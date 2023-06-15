---
layout: principle
id: fp-006-textual-definitions
title: Textual Definitions (principle 6)
---
GO TO: [Recommendations/Requirements](#recommendations-and-requirements) &#124; [Implementation](#implementation) &#124; [Examples/Counter&#8209;Examples](#examples) &#124; [Criteria&nbsp;for&nbsp;Review](#criteria-for-review) &#124; [Feedback/Discussion](#feedback-and-discussion)

## Summary

The ontology has textual definitions for the majority of its classes and for top level terms in particular.

## Purpose

A textual definition provides a human-readable understanding about what is a member of the associated class. Textual definitions are, optimally, in concordance with associated machine-readable logical definitions (the latter of which are OPTIONAL).

## Recommendations and Requirements

Textual definitions MUST be unique within an ontology (i.e. no two terms should share a definition) and be written in English. Textual definitions SHOULD follow Aristotelian form (e.g. “a B that Cs” where B is the parent and C is the differentia), where this is practical.

For terms lacking textual definitions, there should be evidence of implementation of a strategy to provide definitions for all remaining undefined terms. In lieu of textual definitions, there can be elucidations when the term can not be rigorously defined. Note that textual definitions can be programmatically generated from logical definitions, if available (see [http://oro.open.ac.uk/21501/1/](http://oro.open.ac.uk/21501/1/)). In addition, [Dead Simple Ontology Design Patterns](https://github.com/INCATools/dead_simple_owl_design_patterns) (DOSDPs) can be used to generate both textual and logical definitions. DOSDPs are design specifications, written in YAML format, that specify structured text definitions and logical definitions for groups of ontology terms. These are widely used in many OBO Foundry ontologies, such as Mondo and uPheno. For some example patterns, see [Mondo patterns](https://mondo.readthedocs.io/en/latest/editors-guide/patterns/) and [uPheno patterns](https://github.com/obophenotype/upheno/tree/master/src/patterns/dosdp-patterns).

Logical definitions, when present, should agree with textual definitions and vice versa. This is important for two reasons: (1) Reasoners classify terms solely based on logical definitions, while humans predominantly classify terms based on textual definitions, and mismatches between the two can cause unexpected misclassification; and (2) Curators could create incorrect annotations. An example of mismatched definitions:

```
http://purl.obolibrary.org/obo/OBI_0003243 blood assay datum

Text definition: "A data item that is the specified output of a blood assay."
```

Logical definition (that does not match the textual def): 
```
= 'information content entity' and (is_specified_output_of some 'blood assay')
```

Logical definition (that matches the textual def): 
```
= 'data item' and (is_specified_output_of some 'blood assay')
```

While both logical definitions can be used to define the class, one better fits with the textual definition than the other.

Note that it’s permissible to not to have a logical definition if the class is fuzzy or the axioms/relations can’t be composed equivalence axioms.

Terms often benefit from examples of usage, as well as editor notes about edge cases and the history of the term, but these should be included as separate annotations and not in the definition.

Instances, such as organizations or geographical locations, can benefit from definitions although it is understood that definitions for instances are not required. It is recognized that OBO format (e.g., versions 1.2 and 1.4) does not allow this as an option.

## Implementation

Textual definitions should be identified using the annotation property: ‘definition’ [http://purl.obolibrary.org/obo/IAO_0000115](http://purl.obolibrary.org/obo/IAO_0000115). The source of the definition should be provided using the annotation property ‘definition source’ [http://purl.obolibrary.org/obo/IAO_0000119](http://purl.obolibrary.org/obo/IAO_0000119), or as an axiom annotation on the definition assertion.

An example of providing source in an axiom annotation:

```
<http://purl.obolibrary.org/obo/GO_0000109> rdf:type owl:Class ;
                                            <http://purl.obolibrary.org/obo/IAO_0000115> "Any complex formed of proteins that act in nucleotide-excision repair."@en ;
                                            rdfs:label "nucleotide-excision repair complex"^^xsd:string .

[ rdf:type owl:Axiom ;
   owl:annotatedSource <http://purl.obolibrary.org/obo/GO_0000109> ;
   owl:annotatedProperty <http://purl.obolibrary.org/obo/IAO_0000115> ;
   owl:annotatedTarget "Any complex formed of proteins that act in nucleotide-excision repair."@en ;
   <http://www.geneontology.org/formats/oboInOwl#hasDbXref> "PMID:10915862"^^xsd:string
 ] .

```

this corresponds to the obo format:

```
id: GO:0000109
name: nucleotide-excision repair complex
def: "Any complex formed of proteins that act in nucleotide-excision repair." [PMID:10915862]
```

## Examples

<i><b>Class</b></i>: primary phloem sieve element
<br> <i><b>Term IRI</b></i>: [http://purl.obolibrary.org/obo/PO_0025452](http://purl.obolibrary.org/obo/PO_0025452)
<br> <i><b>Definition</b></i>: A sieve element (PO:0025406) that is part of a portion of primary phloem (PO:0006075).
<br> <i><b>Logical definition</b></i>:

```
'sieve element'
 and ('part of' some 'primary phloem')
```

<i><b>Class</b></i>: ecto-epithelial cell
<br> <i><b>Term IRI</b></i>: [http://purl.obolibrary.org/obo/CL_0002077](http://purl.obolibrary.org/obo/CL_0002077)
<br> <i><b>Definition</b></i>: An epithelial cell derived from ectoderm.
<br> <i><b>Logical definition</b></i>:

```
'epithelial cell'
 and ('develops from' some 'ectodermal cell')
```

## Counter-Examples

- No definition
- Circular/Self-referential definition
  “A chromatography device is a device that uses chromatography” when chromatography is not defined elsewhere

## Criteria for Review

Each definition MUST be unique. Each entity MUST NOT have more than one textual definition (tagged using [IAO:0000115](http://purl.obolibrary.org/obo/IAO_0000115)). Textual definitions SHOULD be provided for most terms, and for top level terms especially.

[This check is automatically validated.](checks/fp_006)

## Feedback and Discussion

To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%236+%22Definitions%22+%3CENTER+ISSUE+TITLE%3E).

To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Technical+WG,automated+validation+of+principles&title=Principle+%236+%22Definitions%22+-+automated+validation+%3CENTER+ISSUE+TITLE%3E).
