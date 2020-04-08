---
layout: ontology_detail
id: go
in_foundry_order: 1
homepage: geneontology.org
contact:
  email: suzia@stanford.edu
  label: Suzi Aleksander
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
label: GO
description: An ontology for describing the function of genes and gene products
title: Gene Ontology
review:
  date: 2010
homepage: http://geneontology.org/
twitter: news4go
facebook: https://www.facebook.com/Gene-Ontology-305908656519/ 
tracker: https://github.com/geneontology/go-ontology/issues/
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
browsers:
  - label: AmiGO
    title: Gene Ontology AmiGO 2 Browser
    url: http://amigo.geneontology.org/amigo/term/GO:0008150#display-lineage-tab
products:
 - id: go.owl
   title: "GO (OWL edition)"
   description: "The main ontology in OWL. This is self contained and does not have connections to other OBO ontologies"
   page: http://geneontology.org/page/download-ontology
 - id: go.obo
   title: "GO (OBO Format edition)"
   description: "Equivalent to go.owl, in obo format"
   page: http://geneontology.org/page/download-ontology
 - id: go.json
   title: "GO (JSON edition)"
   description: "Equivalent to go.owl, in obograph json format"
   page: https://github.com/geneontology/obographs/
 - id: go/extensions/go-plus.owl
   title: GO-Plus
   description: "The main ontology plus axioms connecting to select external ontologies"
   page: http://geneontology.org/page/download-ontology
 - id: go/extensions/go-plus.json
   title: GO-Plus
   description: "As go-plus.owl, in obographs json format"
   page: https://github.com/geneontology/obographs/
 - id: go/go-basic.obo
   title: "GO-Basic, Filtered, for use with legacy tools"
   description: "The main ontology plus axioms connecting to select external ontologies"
   page: http://geneontology.org/page/download-ontology
 - id: go/go-basic.json
   title: "GO-Basic, Filtered, for use with legacy tools (JSON)"
   description: "As go-basic.obo, in json format"
   page: http://geneontology.org/page/download-ontology
 - id: go/extensions/go-taxon-groupings.owl
   title: GO Taxon Groupings
   description: "Classes added to ncbitaxon for groupings such as prokaryotes"
   page: http://geneontology.org/page/download-ontology
 - id: go/snapshot/go.owl
   title: "GO (OWL edition), daily snapshot release"
   description: "Equivalent to go.owl, but released daily. Note the snapshot release is not archived."
   page: http://geneontology.org/page/download-ontology
 - id: go/snapshot/go.obo
   title: "GO (OBO Format edition), daily snapshot release"
   description: "Equivalent to go.owl, but released daily. Note the snapshot release is not archived."
   page: http://geneontology.org/page/download-ontology
depicted_by: http://geneontology.org/assets/go-logo-icon.mini.png
usages:
 - user: http://geneontology.org
   type: annotation
   description: The GO ontology is used by the GO consortium for functional annotation of genes
   examples:
    - url: http://amigo.geneontology.org/amigo/term/GO:0055085
      description: annotations to transmembrane transport
activity_status: active
---

The goal of the GeneOntology (GO) project is to provide a uniformway to describe the functions of gene products from organisms across all kingdoms of life and thereby enable analysis of genomic data

