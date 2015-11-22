---
layout: ontology_detail
id: eco
description: An ontology for experimental and other evidence statements.
domain: experiments
homepage: https://github.com/evidenceontology/evidenceontology/
tracker: https://github.com/evidenceontology/evidenceontology/issues
products:
  - id: eco.owl
  - id: eco.obo
title: Evidence ontology
jobs:
  - id: https://travis-ci.org/evidenceontology/evidenceontology
    type: travis-ci
build:
  notes: switch to vcs
  source_url: https://raw.githubusercontent.com/evidenceontology/evidenceontology/master/eco.obo
  method: obo2owl
  infallible: 1
contact:
  email: MChibucos@som.umaryland.edu
  label: "Chibucos, Marcus" 
publications:
  - id: http://www.ncbi.nlm.nih.gov/pubmed/25052702
    title: "Standardized description of scientific evidence using the Evidence Ontology (ECO)"
funded_by:
  - "http://www.nsf.gov/awardsearch/showAward?AWD_ID=1458400"
---

<img src="https://avatars1.githubusercontent.com/u/12802432" alt="ECO logo"/>

The Evidence Ontology (EO) describes types of scientific evidence within the realm of biological research that can arise from laboratory experiments, computational methods, manual literature curation, and other means. Researchers can use these types of evidence to support assertions about things (such as scientific conclusions, gene annotations, or other statements of fact) that result from scientific research.

EO comprises two high-level classes, evidence and assertion method, where evidence is defined as “a type of information that is used to support an assertion,” and assertion method is defined as “a means by which a statement is made about an entity.” Together evidence and assertion method can be combined to describe both the support for an assertion and whether that assertion was made by a human being or a computer. However, EO can not be used to make the assertion itself; for that, one would use another ontology, free text description, or some other means.

EO was originally created around the year 2000 to support gene product annotation by the Gene Ontology, which now uses EO in AmiGO 2. Today EO is used by many groups concerned with provenance in scientific research. 

***
For **advice on requesting new terms**, please see **[the Evidence Ontology wiki](https://github.com/evidenceontology/evidenceontology/wiki/New-term-request-how-to)**.

For **further information** visit the **[Evidence Ontology website](http://www.evidenceontology.org/)**.

Please **cite** the following paper: [Chibucos MC, Mungall CJ, Balakrishnan R, Christie KR, Huntley RP, White O, Blake JA, Lewis SE, and Giglio M. (2014) **Standardized description of scientific evidence using the Evidence Ontology (ECO)**. _Database_. Vol. **2014**: article ID bau066.](http://database.oxfordjournals.org/content/2014/bau075.long)

This work is made possible by **[award number 1458400](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1458400)** from the **US National Science Foundation's Division of Biological Infrastructure**.
