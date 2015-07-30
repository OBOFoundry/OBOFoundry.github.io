---
layout: ontology_detail
id: go
in_foundry: true
label: GO
description: An ontology for describing the function of genes and gene products
title: Gene Ontology
twitter: news4go
tracker: https://github.com/geneontology/go-ontology/issues/
termgenie: http://go.termgenie.org
taxon: 
  id: NCBITaxon:1
  label: All life
domain: biology
integration_server: http://build.berkeleybop.org/view/GO
dependencies:
 - id: uberon
   subset: go/extensions/uberon_import.owl
 - id: cl
   subset: go/extensions/cl_import.owl
 - id: ncbitaxon
   subset: go/extensions/ncbitaxon_import.owl
 - id: ro
   subset: go/extensions/ro_import.owl
 - id: go/extensions/go-bridge-to-nifstd.owl
   type: BridgeOntology
   title: GO bridge to NIFSTD
   description: Bridging axioms between nifstd and go
   publications:
     - id: http://www.ncbi.nlm.nih.gov/pubmed/24093723
       title: "The Gene Ontology (GO) Cellular Component Ontology: integration with SAO (Subcellular Anatomy Ontology) and other recent developments."
   connects:
     - id: nifstd
     - id: go
products:
 - id: go.owl
 - id: go/extensions/go-plus.owl
   title: GO-Plus
depicted_by: http://geneontology.org/sites/default/files/go-logo-icon.mini__0.png
---

The goal of the GeneOntology (GO) project is to provide a uniformway to describe the functions of gene products from organisms across all kingdoms of life and thereby enable analysis of genomic data

