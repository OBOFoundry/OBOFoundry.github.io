---
layout: ontology_detail
id: go
label: GO
title: Gene Ontology
twitter: news4go
tracker: http://sourceforge.net/p/geneontology/ontology-requests/
termgenie: http://go.termgenie.org
taxon: 
  id: NCBITaxon:1
  label: All life
domain: biology
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
   connects:
     - id: nifstd
     - id: go
products:
 - id: go.owl
depicted_by: http://geneontology.org/sites/default/files/go-logo-icon.mini__0.png
---

Bridging axioms between nifstd and go