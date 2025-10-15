---
layout: default
title: ID Policy
---

# OBO Foundry Identifier Policy

## Background

This document outlines the OBO policy for identifiers and PURLs for OBO ontologies.

In the OWL language, all elements of an ontology (including classes/terms, and the ontology itself) are uniquely identified by a [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier). Within the OBO family of ontologies, we require the use of Permanent URLs (PURLs) with a standard base prefix.

For example:

- <http://purl.obolibrary.org/obo/UBERON_0000955> UBERON class PURL for 'brain'
- <http://purl.obolibrary.org/obo/obi.owl> ontology PURL for OBI

Note that legacy formats such as obo-format and many bioinformatics databases require the use of short-form identifiers (e.g. GO:0008150) to identify ontology terms. In this document we provide a well-defined mapping between these short prefixed identifiers and PURLs by considering the identifiers to be [CURIE](https://en.wikipedia.org/wiki/CURIE)s.

This document addresses identifiers _only_ for ontology terms, and not for Dbxrefs.

## Design goals

- There must be a predictable, bidirectional mapping between OBO IDs, and OBO Foundry-compliant URIs.
- The URIs should resolve to useful information about a term.
- The URIs should be designed so that they can be maintained over time to keep pointing to useful information.
- Each OBO ID is assigned to a only single term within the set of all OBO ontologies.
- There is a 1:1 mapping of OBO IDs to Foundry-compliant URIs.

### Format of OBO-format IDs

See [OBO syntax](http://owlcollab.github.io/oboformat/doc/obo-syntax.html) for details.

All OBO term IDs are CURIEs (prefixed identifiers) of the form `IDSPACE:LOCALID`.

Note that internally within an OBO Format document, relation IDs may be short form such as `part_of`, but these are mapped to CURIEs via the xref field.

### Format of Foundry-compliant URIs

`FOUNDRY_OBO_URI ::= "http://purl.obolibrary.org/obo/" IDSPACE "_" LOCALID`

### Mapping of OWL IDs to OBO format IDs

The recommended way is to use the [OBO JSON LD context](https://raw.githubusercontent.com/OBOFoundry/OBOFoundry.github.io/master/registry/context.jsonld)

This provides mappings between the OBO prefix and a base URI. See the [JSON-LD spec](https://json-ld.org/spec/latest/json-ld/) for a full specification of the expansion/contraction mechanism.

CURIE to URI:

`s@((**[A-Za-z_]***):(d+))@http://purl.obolibrary.org/obo/$1_$2@`

URI to CURIE:

`s@http://purl.obolibrary.org/obo/(**[A-Za-z_]***)_(d+)@$1:$2@`

Using these rules the OBO ID **GO:0050918** is mapped to the Foundry-compliant URI <http://purl.obolibrary.org/obo/GO_0050918>.

## Response to Web requests for OBO URIs

It is expected that the Foundry-compliant URIs behave, on the web, usefully. It will be the role of the OBO Foundry to supply generic software for responding to requests at URIs that identify OBO terms.

We borrow the criteria from the [Shared Name Initiative](https://web.archive.org/web/20170526125335/http://sharedname.org/page/Main_Page) as a baseline. (Note: sharedname.org has disappeared and is only available via the web archive.) The OBO Foundry may issue further recommendations if experience shows them to be considered generally useful.

1. It must be clearly stated what the intended referent of each URI is supposed to be, i.e. that the URI denotes some particular record from some particular database.

2. Information about the URI and its referent, including such a statement, must be made available, and in order to leverage existing protocol stacks, it must be obtainable via HTTP. (We will call such information "URI documentation".)

3. URI documentation must be provided in RDF.

4. Provision of URI documentation must be an ongoing concern. The ability to provide it may have to outlive the original ontology developer's group or creator.

5. The provider of the URI documentation must be responsive to community needs, such as the need to have mistakes fixed in a timely manner.

6. URI documentation must be open so that it can be replicated and reused.

Individual ontology projects may, at their discretion, choose to manage these responses, with the understanding that if service lapses the Foundry may substitute the generic software for handling them in order to maintain service.

### Allocating IDSPACEs

All OBO ontologies should use PURLs that have a base URL within their allocated space (in CURIE form these would be prefixed with their IDSPACE). IDSPACEs within the OBO library are unique for a given project and are chosen not to conflict with prefix for other resources. Although IDSPACEs are case-sensitive, there will never be more than one IDSPACEs that are the same when compared in a case-insensitive manner. Therefore, although "GO" and "go", "Go" and "gO" are different IDSPACEs, the IDSPACE "go", "Go" and "gO" will not be used as "GO" has already been allocated.

A registry of allocated IDSPACEs will be maintained. Requests for an IDSPACE should be made by creating a ticket on our [GitHub tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues) as described on [this page](https://github.com/OBOFoundry/OBOFoundry.github.io/blob/master/docs/Policy_for_OBO_namespace_and_associated_PURL_requests.md).
A request should include information about the ontology, such as scope and maintainer and a confirmation that the ontology is open access.

#### Guidelines for selecting an IDSPACE

- Use three or more letters; the OBO Library **does not** accept new two-letter IDSPACEs
- Avoid the letter "O" in three-letter IDSPACES; many ontologies use "O" for "Ontology" which limits the number of combinations
- Select a longer IDSPACE for ontologies that are more restricted in scope (e.g., species-specific phenotype ontologies)
- Search **each** of the following registries to make sure your IDSPACE doesn't conflict with one inside or outside of the OBO Library:
  <br>&emsp; - [OBO Foundry](https://obofoundry.org)
  <br>&emsp; - [Bioregistry](https://bioregistry.io) (or [browse here](https://bioregistry.io/registry/))
  <br>&emsp; - [BioPortal](https://bioportal.bioontology.org/) (or [browse here](https://bioportal.bioontology.org/ontologies))

### Current ontology document

The most current version of an ontology will be at the following URL, where "idspace" is replaced with the IDSPACE of the given ontology in lower case.

- Current OWL: http://purl.obolibrary.org/obo/idspace.owl
- Current OBO: http://purl.obolibrary.org/obo/idspace.obo

For example, the Ontology for Biomedical Investigations has the IDSPACE "OBI", so the current version of the OWL document would be at http://purl.obolibrary.org/obo/obi.owl

Additionally other ontology products can be included underneath this. For examples, see "products" under [http://obofoundry.org/ontology/go](http://obofoundry.org/ontology/go)

## Versions of ontologies

Versions are named by a date in the following format: YYYY-MM-DD. For a given version of an ontology, the ontology should be accessible at the following URL, where _idspace_; is replaced by the IDSPACE in lower case:

- OWL: http://purl.obolibrary.org/obo/*idspace*/YYYY-MM-DD/*idspace*.owl
- OBO: http://purl.obolibrary.org/obo/*idspace*/YYYY-MM-DD/*idspace*.obo

For example, for the version of OBI released 2009-11-06, the OWL document is accessible at <http://purl.obolibrary.org/obo/obi/2009-11-06/obi.owl>.

An accepted alternative to the above scheme is to include `/releases/` in the PURL, as follows:

- OWL: http://purl.obolibrary.org/obo/*idspace*/releases/YYYY-MM-DD/*idspace*.owl
- OBO: http://purl.obolibrary.org/obo/*idspace*/releases/YYYY-MM-DD/*idspace*.obo

This makes it easier to provide a generic PURL redirect to the relevant store (GitHub, S3, etc).

Note that other products can be versioned in addition to the main obo and owl files.

## Home page

If the ontology has a home page on the Web, it is accessible at http://purl.obolibrary.org/obo/IDSPACE. For example the OBI home page is accessible at: <http://purl.obolibrary.org/obo/obi>.

If the ontology has a tracker for submitting an monitoring term and other requests, it is accessible at
<http://purl.obolibrary.org/obo/IDSPACE/tracker>. For example the OBI tracker is accessible at: <http://purl.obolibrary.org/obo/obi/tracker>.

### Browse

If the ontology developers provide or suggest a way of browsing the ontology, it is accessible at
http://purl.obolibrary.org/obo/IDSPACE/browse. For example the OBI project suggests people browse OBI using the NCBO Bioportal, and so <http://purl.obolibrary.org/obo/obi/browse> redirects to the Bioportal view on OBI.

## History and Rationale

For a history of this document see [history on github](https://github.com/OBOFoundry/OBOFoundry.github.io/commits/master/id-policy.html).

## Acknowledgments

This policy has been initially discussed, drafted and implemented as part of the development of the OBI project.

Authors: Alan Ruttenberg, Melanie Courtot and Chris Mungall. Thanks to Jonathan Rees, Bill Bug, Colin Batchelor, David Osumi-Sutherland, Duncan Hull, Peter Robinson, Michel Dumontier, the OBO coordinators and the OBI Consortium for their help.
