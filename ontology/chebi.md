---
layout: ontology_detail
id: chebi
title: Chemical Entities of Biological Interest
browsers:
- title: EBI CHEBI Browser
  label: CHEBI
  url: http://www.ebi.ac.uk/chebi/chebiOntology.do?treeView=true&chebiId=CHEBI:24431#graphView
build:
  infallible: 1
  method: obo2owl
  source_url: ftp://ftp.ebi.ac.uk/pub/databases/chebi/ontology/chebi.obo
contact:
  email: amalik@ebi.ac.uk
  github: amalik01
  label: Adnan Malik
  orcid: 0000-0001-8123-5351
depicted_by: https://www.ebi.ac.uk/chebi/chebi_logo.svg
description: A structured classification of molecular entities of biological interest focusing on 'small' chemical compounds.
domain: chemistry and biochemistry
homepage: http://www.ebi.ac.uk/chebi
in_foundry_order: 1
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
page: http://www.ebi.ac.uk/chebi/init.do?toolBarForward=userManual
preferredPrefix: CHEBI
products:
- id: chebi.owl
- id: chebi.obo
- id: chebi.owl.gz
  title: chebi, compressed owl
- id: chebi/chebi_lite.obo
  title: chebi_lite, no syns or xrefs
- id: chebi/chebi_core.obo
  title: chebi_core, no xrefs
publications:
- id: https://doi.org/10.1093/nar/gkaf1271
  title: 'ChEBI: re-engineered for a sustainable future'
- id: https://www.ncbi.nlm.nih.gov/pubmed/26467479
  title: 'ChEBI in 2016: Improved services and an expanding collection of metabolites.'
repository: https://github.com/ebi-chebi/ChEBI
tracker: https://github.com/ebi-chebi/ChEBI/issues
twitter: chebit
usages:
- description: Rhea uses CHEBI to annotate reaction participants
  examples:
  - description: Query for all usages of CHEBI:29748 (chorismate)
    url: https://www.rhea-db.org/searchresults?q=CHEBI:29748
  user: https://www.rhea-db.org/
- description: ZFIN uses CHEBI to annotate experiments
  examples:
  - description: A curated zebrafish experiment involving exposure to (5Z,8Z,14Z)-11,12-dihydroxyicosatrienoic acid (CHEBI:63969)
    url: http://zfin.org/action/expression/experiment?id=ZDB-EXP-190627-10
  user: http://zfin.org
activity_status: active
---

A freely available dictionary of molecular entities focused on ‘small’ chemical compounds.
The term ‘molecular entity’ refers to any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer, etc., identifiable as a separately distinguishable entity. The molecular entities in question are either products of nature or synthetic products used to intervene in the processes of living organisms.

ChEBI incorporates an ontological classification, whereby the relationships between molecular entities or classes of entities and their parents and/or children are specified.

ChEBI uses nomenclature, symbolism and terminology endorsed by the following international scientific bodies:

- International Union of Pure and Applied Chemistry (IUPAC)
- Nomenclature Committee of the International Union of Biochemistry and Molecular Biology (NC-IUBMB)

Molecules directly encoded by the genome (e.g. nucleic acids, proteins and peptides derived from proteins by cleavage) are not as a rule included in ChEBI.
