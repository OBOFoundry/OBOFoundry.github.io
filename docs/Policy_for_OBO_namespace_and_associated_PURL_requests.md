---
layout: doc
id: Policy_for_OBO_namespace_and_associated_PURL_requests
title: Policy_for_OBO_namespace_and_associated_PURL_requests
---

**This policy has been formally adopted on April 19th 2013. Do not edit this page without consulting with the OBO Technical group.**

**Change adopted March 2017 to add obsolete metadata to non-maintained PURLs. See issue https://github.com/OBOFoundry/OBOFoundry.github.io/issues/344.**

**Change suggested August 2019 to accomodate new requirements to do original work and work with existing ontologies. See issue https://github.com/OBOFoundry/OBOFoundry.github.io/issues/620.**

Comments to [obo-discuss@googlegroups.com](mailto:obo-discuss@googlegroups.com)


# Background

Identifiers are managed by giving requesting projects a series of numerical ids that have a common prefix, sometimes known as a _namespace_. For example, a project might request and obtain the prefix "MOBO". The ontology would then use ids of the form http://purl.obolibrary.org/obo/MOBO_0000001 , http://purl.obolibrary.org/obo/MOBO_0000002 ...

In order to ensure that there is no prefix redundancy, i.e. only one project/resource is using the namespace "MOBO", these are allocated by the OBO Foundry technical working group.

The technical working group reserves the right to make decisions based on their experience and judgement. In addition to uniqueness of prefixes, other criteria are for example that there not be overlaps of usage. This includes awareness that there can be the appearance of overlap between accession numbers used in databases and [prefixed URIs](http://www.w3.org/TR/curie/). For example, we would probably not create a prefix "ISBN" and would instead make alternative suggestions.

# Process #

## OBO PURLs##
  1. While there are no review requirements for an OBO Foundry PURL, participation in the OBO Foundry implies willingness to discuss your project and collaboratively develop it. You are strongly encouraged to build upon the existing suite of ontologies available in the [OBO library](http://obofoundry.org).
  1. We recommend projects be orthogonal to each other (i.e. no domain overlap). For those classes that are common across multiple resources (e.g., the class _cell_) we recommend importing terms from an already existing ontology. Application ontologies (those developed for specific data integration tasks) should reuse terms from existing OBO Foundry domain ontologies. At a minimum, we expect attribution of existing work, specifically through the use of PURLs for individual terms and ontologies.

## Status of ontology development ##

  1. A project should exist, with work started. We will not "pre-book" prefixes and domains for potential future resources.
  1. A project must be doing original work within the biological ontology community. 
      * We will not provide namespaces for projects that are issuing new identifier for existing ontologies.
      * If there is clear overlap with an existing domain ontology, you must demonstrate a good faith effort to work with that ontology to provide any new terms needed.
  1. The required namespace must be available.
  1. The resource must be publicly available when released. The general expectation is that the ontology source code is available on a public repository such as GitHub.
  1. There must be a contact person for the resource. The contact person for resources must be subscribed to our main communication channel, the obo-discuss list.
  1. The requestor and/or contact person should be ready to discuss issues such as whether the ontology is orthogonal, whether there is potential to collaborate with existing efforts.
  1. It is expected that solicitation of a prefix is done _before_ the prefix is used for identifiers. A common strategy is to develop an ontology, request a prefix, and translate the initial URIs used to the PURLs some time before the initial release.  **There is no guarantee that you will be granted your prefix, even if you have been using it in your file**.


## Requesting the prefix ##

  1. First send an email to [obo-discuss](mailto:obo-discuss@googlegroups.com) with your request to allow community feedback (you may need to [apply to join group](https://groups.google.com/forum/#!forum/obo-discuss) first.)

  1. Submit your request to [our tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues). Select `New Issue` and then select `New Ontology Request`. To request a new PURL/namespace you must provide a stable URL (in a public repository) for the ontology, as well as the following metadata:

 * id: prefix of ontology in lowercase, e.g. mobo, uberon, chebi, cl
 * title: concise title of your ontology
 * home page: this can be a GitHub URL
 * contact: name, email and github username
 * tracker: URL of issue tracker (typically GitHub)
 
 We recommend you set up an ontology repository in GitHub using the [Ontology Development Kit](https://github.com/INCATools/ontology-development-kit). This will create the required metadata fields for you.

  1. (Optional) make a Pull Request on [OBOFoundry.github.io](https://github.com/OBOFoundry/OBOFoundry.github.io) and [purl.obolibrary.org/](https://github.com/OBOFoundry/purl.obolibrary.org/)

We expect general discussion to take place on the obo-discuss list, while technical follow-up will take place on the tracker.

Example of such request:

 * OHMI
    * [obo-discuss message](https://sourceforge.net/p/obo/mailman/message/35692927/)
    * [tracker message](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/397)

## Response ##

Allocate 2 weeks to give members of the community time to provide feedback and for the operations committee to act on the request. We will usually respond on the tracker ticket and acknowledge your request/provide a tentative creation date.
If you don't hear back from us after 2 weeks, please send a note to the [obo-foundry-technical-working-group@googlegroups.com](mailto:obo-foundry-technical-working-group@googlegroups.com) or request follow-up via the tracker ticket.

