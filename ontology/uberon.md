---
layout: ontology_detail
id: uberon
type: owl:Ontology
label: Uberon
title: Uberon multi-species anatomy ontology
build:
  checkout: svn --ignore-externals co http://svn.code.sf.net/p/obo/svn/uberon/trunk
  email_cc: cjmungall@lbl.gov
  system: svn
  method: vcs
  infallible: 1
description: An integrated cross-species anatomy ontology covering animals and bridging multiple species-specific ontologies
homepage: http://uberon.org
page: http://en.wikipedia.org/wiki/Uberon
twitter: uberanat
google_plus: "+UberonOrg"
wikidata_template: https://en.wikipedia.org/wiki/Template:Uberon
mailing_list: https://lists.sourceforge.net/lists/listinfo/obo-anatomy
biosharing: https://www.biosharing.org/bsg-000016
used_by:
 - url: http://bgee.org/
   seeAlso: https://www.biosharing.org/biodbcore-000228
   label: bgee
   type: Database
 - url: https://www.encodeproject.org/
   seeAlso: https://www.biosharing.org/biodbcore-000034
   label: ENCODE
 - url: http://fantom5-collaboration.gsc.riken.jp/
   label: FANTOM5
 - url: https://monarchinitiative.org/
   label: Monarch
   type: Database
 - url: https://geneontology.org/
   label: GO Database
   type: Database
 - url: http://phenoscape.org
   label: Phenoscape
 - url: https://neuinfo.org/
   label: Neuroscience Information Framework
   type: Database
 - url: https://scicrunch.org/
   label: SciCrunch
   type: Database
funded_by:
 - "NIH R24OD011883"
 - "NIH R01HG004838"
 - "NIH P41HG002273"
 - "NSF DEB-0956049"
canonical: uberon.owl
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
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
    title: "Uberon, an integrative multi-species anatomy ontology"
  - id: http://www.ncbi.nlm.nih.gov/pubmed/25009735
    title: "Unification of multi-species vertebrate anatomy ontologies for comparative biology in Uberon"
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
browsers:
  - label: RGD
    title: Gene Ontology AmiGO 2 Browser
    url: http://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=UBERON:0001062
  - label: AmiGO (SUBSET)
    title: Gene Ontology AmiGO 2 Browser
    url: http://amigo.geneontology.org/amigo/term/UBERON:0001062#display-lineage-tab
  - label: Bgee (gene expression)
    title: Bgee gene expression queries
    url: http://bgee.org/?page=gene
products:
 - id: uberon.owl
   type: owl:Ontology
   title: Uberon
   description: "core ontology"
   is_canonical: true
 - id: uberon/ext.owl
   type: owl:Ontology
   description: Uberon extended
   title: "Uberon edition that includes subsets of other ontologies and axioms connecting to them"
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
   description: Extended uberon plus all metazoan ontologies
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
