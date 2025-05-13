---
layout: principle
id: fp-001-open
title: Open (principle 1)
---
GO TO: [Recommendations/Requirements](#recommendations-and-requirements) &#124; [Implementation](#implementation) &#124; [Examples/Counter&#8209;Examples](#examples) &#124; [Criteria&nbsp;for&nbsp;Review](#criteria-for-review) &#124; [Feedback/Discussion](#feedback-and-discussion)

## Summary

The ontology MUST be openly available to be used by all without any constraint other than (a) its origin must be acknowledged and (b) it is not to be altered and subsequently redistributed in altered form under the original name or with the same identifiers.

## Purpose

OBO Foundry ontologies are resources for the entire biological and biomedical community. Furthermore, in order to realize the OBO Foundry vision of a suite of interoperable ontologies, ontology developers must be free to re-use terms from any OBO Foundry ontology. For these reasons, the ontologies must be available to all without any constraint on their use or redistribution. Nonetheless, it is proper that their original source is always credited and that after any external alterations, ontologies must never be redistributed under the same name or with the same identifiers.

## Recommendations and Requirements

### For ontology providers

OBO Foundry Ontologies MUST EITHER be released under a [Creative Commons Attribution 3.0 Unported (CC BY 3.0)](https://creativecommons.org/licenses/by/3.0/) license or later (e.g. [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), OR released into the public domain under [Creative Commons CC0 1.0 Public Domain Dedication (CC0 1.0)](https://creativecommons.org/publicdomain/zero/1.0/). The license MUST be clearly stated using the [http://purl.org/dc/terms/license](http://purl.org/dc/terms/license) property followed by the URL representing the license (e.g. [https://creativecommons.org/licenses/by/3.0/](https://creativecommons.org/licenses/by/3.0/)) in the ontology file ([OWL example](https://oboacademy.github.io/obook/reference/formatting-license/)).

Note: CC-BY licenses allow others to distribute, remix, tweak, and build upon the work, even commercially, as long as they credit the creators for the original creation. CC0 specifies that the creators of an ontology waive, to the extent that they legally can be, all rights and place the ontology in the public domain. It does not prevent them from requesting that the ontology be properly credited and cited, but prevents any legal recourse if it is not credited. Many pros and cons of CC-BY versus CC0 are laid out in [this discussion](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/285). It is important to note that one can move from CC-BY to CC0 but not the other way around.

### For ontology re-use

1. The original source of an ontology must be credited according to the terms specified in the comment annotation of the ontology.

2. Altered versions of an ontology that are not part of an official release (that is, by the ontology developers) must not be redistributed under the same name or with the same ontology IRI.

3. If an individual term is reused without change to the definition, the original term IRI should be used. If the definition of a term (either text or logical) is changed, the original term IRI should not be reused. Suggestions for changes or improvements to term definitions should be submitted to the appropriate ontology issue tracker.

4. Regardless of which license an ontology uses, we strongly request and recommend that any reuse of an ontology attributes the source in accordance with scientific norms and the [OBO Citation and Attribution Policy](http://www.obofoundry.org/docs/Citation).

## Implementation

### For ontology providers

#### `.owl` files

1. OBO Foundry Ontologies MUST specify the reuse constraints using the following annotations in any publically released OWL version of the ontology:

   1. dcterms:license - specifies the license - see Example 1 (below)
   2. rdfs:comment - specifies terms of reuse - see Example 1 (below)

2. OBO Foundry Ontologies that host terms developed by an external group (but which are not part of an existing ontology) must credit the external group - see Examples (below)

3. See below under ontology re-use for guidelines on importing individual terms from external ontologies.

#### `.obo` files

1. OBO Foundry Ontologies must specify the reuse constraints using the following annotations in any publically released OBO version of the ontology:
   1. the license in a separate property annotation, which can be converted to a dc:license statement if the ontology is converted to OWL - see Example 2 (below)
   2. the reuse constraints using a comment in the official OBO version of the ontology - see Example 2 (below)

### For ontology re-use

#### Individual terms

The attribution method for individual terms reused in another ontology (e.g., by MIREOT) is via use of their original IRI or ID - see Examples (below).

1. **In OWL** - Any ontology re-using individual terms from another ontology should:

   1. re-use the original term IRI (which for OBO Foundry ontologies is generally in the form of an OBO Foundry PURL)
   2. use an IAO:imported from annotation <http://purl.obolibrary.org/obo/IAO_0000412> on each imported term to link back to the group (i.e. ontology) maintaining it, where more information would be available about the license
   3. include any annotations for term or definition editors from the original ontology

2. **In OBO** - Any ontology re-using individual terms from another ontology should:
   1. re-use the original term ID (of the form <GO:0000001>)
   2. include any XREFs to the original term editor(s) from the original ontology

#### Full ontologies

The attribution method for importing an entire ontology in OWL is simply to import the ontology without modification.

3. The attribution method for using an ontology for an analysis is to cite the ontology as requested by the ontology developers. If the developers have not specified how to cite their ontology, use the ontology IRI, a publication if available, and the ontology website if available.

## Examples

NOTE: All examples are for illustration purposes and should not be considered valid ontology axioms.

### Example 1: RDF-XML code for the license annotations:

```
<dcterms:license rdf:resource="http://creativecommons.org/licenses/by/4.0/"/>

<rdfs:comment xml:lang="en">"Ontology name" by "developer groups" is licensed
under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).</rdfs:comment>

<rdfs:comment xml:lang="en">"Ontology name" by developer groups is
licensed under CC BY 4.0. You are free to share (copy and redistribute
the material in any medium or format) and adapt (remix, transform, and
build upon the material) for any purpose, even commercially. for any
purpose, even commercially. The licensor cannot revoke these freedoms as
long as you follow the license terms. You must give appropriate credit
(by using the original ontology IRI for the whole ontology and original
term IRIs for individual terms), provide a link to the license, and
indicate if any changes were made. You may do so in any reasonable
manner, but not in any way that suggests the licensor endorses you or
your use.</rdfs:comment>
```

The above comment for reuse conditions is for example only. Ontologies may use different wording appropriate to their own needs, as long as it is consistent with the license.

### Example 2: Example of OBO code for the license annotation:

```
property_value: http://purl.org/dc/terms/license http://creativecommons.org/licenses/by/4.0/

remark: *Ontology name* by *developer group(s)* is licensed under CC BY 4.0. You
    are free to share (copy and redistribute the material in any medium
    or format) and adapt (remix, transform, and build upon the material)
    for any purpose, even commercially. You must give appropriate credit
    (by using the original ontology IRI for the whole ontology or
    original term IRIs for individual terms), provide a link to the
    license, and indicate if any changes were made. You may do so in any
    reasonable manner, but not in any way that suggests the licensor
    endorses you or your use.

```

### Example 3: How to credit an external group for developing a term in your ontology.

The first course of action should be to reuse the external term as is, by importing it with the original IRI (e.g. by MIREOT). At a minimum, the term definition should be imported, but there is still an open discussion about which other annotation need to be imported.

Please see the discussion tab for additional discussion of how to use different annotation properties to credit external ontologies or definition sources.

#### Example 3A: IAO:imported from

The Ontology for Biomedical Investigation (OBI) imports the class "environmental material" from the Environment Ontology (ENVO), using OntoFox. The imported from axiom is automatically generated by Ontofox and added to "environmental material" in OBI:

```
<!-- <http://purl.obolibrary.org/obo/ENVO_00010483> -->

<owl:Class rdf:about="&obo;ENVO_00010483">

<rdfs:label rdf:datatype="&xsd;string">environmental
material</rdfs:label>

<rdfs:subClassOf rdf:resource="&obo;BFO_0000040"/>

<obo:IAO_0000115 rdf:datatype="&xsd;string">Material in or on which
organisms may live.</obo:IAO_0000115>

<obo:IAO_0000111 rdf:datatype="&xsd;string">environmental
material</obo:IAO_0000111>

<obo:IAO_0000412 rdf:resource="&obo;envo.owl"/>

</owl:Class>
```

## Counter-Examples

- An ontology with no license statement is by default subject to the most restrictive copyright laws for those parts of the ontology that are copyrightable, and therefore is not useful within the OBO Foundry.
- CC BY-ND allows for redistribution, commercial and non-commercial, as long as it is passed along unchanged and in whole, with credit to the creators. This license is too restrictive for the OBO Foundry, because it requires that the ontology be re-used in its entirety, which prevents the re-use of individual terms.

## Criteria for Review

The ontology must have a license that is equivalent to or less restrictive than CC-BY, specified as described in the text and examples above.

[This check is automatically validated.](checks/fp_001) The automatic check fully covers the requirements for this principle.

## Feedback and Discussion

To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%231+%22Open%22+%3CENTER+ISSUE+TITLE%3E).

To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Technical+WG,automated+validation+of+principles&title=Principle+%231+%22Open%22+-+automated+validation+%3CENTER+ISSUE+TITLE%3E).

See also [this discussion of licensing](https://github.com/OBOFoundry/Operations-Committee/issues/103) by the OBO Foundry Operations Committee focusing on Creative Commons licenses.
