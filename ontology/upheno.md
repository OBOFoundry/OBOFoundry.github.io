---
layout: ontology_detail
id: upheno
title: Unified phenotype ontology (uPheno)
description: The uPheno ontology integrates multiple phenotype ontologies into a unified cross-species phenotype ontology.
homepage: https://github.com/obophenotype/upheno
tracker: https://github.com/obophenotype/upheno/issues
license:
  url: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
contact:
  label: Nicole Vasilevsky
  email: vasilevs@ohsu.edu
  github: nicolevasilevsky
  orcid: 0000-0001-5208-3432
mailing_list: https://groups.google.com/forum/#!forum/phenotype-ontologies-editors
products:
  - id: upheno.owl
    title: "uPheno 1 (inactive)"
    description: "uPheno 1 is no longer actively maintained, please start using uPheno 2 (see below)."
    page: https://github.com/obophenotype/upheno
  - id: upheno/mp-hp-view.owl
    title: "uPheno MP-HP equivalence axioms"
    description: "No longer actively maintained."
    page: https://github.com/obophenotype/upheno/tree/master/hp-mp
  - id: upheno/v2/upheno.owl
    title: "uPheno 2"
    description: "The new version of uPheno, along with species independent phenotypes amd additional phenotype relations. The ontology is still in Beta status, but we recommend users to migrate their infrastructures to uPheno 2 as uPheno 1 is no longer actively maintained."
    page: https://github.com/obophenotype/upheno-dev
publications:
   - id: https://zenodo.org/record/2382757
     title: "Phenotype Ontologies Traversing All The Organisms (POTATO) workshop aims to reconcile logical definitions across species"
   - id: https://zenodo.org/record/3352149
     title: "Phenotype Ontologies Traversing All The Organisms (POTATO) workshop: 2nd edition"
usages:
  - user: https://monarchinitiative.org/
    type: analysis
    description: uPheno is used by the Monarch Initiative for cross-species inference.
    examples:
      - url: https://monarchinitiative.org/phenotype/HP:0001300#disease
        description: "Characteristic neurologic anomaly resulting form degeneration of dopamine-generating cells in the substantia nigra, a region of the midbrain, characterized clinically by shaking, rigidity, slowness of movement and difficulty with walking and gait."
    publications:
      - id: https://www.ncbi.nlm.nih.gov/pubmed/27899636
        title: "The Monarch Initiative: an integrative data and analytic platform connecting phenotypes to genotypes across species "
build:
  source_url: http://build.berkeleybop.org/job/build-pheno-ontologies/lastSuccessfulBuild/artifact/*zip*/archive.zip
  path: archive/ontology
  method: archive
activity_status: active
repository: https://github.com/obophenotype/upheno
preferredPrefix: UPHENO
---
