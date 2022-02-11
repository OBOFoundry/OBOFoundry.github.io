---
layout: ontology_detail
id: pcl
title: "Provisional Cell Ontology"
contact:
  email: davidos@ebi.ac.uk
  label: David Osumi-Sutherland
  github: dosumis
  orcid: 0000-0002-7073-9172
description: "Cell types that are provisionally defined by experimental techniques such as single cell or single nucleus transcriptomics rather than a straightforward & coherent set of properties."
domain: phenotype
homepage: https://github.com/obophenotype/provisional_cell_ontology
products:
  - id: pcl.owl
  - id: pcl.obo
  - id: pcl.json
  - id: pcl-base.owl
  - id: pcl-base.obo
  - id: pcl-base.json
  - id: pcl-full.owl
  - id: pcl-full.obo
  - id: pcl-full.json
  - id: pcl-simple.owl
  - id: pcl-simple.obo
  - id: pcl-simple.json
dependencies:
  - id: pr
  - id: go
  - id: uberon
  - id: ro
  - id: pato
  - id: ncbitaxon
  - id: bfo
  - id: cl
  - id: omo
  - id: nbo
  - id: chebi
  - id: so
usages:
  - user: https://biccn.org/
    type: annotation
    description: The brain data standards component of pcl is used by the brain initiative for annotation.
    examples:
      - url: https://www.ebi.ac.uk/ols/ontologies/pcl/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPCL_0011003
        description: transcriptomically defined cell type Lamp5 Egln3_2 primary motor cortex GABAergic interneuron (Mus musculus)
    publications:
      - id: https://doi.org/10.1101/2021.10.10.463703
        title: "Brain Data Standards Ontology: A data-driven ontology of transcriptomically defined cell types in the primary motor cortex"
tracker: https://github.com/obophenotype/provisional_cell_ontology/issues
license:
  url: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
activity_status: active
repository: https://github.com/obophenotype/provisional_cell_ontology
preferredPrefix: PCL
---
