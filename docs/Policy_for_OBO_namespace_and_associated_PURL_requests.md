---
layout: doc
id: Policy_for_OBO_namespace_and_associated_PURL_requests
title: OBO Foundry membership requirements and technical details
---

# Expectations for OBO Membership

1. Participation in the OBO Foundry implies willingness to discuss your project and collaboratively develop it. You are strongly encouraged to build upon the existing suite of ontologies available in the [OBO library](http://obofoundry.org).

2. We recommend projects be orthogonal to each other (i.e. no domain overlap). For those classes that are common across multiple resources (e.g., the class _cell_) we recommend importing terms from an already existing ontology. Application ontologies (those developed for specific data integration tasks) should reuse terms from existing OBO Foundry domain ontologies. At a minimum, we expect attribution of existing work, specifically through the use of PURLs for individual terms and ontologies.

3. OBO projects are [open](http://obofoundry.org/principles/fp-001-open.html) and use [version control](http://obofoundry.org/principles/fp-004-versioning.html), and so we recommend that you set up an ontology repository on [GitHub](https://github.com) (or another public version control system). We provide the [Ontology Development Kit](https://github.com/INCATools/ontology-development-kit) to help with common ontology development tasks, including the creation of a GitHub repository and appropriate metadata files (see below).

4. Before you participate in our community, please read and agree to follow our [Code of Conduct](http://obofoundry.org/docs/COC.html).

# Requirements for OBO Membership

1. A project should exist, with work started. We will not "pre-book" IDSPACEs and domains for potential future resources.
2. A project must be doing original work within the biological ontology community.
   - We will not provide an IDSPACE for a project that is issuing new identifier for existing ontologies.
   - If there is clear overlap with an existing domain ontology, you must demonstrate a good faith effort to work with that ontology to provide any new terms needed.
3. The required IDSPACE must be available. We do not allow two-letter IDSPACEs and strongly discourage three-letter IDSPACEs that contain the letter "O". For more details, please see the guidelines for [allocating IDSPACEs](http://obofoundry.org/id-policy.html#allocating-idspaces).
4. The resource must be publicly available when released. The general expectation is that the ontology source code is available on a public repository such as GitHub.
5. There must be a contact person for the resource. The contact person for resources must be subscribed to our main communication channel, the [obo-discuss](https://groups.google.com/forum/#!forum/obo-discuss) mailing list.
6. The requestor and/or contact person should be ready to discuss issues such as whether the ontology is orthogonal, whether there is potential to collaborate with existing efforts.
7. It is expected that solicitation of a IDSPACE is done _before_ the IDSPACE is used for identifiers. A common strategy is to develop an ontology, request a IDSPACE, and translate the initial URIs used to the PURLs some time before the initial release. **There is no guarantee that you will be granted your IDSPACE, even if you have been using it in your file**.
8. As of 4th May 2021, every new ontology submission is required to pass the [OBO Dashboard](http://dashboard.obofoundry.org/) quality control, which means that they are not allowed to have any substantial errors (anything "red"). The only exceptions to this requirement are (1) `Users`, and (2) results in the `Report` that pertain to terms from imported (external) ontologies. Your ontology will be set up in a [provisional Dashboard](https://obofoundry.github.io/obo-nor.github.io/dashboard/index.html) as soon as the GitHub submission request is made. OBO foundry will provide support to help you fix any issues your submission might have.

# Process

## 1. Submitting your ontology to request the IDSPACE

1. Submit your request on our [GitHub tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues). Select `New Issue` and then select `New Ontology Request`. Fill out the requested information as completely as possible.
2. Send an email to [obo-discuss](mailto:obo-discuss@googlegroups.com) with your request to allow community feedback (you may need to [apply to join group](https://groups.google.com/forum/#!forum/obo-discuss) first.) Be sure to include the link to the issue you created in step 1.
3. (_Optional_): If you would like to join the obo-community Slack, please indicate this in your email.

We expect general discussion to take place on the obo-discuss list, while technical follow-up will take place on the tracker.

Example of such request for ECTO:

- [tracker issue](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/397)
- [obo-discuss message](https://groups.google.com/forum/#!msg/obo-discuss/Mfbrg5cJ2lM/17HfTEnJDAAJ)

## 2. Response

After your submission to the GitHub tracker, your ontology will be set up in a [provisional Dashboard](https://obofoundry.github.io/obo-nor.github.io/dashboard/index.html). As of 4th May 2021, every new ontology submission is required to pass the dashboard quality control, which means that they are not allowed to have any substantial errors (anything "red"). OBO foundry will provide support to help you fix any issues your submission might have.

After the ontology passes Dashboard quality control, please allow time for members of the community to provide feedback and for the Operations Committee to review the request. If you don't hear back from us after 4 weeks, you can follow-up via the tracker issue you created.

Based on this discussion, the Operations Committee will either approve the IDSPACE request, ask for changes, or decline your request.

## 3. Approval

Once an IDSPACE is approved, two important files must be created. Since your project will be responsible for maintaining these files, it's best if someone on your team reads our documentation and creates these files. If this is impossible, please let us know on your tracker issue, and one of our volunteers will try to accommodate you.

1. An OBO Registry metadata file. An OBO Registry entry provides key metadata about your project for <http://obofoundry.org> and many other uses. See our [FAQ: Edit metadata](http://obofoundry.github.io/faq/how-do-i-edit-metadata.html)

2. An OBO PURL configuration file. The OBO PURL system helps maintain links to your ontology terms and artifacts. See [purl.obolibrary.org/](https://github.com/OBOFoundry/purl.obolibrary.org/) for configuration file formatting and how to add your new file.

If you used the [Ontology Development Kit](https://github.com/INCATools/ontology-development-kit) to create your ontology, then the required YAML files will be created and stored under `src/metadata`.

These two files should be created as GitHub Pull Requests (PRs) in the appropriate repository ([OBO Foundry Registry](https://github.com/OBOFoundry/OBOFoundry.github.io) for the OBO registry entry and [OBO PURLs](https://github.com/OBOFoundry/purl.obolibrary.org/) for the PURL configuration). Once these PRs for these two files are merged, your ontology is officially registered with OBO and your PURLs are available.

## 4. Maintenance

As your ontology project grows and changes, be sure to update the OBO registry entry and PURL configuration for your project using GitHub Pull Requests.

# Background

Every OBO project has an IDSPACE: a short alphanumeric code that uniquely identifies it among the other OBO projects, e.g. "MOBO". The IDSPACE is an important part of the project PURLs (Persistent Uniform Resource Locators), which are used to identify individual ontology terms as well as project artifacts such as OWL files.

In order to ensure that there is no IDSPACE redundancy, i.e. only one project/resource is using the IDSPACE "MOBO", these are allocated by the OBO Foundry Technical Working Group.

The Technical Working Group reserves the right to make decisions based on their experience and judgement. In addition to uniqueness of IDSPACEs, other criteria are for example that there not be overlaps of usage. This includes awareness that there can be the appearance of overlap between accession numbers used in databases and [prefixed URIs](http://www.w3.org/TR/curie/). For example, we would probably not create a IDSPACE "ISBN" and would instead make alternative suggestions.
