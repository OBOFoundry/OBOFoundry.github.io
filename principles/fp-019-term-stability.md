---
layout: principle
id: fp-019-term-stability
title: Stability of Term Meaning (principle 19)
---

GO TO: [Recommendations/Requirements](#recommendations-and-requirements) &#124; [Implementation](#implementation) &#124; [Examples/Counter&#8209;Examples](#examples) &#124; [Criteria&nbsp;for&nbsp;Review](#criteria-for-review) &#124; [Feedback/Discussion](#feedback-and-discussion)

Summary
-------

The definition of a term MUST always denote the same thing(s)--known as "referent(s)"--in reality. If a proposed change to the definition would change its referents, then a new term with new IRI and definition MUST instead be created.

Purpose
-------

Users of an ontology depend on the stability of its terms and their meanings. Therefore, changes to the definition of a term should never shift its meaning. Put another way, its set of referents MUST remain stable. That is, changes to a term definition should not cause that term to point to different entities than it denotes already.

Recommendations and Requirements
-------

If changing a term definition would change its referent, then instead a new term MUST be created with a new IRI and the new definition. Minor changes to the definition for clarity, grammar, and/or proper punctuation that do not change the referent are permitted.

Conditions under which a term must be deprecated according to this principle, or for which term deprecation should be considered, include:

1) The old textual definition misses its intended target. This includes cases where the term refers to non-existent referents (as might happen, for example, when new research reveals that the referent does not exist in reality).
1) The original term definition is considered sufficiently “damaged” (too vague, too restrictive, too misused or too misunderstood).

In all cases the developers SHOULD provide guidance on how to handle deprecated terms (either by exact replacement or by considering other terms), and be mindful of the potential costs to users of the ontology who might use the existing term. As well, developers SHOULD pre-announce term obsoletions. See [Principle 13](http://obofoundry.org/principles/fp-013-notification.html) for guidance on such announcements.

Implementation
-------

Detailed procedures for obsoleting a term are described on the OBO Academy page [Obsoleting an Existing Ontology Term](https://oboacademy.github.io/obook/howto/obsolete-term/). 

<i><b>To obsolete a term, the ontology developer</b></i> MUST:
1) Mark the term as obsolete
  - OWL format: Add an "owl:deprecated" annotation with value of "true^xsd:boolean"
  - OBO format: Add an "is_obsolete: true" declaration
1) Prepend the string "obsolete " (including the space) to the term label
1) Remove existing logical axioms from the term
1) Remove or replace all usages of the term elsewhere in the ontology

<i><b>To obsolete a term, the ontology developer</b></i> SHOULD:
1) Indicate any exact term replacement:
  -  OWL: Use the "term replaced by" annotation property from OMO ([IAO:0100001](http://purl.obolibrary.org/obo/IAO_0100001)) with the value set to the IRI of the relevant term
  -  OBO: Use the "replaced_by:" tag with the value set to the CURIE of the relevant term
1) Indicate any inexact term replacements:
  -  OWL: Use the "oboInOwl:consider" annotation property with the value set either to  the full IRI(s) or to the CURIE(s) of the relevant term(s)
```
   IRI method:   <oboInOwl:consider rdf:resource="http://purl.obolibrary.org/obo/OBI_0001544)>
   CURIE method: <oboInOwl:consider rdf:datatype="http://www.w3.org/2001/XMLSchema#string">OBI:0001544</oboInOwl:consider>
``` 

  -  OBO: Use the "consider:" tag with the value set to the CURIE(s) of the relevant term(s)

<i><b>To obsolete a term, the ontology developer</b></i> MAY:

1) Prepend the string "OBSOLETE. " (including the space) to the term definition
1) Indicate the reason(s) for obsoleting:
  -  OWL: Use the "has obsolescence reason" annotation property from OMO ([IAO:0000231](http://purl.obolibrary.org/obo/IAO_0000231])) with the value set to the IRI of one of the individuals of the "obsolescence reason specification" term [IAO:0000225](http://purl.obolibrary.org/obo/IAO_0000225)
  -  OBO: ?? 

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
is_obsolete: true
replaced_by: OBI:0001544
```

Counter-example
-------

The PRO term "phosphoprotein" (PR:000037070) is defined as "A protein that includes at least one phosphorylated residue." A study finds 2000 more examples than was previously known. In this case, no new term needs to be made (nor the original deleted) because (1) the term definition did not change; and (2) the referent--proteins with a phophoresidue--did not change (that is, the newly-discovered phosphoproteins are just additional examples of that referent).

Criteria for review
-------

TBD

Feedback and Discussion
-------

To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%2319+%22Stability%22of%22Term%22Meaning%22+%3CENTER+ISSUE+TITLE%3E).

To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub]().

See also [this discussion](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/597) by the OBO Foundry Operations Committee focusing on term deprecation and [this discussion](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/964) regarding the proposal of this principle.
