---
layout: post
categories: newsletter
title: "OBO Foundry Newsletter Issue 3"
date: 2023-12-18
author:
  - Leila Kiani
---


## OBO Foundry Newsletter Issue 3

Season's Greetings from the OBO Foundry Community!

As we wrap up another year with many developments in and around bio-ontologies, we are excited to present the third edition of the OBO Foundry Newsletter during this festive season. In the spirit of celebration and reflection, we want to thank the entire OBO community for their continued dedication and contributions.

In this edition, we will share highlights of the achievements and milestones reached throughout the year. From collaborative projects to individual accomplishments, we aim to showcase the collective success of our community. We will shine our spotlight on two long-standing OBO Foundry members, Nomi Harris and James Overton, and two ontologies, the Uberon anatomy ontology and the recently renamed Ontology for Modeling and Representation of Social Entities (OMRSE). 

Wishing you a joyful holiday season and a prosperous New Year filled with exciting developments in the bio-ontological world!

Best regards,  [The OBO Foundry Operations Committee.](https://obofoundry.org/docs/OperationsCommittee.html)


## Highlights 


### OBO Foundry 2023:  Year at a Glance

This is a spotlight summary of the key developments for the OBO Foundry in 2023:



* New ontologies were added after a review process, including: [MCRO](https://obofoundry.org/ontology/mcro.html), [VBO](https://obofoundry.org/ontology/vbo.html), [NGBO](https://obofoundry.org/ontology/ngbo.html), [ADO](https://obofoundry.org/ontology/ado.html) and [OCCO](https://obofoundry.org/ontology/occo.html).  
* A decision was made to mandate OBO Dashboard validation starting in January 2024. At first, this will result only in presentational consequences on the website.
* Community outreach was strengthened through newsletter relaunch and member surveys.
* Technical infrastructure was upgraded through ROBOT, ODK, and PURL server improvements.
* Discussion began about the possibility of starting a nonprofit organization to support work on OBO Foundry.

2023 was a year of important decisions and advances for OBO Foundry. The mandatory dashboard validation and increased focus on community outreach will support future improvements.


---


### Important Reminder: OBO Dashboard Compliance in 2024

As we approach the third edition of our newsletter, we wish to remind the OBO community that, starting January 1<sup>st</sup>, 2024, passing the [OBO Dashboard](http://dashboard.obofoundry.org/dashboard/index.html) will be mandatory. The OBO Foundry will introduce a visual indicator on the [OBO Foundry homepage](https://obofoundry.org/) to display each ontology's compliance state. Non-compliant ontologies will be sorted and shaded at the bottom of their default ontology-by-topic view group. This serves as an informative measure for users and encourages ontology curators to strive for excellence in quality control. 

Remember, only dashboard errors (black X on a red background) cause non-compliance. Warnings (yellow triangle) or information (blue i) in the final 'Summary' column are (still) acceptable. 

An explanation of the dashboard report is available here ([link to dashboard video](https://youtu.be/m2khZcJVKU0?feature=shared&t=1319)); more information can be found at [http://dashboard.obofoundry.org/dashboard/about.html](http://dashboard.obofoundry.org/dashboard/about.html).


---


## Decisions Made and Important Updates



* Claudia Sánchez-Beato Johnson [started a discussion](https://github.com/information-artifact-ontology/ontology-metadata/issues/135) with a request to add a "has_acronym" property to OMO. The debate centered on whether acronyms should be a distinct property or follow the “synonym type” pattern. Consensus at the OBO Foundry Operations Committee meeting led to the addition of a new 'acronym' synonym type in OMO. The decision avoided introducing a separate 'has_acronym' property to maintain consistency and prevent disruptions to existing tools.


---


## Ongoing Discussions

Here, we list some of the discussions happening around the OBO-sphere:



* Criteria and process for marking ontologies as inactive, unresponsive, orphaned, etc. The OBO Operations Committee is working to define these different status labels clearly. [ Join the discussion. ](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2255)
* The movement to standardize synonym types (e.g. abbreviation, UK spelling, layperson)  across OBO Foundry ontologies is ongoing. [Join the discussion](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2450) or find a [list of the current synonym types on ontobee](https://ontobee.org/ontology/OMO?iri=http://www.geneontology.org/formats/oboInOwl%23SynonymTypeProperty).
* The potential need for paid staff to accelerate progress is being considered as part of a discussion on whether the OBO Foundry should transition to a non-profit organization ([join the discussion](https://github.com/OBOFoundry/OBOFoundry.github.io/discussions/2477) if you have experience and would be able to help out).
* Related to the above, a discussion on OBO Foundry's governance practices led to recommendations for enhancing governance by defining the community, establishing a steering committee, documenting decision-making, improving conflict resolution, ensuring consistent policies, and creating SOPs for ontology status. The ultimate goal is to strengthen governance, enabling funding applications, priority oversight, community engagement, and potential non-profit transition, while acknowledging the required effort. The aim is to enhance transparency, equity, accessibility, and community participation in OBO Foundry's activities.


---


## Ontologies


### Reviewing Ontologies for OBO Membership

[The Standard Operating Procedure (SOP)](https://obofoundry.org/docs/SOP.html#ROOM) for reviewing ontologies outlines the criteria for a comprehensive yet time-efficient manual review of ontologies submitted for registration with the OBO Foundry. There are four roles involved in the review process: 



* The “submitter” is the individual who originally submitted the request for OBO Membership and the point of contact on behalf of the ontology. 
* The [New Ontology Request (NOR) Manager](https://obofoundry.org/roles/nor-manager), a specific role in OBO currently held by Paul Fabry, is responsible for guiding the submitter through the submission process and performing the initial review of the ontology, which includes ensuring that the submission request is completed appropriately and that the ontology is validated in the [OBO Dashboard](https://obofoundry.org/obo-nor.github.io/dashboard/index.html).
* The OBO Foundry reviewer is the primary reviewer assigned by the OBO Operations Committee to perform the in-depth review of the ontology.
* The OBO community is any member of the community that wishes to contribute to the full open review of the ontology. While feedback by the community is welcome, the OBO Foundry reviewer is ultimately responsible to decide which feedback affects the membership decision.

The review focuses on key aspects such as ontology scope, adherence to the OBO identifier scheme, accurate use of imported terms, appropriate axiomatic patterns, and correct application of object properties. The SOP underscores the importance of demonstrating the ontology's relevance to life sciences, using expert input, and justifying any overlaps with	existing terms. Submitters are expected to be willing to address identified issues within two months. Once the OBO Foundry reviewer reaches a decision, the decision is presented to the OBO Foundry Operations Committee, and unless there is a veto from any of the committee members, the ontology is either accepted or rejected.


### Ontologies currently under review 



* [The Caroli's Disease and Syndrome ontology. ](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2406)CaroliO, focusing on Caroli's Disease and Syndrome, has been submitted for inclusion in the OBO Foundry ontologies. The ontology aims to improve the diagnosis and treatment of these rare liver conditions. It offers a structured representation of symptoms, outcomes, and treatment options, supporting researchers and healthcare professionals in advancing their understanding and strategies. CaroliO is currently under review; the contributors are actively addressing feedback and making necessary updates to enhance the ontology's quality and alignment with OBO Foundry standards. [Join the discussion](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2406)
* [The African Population Ontology (AfPO)](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2461) was developed to comprehensively classify African study participants in prospective research studies. CaroliO is currently under review. [Join the discussion](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2461).


### Spotlight on well-established OBO ontologies

In this issue, we would like to highlight two ontologies from the OBO Foundry family: [Uberon multi-species anatomy ontology](https://obofoundry.org/ontology/uberon.html) and [OMRSE](https://obofoundry.org/ontology/omrse.html).



* [Uberon multi-species anatomy ontology](https://obofoundry.org/ontology/uberon.html) is a comprehensive species-neutral ontology that aims to represent anatomical structures consistently across a wide range of taxa. Uberon incorporates extensive connections to taxon-specific anatomical ontologies, facilitating the integration of expression, function and phenotypic data. The ontology currently contains over 16,000 terms covering structures found across various metazoans and integrates with other ontologies, such as the Cell Ontology (CL) or the Gene Ontology (GO). Uberon was released in 2012, and soon thereafter became part of the OBO Foundry. The ontology is constantly expanding with new terms and relations thanks to volunteer editors, developers and users that provide constant feedback. In the last few years, programs like HuBMAP have contributed not only to expanding and refining Uberon, but also to integrating 3D reference objects and 2D reference functional tissue units. 
* The [Ontology for Modeling and Representation of Social Entities (OMRSE)](https://obofoundry.org/ontology/omrse.html) is an ontology that represents the various entities that arise from human social interactions, such as social acts, social roles, social groups, and organizations. OMRSE, formerly known as the 'Ontology of Medically Relevant Social Entities,' has recently been renamed the 'Ontology for Modeling and Representation of Social Entities'. This change reflects its broader scope encompassing all entities emerging from human social interactions, such as roles in organizations, households, education, language, and money. The primary reasons for the change were to clarify its domain and acknowledge that most social entities are medically relevant, addressing concerns within the OBO (Open Biomedical Ontologies) community. This shift was initiated during discussions with the Occupation Ontology (OccO) team, particularly regarding the representation of occupations and their related social entities.

    Implementing the name change was complex, involving updates across various platforms, including OBO metadata, the OMRSE GitHub site, OWL artifacts, and more. The OMRSE team carefully planned this transition to ensure simultaneous updates across all channels. Despite the change, the acronym OMRSE and its OBO ID remained the same to maintain stable identifiers. The revision process also provided an opportunity to update documentation and references on the GitHub site. Overall, this consensus-driven name change aimed to enhance clarity and facilitate better categorization of social entities within the OBO framework and was executed smoothly thanks to thorough preparation.



---


## Members and Volunteers 

The OBO Foundry is excited to spotlight James A. Overton and Nomi Harris in the third issue of our newsletter.

James Overton is a longtime member of the OBO community and has made significant contributions as a leading member of the OBO Foundry Technical Working Group. His work has had a lasting impact on the OBO community and beyond.

Nomi Harris is a dedicated OBO member who has been vital to the community for many years. She has played an instrumental role in organizing issue trackers, editorial work, and general cat-herding.


### Nomi Harris



<img src="https://obofoundry.org/images/nlharris_portrait.jpg" style="height: 250px" alt="Nomi Harris" />




[Nomi Harris](https://www.linkedin.com/in/nomiharris) is a Program Manager for the Berkeley Bioinformatics Open-Source Projects ([BBOP](http://www.berkeleybop.org/)) group at the Lawrence Berkeley National Laboratory. The group is led by [Chris Mungall](https://biosciences.lbl.gov/profiles/chris-mungall/), who is well known in the ontology world and was one of the co-founders of OBO. Nomi has a master’s degree in computer science from MIT, and wrote bioinformatics software for years before transitioning to project management. She has been involved with the OBO Foundry since 2007.

In addition to coordinating about a dozen projects for BBOP, Nomi chairs the annual Bioinformatics Open Source Conference ([BOSC](https://open-bio.org/events/bosc-2024/)) and is on the Boards of the [Open Bioinformatics Foundation](https://www.open-bio.org/) and the [International Society for Computational Biology](https://www.iscb.org/cms_addon/leadership/index.php/past-officers-and-board-of-directors) (ISCB, the organization that runs the [ISMB](https://www.iscb.org/ismb2024/home) conference). In her spare time, she leads a quartet that sings Renaissance music for fun; co-leads a folk music song circle; and fosters kittens.


### James A. Overton



<img src="https://obofoundry.org/images/jamesaoverton_portrait.jpg" style="height: 250px" alt="James Overton" />




James builds open source software for open science, and OBO is fundamental to his work. Through his consulting company [Knocean](https://www.lji.org/), he works for various scientific databases and ontology projects across our community. Since completing his PhD in 2012, James has worked with Bjoern Peters and Randi Vita at the [La Jolla Institute](https://www.lji.org/) on many projects that apply ontologies to immunology, including the [Immune Epitope Database](https://www.iedb.org/), clinical and biological databases for COVID, standards development for [ImmPort](https://www.immport.org/) and [ImmuneSpace](https://immunespace.org/), and the new HIPC Coordinating Center. He has also worked for the National Toxicity Program's [Chemical Effects in Biological Systems](https://cebs.niehs.nih.gov/cebs/) database for many years, for the Gene Ontology on tools for ontologies such as ROBOT, with the Critical Path Institute on documentation such as the [OBO Academy](https://oboacademy.github.io/obook/), and projects for the European Bioinformatics Institute and various universities. James is best known for leading the development of open source software that helps all of OBO, including [ROBOT](http://robot.obolibrary.org/) (the ontology automation tool), the [OBO PURL system](https://github.com/OBOFoundry/purl.obolibrary.org/), the [OBO Dashboard](http://dashboard.obofoundry.org/), and is hard at work on the next generation of open tools for open science. 

---



## Spotlight on Research in the OBO community


### Open code, open data, and open infrastructure to promote the longevity of curated scientific resources

In light of the widespread issue of curated scientific resources becoming out of date, abandoned, or inaccessible, Charles Tapley Hoyt and Benjamin M. Gyori propose the [Open Code, Open Data, and Open Infrastructure (O3)](https://osf.io/vuzt3) guidelines as an actionable roadmap towards promoting the longevity and sustainability of such resources. The O3 guidelines cover three aspects:



1. **Technical Aspect**: make code and data open, version-controlled, permissively licensed, and approachable to contributors. Build on open infrastructure to enable automation of quality control, release, and other technical workflows.
2. **Social Aspect**: use public collaborative tools like GitHub for issue tracking, discussion, and code/data review. Emphasize community engagement by building training materials, curation guidelines, and instituting a welcoming code of conduct.
3. **Governance Aspect**: establish a minimal governance model early, distribute authority across institutions, codify a liberal attribution policy, and encourage transparent discussion.



<img src="https://obofoundry.org/images/o3.jpg" style="height: 250px" alt="Open Code, Open Data, and Open Infrastructure (O3)" />


![alt_text](images/image3.png "image_tooltip")


**[Figure 1.](https://zenodo.org/records/10159888)** A schematic diagram of how social workflows, technical workflows, and project governance interact with the open data, open code, and open infrastructure (O3) guidelines.

The authors suggest that implementing the O3 guidelines enables increased community participation, better highlights individual and institutional contributions, promotes inclusivity, and reduces financial and time burden on maintainers. In turn, these can mitigate the risks of the fluctuation in personnel, funding, and institutional priorities, reduce overlapping curation efforts, broaden opportunities for contribution, and ultimately create better resources. 

While not (yet) endorsing the O3 principles directly as part of our own recommendations, the OBO Foundry is deeply committed to improving technical, social and project workflows in the spirit of the proposal.

Watch a [related presentation](https://www.youtube.com/watch?v=kuJsl-rRjZY) by the authors from the Biocuration 2023 Conference.


---


## Spotlight on OBO Principles 

In this issue, we continue with Principle 2 of the OBO Foundry's series of principles. The OBO Foundry has established these principles as best practices for creating usable, sustainable, and interoperable ontologies. Each principle serves as a criterion for evaluating the potential inclusion of new ontologies. Starting with Principle 1 in a previous newsletter, we now explore Principle 2 in this edition. 


### OBO Foundry Principle 2: Common Format:

The OBO Foundry pursues interoperability at four different levels (Figure 2). In the [last newsletter](https://obofoundry.org/newsletter/2023/09/15/second-issue-newsletter.html), we talked about the importance of the “Open” principle (layer 4 in Figure 2 below), which mandates a standardized open license for all OBO ontologies. Today, we are going to remind you about the importance of supplying ontologies in a “common format” (layer 3 in the Figure), as specified by [Principle 2](http://obofoundry.org/principles/fp-002-format.html).

A format comprises two components: a data model (like OWL, SKOS, or RDFS) and a serialization (RDF/XML, OBO Format, Functional Syntax). Over the course of the last 20 years, the OBO Foundry has promoted the use of the OWL model for representing ontologies, mapping other standards like the OBO Format, which is used by a large number of ontologies, to OWL and writing standard “converters” to translate between the two. But using a common data model is not all that is needed: if ontologies are distributed in different serializations, interoperability is hampered because most tools do not provide parsers for all serializations (with the exception of the [OWL API](https://github.com/owlcs/owlapi)). To maximize uptake across various communities of practice, the OBO Foundry mandates the RDF/XML standard as the main serialization for OWL ontologies, making it possible to process ontologies using a wide variety of standard RDF tools as well as specialized OWL tools. The Common Format principle therefore ensures that all primary ontology releases must be serialized in RDF/XML.

The implementation of the “Common Format” principle has been [one of the most successful OBO principles](https://dashboard.obofoundry.org/dashboard/analysis.html), with only a handful of ontologies in the Foundry failing to provide an RDF/XML release. To pass this principle, which is mandatory for our January 1<sup>st</sup> 2024 deadline (see above), your primary ontology release MUST be in RDF/XML.



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")


**Figure 2.** The four “layers” of interoperability in the OBO Foundry.


---


## Spotlight on Software Tools

We continue spotlighting important software tools for the Open Biomedical Ontologies (OBO) Foundry community in this issue. These tools play a vital role in collaborative efforts, ensuring data integrity and facilitating the editing and validation of ontologies. 

The table below provides an overview of several of these tools, some of which are used and actively developed by members of the OBO Foundry community.


<table>
  <tr>
   <td><strong>Software Package</strong>
   </td>
   <td><strong>Links</strong>
   </td>
   <td><strong>OBO Slack channel</strong>
   </td>
   <td><strong>Core Features</strong>
   </td>
  </tr>
  <tr>
   <td>Bioregistry
   </td>
   <td><a href="https://github.io/biopragmatics/bioregistry">https://github.com/biopragmatics/bioregistry</a>
   </td>
   <td>#prefixes
   </td>
   <td>Integrative registry of prefixes and URI format strings for ontologies, databases, and other semantic spaces
   </td>
  </tr>
  <tr>
   <td>ODK
   </td>
   <td><a href="https://github.com/INCATools/ontology-development-kit">https://github.com/INCATools/ontology-development-kit</a>
   </td>
   <td>#ontology-development-kit
   </td>
   <td>Executable workflows for ontology development incl release, quality control and automated import system.
   </td>
  </tr>
  <tr>
   <td>Protégé
   </td>
   <td><a href="https://github.com/protegeproject/protege">https://github.com/protegeproject/protege</a>
   </td>
   <td>#protege
   </td>
   <td>The most popular desktop graphical UI for editing ontologies in the OBO community.
   </td>
  </tr>
</table>



---


## Events


### [OBO Academy: Monarch Seminar Series](https://oboacademy.github.io/obook/courses/monarch-obo-training/) (ongoing)



* [Tutorial 2024/01/24: Curation with Synonyms Tutorial](https://github.com/OBOAcademy/obook/issues/450)

    This tutorial will discuss best practices for assigning synonyms during ontology curation. The focus is on concrete examples and common issues when determining the proper scope for a synonym.


Don't forget you can vote for future training topics here: [https://github.com/OBOAcademy/obook/discussions/categories/tutorial-requests](https://github.com/OBOAcademy/obook/discussions/categories/tutorial-requests)

### Updates on past events



* Chris Mungall gave an OBO Academy presentation on a framework called [Enhancing curation workflows with CurateGPT](https://www.youtube.com/watch?v=p6j3WwzIv40). The presentation provided an overview of [CurateGPT's](https://www.youtube.com/watch?v=p6j3WwzIv40) capabilities, including searching, querying, completing, extracting from text, finding evidence, and editing. Chris discussed evaluations on using the tool for automating parts of ontology development, such as defining terms and predicting relationships. The idea is for an integrated system to organize complex ontology curation workflows with collaboration with humans and AI.
* Chris Mungall and Nico Matentzoglu gave an introduction to OBO ontologies and related issues to the Pharma community as part of the Seminar Series [“Demystifying Ontologies for Life Science Leaders”.](https://www.pistoiaalliance.org/eventdetails/demystifying-ontologies-for-life-science-leaders/) The slides can be accessed [here](https://docs.google.com/presentation/d/1kBc-S01TKtr4wTEtKHNp2bG-PtYKWnopDOatuk5_fL8/edit#slide=id.p), the recording [here](https://vimeo.com/873399143/26bbb4505b).  
* Nico Matentzoglu and Charles Tapley Hoyt gave their [International Society for Biocuration](https://www.biocuration.org/) Career award talks about “[Closing the gap between effective biocuration and meaningful ontology development](https://docs.google.com/presentation/d/16eJVwRGsPZcFps1dK_-1MEubqpOSC8Yclrx817K7QCg/edit#slide=id.p)” and “[Democratizing Biocuration”](https://docs.google.com/presentation/d/1D6P-1hQefXU_yRODSJkOFLH3tPxsk9Abi20ycA0xKWU/edit?usp=sharing).
* Deepak R. Unni gave a presentation on [principles and practices for open and reusable ontologies](https://docs.google.com/presentation/d/1x7VBlLh4s9bUWx2YvhywPFPiUDq0S49HyPj3CmEgtSI/edit#slide=id.g27e4dc7fe9d_0_103) at a [FAIR IMPACT Workshop](https://fair-impact.eu/events/fair-impact-events/fair-impact-semantic-artefact-governance-workshop) on Governance of Semantic artifacts, and talked about ways that [OBO Foundry](https://obofoundry.org/) actively facilitates interoperability. The Slides can be accessed [here](https://docs.google.com/presentation/d/1HoFTjHLCUAFrvJptf8EQbv7Ab46w5urc/edit?pli=1#slide=id.g27dd3c59bde_0_2). The recording [here](https://www.youtube.com/watch?v=_5HPg-eYLds). 


---


## Ways to be part of the OBO Foundry community

There are many ways to be part of the OBO Foundry community, beyond [using our website to find ontologies of interest](https://obofoundry.org). For example:



* Join the [obo-discuss mailing list](https://groups.google.com/forum/#!forum/obo-discuss) (low-traffic, no spam)
* If you are interested in the technical aspects, you can also join the [obo-tools mailing list](https://groups.google.com/forum/#!members/obo-tools)
* Join the conversation in our [Slack workspace](https://obo-communitygroup.slack.com/archives/C01DP18L5GW) (when you join the obo-discuss mailing list, the welcome message has an invitation link for the Slack workspace).
* Use our public [issue tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues) to report a problem you discovered on obofoundry.org or request a new feature
    * Note that most issues relating to individual ontologies (e.g., a request to add a new term) should be added to the issue tracker for the specific ontology
* Propose a fix to an issue you see on our issue tracker (this is done via a GitHub Pull Request, which will be checked and approved by someone in the Foundry). Since all of [our code is publicly readable](https://github.com/OBOFoundry), you may be able to pinpoint where a bug fix needs to go.
* [Request that your ontology be considered for inclusion in the Foundry](https://obofoundry.org/faq/how-do-i-register-my-ontology.html)
* If you want to take your contributions to OBO Foundry to the next level, you can [nominate yourself to be considered for the OBO Operations Committee](https://obofoundry.org/docs/NewOBOFC.html). There are various roles in which you can contribute, including assisting with the production of this newsletter
