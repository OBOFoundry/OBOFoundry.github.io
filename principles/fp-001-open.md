---
layout: principle
id: fp-001-open
title: open
---

Principle Name
--------------

open

Summary
-------

The ontology MUST be openly available to be used by all without any
constraint other than (a) its origin must be acknowledged and (b) it is
not to be altered and subsequently redistributed in altered form under
the original name or with the same identifiers.

Purpose
-------

OBO Foundry ontologies are resources for the entire biological and
biomedical community. Furthermore, in order to realize the OBO Foundry
vision of a suite of interoperable ontologies, ontology developers must
be free to re-use terms from any OBO Foundry ontology. For these
reasons, the ontologies must be available to all without any constraint
on their use or redistribution. Nonetheless, it is proper that their
original source is always credited and that after any external
alterations, ontologies must never be redistributed under the same name
or with the same identifiers.

Recommendations
---------------

### For ontology providers:

​1. OBO Foundry Ontologies must:

EITHER be copyrighted under a Creative Commons CC-BY license version 4.0
or later, which lets others distribute, remix, tweak, and build upon the
work, even commercially, as long as they credit the creators for the
original creation

OR released into the public domain under CC0 (which is, technically, not
a license). Note that CC0 specifies that the creators of an ontology
waive all rights and place it in the public domain. It does not prevent
them from requesting that the ontology be properly credited and cited,
but prevents any legal recourse if it is not credited.

​2. We recommend that new ontologies choose a CC-BY license because a
CC-BY license can be converted into a more permissive CC0, while the
reverse is not true. That is, If you develop and license your work under
CC0 you will not be able to later update it to CC-BY.

### For ontology re-use:

​1. The original source of an ontology must be credited according to the
terms specified in the comment annotation of the ontology.

​2. After any external alterations to an ontology, the ontology must not
be redistributed under the same name or with the same ontology IRI.

​3. If an individual term is reused without change to the definition,
the original term IRI should be used. If the definition of a term
(either text or logical) is changed, the original term IRI should not be
reused. Suggestions for changes or improvements to term definitions
should be submitted to the appropriate ontology issue tracker.

### Remark:

In general, copyright legislation says that facts that are not
copyrightable are excluded from copyright protection. Therefore, some
ontology content may not be copyrightable.

Implementation
--------------

### For ontology providers:

#### 1. .owl files

​a. OBO Foundry Ontologies MUST specify the reuse constraints using the
following annotations in any publically released OWL version of the
ontology:

​i. dc:license - specifies the license - see Example 1 (below)

​11. rdfs:comment - specifies terms of reuse - see Example 1 (below)

​b. OBO Foundry Ontologies that host terms developed by an external
group (but which are not part of an existing ontology) must credit the
external group - see Examples (below)

​c. See below under ontology re-use for guidelines on importing
individual terms from external ontologies.

#### 2. .obo files:

​a. OBO Foundry Ontologies must specify the reuse constraints using the
following annotations in any publically released OBO version of the
ontology:

​i. the license in a separate annotation, which can be converted to a
dc:license statement if the ontology is converted to OWL - see Examples
(below)

​b. the reuse constraints using a comment
(http://www.geneontology.org/GO.format.obo-1\_4.shtml\#S.2.1) in the
official OBO version of the ontology - see Examples (below)

### For ontology re-use:

​1. The attribution method for individual terms reused in another
ontology (e.g., by MIREOT) is via use of their original IRI or ID - see
Examples (below).

​a. **In OWL** - Any ontology re-using individual terms from another
ontology should:

​i. re-use the original term IRI (which for OBO Foundry ontologies is
generally in the form of an OBO Foundry PURL)

​ii. use an IAO:imported from annotation
(http://purl.obolibrary.org/obo/IAO\_0000412) on each imported term to
link back to the group (i.e. ontology) maintaining it, where more
information would be available about the license

​iii. include any annotations for term or definition editors from the
original ontology

​b. **In OBO** - Any ontology re-using individual terms from another
ontology should:

​i. re-use the original term ID (of the form <GO:0000001>)

​ii. include any XREFs to the original term editor(s) from the original
ontology

​2. The attribution method for importing an entire ontology in OWL is
simply to import the ontology without modification.

​3. The attribution method for using an ontology for an analysis is to
cite the ontology as requested by the ontology developers. If the
developers have not specified how to cite their ontology, use the
ontology IRI, a publication if available, and the ontology website if
available.

Examples
--------

NOTE: All examples are for illustration purposes and should not be
considered valid ontology axioms.

### Example 1: RDF-XML code for the license annotations:

\<blockquote\> \<dc:license
rdf:resource="[http://creativecommons.org/licenses/by/4.0/"/\>](http://creativecommons.org/licenses/by/4.0/"/>)

\<rdfs:comment xml:lang="en"\>"Ontology name" by "developer groups" is
licensed under CC BY 4.0
(https://creativecommons.org/licenses/by/4.0/).\</rdfs:comment\>

\<rdfs:comment xml:lang="en"\>"Ontology name" by developer groups is
licensed under CC BY 4.0. You are free to share (copy and redistribute
the material in any medium or format) and adapt (remix, transform, and
build upon the material) for any purpose, even commercially. for any
purpose, even commercially. The licensor cannot revoke these freedoms as
long as you follow the license terms. You must give appropriate credit
(by using the original ontology IRI for the whole ontology and original
term IRIs for individual terms), provide a link to the license, and
indicate if any changes were made. You may do so in any reasonable
manner, but not in any way that suggests the licensor endorses you or
your use.\</rdfs:comment\>

\</blockquote\>

The above comment for reuse conditions is for example only. Ontologies
may use different wording appropriate to their own needs, as long as it
is consistent with the license.

### Example 2: Example of OBO code for the license annotation:

\<blockquote\> \<license annotation\>

1.  "Ontology name" by developer groups is licensed under CC BY 4.0. You
    are free to share (copy and redistribute the material in any medium
    or format) and adapt (remix, transform, and build upon the material)
    for any purpose, even commercially. You must give appropriate credit
    (by using the original ontology IRI for the whole ontology or
    original term IRIs for individual terms), provide a link to the
    license, and indicate if any changes were made. You may do so in any
    reasonable manner, but not in any way that suggests the licensor
    endorses you or your use.

\</blockquote\>

### Example 3: How to credit an external group for developing a term in your ontology.

The first course of action should be to reuse the external term as is,
by importing it with the original IRI (e.g. by MIREOT). At a minimum,
the term definition should be imported, but there is still an open
discussion about which other annotation need to be imported.

Please see the discussion tab for additional discussion of how to use
different annotation properties to credit external ontologies or
definition sources.

#### 3A, example with IAO:imported from

The Ontology for Biomedical Investigation (OBI) imports the class
“environmental material” from the Environment Ontology (ENVO), using
OntoFox. The imported from axiom is automatically generated by Ontofox
and added to “environmental material” in OBI:

\<blockquote\> \<!-- <http://purl.obolibrary.org/obo/ENVO_00010483> --\>

\<owl:Class rdf:about="&obo;ENVO\_00010483"\>

\<rdfs:label rdf:datatype="&xsd;string"\>environmental
material\</rdfs:label\>

\<rdfs:subClassOf rdf:resource="&obo;BFO\_0000040"/\>

\<obo:IAO\_0000115 rdf:datatype="&xsd;string"\>Material in or on which
organisms may live.\</obo:IAO\_0000115\>

\<obo:IAO\_0000111 rdf:datatype="&xsd;string"\>environmental
material\</obo:IAO\_0000111\>

\<obo:IAO\_0000412 rdf:resource="&obo;envo.owl"/\>

\</owl:Class\>

\</blockquote\>

Counter-Examples
----------------

-   An ontology with no license statement is by default subject to the
    most restrictive copyright laws for those parts of the ontology that
    are copyrightable, and therefore is not useful within the OBO
    Foundry.
-   CC BY-ND allows for redistribution, commercial and non-commercial,
    as long as it is passed along unchanged and in whole, with credit to
    the creators. This license is too restrictive for the OBO Foundry,
    because it requires that the ontology be re-used in its entirety,
    which prevents the re-use of individual terms.

External documentation:
-----------------------

Discussion of licensing on OBO Foundry Operations Committee Issue 103
About Creative Commons licenses

Criteria for review
-------------------

To pass review, the ontology must have a license that is equivalent to
or less restrictive than CC-BY, specified as described in the text and
examples above.

Original Formulation
--------------------

See the history tab for older formulations.

<Category:Principles> <Category:Accepted>
