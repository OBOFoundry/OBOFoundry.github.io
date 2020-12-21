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
slack: https://obo-communitygroup.slack.com/archives/C01CR698CF2
wikidata_template: https://en.wikipedia.org/wiki/Template:Uberon
mailing_list: https://lists.sourceforge.net/lists/listinfo/obo-anatomy
biosharing: https://www.biosharing.org/bsg-000016
usages:
 - user: http://bgee.org/
   seeAlso: https://www.biosharing.org/biodbcore-000228
   type: annotation
   description: Bgee is a database to retrieve and compare gene expression patterns between animal species. Bgee in using Uberon to annotate the site of expression, and Bgee curators one the major contributors to the ontology.
   examples:
    - url: http://bgee.org/?page=gene&gene_id=ENSG00000244734
      description: "Uberon terms used to annotate expression of human hemoglobin subunit beta"
 - user: https://www.encodeproject.org/
   seeAlso: https://www.biosharing.org/biodbcore-000034
   type: annotation
   description: The National Human Genome Research Institute (NHGRI) launched a public research consortium named ENCODE, the Encyclopedia Of DNA Elements, in September 2003, to carry out a project to identify all functional elements in the human genome sequence. The ENCODE DCC users Uberon to annotate samples
   reference: https://doi.org/10.1093/database/bav010
 - user: http://fantom5-collaboration.gsc.riken.jp/
   type: annotation
   description: FANTOM5 is using Uberon and CL to annotate samples allowing for transcriptome analyses with cell-type and tissue-level specificity.
   examples:
    - url: http://fantom.gsc.riken.jp/5/sstar/UBERON:0001893
      description: FANTOM5 samples annotated to telencephalon or its parts
 - user: https://monarchinitiative.org/
   type: query
   description: Querying expression and phenotype data
 - user: https://geneontology.org/
   label: GO Database
   type: query
   description: Querying for functional annotations relevant to a tissue
   examples:
    - url: http://amigo.geneontology.org/amigo/term/UBERON:0000955
      description: GO annotations relevant to the uberon class for brain
 - user: http://phenoscape.org
   label: Phenoscape
   description: The Phenoscape project is both a major driver of and contributor to Uberon, contibuting thousands of terms. The teleost (bony fishes) component of Uberon was derived from the Teleost Anatomy Ontology, developed by the Phenoscape group. Most of the high level design of the skeletal system comes from the Vertebrate Skeletal Anatomy Ontology (VSAO), also created by the Phenoscape group. Phenoscape curators continue to extend the ontology, covering a wide variety of tetrapod structures, with an emphasis on the appendicular system.
 - url: https://neuinfo.org/
   label: Neuroscience Information Framework
   type: Database
 - url: https://scicrunch.org/
   label: SciCrunch
   type: Database
 - url: http://single-cell.clst.riken.jp/
   label: SCPortalen
   reference: https://doi.org/10.1093/nar/gkx949
   type: Database
 - url: https://www.ebi.ac.uk/chembl/
   label: ChEMBL
   description: "ChEMBL uses Uberon to describe organ/tissue information in assays"
   reference: https://doi.org/10.1093/nar/gky1075
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
  - label: FANTOM5
    title: FANTOM5 Data Portal
    url: http://fantom.gsc.riken.jp/5/sstar/UBERON:0001890
  - label: KnowledgeSpace
    title: INCF KnowledgeSpace Portal
    url: https://knowledge-space.org/index.php/pages/view/UBERON:0000061
products:
 - id: uberon.owl
   type: owl:Ontology
   title: Uberon
   description: "core ontology"
   is_canonical: true
 - id: uberon/uberon-base.owl
   title: Uberon base ontology
   description: Axioms defined within Uberon and to be used in imports for other ontologies
   page: https://github.com/INCATools/ontology-development-kit/issues/50
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
 - id: uberon/composite-vertebrate.owl
   type: MergedOntology
   title: Uberon composite vertebrate ontology
   page: https://github.com/obophenotype/uberon/wiki/Multi-species-composite-ontologies
   taxon: Metazoa
   mireots_from:
    - zfa
    - xao
    - fbbt
    - wbbt
    - ma
    - fma
    - emapa
    - ehdaa2
activity_status: active
---

Uberon is an integrated cross-species ontology covering anatomical structures in animals. See the <a href="http://uberon.org">Uberon website</a> for more info, or read the <a
 href="http://genomebiology.com/2012/13/1/R5">Uberon paper in Genome Biology</a>.

![uberon](http://uberon.github.io/images/u-logo.jpg)
