---
layout: ontology_detail
id: nomen
label: NOMEN
title: NOMEN - A nomenclatural ontology for biological names
contact:
  email: diapriid@gmail.com
  label: Matt Yoder
  github: mjy
  orcid: 0000-0002-5640-5491
license:
  url: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
description: NOMEN is a nomenclatural ontology for biological names (not concepts).  It encodes the goverened rules of nomenclature.
domain: information
tags:
  - biological nomenclature
homepage: https://github.com/SpeciesFileGroup/nomen
products:
  - id: nomen.owl
    type: owl:Ontology
    title: NOMEN
    description: "core ontology"
    is_canonical: true
build:
  checkout: git clone https://github.com/SpeciesFileGroup/nomen.git
  system: git
usages:
  - user: https://taxonworks.org
    seeAlso: https://github.com/SpeciesFileGroup/taxonworks
    description: TaxonWorks is an integrated web-based workbench for taxonomists and biodiversity scientists.
    type: application
mailing_list: https://groups.google.com/forum/#!forum/nomen-discuss
tracker: https://github.com/SpeciesFileGroup/nomen/issues
funded_by:
  - "NSF-ABI-1356381"
  - "Species File Group"
canonical: nomen.owl
activity_status: active
repository: https://github.com/SpeciesFileGroup/nomen
preferredPrefix: NOMEN
---

NOMEN is a nomenclatural ontology for biological names (not concepts).  See the <a href="https://github.com/SpeciesFileGroup/nomen">NOMEN homepage</a> for more info.
