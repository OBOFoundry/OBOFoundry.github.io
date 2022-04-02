---
layout: ontology_detail
id: eco
description: An ontology for experimental and other evidence statements.
domain: investigations
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
  email: mgiglio@som.umaryland.edu
  label: Michelle Giglio
  github: mgiglio99
  orcid: 0000-0001-7628-5565
publications:
  - id: http://www.ncbi.nlm.nih.gov/pubmed/30407590
    title: "ECO, the Evidence & Conclusion Ontology: community standard for evidence information."
  - id: http://www.ncbi.nlm.nih.gov/pubmed/25052702
    title: "Standardized description of scientific evidence using the Evidence Ontology (ECO)"
license:
  url: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
funded_by:
  - "http://www.nsf.gov/awardsearch/showAward?AWD_ID=1458400"
usages:
  - user: http://geneontology.org
    type: annotation
    description: ECO is used by the GO consortium for evidence on GO associations
    examples:
      - url: http://amigo.geneontology.org/amigo/term/GO:0055085
        description: annotations to transmembrane transport
  - user: https://monarchinitiative.org/
    type: annotation
    description: ECO is used by the Monarch Initiative for evidence types for disease to phenotype annotations.
    examples:
      - url: https://monarchinitiative.org/phenotype/HP%3A0001300#disease
        description: "Parkinsonism: Characteristic neurologic anomaly resulting form degeneration of dopamine-generating cells in the substantia nigra, a region of the midbrain, characterized clinically by shaking, rigidity, slowness of movement and difficulty with walking and gait."
    publications:
      - id: https://academic.oup.com/nar/article/45/D1/D712/2605791
        title: "The Monarch Initiative: an integrative data and analytic platform connecting phenotypes to genotypes across species"
activity_status: active
repository: https://github.com/evidenceontology/evidenceontology
preferredPrefix: ECO
depicted_by: https://avatars1.githubusercontent.com/u/12802432
---

The Evidence & Conclusion Ontology (ECO) describes types of scientific evidence within the realm of biological research that can arise from laboratory experiments, computational methods, manual literature curation, and other means. Researchers can use these types of evidence to support assertions about things (such as scientific conclusions, gene annotations, or other statements of fact) that result from scientific research.

ECO comprises two high-level classes, evidence and assertion method, where evidence is defined as “a type of information that is used to support an assertion,” and assertion method is defined as “a means by which a statement is made about an entity.” Together evidence and assertion method can be combined to describe both the support for an assertion and whether that assertion was made by a human being or a computer. However, ECO is _not_ used to make the assertion itself; for that, one would use another ontology, free text description, or some other means.

ECO was originally created around the year 2000 to support gene product annotation by the Gene Ontology, which now displays ECO in AmiGO 2. Today ECO is used by many groups concerned with evidence in scientific research.

***
For **advice on requesting new terms**, please see **[the Evidence & Conclusion Ontology wiki](https://github.com/evidenceontology/evidenceontology/wiki/New-term-request-how-to)**.

For **further information** visit the **[Evidence & Conclusion Ontology website](http://www.evidenceontology.org/)**.

Please **cite** the following paper: [Giglio M, Tauber R, Nadendla S, Munro J, Olley D, Ball S, Mitraka E, Schriml LM, Gaudet P, Hobbs ET, Erill I, Siegele DA, Hu JC, Mungall C, Chibucos MC. **ECO, the Evidence & Conclusion Ontology: community standard for evidence information**. Nucleic Acids Res. 2019 Jan 8;47(D1):D1186-D1194.](https://www.ncbi.nlm.nih.gov/pubmed/30407590)

This work is made possible by **[award number 1458400](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1458400)** from the **US National Science Foundation's Division of Biological Infrastructure**.
