---
layout: post
categories: newsletter
title: "OBO Foundry Newsletter Issue 4"
date: 2024-03-18
author:
  - OBO Operations Commitee
---

## OBO Foundry Newsletter Issue 4

Well into the new year, we are happy to present the 4th issue of the OBO Foundry newsletter. 

This edition highlights two great contributors, Anita Caron, and Bill Duncan, and two well-established ontologies, OccO (the Occupation Ontology) and FoodOn. Additionally, we shine a light on two new members of the OBO operation committees, James Stevenson and Vinicius de Souza.

Several ontology reviews are underway, with constructive dialogues aligning with OBO Foundry standards. We also summarize two research studies published by members of the OBO community.

Like spring's renewal, our community grows through collaboration. We remain committed to creating usable, interoperable ontologies to advance biomedical research. With much potential still unfolding, we look forward to continued growth and contributions!

Happy spring season! We are looking forward to great things in bio-ontology!

Best regards,  [The OBO Foundry Operations Committee.](https://obofoundry.org/docs/OperationsCommittee.html)


## Highlights 

### OBO Dashboard Compliance is Live Now

With the arrival of 2024, mandatory compliance with the OBO Dashboard is now in effect. The OBO Foundry will soon be showing a visual indicator on the homepage to display each ontology's compliance status. Non-compliant ontologies will be sorted and shaded at the bottom of their default ontology-by-topic view group. This will serve as an informative measure for users and encourages ontology curators to strive for quality control.

Remember, only dashboard errors (black X on a red background) cause non-compliance. Warnings (yellow triangle) or information (blue i) in the final 'Summary' column are still acceptable. Ontologies in the dashboard are sorted by Dashboard status, which means that ontologies without errors are shown first: [https://dashboard.obofoundry.org/dashboard/index.html](https://dashboard.obofoundry.org/dashboard/index.html).

An explanation of the dashboard report is available here ([link to dashboard video](https://www.youtube.com/watch?feature=shared&t=1319&v=m2khZcJVKU0)); more information can be found at [http://dashboard.obofoundry.org/dashboard/about.html](https://dashboard.obofoundry.org/dashboard/about.html).

---

## Decisions Made and Important Updates

* Addition of a new ontology status: “[unresponsive](https://obofoundry.org/docs/OntologyStatus.html)”, which signifies that the ontology project does not have a contact person who is responsive, but the ontology is still being actively maintained. 
* New Ontology submissions no longer need to pass the criterion “resolvable version IRI” during the submission process, as this is tied to the PURL resolution system. It is, however, expected that when an ontology is officially admitted, the version IRI does resolve correctly,  
* Updating the [SOP document](https://obofoundry.org/docs/SOP.html) to include a new subsection under "Reviewing Ontologies for OBO Membership." This subsection, titled "Rules of Communication," designates the official ontology reviewer as the authority to decide which community suggestions need to be addressed and which do not, aiming to manage situations where community input might not meet the established principles. This addition is intended to streamline the review process and clarify the role of community feedback in ontology evaluations. For more details, please visit the pull request page #[2528](https://github.com/OBOFoundry/OBOFoundry.github.io/pull/2528)
* The EWG improved the OBO Foundry ontology review process by specifying how community input should be taken into account during the review process. The Ontology reviewer has the last word, and is responsible to communicate which feedback is optional, and which mandatory to be addressed before admission (Issue #[2459](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2459)).
* The EWG created an improved FAQ about the OBO Dashboard, covering its role in the Ontology Review process and guides on how to address specific issues.  (Issue #[2263](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2263))

---

## Ongoing Discussions

Here, we list some of the discussions happening around the OBO-sphere:

* The OBO Foundry team is considering implementing lexical matching in their review process for new ontology requests. This method would use a script to identify any content overlaps with existing ontologies, aiming to preserve the distinctiveness and compatibility of ontologies in the Foundry. The discussion focuses on developing an automated script for overlap detection, addressing potential inaccuracies, and enhancing the efficiency and precision of the review procedure. [Join the discussion.](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2517)
* Discussion about adding a metadata field to ontologies that links to annotations, such as text mining corpora and gene associations, to facilitate easier navigation for ontology users. This aims to address challenges in accessing information about the use of ontologies in various datasets, including details on versions, subsets used, and curation practices. A suggested format for this metadata includes identifiers and URLs for annotated datasets. [Join the discussion.](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2527)
* A testable solution for supporting prefix declarations in OBO format has been provided by Jim Balhoff. Please help out with testing this important change!: [https://github.com/owlcs/owlapi/pull/1102#issuecomment-1924073439](https://github.com/owlcs/owlapi/pull/1102#issuecomment-1924073439)

---

## Ontologies

### Reviewing Ontologies for OBO Membership

We recently updated [the Standard Operating Procedure (SOP)](https://obofoundry.org/docs/SOP.html#ROOM:~:text=Ontology%20Acceptance/Rejection%20Decision) for Ontology Acceptance/Rejection Decision. The reviewer presents their assessment and recommendation regarding a new ontology to the OBO Operations Committee. The committee may request clarifications from the reviewer before making a decision on the ontology's acceptance. The decision is made by consensus among the attendees on the call, meaning no strong objections are raised. There is no minimum number of attendees required for the decision to be made.

### Ontology Acceptance Notification

The ontology reviewer should notify the ontology owner about their ontology's acceptance, both in the ticket and via email (copying obo-discuss & obo-operations-committee), using a provided template. The template informs the owner about the next steps, which include creating a metadata record for their ontology in the OBO Foundry GitHub repository and creating a PURL registry entry. The metadata record should be based on the curated metadata from the obo-nor.github.io repository, and the pull request for adding the record should include a link to the New Ontology Request issue. The ontology owner is also provided with examples of a metadata record and a PURL yml file. 

### New ontologies accepted in the OBO Foundry Ontology Library
 
* [The Gall Ontology](https://github.com/adeans/gallont). The GALLONT submission to OBO Foundry, discussed in GitHub issue [#2522](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2522), proposes an ontology for plant gall phenotypes. It aims to provide a controlled vocabulary for describing plant galls, integrating terms from [PATO](https://obofoundry.org/ontology/pato.html), [PO](https://obofoundry.org/ontology/po.html), and other OBO ontologies. The ontology has been formally accepted and is now [included on obofoundry.org](https://obofoundry.org/ontology/gallont.html).


### New ontologies currently under review 

* [The Space LIfe Sciences Ontology](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2518) The Space Life Sciences Ontology (LSDAO) submission for OBO Foundry inclusion supports NASA's Life Sciences Data Archive and related systems, offering definitions and organization for space life science research data. It integrates concepts from several OBO Foundry ontologies and the Science Data Discovery Ontology for broader research applicability. Ongoing discussions focus on refining LSDAO for clarity, accuracy, and OBO Foundry compatibility. [ Join the discussion.](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2518)

### Spotlight on well-established OBO ontologies

In this issue, we continue our ontology spotlight series, highlighting two other ontologies from the OBO Foundry family. [Occupation Ontology (OccO)](https://obofoundry.org/ontology/occo.html) and Food [Ontology (FoodOn)](https://obofoundry.org/ontology/foodon.html)

* [Occupation Ontology (OccO)](https://obofoundry.org/ontology/occo.html) is a reference ontology in the domain of human occupations. It is designed to ontologize and harmonize the occupation classification from many existing occupation standards, including the US Bureau of Labor Statistics Standard Occupational Classification (US SOC), the International Standard Classification of Occupations (ISCO), the UK National Statistics Standard Occupational Classification (UK SOC), and the European Skills, Competences, Qualifications, and Occupations (ESCO) of the European Union. Currently, the ontology contains over 1,600 occupations, encompassing all US SOC occupations. In addition to occupations, the ontology also defines skills, abilities, and credentials highly related to the occupations. One ongoing OccO use case study aims to facilitate the Alabama government’s Talent Triad initiative, which connects individuals, employers, and credential providers using a common skills-based occupation framework. OccO was initiated by Sam Smith and Oliver He at the University of Michigan Medical School, Ann Arbor, MI, USA, in 2018, and since then has involved more ontology developers and domain experts from the University at Buffalo, Simon Fraser University, and the US Alabama Commission on Higher Education, among others. OccO has been presented at many meetings, including OSS2022, ICBO2022, and OSS2023. The ontology was accepted as a member of the OBO Foundry library ontologies in 2023. OccO is actively developing with weekly development calls and continuously seeks collaborators to contribute to the ontology.
* [Food Ontology (FoodOn)](https://obofoundry.org/ontology/foodon.html) is an ontology of over 35,000 classes focused primarily on naming kinds of food material for human and domesticated animal consumption. This includes both plant, animal and fungal material as well as inorganic chemicals.  Terms for many foundational “single organism” food materials include details of taxonomic category, anatomical part, and even life cycle. As well, thousands of common (non-brand name) multi-component food products are included. Vocabulary to describe food characteristics and processing steps, as well as other contextual facets to describe packaging, dietary pattern, nutritional term hierarchy, and agricultural source are provided. To maximize FAIR data interoperability, FoodOn imports from UBERON, the Plant Ontology, ENVO, ChEBI, the Ontology for Nutritional Studies, and the OBO Relations ontology, among others.  In addition to using FoodOn to describe food composition of meals in a “bag-of-terms'' way (FoodOn was derived from [LanguaL](https://www.langual.org), a longstanding food composition database thesaurus), the ontology can be used like a grammar to construct graph knowledge base statements about food which can be queried or reasoned with. For global resource integration, mapping to USDA nutrition [databases](https://fdc.nal.usda.gov/) such as Foundation Foods and SR Legacy is underway, as well as the European EFSA FoodEx2 vocabulary. For more information and opportunity to participate, see ongoing development and ontology design information at [www.foodon.org](https://www.foodon.org) and the [GitHub](https://github.com/FoodOntology/foodon/) repository.

---

## Members and Volunteers 

The OBO Foundry is honored to highlight two members who are making valuable contributions to our community: 

### Anita Caron

<img src="https://obofoundry.org/images/ofoc/anitacaron.png" height="200" alt="Anita Caron" />

Anita Caron has been a Semantic Web Developer at the European Bioinformatics Institute (EMBL-EBI) since 2021 as part of the Samples, Phenotypes, and Ontologies (SPOT) team. She is deeply involved in technical improvements across many ontologies, such as Uberon, Cell Ontology, and Relation Ontology (RO) which are crucial components to the Human Reference Atlas (HRA), part of the Human BioMolecular Atlas Program (HuBMAP). She also has contributed to developing the most recent versions of the Ontology Development Kit (ODK). Passionate about advancing metadata standardization, her contributions extend beyond ontology development, as she actively participates in organizing tutorials to educate and empower other ontology developers on best practices in metadata standardization and quality control. More details are in the section “Recent OBO Academy seminars”.

Anita holds an important role at OBO Foundry as the OBO Dashboard Maintainer. She is entrusted with the responsibility of maintaining and releasing the OBO Dashboard, a key resource for the community.


### Bill Duncan

<img src="https://obofoundry.org/images/ofoc/wdduncan.png" height="200" alt="Bill Duncan" />

Bill Duncan is an AI researcher and faculty member at the University of Florida College of Dentistry. He has been involved in the OBO Foundry for more than a decade and is the lead developer of the Oral Health Disease Ontology (OHD). In addition to the OHD, Bill has contributed to several OBO Foundry ontologies over the years, such as the Relation Ontology (RO), Environment Ontology (ENVO), Ontology for General Medical Science (OGMS), Ontology for Modeling and Representation of Social Entities (OMRSE), Occupation Ontology (OCCO), and the UBERON multi-species anatomy ontology (as well as others). He is also currently working on non-OBO Foundry ontologies. These include the Pain Ontology and the Neural Interface Ontology, an ontology for representing devices that augment the nervous system, such bionic vision devices and cochlear implants.

As a bioinformatician, Bill has been involved in a number of clinical studies in the dental and cancer domains. In the dental domain, he has been an innovator in the use of private-practice dental records to study dental treatment outcomes, such as root canals and tooth restorations. In the cancer domain, he has been involved in studies to assess the role that the circadian rhythm plays in mitigating oral mucositis in oral-cancer patients undergoing radiation therapy, and how variations in a patient’s chemotherapy regimen affects the treatment of ovarian cancer. Prior to joining the University of Florida, Bill was an ontologist and software developer for the National Microbiome Data Collaborative, which aims to promote microbiome research through the development of data standards that enable the sharing of microbiome research data.

Outside of work, Bill enjoys time with his family and plays a mean game of pickleball 😊


#### New Members of the OBO Operations Committee

In this issue we introduce two volunteers that recently joined the OBO Operations Committee. Welcome aboard Vinícius de Souza and James Stevenson! James will take over the role of OBO Website Coordinator from Erik Whiting who has served in that role for over a year now. Thank you for all your work, Erik!


<table>
  <tr>
   <td><strong>Picture</strong>
   </td>
   <td><strong>Name</strong>
   </td>
   <td><strong>GitHub</strong>
   </td>
   <td><strong>Affiliation</strong>
   </td>
   <td><strong>Country</strong>
   </td>
   <td><strong>Role</strong>
   </td>
  </tr>
  <tr>
   <td>

<img width="265" alt="image" src="https://github.com/LK112019/OBOFoundry.github.io/assets/7070631/87110291-66a2-4410-87b5-0ff965c59de3">


   </td>
   <td>Vinícius de Souza
   </td>
   <td>@souzadevinicius
   </td>
   <td>EMBL-EBI
   </td>
   <td>UK
   </td>
   <td>Technical Working Group OBO Operations - OBO Website
   </td>
  </tr>
  <tr>
   <td>

<img width="246" alt="image" src="https://github.com/LK112019/OBOFoundry.github.io/assets/7070631/6f5ec81d-f887-4b40-8d9e-a2dc56eb839a">


   </td>
   <td>James Stevenson
   </td>
   <td>@jsstevenson
   </td>
   <td>Nationwide Children’s Hospital (Columbus, OH) 
   </td>
   <td>USA
   </td>
   <td>OBO Website Coordinator
   </td>
  </tr>
</table>

---

## Spotlight on Research in the OBO community


### Dynamic Retrieval Augmented Generation of Ontologies using Artificial Intelligence ([DRAGON-AI](https://arxiv.org/abs/2312.10904))

This preprint introduces "Dynamic Retrieval Augmented Generation of Ontologies using AI ([DRAGON-AI](https://arxiv.org/abs/2312.10904))," a method that employs Large Language Models to automate the creation of ontological components. Aiming to simplify the complex process of ontology development in fields like biomedical and environmental sciences, DRAGON-AI was tested on ten diverse ontologies, showing its efficacy in producing accurate relationships and definitions. Despite its potential to streamline ontology construction, the research emphasizes the critical need for domain experts to refine AI-generated outputs to ensure their precision and reliability. Thus, DRAGON-AI marks a pivotal move towards blending AI with human expertise to facilitate more efficient and effective ontology maintenance and development. 

<img width="618" alt="image" src="https://github.com/LK112019/OBOFoundry.github.io/assets/7070631/57562806-c684-42e9-a7e8-c865239eabba">

**[Figure 1.](https://arxiv.org/abs/2312.10904)** DRAGON-AI approach 


### [Structured Prompt Interrogation and Recursive Extraction of Semantics (SPIRES): a method for populating knowledge bases using zero-shot learning](https://arxiv.org/abs/2304.02711)

The paper presents "SPIRES," a novel approach for populating knowledge bases using Large Language Models (LLMs) without needing extensive training data. Utilizing LLMs' zero-shot learning capabilities, SPIRES extracts information that fits a predefined knowledge schema through recursive structured prompting. This method enables the extraction of complex data structures and improves accuracy by aligning entities with existing ontologies. Demonstrated across various domains like food recipes and disease treatments, SPIRES offers accuracy comparable to traditional methods but excels in entity grounding. It highlights the method's flexibility, ease of use, and ability to adapt to new tasks, promoting LLMs' role in knowledge curation. SPIRES is part of the open-source [OntoGPT package](https://monarch-initiative.github.io/ontogpt/), facilitating its adoption and adaptation for different knowledge extraction tasks. This approach represents a significant step forward in using AI and NLP technologies to efficiently and accurately assemble knowledge bases, offering a scalable and adaptable tool for researchers and organizations dealing with large volumes of unstructured information.

<img width="549" alt="image" src="https://github.com/LK112019/OBOFoundry.github.io/assets/7070631/04d7c759-cb9c-4377-956f-df5a9a43b009">

**[Figure 1.](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btae104/7612230?login=false)** Overview of the SPIRES approach. . 

---

## Spotlight on OBO Principles 

In this issue, we continue with [Principle 3](https://obofoundry.org/principles/fp-003-uris.html) of the OBO Foundry's series of principles. 

The OBO Foundry emphasizes the importance of interoperability by requiring ontologies to use standardized IRIs, as outlined in [Principle 3](https://obofoundry.org/principles/fp-003-uris.html). This ensures ontologies are easily accessible and identifiable on the web, promoting seamless integration and use across different platforms and systems.

### OBO Foundry Principle 3: URI/Identifier Space:

The OBO Foundry insists on unique IRIs, designated as PURLs, to ensure ontologies are easily identifiable and accessible online, incorporating approved, concise namespaces. 

This requirement facilitates the prompt identification of ontology elements, in line with OBO Foundry's [ID policy](http://obofoundry.org/id-policy), enhancing standardization and web presence of ontological data. Compelling proper IRI structures for ontologies and their components highlights the criticality of adhering to established guidelines. 

An automated verification mechanism checks that namespaces are duly registered and IRIs precisely follow specified formats, supporting consistency and ensuring broad compliance across the ontological spectrum.

---

## Spotlight on Tools

A [major release (1.5) of the Ontology Development KIT (ODK)](https://github.com/INCATools/ontology-development-kit/releases/tag/v1.5) was published after more than a year of development, with significant contributions from members of the OBO Technical Working group ([Blog post](https://monarchinit.medium.com/automating-the-ontology-lifecycle-version-1-5-of-the-odk-e196a8d87936)). Some highlights include the introduction of the “International Release” and a complete workflow system for ontology internationalization, the redefinition of “Base Release”, a fundamental piece of our vision for decentralized ontology development and added support for ROBOT plugins, which supports the inclusion of custom ROBOT plugins in your ODK workflows. 

---

## Events

### [OBO Academy: Monarch Seminar Series](https://oboacademy.github.io/obook/courses/monarch-obo-training/) (ongoing)


* Tutorial 2024/04/02: Synonym Type curation - a deep dive 
* Tutorial 2024/04/16: AI-assisted ontology editing workflows 2

Don’t forget you can vote for future training topics here: [https://github.com/OBOAcademy/obook/discussions/categories/tutorial-requests](https://github.com/OBOAcademy/obook/discussions/categories/tutorial-requests)


### Recent OBO Academy seminars

* Harry Caufield from Lawrence Berkeley National Laboratory discussed the Bridge to AI ([Bridge2AI](https://www.youtube.com/watch?v=zaZtcDbjqTw)) data standards developed to make biomedical and biological data AI-ready. He covered the challenges in determining data AI-readiness, the Bridge2AI standards registry using LinkML, the importance of structuring data and metadata, the development of the "Data Sheets for Datasets" (D4D) schema, efforts to align Bridge2AI standards with existing standards, and suggestions for biocurators and ontologists to contribute to making data AI-ready. The presentation emphasized the importance of developing standards and tools to unify data attributes, making data more accessible, reliable, and suitable for AI-driven methods in biomedicine. The tutorial was called “Bridge2AI data standards: a practical introduction” and the recording can be accessed [here](https://www.youtube.com/watch?v=zaZtcDbjqTw).
* In this OBO Academy training session, Anita Caron from EMBL-EBI presented the importance of ontology metadata standardization for building an interoperable knowledge graph in the biological and biomedical domains. She highlighted the challenges of integrating diverse ontologies and the need to use standardized annotation properties. She introduced tools for ontology metadata validation, such as ROBOT reports, custom SPARQL queries, and the OAK Validate tool. Anita also discussed the Ontology Metadata Model, a LinkML schema for the ontology metadata. She emphasized the need for further discussion and agreement on metadata standardization practices within the OBO community to enable development of interoperable ontologies for the life sciences. The tutorial was called “Ontology Metadata Standardisation” and the slides can be accessed [here](https://docs.google.com/presentation/d/12ig7zQ9R4lQAybuTQKb73gB22pIq5MEaowwbYOl5Ei8/edit#slide=id.g2ba19fa145d_0_5). The recording is [here](https://www.youtube.com/watch?feature=shared&v=tso8zawC3Tw).
* Chris Mungall demonstrated AI-assisted ontology editing workflows using large language models (LLMs) like ChatGPT and Claude. He showcased capabilities such as review-based workflows to identify errors, enhancement workflows to fill in missing information, and utilizing plugins for generating ontology terms and searching the literature. Chris discussed the pros and cons of LLMs in ontology curation, the need for human oversight, and the potential of using tools like [Curate GPT](https://curategpt.io/) to improve reliability. The presentation encouraged the OBO community to explore and share experiences in this emerging field. The tutorial was called “AI-assisted ontology editing workflows, Part 1” and the slides can be accessed [here](https://docs.google.com/presentation/d/13Hlm-iJo7a1NAaUqLsrUlbn-tLUVbF25WBjwAgIuLdA/edit#slide=id.g24560ef6bb7_0_84). The recording is [here](https://www.youtube.com/watch?v=wGoGr2dmxZI).


### Updates on past events

* The [17th Annual International Biocuration Conference](https://ibdc.rcb.res.in/biocuration2024/) was held in Faridabad, India from March 5-8th, 2024. Several active members of the OBO community attended the event, as well as a large delegation of Indian researchers and students who use OBO Foundry ontologies in their work. Many of the Indian delegates work in agriculture and crop sciences and use OBO Foundry ontologies for the annotation of genotypes, metabolites, and phenotypes in their work to increase crop yields, nutritional value, and decrease disease. Charles Tapley Hoyt wrote a blog post ([https://cthoyt.com/2024/03/11/biocuration2024-discussions.html](https://cthoyt.com/2024/03/11/biocuration2024-discussions.html)) summarizing some of his personal experiences at the conference. \

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
