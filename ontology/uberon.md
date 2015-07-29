---
layout: ontology_detail
id: uberon
type: owl:Ontology
label: Uberon
title: Uberon multi-species anatomy ontology
description: Uberon is an integrated cross-species anatomy ontology representing a variety of entities classified according to traditional anatomical criteria such as structure, function and developmental lineage. The ontology includes comprehensive relationships to taxon-specific anatomical ontologies, allowing integration of functional, phenotype and expression data
homepage: http://uberon.org
page: http://en.wikipedia.org/wiki/Uberon
twitter: uberanat
google_plus: "+UberonOrg"
mailing_list: https://lists.sourceforge.net/lists/listinfo/obo-anatomy
canonical: uberon.owl
taxon: 
  id: NCBITaxon:33208
  label: Metazoa
domain: anatomy
repository: https://github.com/obophenotype/uberon
tracker: https://github.com/obophenotype/uberon/issues
releases: http://purl.obolibrary.org/obo/uberon/releases/
contact: 
  email: cjmungall@lbl.gov
  label: Chris Mungall
publications:
  - id: http://www.ncbi.nlm.nih.gov/pubmed/22293552
    title: Uberon, an integrative multi-species anatomy ontology
depicted_by: http://uberon.github.io/images/u-logo.jpg
exampleClass: UBERON_0002046
redirects:
  - match: "releases/"
    url: "http://svn.code.sf.net/p/obo/svn/uberon/releases/"
  - match: ""
    url: "http://berkeleybop.org/ontologies/uberon/"
dependencies:
 - id: go
   subset: uberon/go_import.owl
 - id: cl
   subset: uberon/cl_import.owl
 - id: chebi
   subset: uberon/chebi_import.owl
 - id: pr
   subset: uberon/pr_import.owl
products:
 - id: uberon.owl
   type: owl:Ontology
   title: Uberon
   is_canonical: true
 - id: uberon/ext.owl
   type: owl:Ontology
   description: Uberon extended
   title: Uberon edition that includes subsets of other ontologies
   mireots_from: cl
   mireots_from: pr
   mireots_from: envo
   mireots_from: go
   mireots_from: pato
   mireots_from: ncbitaxon
 - id: uberon/basic.obo
   title: Uberon basic
   description: Uberon edition that excludes external ontologies and most relations
   format: obo
   type: obo-basic-ontology
 - id: uberon/bridge/uberon-bridge-to-zfa.owl
   type: BridgeOntology
   page: https://github.com/obophenotype/uberon/wiki/inter-anatomy-ontology-bridge-ontologies
   title: Uberon bridge to ZFA
   description: Taxonomic equivalence axioms connecting zebrafish-specific classes to generic uberon counterparts
   connects:
     - id: uberon
     - id: zfa
 - id: uberon/bridge/uberon-bridge-to-ma.owl
   type: BridgeOntology
   page: https://github.com/obophenotype/uberon/wiki/inter-anatomy-ontology-bridge-ontologies
   title: Uberon bridge to MA
   description: Taxonomic equivalence axioms connecting adult mouse specific classes to generic uberon counterparts
   connects:
     - id: uberon
     - id: ma
 - id: uberon/composite-metazoan.owl
   type: MergedOntology
   title: Uberon composite metazoan ontology
   page: https://github.com/obophenotype/uberon/wiki/Multi-species-composite-ontologies
   taxon: Metazoa
   mireots_from: zfa
   mireots_from: xao
   mireots_from: fbbt
   mireots_from: wbbt
   mireots_from: ma
   mireots_from: fma
   mireots_from: emapa
   mireots_from: ehdaa2
 - id: uberon/composite-vertebrate.owl
   type: MergedOntology
   title: Uberon composite vertebrate ontology
   page: https://github.com/obophenotype/uberon/wiki/Multi-species-composite-ontologies
   taxon: Metazoa
   mireots_from: zfa
   mireots_from: xao
   mireots_from: fbbt
   mireots_from: wbbt
   mireots_from: ma
   mireots_from: fma
   mireots_from: emapa
   mireots_from: ehdaa2
---

Uberon is an integrated cross-species ontology covering anatomical structures in animals. See the <a href="http://uberon.org">Uberon website</a> for more info, or read the <a
 href="http://genomebiology.com/2012/13/1/R5">Uberon paper in Genome Biology</a>.

![uberon](http://www.obofoundry.org/wiki/images/9/91/Uberon.png)
