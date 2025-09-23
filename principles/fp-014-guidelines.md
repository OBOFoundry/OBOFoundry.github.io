---
layout: principle
id: fp-014-guidelines
title: Guidelines (principle 4)
---
GO TO: [Recommendations/Requirements](#recommendations-and-requirements) &#124; [Implementation](#implementation) &#124; [Examples/Counter&#8209;Examples](#examples) &#124; [Criteria&nbsp;for&nbsp;Review](#criteria-for-review) &#124; [Feedback/Discussion](#feedback-and-discussion)

## Summary

The ontology provider follows the recommendations and requirements outlined on the Ontology Standardization Guidelines page and the Project Management Guidelines page.

## Purpose

OBO projects share their ontologies using files in OWL or OBO format (see [Principle 2](https://obofoundry.org/principles/fp-002-format.html)). Ontologies are expected to change over time as they are developed and refined (see [Principle 16](https://obofoundry.org/principles/fp-016-maintenance.html)). This will lead to a series of different files. Consumers of ontologies must be able to specify exactly which ontology files they used to encode their data or build their applications, and be able to retrieve unaltered copies of those files in perpetuity. Note that this applies only to those versions which have been officially released.

## Recommendations and Requirements

In addition to an IRI specifying the current release (see [Principle 3](https://obofoundry.org/principles/fp-003-uris.html)), each official release MUST have a unique version IRI that resolves to the specific ontology artifact indicated. Consumers can then use the version IRI to uniquely identify which official release of the ontology they used, and to retrieve unaltered copies of the file(s). A _version IRI_ is a full path that MUST resolve to the particular version of the ontology artifact. Both the version IRI and the corresponding artifact MUST contain an identical _version identifier_ string.

Version identifiers MUST either be of the form "YYYY-MM-DD" (that is, a date) OR use a numbering system (such as semantic versioning, i.e, of the form "NN.n"). Each version MUST associate with a <b>distinct</b> official release. The date versioning system is preferred, as it meshes with the requirement that version IRIs be specified using dated PURLs (see below).

If a date-based version identifier is used, it MUST conform to [ISO-8601](https://www.iso.org/iso-8601-date-and-time-format.html), ie. "YYYY-MM-DD". Variants of this--such as (a) using two digits for year instead of four (b) using one digit for month or year (c) using a delimiter other than a hyphen (d) any other ordering such as day/month/year or month/day/year (c) any other variant--MUST NOT be used.

All OBO projects MUST also have versioned PURLs that resolve to the corresponding artifacts specified by the version IRIs, in perpetuity. If the files are moved, the PURL MUST be updated to resolve to the new location.

Note that the content of official release files MUST NOT be changed. For example, if a bug is found in some official released file for some ontology, the bug MUST NOT be fixed by changing the file(s) for that official release. Instead the bug fixes should be included in a new official release, with new files, and consumers can switch to the new release.

Additionally, each ontology SHOULD have an owl:versionInfo statement. When this is stated, it MUST correspond to the version Info.

## Implementation

See examples (below) for guidelines on how to specify the version within the ontology itself. If terms are imported from an external ontology, the “IAO:imported from” annotation (see [Principle 1](http://obofoundry.org/principles/fp-001-open.html)) may specify a dated version of the ontology from which they are imported.

Regardless of the versioning system used for the ontology artifact, the version IRI SHOULD use an ISO-8601 dated PURL. In cases where there are multiple releases on the same day, the PURL points to the newest, and the previous release stays in the same folder or a subfolder, named in such a way as to distinguish the releases. Specifications for version IRIs are fully described in the OBO Foundry [ID policy](http://obofoundry.org/id-policy) document. In short:

For a given version of an ontology, the ontology should be accessible at the following URL, where 'idspace' is replaced by the IDSPACE in lower case:

    OWL: http://purl.obolibrary.org/obo/idspace/YYYY-MM-DD/idspace.owl
    OBO: http://purl.obolibrary.org/obo/idspace/YYYY-MM-DD/idspace.obo

For example, for the version of OBI released 2009-11-06, the OWL document is accessible at http://purl.obolibrary.org/obo/obi/2009-11-06/obi.owl.

An accepted alternative to the above scheme is to include /releases/ in the PURL, as follows:

    OWL: http://purl.obolibrary.org/obo/idspace/releases/YYYY-MM-DD/idspace.owl
    OBO: http://purl.obolibrary.org/obo/idspace/releases/YYYY-MM-DD/idspace.obo

## Examples

For an OBO format ontology use the metadata tag:

    data-version: 2015-03-31
    data-version: 44.0

For an OWL format ontology, owl:versionInfo identifies the version and versionIRI identifies the resource:

    <owl:versionInfo rdf:datatype="http://www.w3.org/2001/XMLSchema#string">2014-12-03</owl:versionInfo>
    <owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/obi/2014-12-03/obi.owl"/>

CHEBI is an example of an OBO ontology that uses a non-date based system system for version identifier. An example versionIRI for CHEBI is http://purl.obolibrary.org/obo/chebi/187/chebi.owl. This corresponds to a value of `187` for `data-version` in OBO format.

## Criteria for Review

The released ontology MUST have a version IRI. The version IRI MUST use a date format (NS/YYYY-MM-DD/ontology.owl) OR use a semantic versioning format (e.g., NS/NN.n/ontology.owl). The version IRI MUST resolve to an ontology artifact that is associated with the same version identifier as used in the version IRI.

[This check is automatically validated.](checks/fp_004)

## Feedback and Discussion

To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%234+%22Versioning%22+%3CENTER+ISSUE+TITLE%3E).

To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Technical+WG,automated+validation+of+principles&title=Principle+%234+%22Versioning%22+-+automated+validation+%3CENTER+ISSUE+TITLE%3E).
