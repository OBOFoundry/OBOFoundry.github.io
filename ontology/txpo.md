---
layout: ontology_detail
id: txpo
title: Toxic Process Ontology
browsers:
- title: BioPortal Browser
  label: BioPortal
  url: http://bioportal.bioontology.org/ontologies/TXPO?p=classes
- title: TOXPILOT
  label: TOXPILOT
  url: https://toxpilot.nibiohn.go.jp/
contact:
  email: yuki.yamagata@riken.jp
  github: yuki-yamagata
  label: Yuki Yamagata
  orcid: 0000-0002-9673-1283
description: TOXic Process Ontology (TXPO) systematizes a wide variety of terms involving toxicity courses and processes. The first version of TXPO focuses on liver toxicity.
domain: chemistry and biochemistry
homepage: https://toxpilot.nibiohn.go.jp/
license:
  label: CC BY 3.0
  url: https://creativecommons.org/licenses/by/3.0/
preferredPrefix: TXPO
products:
- id: txpo.owl
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/32883995
  title: Ontological approach to the knowledge systematization of a toxic process and toxic course representation framework for early drug risk management
repository: https://github.com/txpo-ontology/TXPO
tags:
- toxicity
tracker: https://github.com/txpo-ontology/TXPO/issues
activity_status: active
---

Elucidating the mechanism of toxicity is crucial in drug safety evaluations. TOXic Process Ontology (TXPO) systematizes a wide variety of terms involving toxicity courses and processes. The first version of TXPO focuses on liver toxicity.
The TXPO contains an is-a hierarchy that is organized into three layers: the top layer contains general terms, mostly derived from the Basic Formal Ontology. The intermediate layer contains biomedical terms in OBO foundry, and the lower layer contains toxicological terms.

In applied work, we have developed a prototype of TOXPILOT, a TOXic Process InterpretabLe knOwledge sysTem. TOXPILOT provides visualization maps of the toxic course, which facilitates capturing the comprehensive picture for understanding toxicity mechanisms.
A prototype of TOXPILOT is available:  https://toxpilot.nibiohn.go.jp
