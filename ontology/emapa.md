---
layout: ontology_detail
id: emapa
contact:
  email: Terry.Hayamizu@jax.org
  label: Terry Hayamizu
  github: tfhayamizu
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY 4.0
description: "An ontology for mouse anatomy covering embryonic development and postnatal stages."
domain: anatomy
homepage: http://www.informatics.jax.org/expression.shtml
tracker: https://github.com/obophenotype/mouse-anatomy-ontology/issues
products:
  - id: emapa.owl
  - id: emapa.obo
taxon:
  id: NCBITaxon:10088
  label: Mus
title: Mouse Developmental Anatomy Ontology
tracker: https://github.com/obophenotype/mouse-anatomy-ontology/issues
build:
  notes: new url soon
  source_url: ftp://ftp.hgu.mrc.ac.uk/pub/MouseAtlas/Anatomy/EMAPA.obo
  method: obo2owl
usages:
 - user: http://www.informatics.jax.org/expression.shtml
   seeAlso: https://www.biosharing.org/biodbcore-000659
   description: GXD
activity_status: active
---


## BACKGROUND

The ontology of mouse developmental anatomy was originally developed by Jonathan Bard and his colleagues as part of the Edinburgh Mouse Atlas Project (EMAP) in order to provide a structured controlled vocabulary of stage-specific anatomical structures for the developing laboratory mouse.[1]

Initial versions listed anatomical entities for each developmental stage (Theiler Stages 1 through 26) separately. Stage-specific instances were presented as uniparental hierarchies organized solely using part-of relationships (i.e. as a strict partonomy). An ‘abstract’ (i.e. non-stage-specific) representation of the mouse developmental anatomy ontology was subsequently developed.

The mouse developmental anatomy ontology has been substantially extended and refined over many years in a collaborative effort between EMAP and the Gene Expression Database (GXD) project (www.informatics.jax.org/expression.shtml), part of the Mouse Genome Informatics (MGI) resource at The Jackson Laboratory. The ontology continues to be maintained and expanded by GXD.

Overviews of the evolution and current status of the mouse anatomy ontologies, including some of the rationale for ontology content augmentation, restructuring of hierarchies, and other enhancements have been presented in various publications.[2,3,4]

## SUMMARY

An extensive ontology of mouse anatomical terms, entitled EMAPA, has been developed in order to represent both developmental and postnatal mouse anatomy in a standardized and searchable format. The current version of the ontology includes the following significant modifications (compared to the initial versions described above):

 * All instances for a given anatomical entity are presented as a single term, together with the first and last (i.e. start and end) Theiler stage at which the entity is considered to be present in the developing embryo.
 * Terms have unique names, with compound names constructed using standardized nomenclature conventions, and alternative names associated as synonyms.
 * Anatomical entities are presented in a hierarchical format that allows multiple parentage for a given entity (i.e. as a directed acyclic graph). 
 * Subsumption classification (“is_a”) as well as partonomic and other types of relationships (e.g. "develops_from") can now be represented.
 * The ontology has been extended through newborn (TS27) and postnatal (TS28) stages of mouse anatomy, with the latter substantially augmented by terma and relationships from the adult mouse anatomy (MA) ontology.[5]
 * The urinary and reproductive systems have been extensively revised and refined by curators from the GenitoUrinary Development Molecular Anatomy Project (GUDMAP).[6]
 * Extensive additions and revisions have been made in response to the expression annotation efforts of GXD, Edinburgh Mouse Atlas of Gene Expression (EMAGE)[7], GUDMAP and other projects.

GXD and other resources use the EMAPA ontology for annotation of mouse gene expression at embryonic and postnatal (including adult) stages. The GXD browser www.informatics.jax.org/vocab/gxd/anatomy enables users to navigate the ontology, to locate specific anatomical structures, and to obtain associated expression data in GXD.

The EMAPA ontology is available for download in OWL and OBO formats (see below).

# REFERENCES

 * [1] Bard JBL, Kaufman MH, Dubreuil C, Brune RM, Burger A, Baldock RA, Davidson DR (1998). An internet-accessible database of mouse developmental anatomy based on a systematic nomenclature. Mech Dev 74, 111-120.
 <https://www.sciencedirect.com/science/article/pii/S0925477398000690?via%3Dihub>
 * [2] Hayamizu TF, Wicks MN, Davidson DR, Burger A, Ringwald M, Baldock RA (2013). EMAP/EMAPA ontology of mouse developmental anatomy: 2013 update. Journal of Biomedical Semantics 4:15.
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3851555/>
 * [3] Hayamizu TF, Baldock RA, Ringwald M (2015). Mouse Anatomy Ontologies: Enhancements and Tools for Exploring and Integrating Biomedical Data. Mamm Genome 26, 422-30.
 <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4602063/>
 * [4] Hayamizu TF, Ringwald (2016). Textual Anatomics: the Mouse Developmental Anatomy Ontology and the Gene Expression Database for Mouse Development (GXD). In: Kaufman's Atlas of Mouse Development Supplement. Academic Press.
<https://www.sciencedirect.com/science/article/pii/B9780128000434000233>
 * [5] Hayamizu TF, Mangan M, Corradi JP, Kadin JA, Ringwald M (2005). The Adult Mouse Anatomical Dictionary: A tool for annotating and integrating data. Genome Biology 6:R29.
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1088948/>
 * [6] Little MH, Brennan J, Georgas K, Davies JA, Davidson DR, Baldock RA, Beverdam A, Bertram JF, Capel B, Chiu HS, Clements D, Cullen-McEwen L, Fleming J, Gilbert T, Herzlinger D, Houghton D, Kaufman MH, Kleymenova E, Koopman PA, Lewis AG, McMahon AP, Mendelsohn CL, Mitchell EK, Rumballe BA, Sweeney DE, Valerius MT, Yamada G, Yang Y, Yu J (2007). A high-resolution anatomical ontology of the developing murine genitourinary tract. Gene Exp Patterns 7, 680-99.
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2117077/>
 * [7] Richardson L, Venkataraman S, Stevenson P, Yang Y, Moss J, Graham L, Burton B, Hill B, Rao J, Baldock RA, Armit C (2014). EMAGE mouse embryo spatial gene expression database: 2014 update. Nucleic Acids Res. 42, D835-D844.
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3965061/>
