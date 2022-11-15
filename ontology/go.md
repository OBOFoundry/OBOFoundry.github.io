---
layout: ontology_detail
id: go
title: Gene Ontology
browsers:
- title: Gene Ontology AmiGO 2 Browser
  label: AmiGO
  url: http://amigo.geneontology.org/amigo/term/GO:0008150#display-lineage-tab
contact:
  email: suzia@stanford.edu
  github: suzialeksander
  label: Suzi Aleksander
  orcid: 0000-0001-6787-2901
dependencies:
- id: cl
  subset: go/extensions/cl_import.owl
- id: go/extensions/go-bridge-to-nifstd.owl
  title: GO bridge to NIFSTD
  connects:
  - id: nifstd
  - id: go
  description: Bridging axioms between nifstd and go
  publications:
  - id: http://www.ncbi.nlm.nih.gov/pubmed/24093723
    title: 'The Gene Ontology (GO) Cellular Component Ontology: integration with SAO (Subcellular Anatomy Ontology) and other recent developments.'
  type: BridgeOntology
- id: ncbitaxon
  subset: go/extensions/ncbitaxon_import.owl
- id: ro
  subset: go/extensions/ro_import.owl
- id: uberon
  subset: go/extensions/uberon_import.owl
depicted_by: http://geneontology.org/assets/go-logo-icon.mini.png
description: An ontology for describing the function of genes and gene products
domain: biological systems
github_date_added: 2015-07-28
homepage: http://geneontology.org/
in_foundry_order: 1
integration_server: http://build.berkeleybop.org/view/GO
label: GO
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: GO
products:
- id: go.owl
  title: GO (OWL edition)
  description: The main ontology in OWL. This is self contained and does not have connections to other OBO ontologies
  page: http://geneontology.org/page/download-ontology
- id: go.obo
  title: GO (OBO Format edition)
  description: Equivalent to go.owl, in obo format
  page: http://geneontology.org/page/download-ontology
- id: go.json
  title: GO (JSON edition)
  description: Equivalent to go.owl, in obograph json format
  page: https://github.com/geneontology/obographs/
- id: go/extensions/go-plus.owl
  title: GO-Plus
  description: The main ontology plus axioms connecting to select external ontologies, with subsets of those ontologies
  page: http://geneontology.org/page/download-ontology
- id: go/go-base.owl
  title: GO Base Module
  description: The main ontology plus axioms connecting to select external ontologies, excluding the external ontologies themselves
  page: http://geneontology.org/page/download-ontology
- id: go/extensions/go-plus.json
  title: GO-Plus
  description: As go-plus.owl, in obographs json format
  page: https://github.com/geneontology/obographs/
- id: go/go-basic.obo
  title: GO-Basic, Filtered, for use with legacy tools
  description: Basic version of the GO, filtered such that the graph is guaranteed to be acyclic and annotations can be propagated up the graph. The relations included are is a, part of, regulates, negatively regulates and positively regulates. This version excludes relationships that cross the 3 GO hierarchies.
  page: http://geneontology.org/page/download-ontology
- id: go/go-basic.json
  title: GO-Basic, Filtered, for use with legacy tools (JSON)
  description: As go-basic.obo, in json format
  page: http://geneontology.org/page/download-ontology
- id: go/extensions/go-taxon-groupings.owl
  title: GO Taxon Groupings
  description: Classes added to ncbitaxon for groupings such as prokaryotes
  page: http://geneontology.org/page/download-ontology
- id: go/snapshot/go.owl
  title: GO (OWL edition), daily snapshot release
  description: Equivalent to go.owl, but released daily. Note the snapshot release is not archived.
  page: http://geneontology.org/page/download-ontology
- id: go/snapshot/go.obo
  title: GO (OBO Format edition), daily snapshot release
  description: Equivalent to go.owl, but released daily. Note the snapshot release is not archived.
  page: http://geneontology.org/page/download-ontology
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/10802651
  title: 'Gene ontology: tool for the unification of biology. The Gene Ontology Consortium'
- id: https://www.ncbi.nlm.nih.gov/pubmed/33290552
  title: 'The Gene Ontology resource: enriching a GOld mine'
repository: https://github.com/geneontology/go-ontology
review:
  date: 2010
tags:
- biology
taxon:
  id: NCBITaxon:1
  label: All life
tracker: https://github.com/geneontology/go-ontology/issues/
twitter: news4go
usages:
- description: The GO ontology is used by the GO consortium for functional annotation of genes
  examples:
  - description: annotations to transmembrane transport
    url: http://amigo.geneontology.org/amigo/term/GO:0055085
  type: annotation
  user: http://geneontology.org
- description: Uniprot uses GO to show the function of proteins
  examples:
  - description: functional annotations of human Sonic hedgehog protein
    url: https://www.uniprot.org/uniprot/Q15465#function
  type: annotation
  user: https://www.uniprot.org
- description: Reactome annotates activities, pathways, and cellular localization using GO
  examples:
  - description: protein tyrosine kinase activity of an EGFR complex
    url: https://reactome.org/content/detail/R-HSA-177934
  type: annotation
  user: https://reactome.org
- description: The Alliance of Genome Resources uses GO for model organism gene function annotation
  examples:
  - description: Functional summary of C elegans nsy-1 gene
    url: https://www.alliancegenome.org/gene/WB:WBGene00003822#function---go-annotations
  - description: Gene Ontology Causal Activity Models for C elegans nsy-1 gene
    url: https://www.alliancegenome.org/gene/WB:WBGene00003822#pathways
  type: annotation
  user: https://www.alliancegenome.org
- description: Rhea uses GO to describe individual biochemical reactions
  examples:
  - description: Glutamine scyllo-inositol transaminase reaction and associated GO term
    url: https://www.rhea-db.org/rhea/22920
  type: mapping
  user: https://www.rhea-db.org
activity_status: active
---

The goal of the GeneOntology (GO) project is to provide a uniformway to describe the functions of gene products from organisms across all kingdoms of life and thereby enable analysis of genomic data
