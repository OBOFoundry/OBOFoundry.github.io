---
layout: ontology_detail
id: fypo
title: Fission Yeast Phenotype Ontology
build:
  source_url: https://raw.githubusercontent.com/pombase/fypo/master/release/fypo.owl
  method: obo2owl
  infallible: 1
contact:
  email: vw253@cam.ac.uk
  label: Val Wood
  github: ValWood
  orcid: 0000-0001-6330-7526
description: FYPO is a formal ontology of phenotypes observed in fission yeast.
domain: phenotype
homepage: https://github.com/pombase/fypo
products:
  - id: fypo.owl
  - id: fypo.obo
taxon:
  id: NCBITaxon:4896
  label: S. pombe
tracker: https://github.com/pombase/fypo/issues
publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/23658422
    title: "FYPO: The Fission Yeast Phenotype Ontology."
license:
  url: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
depicted_by: https://github.com/pombase/website/blob/master/src/assets/FYPO_logo_tiny.png
usages:
  - user: https://www.pombase.org
    description: Pombase uses fypo for phenotype data annotation in fission yeast
    examples:
      - url: https://www.pombase.org/term/FYPO:0000059
        description: "genotypes annotated to abnormal mitotic cell cycle in fission yeast"
activity_status: active
repository: https://github.com/pombase/fypo
preferredPrefix: FYPO
added: 2015-07-29
---

FYPO is being developed to support the comprehensive and detailed representation of phenotypes in PomBase, the new online fission yeast resource (www.pombase.org). Its scope is similar to that of the Ascomycete Phenotype Ontology (APO), but FYPO includes more detailed pre-composed terms as well as computable definitions.
