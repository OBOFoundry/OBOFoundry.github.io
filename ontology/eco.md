---
layout: ontology_detail
id: eco
title: Evidence ontology
build:
  infallible: 1
  method: obo2owl
  notes: switch to vcs
  source_url: https://raw.githubusercontent.com/evidenceontology/evidenceontology/master/eco.obo
contact:
  email: mgiglio@som.umaryland.edu
  github: mgiglio99
  label: Michelle Giglio
  orcid: 0000-0001-7628-5565
depicted_by: https://avatars1.githubusercontent.com/u/12802432
description: An ontology for experimental and other evidence statements.
domain: investigations
funded_by:
- id: https://www.nsf.gov/awardsearch/showAward?AWD_ID=1458400
  title: NSF ABI-1458400
github_date_added: 2015-07-28
homepage: https://www.evidenceontology.org
jobs:
- id: https://travis-ci.org/evidenceontology/evidenceontology
  type: travis-ci
license:
  label: CC0 1.0
  url: https://creativecommons.org/publicdomain/zero/1.0/
preferredPrefix: ECO
products:
- id: eco.owl
- id: eco.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/30407590
  title: 'ECO, the Evidence & Conclusion Ontology: community standard for evidence information.'
  preferred: true
- id: https://www.ncbi.nlm.nih.gov/pubmed/25052702
  title: Standardized description of scientific evidence using the Evidence Ontology (ECO)
repository: https://github.com/evidenceontology/evidenceontology
tracker: https://github.com/evidenceontology/evidenceontology/issues
usages:
- description: ECO is used by the GO consortium for evidence on GO associations
  examples:
  - description: annotations to transmembrane transport
    url: http://amigo.geneontology.org/amigo/term/GO:0055085
  type: annotation
  user: http://geneontology.org
- description: ECO is used by the Monarch Initiative for evidence types for disease to phenotype annotations.
  examples:
  - description: 'Parkinsonism: Characteristic neurologic anomaly resulting form degeneration of dopamine-generating cells in the substantia nigra, a region of the midbrain, characterized clinically by shaking, rigidity, slowness of movement and difficulty with walking and gait.'
    url: https://monarchinitiative.org/phenotype/HP%3A0001300#disease
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/27899636
    title: 'The Monarch Initiative: an integrative data and analytic platform connecting phenotypes to genotypes across species'
  type: annotation
  user: https://monarchinitiative.org/
activity_status: active
---

The Evidence & Conclusion Ontology (ECO) describes types of scientific evidence within the realm of biological research that can arise from laboratory experiments, computational methods, manual literature curation, and other means. Researchers can use these types of evidence to support assertions about things (such as scientific conclusions, gene annotations, or other statements of fact) that result from scientific research.

ECO comprises two high-level classes, evidence and assertion method, where evidence is defined as “a type of information that is used to support an assertion,” and assertion method is defined as “a means by which a statement is made about an entity.” Together evidence and assertion method can be combined to describe both the support for an assertion and whether that assertion was made by a human being or a computer. However, ECO is _not_ used to make the assertion itself; for that, one would use another ontology, free text description, or some other means.

ECO was originally created around the year 2000 to support gene product annotation by the Gene Ontology, which now displays ECO in AmiGO 2. Today ECO is used by many groups concerned with evidence in scientific research.

***
For **advice on requesting new terms**, please see **[the Evidence & Conclusion Ontology wiki](https://github.com/evidenceontology/evidenceontology/wiki/New-term-request-how-to)**.
