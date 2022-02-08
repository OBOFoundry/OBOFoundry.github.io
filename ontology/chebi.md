---
layout: ontology_detail
id: chebi
in_foundry_order: 1
alternatePrefix: ChEBI
title: Chemical Entities of Biological Interest
review:
  date: 2010
build:
  source_url: ftp://ftp.ebi.ac.uk/pub/databases/chebi/ontology/chebi.obo
  method: obo2owl
  infallible: 1
description: A structured classification of molecular entities of biological interest focusing on 'small' chemical compounds.
twitter: chebit
contact:
  email: amalik@ebi.ac.uk
  label: Adnan Malik
  github: "amalik01"
  orcid: 0000-0001-8123-5351
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
domain: biochemistry
homepage: http://www.ebi.ac.uk/chebi
page: http://www.ebi.ac.uk/chebi/init.do?toolBarForward=userManual
depicted_by: https://www.ebi.ac.uk/chebi/images/ChEBI_logo.png
publications:
  - id: http://europepmc.org/article/MED/26467479
    title: "ChEBI in 2016: Improved services and an expanding collection of metabolites."
browsers:
  - label: CHEBI
    title: EBI CHEBI Browser
    url: http://www.ebi.ac.uk/chebi/chebiOntology.do?treeView=true&chebiId=CHEBI:24431#graphView
products:
  - id: chebi.owl
  - id: chebi.obo
  - id: chebi.owl.gz
    title: "chebi, compressed owl"
  - id: chebi/chebi_lite.obo
    title: "chebi_lite, no syns or xrefs"
  - id: chebi/chebi_core.obo
    title: "chebi_core, no xrefs"
tracker: https://github.com/ebi-chebi/ChEBI/issues
usages:
  - user: https://www.rhea-db.org/
    description: Rhea uses CHEBI to annotate reaction participants
    examples:
      - url: https://www.rhea-db.org/searchresults?q=CHEBI:29748
        description: "Query for all usages of CHEBI:29748 (chorismate)"
  - user: http://zfin.org
    description: ZFIN uses CHEBI to annotate experiments
    examples:
      - url: http://zfin.org/action/expression/experiment?id=ZDB-EXP-190627-10
        description: "A curated zebrafish experiment involving exposure to (5Z,8Z,14Z)-11,12-dihydroxyicosatrienoic acid (CHEBI:63969)"
activity_status: active
repository: https://github.com/ebi-chebi/ChEBI
preferredPrefix: CHEBI
---

A freely available dictionary of molecular entities focused on ‘small’ chemical compounds.
The term ‘molecular entity’ refers to any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer, etc., identifiable as a separately distinguishable entity. The molecular entities in question are either products of nature or synthetic products used to intervene in the processes of living organisms.

ChEBI incorporates an ontological classification, whereby the relationships between molecular entities or classes of entities and their parents and/or children are specified.

ChEBI uses nomenclature, symbolism and terminology endorsed by the following international scientific bodies:

- International Union of Pure and Applied Chemistry (IUPAC)
- Nomenclature Committee of the International Union of Biochemistry and Molecular Biology (NC-IUBMB)

Molecules directly encoded by the genome (e.g. nucleic acids, proteins and peptides derived from proteins by cleavage) are not as a rule included in ChEBI.
