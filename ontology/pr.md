---
layout: ontology_detail
id: pr
in_foundry_order: 1
contact:
  email: dan5@georgetown.edu
  label: Darren Natale
description: An ontological representation of protein-related entities
domain: proteins
homepage: http://proconsortium.org
documentation: ftp://ftp.pir.georgetown.edu/databases/ontology/pro_obo/pro_readme.txt
products:
  - id: pr.owl
title: PRotein Ontology (PRO)
license:
  url: http://creativecommons.org/licenses/by/4.0/
  label: CC-BY
depicted_by: https://avatars3.githubusercontent.com/u/13786296?v=3&u=eb64f0704c2c089036918b9604fce4db7e72132c&s=140
build:
  oort_args: --no-reasoner
  source_url: ftp://ftp.pir.georgetown.edu/databases/ontology/pro_obo/pro.obo
  method: obo2owl
  infallible: 0
tracker: http://sourceforge.net/tracker/?group_id=266825&atid=1135711
development:
  id_policy: https://pir17.georgetown.edu/confluence/display/PROWIKI/PRO+URI+policy
---

PRotein Ontology (PRO) has been designed to describe the relationships of proteins and protein evolutionary classes (ontology for ProEvo), to delineate the multiple protein forms of a gene locus (ontology for protein forms), and to interconnect existing ontologies
