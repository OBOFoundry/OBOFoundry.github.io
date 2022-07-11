---
layout: ontology_detail
id: fypo
title: Fission Yeast Phenotype Ontology
build:
  infallible: 1
  method: obo2owl
  source_url: https://raw.githubusercontent.com/pombase/fypo/master/release/fypo.owl
contact:
  email: vw253@cam.ac.uk
  github: ValWood
  label: Val Wood
  orcid: 0000-0001-6330-7526
depicted_by: https://github.com/pombase/website/blob/master/src/assets/FYPO_logo_tiny.png
description: FYPO is a formal ontology of phenotypes observed in fission yeast.
domain: phenotype
homepage: https://github.com/pombase/fypo
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
preferredPrefix: FYPO
products:
- id: fypo.owl
- id: fypo.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/23658422
  title: 'FYPO: The Fission Yeast Phenotype Ontology.'
repository: https://github.com/pombase/fypo
taxon:
  id: NCBITaxon:4896
  label: S. pombe
tracker: https://github.com/pombase/fypo/issues
usages:
- description: Pombase uses fypo for phenotype data annotation in fission yeast
  examples:
  - description: genotypes annotated to abnormal mitotic cell cycle in fission yeast
    url: https://www.pombase.org/term/FYPO:0000059
  user: https://www.pombase.org
activity_status: active
---

FYPO is being developed to support the comprehensive and detailed representation of phenotypes in PomBase, the new online fission yeast resource (www.pombase.org). Its scope is similar to that of the Ascomycete Phenotype Ontology (APO), but FYPO includes more detailed pre-composed terms as well as computable definitions.
