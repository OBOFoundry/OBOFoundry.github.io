---
layout: ontology_detail
id: aeo
title: Anatomical Entity Ontology
build:
  checkout: git clone https://github.com/obophenotype/human-developmental-anatomy-ontology.git
  method: vcs
  path: src/ontology
  system: git
contact:
  email: J.Bard@ed.ac.uk
  label: Jonathan Bard
description: AEO is an ontology of anatomical structures that expands CARO, the Common Anatomy Reference Ontology
domain: anatomy and development
github_date_added: 2015-07-28
homepage: https://github.com/obophenotype/human-developmental-anatomy-ontology/
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: AEO
products:
- id: aeo.owl
repository: https://github.com/obophenotype/human-developmental-anatomy-ontology
tracker: https://github.com/obophenotype/human-developmental-anatomy-ontology/issues
activity_status: inactive
---

The AEO is an ontology of anatomical structures that expands CARO, the Common Anatomy Reference Ontology, to about 160 classes using the is_a relationship; it thus provides a detailed type classification for tissues. The ~100 new classes were chosen for their use in categorizing the major vertebrate and invertebrate anatomy ontologies at a granularity adequate for tissues of a single cell type. This site is to be used for posting details of the ontologies and updates

The AEO is intended to be useful in increasing the amount of knowledge in anatomy ontologies, facilitating annotation and enabling interoperability across anatomy ontologies.

An important subcategory of the AEO is simple tissue (a synonym of the CARO portion of tissue), a recognisable anatomical entity composed predominantly to a single cell type. CARO had a only few epithelial classes here and these are inadequate for capturing the richness of anatomical tissue knowledge. The AEO has ~70 simple tissues and these are linked to their cell types (~100) as detailed in the cell type ontology through a has_part relationship. The AEO thus includes a subset of the cell type ontology.

The AEO has been refined through its use in annotating the ~2500 terms of the new version of the Ontology of Developing Human Anatomy [namespace: EHDAA2 [1]] and, while this has improved the ontology, it may have given it a mammalian bias.

The ontology can be used to classify most organisms as its terms are appropriate for most plant and fungal tissues. I plan to improve the ontology to include more non-animal anatomical terms.

Anyone interested is welcome to look at the ontology and post comments/criticisms/suggestions on this site. I would appreciate it if they also emailed the text to j.bard@ed.ac.uk

*Jonathan Bard*

## Updates

 * 2011/12/15: This version of the AEO includes some reasoning links [disjoint_from, transitive] and more are planned.
 * 2012/05/31: This version includes the new term "reproductive cell population" and the associated cell types
