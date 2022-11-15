---
layout: ontology_detail
id: cteno
title: Ctenophore Ontology
build:
  checkout: git clone https://github.com/obophenotype/ctenophore-ontology.git
  method: vcs
  path: .
  system: git
contact:
  email: cjmungall@lbl.gov
  github: cmungall
  label: Chris Mungall
  orcid: 0000-0002-6601-2165
dependencies:
- id: ro
- id: uberon
description: An anatomical and developmental ontology for ctenophores (Comb Jellies)
domain: anatomy and development
homepage: https://github.com/obophenotype/ctenophore-ontology
jobs:
- id: https://travis-ci.org/obophenotype/ctenophore-ontology
  type: travis-ci
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: CTENO
products:
- id: cteno.owl
repository: https://github.com/obophenotype/ctenophore-ontology
taxon:
  id: NCBITaxon:10197
  label: Ctenophore
tracker: https://github.com/obophenotype/ctenophore-ontology/issues
activity_status: active
---

An anatomical and developmental ontology for ctenophores (Comb Jellies).

<img alt="Haeckel Ctenophorae" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Haeckel_Ctenophorae.jpg/440px-Haeckel_Ctenophorae.jpg"/>

This ontology is available as a standalone artefact, and is also available as part of Uberon composite-metaozoan
