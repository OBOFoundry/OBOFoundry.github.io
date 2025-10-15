---
layout: ontology_detail
id: pr
title: PRotein Ontology (PRO)
browsers:
- title: BioPortal Browser
  label: BioPortal
  url: http://bioportal.bioontology.org/ontologies/PR?p=classes&conceptid=http://purl.obolibrary.org/obo/PR_000000001
- title: PRO Home
  label: PRO
  url: http://proconsortium.org
build:
  infallible: 0
  method: obo2owl
  oort_args: --no-reasoner
  source_url: https://proconsortium.org/download/current/pro_nonreasoned.obo
contact:
  email: dan5@georgetown.edu
  github: nataled
  label: Darren Natale
  orcid: 0000-0001-5809-9523
depicted_by: https://raw.githubusercontent.com/PROconsortium/logo/master/PROlogo_small.png
description: An ontological representation of protein-related entities
documentation: https://proconsortium.org/download/current/pro_readme.txt
domain: chemistry and biochemistry
homepage: http://proconsortium.org
in_foundry_order: 1
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
preferredPrefix: PR
products:
- id: pr.owl
  title: pro_reasoned.owl
  description: PRO after reasoning has been applied, OWL format. Add '.gz' for compressed.
- id: pr.obo
  title: pro_reasoned.obo
  description: PRO after reasoning has been applied, OBO format.
- id: pr-asserted.owl
  title: pro_nonreasoned.owl
  description: PRO without reasoning applied, OWL format. Add '.gz' for compressed.
- id: pr-asserted.obo
  title: pro_nonreasoned.obo
  description: PRO without reasoning applied, OBO format.
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/27899649
  title: 'Protein Ontology (PRO): enhancing and scaling up the representation of protein entities'
repository: https://github.com/PROconsortium/PRoteinOntology
tags:
- proteins
tracker: https://github.com/PROconsortium/PRoteinOntology/issues
usages:
- description: Colorado Richly Annotated Full-Text (CRAFT) Corpus; PRO is used for entity tagging and annotation
  examples:
  - description: Tagged entities (requires download)
    url: https://github.com/UCDenver-ccp/CRAFT/releases/tag/v4.0.1
  user: https://github.com/UCDenver-ccp/CRAFT
- description: Cell Ontology is a structured controlled vocabulary for cell types in animals; PRO is used for cell type definitions
  examples:
  - description: A B cell that is CD19-positive (uses the PRO term for non-species-specific CD19 molecule, PR:000001002)
    url: http://purl.obolibrary.org/obo/CL_0001201
  user: http://www.obofoundry.org/ontology/cl.html
activity_status: active
---

The PRotein Ontology (PRO) formally defines taxon-specific and taxon-neutral protein-related entities in three major areas: proteins related by evolution; proteins produced from a given gene; and protein-containing complexes.

Licensing and use: The PRotein Ontology is licensed under CC BY 4.0. You are free to share (copy and redistribute the material in any medium or format) and adapt (remix, transform, and build upon the material) for any purpose, even commercially. You must give appropriate credit (by using the original ontology IRI for the whole ontology or original term IRIs for individual terms), provide a link to the license, and indicate if any changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
