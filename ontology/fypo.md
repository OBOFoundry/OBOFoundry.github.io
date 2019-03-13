---
layout: ontology_detail
id: fypo
title: Fission Yeast Phenotype Ontology
build:
  source_url: https://raw.githubusercontent.com/pombase/fypo/master/release/fypo.owl
  method: obo2owl
  infallible: 1
contact:
  email: mah79@cam.ac.uk
  label: Midori Harris
  github: mah11
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
  - id: http://www.ncbi.nlm.nih.gov/pubmed/23658422
    title: "FYPO: The Fission Yeast Phenotype Ontology."
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
depicted_by: https://github.com/pombase/website/blob/master/src/assets/FYPO_logo_tiny.png
usages:
  - user: https://www.pombase.org
    description: Pombase uses fypo for phenotype data annotation in fission yeast
    example:
      - url: https://www.pombase.org/term/FYPO:0000059
        description: "genotypes annotated to abnormal mitotic cell cycle in fission yeast"
activity_status: active
---

FYPO is being developed to support the comprehensive and detailed representation of phenotypes in PomBase, the new online fission yeast resource (www.pombase.org). Its scope is similar to that of the Ascomycete Phenotype Ontology (APO), but FYPO includes more detailed pre-composed terms as well as computable definitions.
