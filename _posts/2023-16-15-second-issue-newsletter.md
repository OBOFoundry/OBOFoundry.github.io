---
layout: post
categories: newsletter
title: "OBO Foundry Newsletter issue 2"
date: 2023-09-15
author:
  - Leila Kiani
---


Welcome to the second issue of the OBO Foundry Newsletter! We are delighted to continue our journey of advancing bio-ontologies and promoting enhanced data integration within our community. From general announcements to training opportunities and event updates, we strive to keep you up-to-date with the latest advancements and activities within the OBO Foundry.

One of our primary goals is to foster collaboration and celebrate the contributions of our community members. In this edition, we will shine a spotlight on some of our current members, highlighting their achievements and fostering a sense of connection and cooperation.

We encourage you to share your thoughts and ideas with the OBO Operations Committee, as your feedback helps shape the future of the OBO Foundry.

Thank you for being part of our community. We hope you enjoy this second edition and find it enriching and informative.

Best regards, [The OBO Foundry Operations Committee.](https://obofoundry.org/docs/OperationsCommittee.html)

---

## In Memoriam: Remembering Michael Ashburner

<img src="https://obofoundry.org/images/ashburner.jpg" style="height: 250px" alt="Michael Ashburner" />

We bid farewell to Michael Ashburner, a distinguished biologist and an unwavering advocate for open science. Ashburner, a pioneering figure in genetics, bioinformatics, and the OBO Foundry, passed away on July 10, 2023, at 81. His visionary leadership at EMBL-EBI left an indelible mark on bioinformatics. He sequenced the Drosophila genome, co-founding FlyBase and shaping ontologies like GO and ChEBI. Advocating for open science, he championed genome accessibility and open publishing. Honored with awards such as the Gregor Mendel Medal, his legacy inspires future scientists. Our heartfelt condolences go out to his family, friends, and colleagues.

 [The OBO Foundry Operations Committee.](https://obofoundry.org/docs/OperationsCommittee.html)

---

## Highlights

### Passing the OBO Dashboard will become mandatory on January 1<sup>st</sup> 2024

On January 1<sup>st</sup>, 2024, OBO Foundry will add a visual indicator to the [https://obofoundry.org/](https://obofoundry.org/) home page ontology list that shows each ontology’s compliance state (compliant / noncompliant) with respect to the dashboard report provided at http://dashboard.obofoundry.org/dashboard/index.html. Non-compliant ontologies will be sorted to the bottom of their default ontology-by-topic view group, and shaded. This is a purely informative indicator to enable OBO users to be aware of certain quality and maintenance issues that may affect their reuse plans; as well, it encourages ontology curators to strive for greater quality control excellence. Some key points:

Only dashboard (black X on a red background) errors cause non-compliance. Warnings (yellow triangle) or information (blue i) in the final “Summary” column are ok.

An explanation of the dashboard report is available here ([link to dashboard video](https://youtu.be/m2khZcJVKU0?feature=shared&t=1319)).

The “Maintained” column is dedicated to indicating recent updates to content in the ontology, and has been changed to avoid an error state. A warning is shown for [inactivity](https://obofoundry.org/docs/OntologyStatus.html) beyond 2 years; an information icon is provided for 1-2 year [inactivity](https://obofoundry.org/docs/OntologyStatus.html). Note that the [OBO Maintenance principle](https://obofoundry.org/principles/fp-016-maintenance.html) also asks that each ontology keep up to date with scientific consensus about its content, but this is not evaluated in the dashboard.

Moving forward, we will provide some guidance on how to pass specific errors on the OBO Dashboard. In this issue, we will explain how to pass the “Open” principle. For details, see “Spotlight on OBO Principles”.

---

## Decisions Made and Important Updates

* All terms in New Ontology Requests MUST follow the OBO identifier scheme (often they are accidentally written wrongly, e.g. using https instead of http). There MUST NOT be a term with the same meaning available in another OBO Foundry ontology, ie there must not be a term referring to a concept that already exists in another OBO Foundry ontology (whether or not the label is identical). There SHOULD NOT be another OBO Foundry ontology whose scope covers any of the new terms. See [Standard Operating Procedures](https://obofoundry.org/docs/SOP.html#ROOM).
* NCIT does NOT count when term overlap with other ontologies is determined. This is relevant because new ontologies are not allowed to create new terms for concepts that already exist in OBO. [See meeting of 27th June 2023](https://docs.google.com/document/d/1qhLFQL5IzTMUIBOtxJ5AqaEHcOCOQgNeXfvAb5O5P0A/edit).
* [Ontologies which redirect to OLS are now redirecting to OLS4.](https://github.com/OBOFoundry/purl.obolibrary.org/pull/922)

---

## Ongoing Discussions

Here, we list some of the more important discussions happening around the OBO-sphere:

* The OBO community discusses the best approach to managing COB identifiers (IDs) and mappings. The discussion revolves around the question of whether COB should mint new identifiers in the COB namespace, or re-use identifiers from existing OBO ontologies. Both have advantages and disadvantages. [Join the discussion.](https://github.com/OBOFoundry/COB/issues/244)
* This year, we have frequently stumbled across the question of whether an OBO ontology needs to be somehow related to the Biomedical or Biological domain or not. [Give us your opinion!](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1918)

---

## Ontologies

In this edition of the OBO newsletter, we will explore aspects of the [procedure for requesting the inclusion of a new ontology in the OBO Foundry](https://obofoundry.org/faq/how-do-i-register-my-ontology.html). Today, we will talk about clearly defining the ontology’s purpose and scope.

### Clearly define the ontology's purpose and scope.

Clearly defining the purpose and scope of the ontology is a crucial step when submitting a new ontology to the OBO Foundry. This should include the ontology's goals, intended applications, and the domain it covers. By articulating the purpose, developers highlight the objectives and benefits for the scientific community, along with potential use cases. Defining the scope entails specifying the aspects of the domain that the ontology will address and what it won't cover while considering the appropriate level of detail. This information enables reviewers to assess the ontology's relevance, significance, and potential impact, ensuring alignment with the OBO Foundry's goals. A well-defined purpose and scope increase the chances of acceptance and integration into the suite of OBO Foundry ontologies.

### New Ontology requests

* [The Occupation Ontology (OccO)](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2428) was recently submitted for inclusion in the OBO Foundry ontologies. The OccO developers actively communicate with OBO Foundry operations members to ensure the ontology adheres to OBO Foundry principles.
OccO provides an initial ontological representation of occupational information from the United States Department of Labor's Standard Occupational Classification (SOC) system, as enhanced by the O*Net system. These occupational taxonomies are developed through a collaboration between the Department of Labor, Bureau of Labor Statistics, and the O*Net Program - the primary source of occupational data in the United States.
In line with OBO Foundry guidelines, OccO reflects the 2019 O*Net-SOC taxonomy based on the 2018 SOC. The underlying O*Net data is provided by the U.S. Department of Labor Employment and Training Administration (USDOL/EGA).

### Spotlight on Ontologies

In this issue, we would like to highlight three ontologies from the OBO Foundry family: the [Human Phenotype Ontology (HPO)](https://obofoundry.org/ontology/hp.html), the [Cell Ontology (CL)](https://obofoundry.org/ontology/cl.html), and the [Ontology for Biomedical Investigations (OBI)](https://obofoundry.org/ontology/obi.html).

* [Ontology for Biomedical Investigations (OBI)](https://obofoundry.org/ontology/obi.html) provides a comprehensive framework for describing biological and clinical investigations. It encompasses various aspects of biomedical research, such as assays (covering all aspects of data generation), material processing, devices, protocols, data, and analysis methods. The latest OBI release includes over 4,000 terms, and re-uses key terms and relationships from other OBO ontologies wherever possible to connect aspects of an investigation to the biomedical terms in other OBO ontologies. OBI was founded in 2006 as a merger of several previous efforts focusing on specific individual experimental techniques (e.g. genomics, proteomics). OBI development has been driven by the specific needs of individual projects, and thus provides more detailed coverage in areas relevant to those projects. OBI continuously seeks input and contributions to broaden this coverage, and welcomes new members to join the active and open weekly development calls.
* [Human Phenotype Ontology](https://obofoundry.org/ontology/hp.html) (HPO) is an ontology developed by the Monarch Initiative used to describe human phenotypic abnormalities seen in genetic disorders and clinical research. It provides a structured representation of abnormal characteristics associated with diseases. HPO helps researchers and clinicians share and integrate phenotypic data, making understanding and diagnosing genetic disorders easier. It uses a hierarchical organization and semantic relationships between terms and allows for annotation of genes and diseases. HPO is used in multiple diagnosis and variant prioritization tools, aiding healthcare professionals and researchers in identifying and classifying genetic conditions. Recently, HPO has released an international edition which covers different languages such as Chinese, Turkish, Japanese, Spanish and Czech ([https://obophenotype.github.io/hpo-translations/](https://obophenotype.github.io/hpo-translations/)). The translations are displayed in the HPO browser (e.g. [https://hpo.jax.org/app/browse/term/HP:0001166](https://hpo.jax.org/app/browse/term/HP:0001166)) and OLS ([https://www.ebi.ac.uk/ols4/ontologies/hp](https://www.ebi.ac.uk/ols4/ontologies/hp)).
* [Cell Ontology (CL)](https://obofoundry.org/ontology/cl.html) is an ontology designed to classify and describe cell types across different organisms. It serves as a resource for model organism and bioinformatics databases. The ontology covers a broad range of cell types in animal cells, with over 2700 cell type classes, and provides high-level cell type classes as mapping points for cell type classes in ontologies representing other species, such as the Plant Ontology or Drosophila Anatomy Ontology. Integration with other ontologies such as Uberon, GO, CHEBI, PR, and PATO enables linking cell types to anatomical structures, biological processes, and other relevant concepts. The Cell Ontology was created in 2004 and has been a core OBO Foundry ontology since the start of the Foundry. Since then, CL has been adopted by various efforts, including the HuBMAP project, Human Cell Atlas (HCA), cellxgene platform, Single Cell Expression Atlas, BRAIN Initiative Cell Census Network (BICCN), ArrayExpress, The Cell Image Library, ENCODE, and FANTOM5, for annotating cell types and facilitating cellular reference mapping, as documented through various publications and examples.

---

## Members and Volunteers

### Member Spotlight:

We are delighted to feature two OBO Foundry members in this month's spotlight! Let us introduce you to Darren Natale and Chris Stoeckert, both of whom have made outstanding contributions to our community.

**Darren Natale**

<img src="https://obofoundry.org/images/ofoc/nataled.png" style="height: 250px" alt="Darren Natale" />

A member of the faculty at Georgetown University Medical Center (Washington, DC, USA) and the Protein Information Resource (headed by Dr. Cathy Wu) since 2002, Darren Natale obtained his PhD in Biology at the University of Buffalo (NY, USA) in 1993. A molecular biologist by training (specializing in the field of DNA replication), Darren began his foray into bioinformatics when he joined the then-recently-established COG protein classification project at NCBI as a curator in 1999. In 2002 he brought his classification expertise to GUMC/PIR for the then-new UniProt project. In 2006 he became interested in working with ontologies, and shortly thereafter joined the OBO Foundry. He is the manager of the Protein Ontology project, which provides an ontological representation of protein-related entities (principally, post-translationally modified proteoforms). Currently, his collaborations include the aforementioned UniProt and PRO, and the Pathways2GO project. He also leads a collaborative project designed to make IEDB epitope data widely available in UniProtKB, PRO, and iPTMnet. Along with participating in the development of several other ontologies, his principal contribution to the OBO Foundry is as an inaugural member of the OBO Foundry Operations Committee, and as long-time chair of the Editorial Working Group. His favorite aspects of working with the OBO Foundry community are the collaborative way challenges to ontological modeling are met, and the often spirited but always informative discussions.

**Chris Stoeckert**

<img src="https://obofoundry.org/images/cstoeckert.png" style="height: 250px" alt="Chris Stoeckert" />

Before retiring at the end of 2022, Chris Stoeckert, Ph.D., was a Research Professor of Genetics at the Institute of Biomedical Informatics at the University of Pennsylvania; he is now an adjunct professor at Penn. Originally a biophysicist and then a molecular and cell biologist, he spent most of his career working on databases supporting the mining of complex datasets. These have included databases on gene expression, orthologous proteins, pancreatic development, Alzheimer’s Disease genomics, and multiple resources associated with the NIAID VEuPathDB Bioinformatic Research Center supporting research on eukaryotic pathogens (e.g., PlasmoDB) and vectors. The database work led to involvement in the development of data standards such as MIAME (Minimal Information About a Microarray Experiment), MAGE-TAB format standard for reporting microarray experiments, and the development of biomedical ontologies such as the MGED Ontology. Chris is a founder and developer of the Ontology for Biomedical Investigations (OBI), has led the development of the Ontology for Biobanking (OBIB), and contributed to a variety of ontologies in the OBO Foundry. Most recently, he applied ontologies for integration and harmonization of clinical data using semantic graphs in the TURBO (Transforming & Unifying Research with Biomedical Ontologies) project at Penn. He has served on the OBO Foundry Operations Committee and participated in the Editorial Working Group. Chris has enjoyed watching the OBO Foundry grow from its beginnings and is excited about its future with the influx of new members and technology.

---

## Spotlight on OBO Principles

The OBO Foundry has developed a series of principles that represent best practices for usable, sustainable, interoperable ontologies and serve as criteria for evaluating the potential inclusion of new ontologies. In this newsletter, we will discuss each of these principles, starting with Principle 1 in this issue.

"[The OBO Foundry: Coordinated Evolution of Ontologies to Support Biomedical Data Integration](https://www.nature.com/articles/nbt1346)" is the publication that lays the groundwork for the OBO Foundry's principles. It focuses on the collaborative development of ontologies to enhance biomedical data integration. This paper discusses how the OBO Foundry plays an important role in facilitating a unified approach to managing biomedical information by establishing a framework for consistent and interoperable ontologies.

### [Principle: Open (principle 1):](http://obofoundry.org/principles/fp-001-open.html)

OBO Foundry Principle 1 emphasizes open access of ontologies in the biological and biomedical domains. It mandates free availability for all users, with only origin acknowledgment and alteration constraints. The aim is to establish OBO Foundry ontologies as shared resources, benefiting the wider community. This principle aligns with fostering interoperable ontologies and encourages term reuse. The principle description outlines recommendations for ontology providers and re-users, establishing responsible sharing and usage practices. This principle sets a strong foundation for collaborative growth and knowledge exchange in biology and biomedicine.

#### How to Pass Open Principle on the OBO Dashboard

The Open Principle can be violated by missing an open license or when the ontology license differs from the one registered in the OBO Foundry. An OBO Foundry ontology must have either an equivalent or less restrictive license than [Creative Commons Attribution 3.0 Unported (CC BY 3.0)](https://creativecommons.org/licenses/by/3.0/). More information on the license type can be found in the [Recommendations and Requirements section](https://obofoundry.org/principles/fp-001-open.html#recommendations) on the principle description page. To resolve this problem, you must include the corresponding axiom based on the ontology serialisation used.

For an ontology serialized in RDF/XML:

```
<dcterms:license rdf:resource="http://creativecommons.org/licenses/by/4.0/"/>
```

For an ontology serialized in OBO:

```
property_value: http://purl.org/dc/terms/license http://creativecommons.org/licenses/by/4.0/
```

The use of the annotation property [http://purl.org/dc/terms/license](http://purl.org/dc/terms/license) is mandatory. For more information on the dashboard and passing the principles, refer to this [YouTube video](https://www.youtube.com/watch?feature=shared&t=1319&v=m2khZcJVKU0).

It is essential to use the same license to ensure consistency and clarity within the ontology and its representation in the OBO Foundry registry. This approach ensures that users and contributors can easily comprehend and follow the ontology's usage and distribution terms and conditions. Kindly [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%231+%22Open%22+%3CENTER+ISSUE+TITLE%3E) to update it in the OBO Foundry registry.

---

## Spotlight on Software Tools

Starting from this issue, we spotlight essential software tools that form the foundation of the Open Biomedical Ontologies (OBO) Foundry community. These tools play a central role in facilitating collaboration, upholding data integrity, and editing and validating ontologies. The table below lists some of the tools that are frequently used by (and, in some cases, developed by) members of the OBO Foundry community.

| Software Package          | Links                                           | Language(s)  | Core Features                                                                                                                                                                         |
|---------------------------|-------------------------------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| curies / curies4j         | cthoyt/curies, cthoyt/curies4j                  | Python, Java | The core library for conversion between URIs and Compact URIs (CURIEs). An essential addon for all Semantic Software Engineers.                                                       |
| ROBOT                     | https://github.com/ontodev/robot                | Java, CLI    | The Swiss Army Knife of Ontology Engineering. Transform your ontologies, manage them with templates and check them for errors! A must have for all ontology engineers!                |
| Ontology Access Kit (OAK) | https://incatools.github.io/ontology-access-kit | Python       | User-facing Python library and CLI tool suite for accessing ontologies, including visualization, mapping and annotation. Indispensable for data scientists that work with ontologies. |
   
---

## Events

### International Society for Biocuration Annual General Meeting: 18 October 2023, 8-9:30am PT

[The International Society for Biocuration](https://www.biocuration.org/) will host their Annual General Meeting to update community members on happenings in the Society over the past year. This webinar will include talks by the 2023 Excellence in Biocuration Award Winners, **Charles Tapley Hoyt**, Laboratory of Systems Pharmacology Harvard Medical School, MA, USA, winner of the **Early Career Award** (talk abstract is [here](https://www.biocuration.org/democratizing-biocuration-or-how-i-learned-to-love-the-drive-by-curation/)) and **Nicolas Matentzoglu**, Monarch Initiative, Semanticly, Greece, winner of the **Advanced Career Award** (talk abstract is [here](https://www.biocuration.org/closing-the-gap-between-effective-biocuration-and-meaningful-ontology-evolution/)). More information about their awards is available [here](https://www.biocuration.org/democratizing-biocuration-or-how-i-learned-to-love-the-drive-by-curation/): [https://www.biocuration.org/announcement-for-2023-winners-of-excellence-in-biocuration-awards](https://www.biocuration.org/announcement-for-2023-winners-of-excellence-in-biocuration-awards)/. To join the webinar, please fill out this [registration form](https://docs.google.com/forms/d/e/1FAIpQLSd2d4F6P0_72urLpwKGDZZrK2r4wctXSXYkOVlF0gt02CtPpA/viewform).

### [OBO Academy: Monarch Seminar Series](https://oboacademy.github.io/obook/courses/monarch-obo-training/) (ongoing)

Monarch OBO Training is a virtual training session that is offered biweekly on Tuesdays at 9 am PT/12 pm ET; it provides semantic engineering training targeted towards members of the Monarch Initiative and OBO community (all are welcome to participate). The sessions focus on various relevant topics which are outlined here: [https://oboacademy.github.io/obook/courses/monarch-obo-training/#schedule](https://oboacademy.github.io/obook/courses/monarch-obo-training/#schedule).

Recent Monarch Training topics have included:

* [How to determine if two entities are the same](https://github.com/OBOAcademy/obook/issues/424)?
* Modern prefix management with Bioregistry and curies, led by Charlie Hoyt

Don't forget you can vote for future training topics here: [https://github.com/OBOAcademy/obook/discussions/categories/tutorial-requests](https://github.com/OBOAcademy/obook/discussions/categories/tutorial-requests)

Updates on past events

* The OBO Technical Working group presented various OBO tools and practices at the [Ontology Summit 2023](https://ontologforum.com/index.php/Special:WhatLinksHere/OntologySummit2023). The Ontology Summit 2023 recordings are available in the [Ontology Summit YouTube Channel.](https://www.youtube.com/channel/UCKK2e8NZ9lyLDBpXY18O_Tg)
* The OBO Academy team presented the OBO Training at ICBO 2023 this year.
    * Info: https://oboacademy.github.io/obook/courses/icbo2023/
    * Recording: [Part 1](https://www.youtube.com/watch?v=83lI3u7KX0g), [Part 2](https://www.youtube.com/watch?v=m2khZcJVKU0)

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
* If you want to take your contributions to OBO Foundry to the next level, you can [nominate yourself to be considered for the OBO Operations Committee](https://obofoundry.org/docs/NewOBOFC.html). There are various roles in which you can contribute, including assisting with the production of this newsletter.
