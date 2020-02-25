---
layout: principle
id: fp-006-textual-definitions
title: Textual Definitions (principle 6)
---

NOTE
-------

The content of this page is scheduled to be reviewed. Improved wording will be posted as it becomes available.

Summary
-------

The ontology has textual definitions for the majority of its classes and for top level terms in particular.

[This check is automatically validated.](checks/fp_006)

Purpose
-------

A textual definition provides a human-readable understanding about what is a member of the associated class.

Recommendation
--------------

Textual definitions MUST be unique within an ontology (i.e. no two terms should share a definition). Textual definitions SHOULD follow Aristotelian form (e.g. “a B that Cs” where B is the parent and C is the differentia), where this is practical.

For terms lacking textual definitions, there should be evidence of implementation of a strategy to provide definitions for all remaining undefined terms. In lieu of textual definitions, there can be elucidations when the term can not be rigorously defined.

Terms often benefit from examples of usage, as well as editor notes about edge cases and the history of the term, but these should be included as separate annotations and not in the definition.

Instances, such as organizations or geographical locations, can benefit from definitions although it is understood that definitions for instances are not required. It is recognized that OBO format (e.g., versions 1.2 and 1.4) does not allow this as an option.

Implementation
--------------

Logical definitions should agree with textual definitions. In fact, logical definitions can be programmatically used to generate textual definitions (see http://oro.open.ac.uk/21501/1/)

Textual definitions should be identified using the annotation property: ‘definition’ http://purl.obolibrary.org/obo/IAO_0000115. The source of the definition should be provided using the annotation property ‘definition source’ http://purl.obolibrary.org/obo/IAO_0000119, or as an axiom annotation on the definition assertion.

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

Examples
--------

<i><b>Class</b></i>: reproductive shoot system
<br>  <i><b>Term IRI</b></i>: http://purl.obolibrary.org/obo/PO_0025082
<br>  <i><b>Definition</b></i>: A shoot system (PO:0009006) in the sporophytic phase that has as part at least one sporangium (PO:0025094).
<br>  <i><b>Logical definition</b></i>:
```intersectionOf: shoot system
intersectionOf: participates_in some reproductive shoot system development stage
```
<i><b>Class</b></i>: chromatography device
<br>  <i><b>Term IRI</b></i>: http://purl.obolibrary.org/obo/OBI_0000048
<br>  <i><b>Definition</b></i>: A device that facilitates the separation of mixtures. The function of a chromatography device involves passing a mixture dissolved in a "mobile phase" through a stationary phase, which separates the analyte to be measured from other molecules in the mixture and allows it to be isolated.
<br>  <i><b>Definition source</b></i>: http://en.wikipedia.org/wiki/Chromatography
<br>  <i><b>Logical definition</b></i>:
```
intersectionOf: device
intersectionOf: has_function some material separation function
```

Counter-Examples
----------------

-   No definition
-   Circular/Self-referential definition
    “A chromatography device is a device that uses chromatography” when chromatography is not defined elsewhere

Date Accepted
-------------

-   Revised wording for principle tentatively accepted June 19, 2018.


History
-------

### Original Formulation

```
 The ontologies include textual definitions for all terms.

Many biological and medical terms may be ambiguous, so terms should be
defined so that their precise meaning within the context of a particular
ontology is clear to a human reader.

Textual definitions (SOP) for a substantial and representative fraction,
plus equivalent formal definitions (for at least a substantial number of
terms). For terms lacking textual definitions, there should be evidence
of implementation of a strategy to provide definitions for all remaining
undefined terms.

Text definitions should be unique (i.e. no two terms should share a
definition)
```


<Category:Principles> <Category:Accepted> <Category:Definitions>
