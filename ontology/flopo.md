---
layout: ontology_detail
id: to
contact:
  email: robert.hoehndorf@kaust.edu.sa
  label: Robert Hoehndorf
description: phenotypes occurring in flora files
domain: phenotype
homepage: https://github.com/flora-phenotype-ontology/flopoontology
license:
  url: https://creativecommons.org/about/cc0
products:
  - id: flopo.owl
taxon:
  id: NCBITaxon:33090
  label: Viridiplantae
title: FLOPO phenotype ontology
tracker: https://github.com/flora-phenotype-ontology/flopoontology/issues
---

Project to identify phenotypes occurring in flora files.

There are three components:

    ParseFloraFile is the original piece of code generated at the pro-iBiosphere Hackathon in Leiden. It will find PO and PATO terms in flora gabon and malaysia.
    Lucene-based indexing: this is a refactoring of the original code that uses the Lucence indexes and analyzers.
    MakePlantPhenotypeOntology generates a phenotype ontology from the generated descriptions.

The resulting ontology is available under a CC-0 license in the ontology folder. All code is available under the BSD license.
