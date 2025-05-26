---
layout: principle
id: fp-019-term-stability
title: Stability of Term Meaning (principle 19)
---

GO TO: [Recommendations/Requirements](#recommendations-and-requirements) &#124; [Implementation](#implementation) &#124; [Examples/Counter&#8209;Examples](#examples) &#124; [Criteria&nbsp;for&nbsp;Review](#criteria-for-review) &#124; [Feedback/Discussion](#feedback-and-discussion)

Summary
-------

The definition of a term MUST always denote the same thing(s)--known as "referent(s)"--in reality. If a proposed change to the definition would substantially change its referents, then a new term with new IRI and definition MUST instead be created.

Purpose
-------

Users of an ontology depend on the stability of its terms and their meanings. Therefore, changes to the definition of a term should never substantially shift its meaning. Put another way, its set of referents MUST remain stable, within reason. That is, changes to a term definition--or any mechanism to denote meaning, including elucidations and logical axioms--should not cause that term to point to different entities than it denotes already.

Recommendations and Requirements
-------

Below, we use 'definition' to encompass all possible mechanisms to denote term meaning, as described above.

If changing a term definition would change its referents, then instead a new term MUST be created with a new IRI and the new definition. Minor changes to the definition for clarity, grammar, and/or proper punctuation that do not change the referents are permitted. What is considered a 'minor change' will likely need to be evaluated on a case-by-case basis; it is left to the ontology developers to decide. However, any feedback from users MUST be taken into account.

The creation of a new term/definition implies that the old term should possibly be deprecated/obsoleted. Conditions under which a term MUST be deprecated according to this principle, or for which term deprecation SHOULD be considered, include:

1) The old textual definition misses the target(s) intended by the ontology developers. This includes cases where the term refers to non-existent referents (as might happen, for example, when new research reveals that the referent does not exist in reality).
1) The original term definition is considered sufficiently “damaged” (too vague, too restrictive, too misused or too misunderstood).

In all cases the developers SHOULD provide guidance on how to handle deprecated terms (either by exact replacement or by considering other terms), and be mindful of the potential costs to users of the ontology who might use the existing term. As well, developers SHOULD pre-announce term obsoletions. See [Principle 13](http://obofoundry.org/principles/fp-013-notification.html) for guidance on such announcements.

Implementation
-------

Detailed procedures for obsoleting a term are described on the OBO Academy page [Obsoleting an Existing Ontology Term](https://oboacademy.github.io/obook/howto/obsolete-term/). 

<i><b>To obsolete a term, the ontology developer</b></i> MUST:
1. Mark the term as obsolete:
   - OWL format: Add an "owl:deprecated" annotation property with value of "true^xsd:boolean"
   - OBO format: Add an "is_obsolete: true" tag
2. Prepend the string "obsolete " (including the space) to the term label <i>and</i> the `editor preferred term` (IAO:0000111), if present
   - NOTE: To be consistent with [Principle 12](https://obofoundry.org/principles/fp-012-naming-conventions.html) "Naming Conventions", the syntax/format MUST be precisely as given above (that is, the exact string as shown, lowercase and space included, with no other punctuation before or after). Thus, the following are disallowed: "Obsolete {label}", "obsolete_{label}", "OBSOLETE {label}" (and variations thereof).
3. Remove all existing logical axioms from the term
4. Remove or replace all usages of the term elsewhere in the ontology. For example, if an ontology has A part-of B, and B has been deprecated with replacement by C, then the corrected axiom would be A part-of C. Likewise, if A part-of B, and B part-of C, if B is deprecated, then any part-of axiom involving B MUST be removed; that is, by stating instead A part-of C.

It is not necessary (and not advisable) to delete the textual definition.

<i><b>To obsolete a term, the ontology developer</b></i> SHOULD:

1. Indicate any exact term replacement:
   -  OWL: Use the `term replaced by` annotation property from OMO ([IAO:0100001](http://purl.obolibrary.org/obo/IAO_0100001)) with the value set to the IRI of the relevant term
   -  OBO: Use the `replaced_by:` tag with the value set to the CURIE of the relevant term
2. Indicate any inexact term replacements:
   -  OWL: Use the `oboInOwl:consider` annotation property with the value set to the full IRI(s) of the relevant term(s)
```
   <oboInOwl:consider rdf:resource="http://purl.obolibrary.org/obo/OBI_0001544">
``` 

   -  OBO: Use the `consider:` tag with the value set to the CURIE(s) of the relevant term(s)
```
   consider: OBI:0001544
```

Note that some older implementations in OWL used the CURIE method as shown below, but this is not preferred.

```
   <oboInOwl:consider rdf:datatype="http://www.w3.org/2001/XMLSchema#string">OBI:0001544</oboInOwl:consider>
```
<i><b>To obsolete a term, the ontology developer</b></i> MAY:

1. Prepend the string "OBSOLETE. " (this precise string, including the space) to the term definition. NOTE: This MUST be implemented consistently. That is, if applied at all, it has to be applied to every obsoleted term definition.
2. Indicate the reason(s) for obsoleting:
   -  OWL: Use the `has obsolescence reason` annotation property from OMO ([IAO:0000231](http://purl.obolibrary.org/obo/IAO_0000231)) with the value set to the IRI of one of the individuals of the "obsolescence reason specification" term [IAO:0000225](http://purl.obolibrary.org/obo/IAO_0000225). See below for example.
   -  OBO: Use `relationship:` with the CURIE for the annotation property (IAO:0000231) and a CURIE for the specific reason (an individual from the "obsolescence reason specification" term [IAO:0000225](http://purl.obolibrary.org/obo/IAO_0000225)). See below for example. Note that older implementations often used alternative methods (described after the examples). These methods are still valid, but are not preferred.

Examples
-------

The Ontology for Biomedical Investigations obsolete term "cell lysate MHC competitive binding assay using radioactivity detection" (OBI:0001574) can be deprecated as follows:

OWL: 
```
<owl:Class rdf:about="http://purl.obolibrary.org/obo/OBI_0001574">
    <obo:IAO_0000111>obsolete cell lysate MHC competitive binding assay using radioactivity detection</obo:IAO_0000111>
    <obo:IAO_0000115>Competitive inhibition of binding assay measuring MHC ligand binding by radioactivity detection using MHC derived from a cell lysate</obo:IAO_0000115>
    <obo:IAO_0000231 rdf:resource="http://purl.obolibrary.org/obo/IAO_0000227"/>
    <obo:IAO_0100001 rdf:resource="http://purl.obolibrary.org/obo/OBI_0001544"/>
    <rdfs:label>obsolete cell lysate MHC competitive binding assay using radioactivity detection</rdfs:label>
    <owl:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</owl:deprecated>
</owl:Class>
```

OBO: 
```
[Term]
id: OBI:0001574
name: obsolete cell lysate MHC competitive binding assay using radioactivity detection
def: "OBSOLETE. Competitive inhibition of binding assay measuring MHC ligand binding by radioactivity detection using MHC derived from a cell lysate." []
relationship: IAO:0000231 IAO:0000227
is_obsolete: true
replaced_by: OBI:0001544
```
Obsolescence reasons have, historically, been indicated multiple ways. In addition to the preferred methods shown above, the following alternatives are in current use:
1) As a free text comment (`rdfs:comment` in OWL or `comment:` in OBO). 
1) In OBO format, using a `property_value:` tag instead of a `relationship:` tag.
1) In OBO format, using an annotation property label-as-identifier (with underscores) instead of the CURIE `IAO:0000231`, and the obsolescence reason label instead of the relevant CURIE. Note that the underscore version of the property label will need to be created in the ontology:
```
[Typedef]
id: has_obsolescence_reason
name: has obsolescence reason
xref: IAO:0000231
is_metadata_tag: true
```
Then:
```
relationship: has_obsolescence_reason IAO:0000227 ! terms merged
```
Or:
```
property_value: has_obsolescence_reason IAO:0000227
```

Counter-example
-------

The PRO term "phosphoprotein" (PR:000037070) is defined as "A protein that includes at least one phosphorylated residue." A study finds 2000 more examples than was previously known. In this case, no new term needs to be made (nor the original deleted) because (1) the term definition did not change; and (2) the referent--proteins with a phophoresidue--did not change (that is, the newly-discovered phosphoproteins are just additional examples of that referent).

Criteria for review
-------

The OBO Dashboard will show:
- An ERROR if any obsolete term (that is, a term with an `owl:deprecated` property or `is_obsolete: true` tag) does not also have 'obsolete ' (that exact string, lowercase and space included, with no other punctuation) prepended to the label
- An ERROR if any obsolete term (as indicated by term label or definition) lacks an `owl:deprecated` property or `is_obsolete: true` tag
- An ERROR if an obsolete term has, itself, any logical axioms (including any subClassOf/is_a declarations) or if it is referenced by logical axioms from other terms
- A WARN if there is at least one term with 'OBSOLETE. ' prepended to the definition but not all obsolete terms are likewise prepended

[This check is automatically validated.](checks/fp_019)

Feedback and Discussion
-------

To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%2319+%22Stability%22of%22Term%22Meaning%22+%3CENTER+ISSUE+TITLE%3E).

To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub]().

See also [this discussion](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/597) by the OBO Foundry Operations Committee focusing on term deprecation and [this discussion](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/964) regarding the proposal of this principle.
