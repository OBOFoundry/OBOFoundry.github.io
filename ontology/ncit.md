---
layout: ontology_detail
id: ncit
title: NCI Thesaurus OBO Edition
contact:
  email: haendel@ohsu.edu
  github: mellybelly
  label: Melissa Haendel
  orcid: 0000-0001-9114-8737
description: NCI Thesaurus (NCIt)is a reference terminology that includes broad coverage of the cancer domain, including cancer related diseases, findings and abnormalities. The NCIt OBO Edition aims to increase integration of the NCIt with OBO Library ontologies. NCIt OBO Edition releases should be considered experimental.
domain: health
homepage: https://github.com/NCI-Thesaurus/thesaurus-obo-edition
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: NCIT
products:
- id: ncit.owl
  title: NCIt OBO Edition OWL format
  description: A direct transformation of the standard NCIt content using OBO-style term and ontology IRIs and annotation properties.
- id: ncit.obo
  title: NCIt OBO Edition OBO format
- id: ncit/ncit-plus.owl
  title: NCIt Plus
  description: This version replaces NCIt terms with direct references to terms from other domain-specific OBO Library ontologies (e.g. cell types, cellular components, anatomy), supporting cross-ontology reasoning. The current release incorporates CL (cell types) and Uberon (anatomy).
  mireots_from:
  - cl
  - uberon
- id: ncit/neoplasm-core.owl
  title: NCIt Plus Neoplasm Core
  description: This is a subset extracted from NCIt Plus, based on the [NCIt Neoplasm Core value set](https://evs.nci.nih.gov/ftp1/NCI_Thesaurus/Neoplasm/About_Core.html) as a starting point.
repository: https://github.com/NCI-Thesaurus/thesaurus-obo-edition
tracker: https://github.com/NCI-Thesaurus/thesaurus-obo-edition/issues
activity_status: active
---

The NCI Thesaurus is a reference terminology that includes broad
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
href="http://ncicb.nci.nih.gov/">http://ncicb.nci.nih.gov</a>).

The NCI Thesaurus is released under the Creative Commons Attribution 4.0
International license (CC BY 4.0). The NCI Thesaurus is produced by the
Enterprise Vocabulary Services group of the Center for Biomedical
Informatics and Information Technology, National Cancer Institute, Maryland,
USA. The name "NCI Thesaurus" is trademarked. Only the NCI Thesaurus
published by the NCI can be released under this name (see
ftp://ftp1.nci.nih.gov/pub/cacore/EVS/NCI_Thesaurus/ThesaurusTermsofUse.htm).
