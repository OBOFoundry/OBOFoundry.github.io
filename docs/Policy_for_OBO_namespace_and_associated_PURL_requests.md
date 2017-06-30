---
layout: doc
id: Policy_for_OBO_namespace_and_associated_PURL_requests
title: Policy_for_OBO_namespace_and_associated_PURL_requests
---

**This policy has been formally adopted on April 19th 2013. Do not edit this page without consulting with the OBO Technical group.**
**Change adopted March 2017 to add obsolete metadata to non-maintained PURLs. See issue #344.**
Comments to [obo-discuss@lists.sourceforge.net](mailto:obo-discuss@lists.sourceforge.net)

# Background

Identifiers are managed by giving requesting projects a series of numerical ids that have a common prefix, sometimes known as a _namespace_. For example, a project might request and obtain the prefix "MOBO". The ontology would then use ids of the form http://purl.obolibrary.org/obo/MOBO_0000001 , http://purl.obolibrary.org/obo/MOBO_0000002 ...

In order to ensure that there is no prefix redundancy, i.e. only one project/resource is using the namespace "MOBO", these are allocated by the OBO Foundry technical working group.

The technical working group reserves the right to make decisions based on their experience and judgement. In addition to uniqueness of prefixes, other criteria are for example that there not be overlaps of usage. This includes awareness that there can be the appearance of overlap between accession numbers used in databases and [prefixed URIs](http://www.w3.org/TR/curie/). For example, we would probably not create a prefix "ISBN" and would instead make alternative suggestions.

# Process #

## OBO ##
  1. While there are no review requirements, participation in the OBO Foundry implies willingness to discuss your project and collaboratively develop it. You are strongly encouraged to build upon the existing suite of ontologies available in the [OBO library](http://obofoundry.org).
  1. We recommend projects be orthogonal to each other (i.e., no domain overlap). For those classes that are common across multiple resources (e.g., the class _cell_) we recommend importing terms from an already existing ontology. At a minimum, we expect attribution of existing work.

## Requestor ##

  1. You will get a PURL for your main file under the OBO PURL domain as well as a PURL domain. You will be part of the administrator group for those resources. Please familiarize yourself with the PURL guide at [PULRGuide](PURLGuide.html) .
  1. As of today (April 7th, 2013), when your prefix is registered it is automatically included for display on the OBO Foundry site. This may change in the future as we modify our registration system.
  1. Once your domain is created under OBO you will automatically benefit from our dereferencing tool [Ontobee](http://www.ontobee.org). If preferred you can, of course, redirect your pages towards your own web pages.
  1. Please keep the OBO PURL group (group ID: OBO) to the maintainers/members of your PURL group

## Status of ontology development ##

  1. A project should exist, with work started. We will not "pre-book" prefixes and domains for potential future resources.
  1. The required namespace must be available.
  1. The resource must be publicly available when released.
  1. There must be a contact person for the resource. We ask that the contact person for resources be subscribed to our main communication channel, the obo-discuss list.
  1. The requestor and/or contact person should be ready to discuss issues such as whether the ontology is orthogonal, whether there is potential to collaborate with existing efforts.
  1. It is expected that solicitation of a prefix is done _before_ the prefix is used for identifiers. A common strategy is to develop an ontology, request a prefix, and translate the initial URIs used to the PURLs some time before the initial release. **There is no guarantee that you will be granted your prefix, even if you have been using it in your file**.

## Information needed for a prefix request ##

  * requested prefix
  * ontology title
  * ontology download link
  * ontology home page
  * point person contact email
  * ontology discussion mailing-list
  * ontology issue tracker link
  * purl.org user ID - please register [there](http://purl.org) if you don't have one

## Requesting the prefix ##

The requests proceeds in 2 steps:

  1. First send an email to [obo-discuss](mailto:obo-discuss@lists.sourceforge.net) with your request to allow community feedback (you may need to [register](https://lists.sourceforge.net/lists/listinfo/obo-discuss) first)

  1. Submit your request to [our tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues)

We expect general discussion to take place on the obo-discuss list, while technical follow-up will take place on the tracker.

Example of such request:

 * OHMI
    * [obo-discuss message](https://sourceforge.net/p/obo/mailman/message/35692927/)
    * [tracker message](hhttps://github.com/OBOFoundry/OBOFoundry.github.io/issues/397)

## Response ##

Allocate 2 weeks to give members of the community time to provide feedback and for the operations committee to act on the request. We will usually respond on the tracker ticket and acknowledge your request/provide a tentative creation date.
If you don't hear back from us after 2 weeks, please send a note to the [obo-foundry-technical-working-group@googlegroups.com](mailto:obo-foundry-technical-working-group@googlegroups.com) or request follow-up via the tracker ticket.

# PURL Maintenance Obligations #

Ontology editors are responsible for maintaining their own PURLs. Help is available from the OBO Foundry Technical WG by filing an issue in the [tracker] (https://github.com/OBOFoundry/OBOFoundry.github.io/issues) associated with this repository. Any PURL that does not work (or never worked) is considered abandoned and will be obsoleted after an initial warning period. If you find that a PURL you maintain was obsoleted when it should not have been, please file an issue in the [tracker] (https://github.com/OBOFoundry/OBOFoundry.github.io/issues) to have it restored.

# For more information #

For instructions on how to create the prefix/domain at purl.org, or to understand how the OBO PURL domain/redirection works, see [OBOPURLDomain](OBOPURLDomain.html)
