---
layout: ontology_detail
id: uberon
title: Uberon multi-species anatomy ontology
browsers:
- title: Gene Ontology AmiGO 2 Browser
  label: RGD
  url: http://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=UBERON:0001062
- title: Gene Ontology AmiGO 2 Browser
  label: AmiGO (SUBSET)
  url: http://amigo.geneontology.org/amigo/term/UBERON:0001062#display-lineage-tab
- title: Bgee gene expression queries
  label: Bgee (gene expression)
  url: http://bgee.org/?page=gene
- title: FANTOM5 Data Portal
  label: FANTOM5
  url: http://fantom.gsc.riken.jp/5/sstar/UBERON:0001890
- title: INCF KnowledgeSpace Portal
  label: KnowledgeSpace
  url: https://knowledge-space.org/index.php/pages/view/UBERON:0000061
build:
  checkout: svn --ignore-externals co http://svn.code.sf.net/p/obo/svn/uberon/trunk
  email_cc: cjmungall@lbl.gov
  infallible: 1
  method: vcs
  system: svn
canonical: uberon.owl
contact:
  email: cjmungall@lbl.gov
  github: cmungall
  label: Chris Mungall
  orcid: 0000-0002-6601-2165
dependencies:
- id: chebi
  subset: uberon/chebi_import.owl
- id: cl
  subset: uberon/cl_import.owl
- id: go
  subset: uberon/go_import.owl
- id: pr
  subset: uberon/pr_import.owl
depicted_by: https://raw.githubusercontent.com/jmcmurry/closed-illustrations/master/logos/uberon-logos/uberon_logo_black-banner.png
description: An integrated cross-species anatomy ontology covering animals and bridging multiple species-specific ontologies
domain: anatomy and development
funded_by:
- id: https://taggs.hhs.gov/Detail/AwardDetail?arg_AwardNum=R24OD011883&arg_ProgOfficeCode=205
  title: NIH R24-OD011883
- id: https://grantome.com/grant/NIH/R01-HG004838
  title: NIH R01-HG004838
- id: https://taggs.hhs.gov/Detail/AwardDetail?arg_AwardNum=P41HG002273&arg_ProgOfficeCode=55
  title: NIH P41-HG002273
- id: https://www.nsf.gov/awardsearch/showAward?AWD_ID=0956049
  title: NSF DEB-0956049
homepage: http://uberon.org
label: Uberon
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
mailing_list: https://lists.sourceforge.net/lists/listinfo/obo-anatomy
page: http://en.wikipedia.org/wiki/Uberon
preferredPrefix: UBERON
products:
- id: uberon.owl
  title: Uberon
  description: core ontology
  is_canonical: true
  type: owl:Ontology
- id: uberon/uberon-base.owl
  title: Uberon base ontology
  description: Axioms defined within Uberon and to be used in imports for other ontologies
  page: https://github.com/INCATools/ontology-development-kit/issues/50
- id: uberon/ext.owl
  title: Uberon edition that includes subsets of other ontologies and axioms connecting to them
  description: Uberon extended
  mireots_from: cl
  type: owl:Ontology
- id: uberon/basic.obo
  title: Uberon basic
  description: Uberon edition that excludes external ontologies and most relations
  format: obo
  type: obo-basic-ontology
- id: uberon/bridge/uberon-bridge-to-zfa.owl
  title: Uberon bridge to ZFA
  connects:
  - id: uberon
  - id: zfa
  description: Taxonomic equivalence axioms connecting zebrafish-specific classes to generic uberon counterparts
  page: https://github.com/obophenotype/uberon/wiki/inter-anatomy-ontology-bridge-ontologies
  type: BridgeOntology
- id: uberon/bridge/uberon-bridge-to-ma.owl
  title: Uberon bridge to MA
  connects:
  - id: uberon
  - id: ma
  description: Taxonomic equivalence axioms connecting adult mouse specific classes to generic uberon counterparts
  page: https://github.com/obophenotype/uberon/wiki/inter-anatomy-ontology-bridge-ontologies
  type: BridgeOntology
- id: uberon/composite-metazoan.owl
  title: Uberon composite metazoan ontology
  description: Extended uberon plus all metazoan ontologies
  page: https://github.com/obophenotype/uberon/wiki/Multi-species-composite-ontologies
  taxon: Metazoa
  type: MergedOntology
- id: uberon/composite-vertebrate.owl
  title: Uberon composite vertebrate ontology
  mireots_from:
  - zfa
  - xao
  - fbbt
  - wbbt
  - ma
  - fma
  - emapa
  - ehdaa2
  page: https://github.com/obophenotype/uberon/wiki/Multi-species-composite-ontologies
  taxon: Metazoa
  type: MergedOntology
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/22293552
  title: Uberon, an integrative multi-species anatomy ontology
- id: https://www.ncbi.nlm.nih.gov/pubmed/25009735
  title: Unification of multi-species vertebrate anatomy ontologies for comparative biology in Uberon
releases: http://purl.obolibrary.org/obo/uberon/releases/
repository: https://github.com/obophenotype/uberon
slack: https://obo-communitygroup.slack.com/archives/C01CR698CF2
taxon:
  id: NCBITaxon:33208
  label: Metazoa
tracker: https://github.com/obophenotype/uberon/issues
twitter: uberanat
usages:
- description: Bgee is a database to retrieve and compare gene expression patterns between animal species. Bgee in using Uberon to annotate the site of expression, and Bgee curators one the major contributors to the ontology.
  examples:
  - description: Uberon terms used to annotate expression of human hemoglobin subunit beta
    url: http://bgee.org/?page=gene&gene_id=ENSG00000244734
  seeAlso: https://fairsharing.org/FAIRsharing.x6d6sx
  type: annotation
  user: http://bgee.org/
- description: The National Human Genome Research Institute (NHGRI) launched a public research consortium named ENCODE, the Encyclopedia Of DNA Elements, in September 2003, to carry out a project to identify all functional elements in the human genome sequence. The ENCODE DCC users Uberon to annotate samples
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/25776021
    title: Ontology application and use at the ENCODE DCC
  seeAlso: https://doi.org/10.25504/FAIRsharing.v0hbjs
  type: annotation
  user: https://www.encodeproject.org/
- description: FANTOM5 is using Uberon and CL to annotate samples allowing for transcriptome analyses with cell-type and tissue-level specificity.
  examples:
  - description: FANTOM5 samples annotated to telencephalon or its parts
    url: http://fantom.gsc.riken.jp/5/sstar/UBERON:0001893
  type: annotation
  user: http://fantom5-collaboration.gsc.riken.jp/
- description: Querying expression and phenotype data
  type: query
  user: https://monarchinitiative.org/
- description: GO Database is used for querying for functional annotations relevant to a tissue
  examples:
  - description: GO annotations relevant to the uberon class for brain
    url: http://amigo.geneontology.org/amigo/term/UBERON:0000955
  type: query
  user: https://geneontology.org/
- description: The Phenoscape project is both a major driver of and contributor to Uberon, contibuting thousands of terms. The teleost (bony fishes) component of Uberon was derived from the Teleost Anatomy Ontology, developed by the Phenoscape group. Most of the high level design of the skeletal system comes from the Vertebrate Skeletal Anatomy Ontology (VSAO), also created by the Phenoscape group. Phenoscape curators continue to extend the ontology, covering a wide variety of tetrapod structures, with an emphasis on the appendicular system.
  user: http://phenoscape.org
- description: Searchable collection of neuroscience data and ontology for neuroscience
  type: Database
  user: https://neuinfo.org/
- description: cooperative data platform to be used by diverse communities in making data more FAIR.
  type: Database
  user: https://scicrunch.org/
- description: SCPortalen
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/29045713
    title: 'SCPortalen: human and mouse single-cell centric database'
  type: Database
  user: http://single-cell.clst.riken.jp/
- description: ChEMBL uses Uberon to describe organ/tissue information in assays
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/30398643
    title: 'ChEMBL: towards direct deposition of bioassay data'
  type: Database
  user: https://www.ebi.ac.uk/chembl/
wikidata_template: https://en.wikipedia.org/wiki/Template:Uberon
activity_status: active
---

Uberon is an integrated cross-species ontology covering anatomical structures in animals.
