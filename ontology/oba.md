---
layout: ontology_detail
id: oba
title: Ontology of Biological Attributes
build:
  checkout: git clone https://github.com/obophenotype/bio-attribute-ontology.git
  method: vcs
  path: .
  system: git
contact:
  email: cjmungall@lbl.gov
  github: cmungall
  label: Chris Mungall
  orcid: 0000-0002-6601-2165
description: "A collection of biological attributes (traits) covering all
kingdoms of life."
domain: phenotype
homepage: https://github.com/obophenotype/bio-attribute-ontology
jobs:
  - id: https://travis-ci.org/obophenotype/bio-attribute-ontology
    type: travis-ci
license:
  label: CC0 1.0
  url: http://creativecommons.org/publicdomain/zero/1.0/
page: http://wiki.geneontology.org/index.php/Extensions/x-attribute
preferredPrefix: OBA
products:
  - id: oba.owl
  - id: oba.obo
  - id: oba/subsets/oba-basic.obo
publications:
  - id: https://doi.org/10.1007/s00335-023-09992-1
    title: "The Ontology of Biological Attributes (OBA) - computational traits
for the life sciences"
repository: https://github.com/obophenotype/bio-attribute-ontology
tracker: https://github.com/obophenotype/bio-attribute-ontology/issues
usages:
  - description: "OBA terms are used by the NHGRI-EBI GWAS Catalog for
    phenotypic trait annotation."
    examples:
      - description: 'age of onset of depressive disorder'
        url: https://www.ebi.ac.uk/gwas/efotraits/OBA_2040166
    publications:
      - id: https://doi.org/10.1093/nar/gkac1010
        title: "The NHGRI-EBI GWAS Catalog: knowledgebase and deposition
resource"
    type: annotation
    user: https://www.ebi.ac.uk/gwas/
  - description: "OBA trait terms facilitate computational drug target
    identification via the Open Targets Platform."
    examples:
      - description: 'age of onset of Alzheimer disease'
        url: https://platform.opentargets.org/disease/OBA_2001000/associations
    publications:
      - id: https://doi.org/10.1093/nar/gkac1046
        title: "The next-generation Open Targets Platform: reimagined,
redesigned, rebuilt"
    type: Database
    user: https://platform.opentargets.org
  - description: "The Encyclopedia of Life (EOL) TraitBank takes advantage of
    the well-axiomatised OBA terms to infer traits in biodiversity data and to
improve their search functionality."
    examples:
      - description: "body mass http://purl.obolibrary.org/obo/OBA_VT0001259
        The amount of matter in the body of an organism."
        url: https://eol.org/terms/search_results?tq%5Bf%5D%5B0%5D%5Bp%5D=260&tq%5Br%5D=record
    publications:
      - id: https://doi.org/10.3233/SW-150190
        title: 'TraitBank: Practical semantics for organism attribute data'
    type: Database
    user: https://eol.org/traitbank
  - description: "OBA terms are used by the Functional Trait Resource for
    Environmental Studies (FuTRES) for the annotation of measurable traits in
vertebrates."
    examples:
      - description: 'body length'
        url: https://futres-data-interface.netlify.app/
    publications:
      - id: https://doi.org/10.1016/j.isci.2022.105101
        title: "A solution to the challenges of interdisciplinary aggregation
and use of specimen-level trait data"
    type: annotation
    user: https://futres.org/
  - description: "The Mouse Phenome Database (MPD) takes advantage of the
    axioms provided by OBA for Vertebrate Trait (VT) ontology terms to
integrate genomic and phenomic data."
    examples:
      - description: 'response to alcohol trait'
        url: https://phenome.jax.org/ontologies/vt:0010489
    publications:
      - id: https://doi.org/10.1093/nar/gkac1007
        title: "Mouse Phenome Database: towards a more FAIR-compliant and
TRUST-worthy data repository and tool suite for phenotypes and genotypes"
    type: Database
    user: https://phenome.jax.org
activity_status: active
---

A collection of biological attributes (traits) covering all kingdoms of life.
Interoperable with VT (vertebrate trait ontology) and TO (plant trait
ontology). Extends PATO.
