---
layout: ontology_detail
id: emap
title: Mouse gross anatomy and development, timed
build:
  insert_ontology_id: true
  method: obo2owl
  notes: new url soon
  source_url: ftp://ftp.hgu.mrc.ac.uk/pub/MouseAtlas/Anatomy/EMAP_combined.obo
contact:
  email: Terry.Hayamizu@jax.org
  github: tfhayamizu
  label: Terry Hayamizu
  orcid: 0000-0002-0956-8634
description: A structured controlled vocabulary of stage-specific anatomical structures of the mouse (Mus).
domain: anatomy and development
homepage: http://emouseatlas.org
is_obsolete: true
page: https://www.emouseatlas.org/emap/about/what_is_emap.html
products:
- id: emap.owl
replaced_by: emapa
taxon:
  id: NCBITaxon:10088
  label: Mus
activity_status: inactive
github_date_added: 2015-07-28
---

## BACKGROUND

The ontology of mouse developmental anatomy was originally developed by Jonathan Bard and his colleagues as part of the Edinburgh Mouse Atlas Project (EMAP) [http://www.emouseatlas.org/emap/home.html (www.emouseatlas.org)] in order to provide a structured controlled vocabulary of stage-specific anatomical structures for the developing laboratory mouse.[1]

The developmental mouse anatomy ontology has subsequently been substantially extended and refined in a collaborative effort between EMAP and the Gene Expression Database (GXD) project [http://www.informatics.jax.org/expression.shtml (www.informatics.jax.org/expression.shtml)], part of the Mouse Genome Informatics (MGI) resource at The Jackson Laboratory. Both GXD and the Edinburgh Mouse Atlas of Gene Expression (EMAGE) database project [http://www.emouseatlas.org/emage/home.php (www.emouseatlas.org/emage/home.php)] currently use this anatomy ontology to describe patterns of gene expression in the mouse embryo.

Previous versions, such as the one posted on the OBO Foundry site under the filename EMAP.obo, listed the anatomical entities for each developmental stage (Theiler Stages 1 through 26) separately. Stage-specific instances were presented as uniparental hierarchical trees organized using part-of relationships only (i.e. as a strict partonomy). These hierarchies have been used for annotation of expression in both the EMAGE and GXD databases, and the associated identifiers for the stage-specific instances are preserved.

## EMAPA

A significantly revised and expanded ‘abstract’ (i.e. non-stage-specific) representation of the mouse developmental anatomy ontology has since been developed. This version, entitled EMAPA, includes the following significant modifications:

 * All instances for a given anatomical entity are presented as a single term, together with the first and last (i.e. start and end) Theiler stage at which the entity is considered to be present in the developing embryo.
 * Anatomical entities are presented in a hierarchical format that allows multiple parentage for a given entity (i.e. as a directed acyclic graph). Subsumption classification (“is_a”) as well as partonomic and other types of relationships can now be represented.
 * Numerous anatomical terms have been added in response to the needs of expression annotation efforts of both EMAGE and GXD.
 * The urinary and reproductive systems have been extensively revised and refined by curators from the GenitoUrinary Development Molecular Anatomy Project (GUDMAP).[2]
 * Most of the anatomical terms now have unique names, with compound names constructed using standardized nomenclature conventions, and alternative names associated as synonyms.

The EMAPA mouse developmental anatomy ontology is now available for download as an obo-formatted file as [ftp://ftp.hgu.mrc.ac.uk/pub/MouseAtlas/Anatomy/EMAPA.obo EMAPA.obo].

In earlier versions of the mouse developmental anatomy ontology, timed-components (EMAP, described  below) were regarded as primary and the non-stage-specific ‘abstract’ terms were secondary. Now the abstract anatomy with associated EMAPA identifiers is considered to be the primary anatomy ontology and should be the terms and identifiers used for use of the ontology in most cases of data annotation and as links to other anatomy ontologies.

## EMAP

Based on the information contained in the EMAPA file for each abstract term, stage-specific terms with associated EMAP identifiers have been instantiated. The resulting revised and expanded set of terms and identifiers includes and is consistent with previous versions of the mouse developmental anatomy.

Furthermore, hierarchies for each of the Theiler stages for mouse development, now presented as separate directed acyclic graphs, have been derived. An obo-formatted file containing all 26 stages has been created to enable visualization of relevant anatomical terms at specific stages. The combined file has been made available as [ftp://ftp.hgu.mrc.ac.uk/pub/MouseAtlas/Anatomy/EMAP_combined.obo EMAP_combined.obo].

[[Image:EMAP-EMAPA.png]]

# MAPPING BETWEEN EMAP AND EMAPA

A number of resources, including GXD and EMAGE, currently utilize stage-specific EMAP terms for data annotation. In order to facillitate interoperability of resources using different sets of developmental mouse anatomy terms, a file has been created in which all corresponding EMAP and EMAPA terms have been mapped. This file is available as [ftp://ftp.hgu.mrc.ac.uk/pub/MouseAtlas/Anatomy/EMAP-EMAPA.txt EMAP-EMAPA.txt].

# REFERENCES

 * [1] Bard JBL, Kaufman MH, Dubreuil C, Brune RM, Burger A, Baldock RA, Davidson DR (1998).  [http://www.emouseatlas.org/emap/about/PDF/Bard_IAdbase.pdf?cmd=Retrieve&db=PubMed&list_uids=9651497&dopt=abstract An internet-accessible database of mouse developmental anatomy based on a systematic nomenclature.] Mech Dev 74, 111-120.
 * [2] Little MH, Brennan J, Georgas K, Davies JA, Davidson DR, Baldock RA, Beverdam A, Bertram JF, Capel B, Chiu HS, Clements D, Cullen-McEwen L, Fleming J, Gilbert T, Herzlinger D, Houghton D, Kaufman MH, Kleymenova E, Koopman PA, Lewis AG, McMahon AP, Mendelsohn CL, Mitchell EK, Rumballe BA, Sweeney DE, Valerius MT, Yamada G, Yang Y, Yu J (2007). [http://www.emouseatlas.org/emap/about/PDF/Little_murineGT.pdf A high-resolution anatomical ontology of the developing murine genitourinary tract.] Gene Exp Patterns 7, 680-99.
