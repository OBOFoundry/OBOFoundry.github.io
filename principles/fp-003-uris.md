---
layout: principle
id: fp-003-uris
title: uris
---

Principle Name
--------------

identifier space

Details
-------

Each class and relation (property) in the ontology must have a unique
URI identifier. The URI should be constructed from a base URI, a prefix
that is unique within the Foundry (e.g. GO, CHEBI, CL) and a local
identifier (e.g. 0000001). The local identifier should not consist of
labels or mnemonics meaningful to humans.

The ID-space / prefix must be registered with the OBO library in
advance. Email obo-admin AT obofoundry DOT org

Notes
-----

See <http://www.obofoundry.org/id-policy.shtml>

### OBO-Format Ontologies

If the source ontology is in OBO-Format, then this is automatically
satisfied so long as all IDs are of the form \<IDSPACE\> : \<NUMBER\>

Date Accepted
-------------

-   original principle

History
-------

### Original Formulation

\<blockquote\> The ontologies possesses a unique identifier space within
the OBO Foundry.

The source of a term (i.e. class) from any ontology can be immediately
identified by the prefix of the identifier of each term. It is,
therefore, important that this prefix be unique. \</blockquote\>

Examples
--------

The OBI class 'imaging assay' has the following URI:
<http://purl.obolibrary.org/obo/OBI_0000185>

Counter-Examples
----------------

-   There are systems that use alphanumeric id's. This should be
    discouraged, especially as these have semantic content.
-   An example is this NCI class: 'Chemotherapy Regimen or Agent
    Combination':
    <http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#Chemotherapy_Regimen>

<Category:Principles> <Category:Accepted>
