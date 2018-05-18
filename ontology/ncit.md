---
layout: ontology_detail
id: ncit
title: NCI Thesaurus OBO Edition
contact:
  email: haendel@ohsu.edu
  label: Melissa Haendel
license:
  url: https://creativecommons.org/licenses/by/3.0/
  label: CC-BY 3.0
homepage: https://github.com/NCI-Thesaurus/thesaurus-obo-edition
tracker: https://github.com/NCI-Thesaurus/thesaurus-obo-edition/issues
description: The NCI Thesaurus (NCIt) OBO Edition project aims to increase integration of the NCIt with OBO Library ontologies. NCIt is a reference terminology that includes broad coverage of the cancer domain, including cancer related diseases, findings and abnormalities. NCIt OBO Edition releases should be considered experimental.
products:
  - id: ncit.owl
    title: NCIt OBO Edition OWL format
    description: "A direct transformation of the standard NCIt content using OBO-style term and ontology IRIs and annotation properties."
  - id: ncit.obo
    title: NCIt OBO Edition OBO format
  - id: ncit/ncit-plus.owl
    title: NCIt Plus
    description: "This version replaces NCIt terms with direct references to terms from other domain-specific OBO Library ontologies (e.g. cell types, cellular components, anatomy), supporting cross-ontology reasoning. The current release incorporates CL (cell types) and Uberon (anatomy)."
    mireots_from: cl
    mireots_from: uberon
  - id: ncit/neoplasm-core.owl
    title: NCIt Plus Neoplasm Core
    description: "This is a subset extracted from NCIt Plus, based on the [NCIt Neoplasm Core value set](https://evs.nci.nih.gov/ftp1/NCI_Thesaurus/Neoplasm/About_Core.html) as a starting point."
license:
  url: ftp://ftp1.nci.nih.gov/pub/cacore/EVS/NCI_Thesaurus/ThesaurusTermsofUse.pdf
  label: See document
---

The NCI Thesaurus is an ontology-like vocabulary that includes broad
coverage of the cancer domain, including cancer related diseases,
findings and abnormalities; anatomy; agents, drugs and chemicals;
genes and gene products and so on. In certain areas, like cancer
diseases and combination chemotherapies, it provides the most granular
and consistent terminology available. It combines terminology from
numerous cancer research related domains, and provides a way to
integrate or link these kinds of information together through semantic
relationships.

The Thesaurus currently contains over 34,000 concepts, structured into
20 taxonomic trees. The NCI Thesaurus provides concept history tables
to record changes in the vocabulary over time as the science
changes. Within NCI, the Thesaurus is used to provide terminology
support to the Institutes public Web portal, <a
href="http://cancer.gov/">http://cancer.gov</a>, numerous portals
supporting consortia and other communities of researchers, and is used
in the caCORE as the semantic base for metadata and objects that form
the infrastructure upon which the NCICB portals are built (see <a
href="http://ncicb.nci.nih.gov/">http://ncicb.nci.nih.gov</a>). It is
published under an open content license in a number of formats
including OWL.
