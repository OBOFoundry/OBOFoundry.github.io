---
layout: ontology_detail
id: fma
title: OBO-specific subset of the Foundational Model of Anatomy Ontology
contact:
  email: mejino@u.washington.edu
  label: Onard Mejino
description: The OBO-specific subset of FMA is now deprecated. Please refer to the official version of FMA instead (http://purl.org/sig/ont/fma.owl).
domain: anatomy and development
homepage: http://si.washington.edu/projects/fma
is_obsolete: true
license:
  label: CC BY 3.0
  url: https://creativecommons.org/licenses/by/3.0/
page: http://en.wikipedia.org/wiki/Foundational_Model_of_Anatomy
preferredPrefix: FMA
products:
- id: fma.owl
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/18688289
  title: Translating the Foundational Model of Anatomy into OWL
- id: https://www.ncbi.nlm.nih.gov/pubmed/18360535
  title: 'The foundational model of anatomy in OWL: Experience and perspectives'
- id: https://www.ncbi.nlm.nih.gov/pubmed/16779026
  title: 'Challenges in converting frame-based ontology into OWL: the Foundational Model of Anatomy case-study'
repository: https://bitbucket.org/uwsig/fma
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
tracker: https://bitbucket.org/uwsig/fma/issues
activity_status: inactive
---

After many years of maintaining a bespoke OBO-format translation of the FMA — restricted to the is_a, part_of, and has_part relationships — we have now deprecated this project.
Users are encouraged to use the official FMA release instead: `http://purl.org/sig/ont/fma.owl`.
Note that the current official FMA release has unsatisfiable classes. Please follow [this issue](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/21) to keep yourself up to date.
