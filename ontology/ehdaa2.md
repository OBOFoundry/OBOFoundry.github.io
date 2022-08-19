---
layout: ontology_detail
id: ehdaa2
title: Human developmental anatomy, abstract
build:
  checkout: git clone https://github.com/obophenotype/human-developmental-anatomy-ontology.git
  method: vcs
  path: src/ontology
  system: git
contact:
  email: J.Bard@ed.ac.uk
  label: Jonathan Bard
dependencies:
- id: aeo
- id: caro
- id: cl
description: A structured controlled vocabulary of stage-specific anatomical structures of the developing human.
domain: anatomy and development
homepage: https://github.com/obophenotype/human-developmental-anatomy-ontology
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
products:
- id: ehdaa2.owl
- id: ehdaa2.obo
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/22973865
  title: A new ontology (structured hierarchy) of human developmental anatomy for the first 7 weeks (Carnegie stages 1-20).
repository: https://github.com/obophenotype/human-developmental-anatomy-ontology
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
tracker: https://github.com/obophenotype/human-developmental-anatomy-ontology/issues
activity_status: inactive
---

A structured controlled vocabulary of stage-specific anatomical structures of the human. It has been designed to mesh with the mouse anatomy and incorporates each Carnegie stage of development (CS1-20). The abstract version of the human developmental anatomy ontology compresses all the tissues present over Carnegie stages 1-20 into a single hierarchy. The heart, for example, is present from Carnegie Stage 9 onwards and is thus represented by 12 EHDA IDs (one for each stage). In the abstract mouse, it has a single ID so that the abstract term given as just <i>heart</i> really means <i>heart (CS 9-20)</i>. Timing details will be added to the abstract version of the ontology in a future release.

## Current Status (2022)

This ontology has been inactive for several years, as of 2022. As of yet there is no complete replacement ontology, but OBO users may want to consider potential alternatives:

 * [HsapDv](https://obofoundry.org/ontology/hsapdv) contains human-specific embryonic stage terms for Carnegie stages
 * [Uberon](https://obofoundry.org/ontology/uberon) includes embryonic anatomy and developmental stage relations, but is more taxonomically general than EHDAA2, and may be less complete and less precise. Uberon includes EHDAA2 in its composite metazoan build.
 * [FMA](https://obofoundry.org/ontology/fma) now includes some himan embryonic anatomy, but is constructed on different principles than EHDAA2, and may be less complete and less precise in places

As of 2022, EHDAA2 still has the most complete set of human structure to stage relationships of any ontology in OBO, but note that it is no longer updated.

## Details


This abstract version of the human developmental anatomy ontology compresses all the tissues present over Carnegie stages 1-20 into a single hierarchy. Its basis lies in a staged ontology of human development made more than a decade ago (Hunter et al, 2003) where the heart, for example, which is present from Carnegie Stage 9 onwards, was represented by 12 EHDA IDs (one for each stage). In this ''abstract'' version of the ontology, it has a single ID so that the abstract term given as just ''heart'' really means ''heart (CS 9-20)''.

The original, staged ontology needs replacing for several reasons

 1: The single ontology for each Carnegie stage is cumbersome and does not accord with modern practice.
 2: The terminology was inconsistent and the unique name of a issue was given by its full path. This only worked because each tissue had a single ''part_of'' parent. This was unsatisfactory because many tissues are naturally part of many systems (the femur is ''part_of'' the leg and ''part_of'' the skeleton).
 3. It turns out that some of the  timing was either wrong or not in accordance with standard texts published more recently (e.g. O'Rahilly & Muller, 2001)

This new version of the ontology is designed along the following lines.

 * a: every anatomical entity (AE) has a unique name
 * b: The basic relationship for navigation is ''part_of'' and AE's may have as many parents as is anatomically appropriate
 * c: every AE has a ''starts_at'' and ''ends_at'' stage
 * d: all leaf tissues carry a ''develops_from'' link, and this allows parentage to be traced back to the fertilized egg.
 * e: every AE is classified via an ''is_a'' relationship to the anatomical entities ontology (AEO)  [http://www.obofoundry.org/]; for details, see [http://www.obofoundry.org/wiki/index.php/AEO:Main_Page].

The version of the AEO currently used for annotating uses the EHDAA2 namespace (with AEO alt-ids). The intention is to replace that version with a new one that uses AEO ids and that is linked to a part version of the cell type ontology. 

## Details of versions and correction

 * 2011-12-16: Thus far the ontology has bee completely rebuilt from the original version (and I thank Mike Wicks [MRC-HGU] for computational help here), each term has been given a unique name, and every system other than that for the forebrain meets conditions a-e. Some checking of the ontology has been done, but no overall consistency checking has ben started.
 * 2012-01-11: The forebrain has been completed, a few errors have been corrected, some additional nuclei have been added and the is_a links have all been checked. The first draft is in place and all comments/criticisms/suggestions are welcome and should be mailed to j.bard@ed.ac.uk.
 * 2012-04-18: This version has a corrected namespace (human_developmental_anatomy), the extraembryonic tissues have been reorganised and simplified, a duplicated tissue has been reduced to a synonym and some timing errors have been coreected.
 * 2012-05-31: This version is a major upgrade following computational help by Mike Wicks (MRC Human Genetics Unit, Edinburgh).  All anatomical entities have had their EHDAA2 class ids replaced with AEO or CARO ids from today's version of the AEO. Timing and part_of inconsistencies have been corrected following computational checking, and this has led to many other minor changes.
 * 2012-06-25: the early lineage of the notochord has been corrected
 * 2013-01-09: the lung terminology has been corrected and some minor errors have been dealt with

EHDAA2 makes use of AEO, CARO and CL
