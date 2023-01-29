---
layout: post
title: "OBO services - grant"
date: 2017-11-07
categories: update
summary: "Good news - we managed to secure some funding for a revamp of the OBO services infrastructure"
---

Dear OBO community,

We are happy to announce some good news: A three year R24 grant through the BD2K initiative to support OBO services was funded (finally, after being in administrative Nirvana for over half a year, and still on hold because NIH is trying to determine if it is human subject research(!)). Below are the specific Aims that this grant is intended to support. Much of it will be dedicated to 'do things right' and built a more long term sustainable and easier to maintain version of the existing technical infrastructure. But there will also be support for establishing some new capability, and those should help making OBO work in general, such as automating aspects of the ontology review process.

A few things to note:

- The funding is very much limited, and much of it is committed to upgrade the OBO 'plumbing' to protect us from potential disasters going forward. Which by definition means there won't be immediate visible improvements. But in the longer term, this should free up volunteer developer time that is now being spent on putting out fires to instead work on new capabilities.
- As we are implementing new checks on ontologies (both in the OBO registry and on the ontology files themselves), there will be an increase in notifications to ontology developers of areas for improvement in their ontologies. Please don't take those as criticisms on your work. We are trying to ensure that the agreed upon standards in OBO can and are being enforced. In several cases, such as ensuring that the ontology is released under an open license, there are many possible way to do this which are all perfectly fine. But agreeing on a single convention will make it easy to automate checking if an ontology confirms with the convention. We will rely on feedback from the OBO community what is a useful degree of stringency, and what is overreach. We plan to announce our activities here, and constructive feedback is very much welcome.
- If you want to be engaged and contribute to this process, consider joining one of the groups in the OBO operations committee, described at
  http://www.obofoundry.org/docs/OperationsCommittee . Membership means work, and there is lots of it, so volunteers are always welcome.

Best,

Chris and Bjoern

Specific Aims
Ontologies are broadly used in the biomedical domain to enable precise and computable representation of entities in the world and their relationships. The success of the Gene Ontology (GO) - which was developed to describe molecular functions, biological processes and cellular components of gene products - motivated researchers to develop ontologies covering domains beyond the scope of GO. To coordinate these ontology development efforts, in 2001 the Open Biomedical Ontologies (OBO) Foundry was established as a community effort to converge toward a suite of freely shared, interoperable ontologies that cover all of biology and biomedicine. To support this mission, OBO provides a number of services to the community, including 1) the OBO registry with metadata on all our ontology projects, 2) the Persistent URL (PURL) system that maintains permanent addresses for our ontologies and terms, 3) optional content hosting for published files, 4) standardized software tools that implement our best practices, 5) OBO principles, guidelines and best practices, reflecting our shared experience and goals, and 6) an outreach effort to build and sustain our community, coordinating effective technical and organizational standards for ontology development and use.

As a grassroots project, OBO has been built through volunteer efforts and resources contributed by its members. This has necessitated a focus on low-cost approaches, building on open source software, running on minimal server infrastructure, and emphasizing "self-serve" systems. This low-cost, high-value approach has proven to be sustainable and scalable over the past 15 years, as the OBO community has grown to include more than 140 active ontology projects. We have accomplished a great deal without dedicated funding for OBO. However, with the one-time funding requested here there is an opportunity to catalyze a range of lasting improvements to our infrastructure, accelerating our mission of collaboration and interoperability. Our goals are to 1) improve robustness, maintainability, and use of standards in our existing services, 2) build new capabilities into the service infrastructure, and 3) increase the ability of the community to participate in the OBO project, all while keeping operating costs low. Accordingly our Specific Aims are as follows:

Aim 1: Upgrade OBO Services Infrastructure for Long Term Sustainability. The technical OBO services (registry, PURLs, content hosting) are indispensable and benefit a broad group of users, far beyond the core OBO community. These services rely on infrastructure and code that has grown over time, and is maintained by a very small team of developers. We thus propose a one-time effort to perform a complete review and update of this infrastructure to ensure its long-term reliability, make better use of standards, and provide documentation that will make it easier to share or transition responsibility for its maintenance, all while keeping running costs minimal.

Aim 2: Enhance OBO Services Infrastructure to Add New Capabilities. Adding a small number of new capabilities will multiply the benefits of our services. We will develop a suite of standardized, automated quality control tests and reports, first for individual ontologies and second for groups of interdependent ontologies. Third, we will update standard software tools to run these quality control tests, and integrate these tools more fully with our services. Fourth, we will deploy a monitoring system to measure the stability and usage of our services.

Aim 3: Enlarge, Train and Sustain the OBO Service Developer Community. Successfully running the OBO services requires developers that can maintain them. To increase the number of developers capable and willing to contribute, we propose a one-time investment to thoroughly improve the technical documentation of the services in order to lower barriers for new developers to get started in participating. In parallel, we propose several training and outreach activities to enlarge the developer community.
