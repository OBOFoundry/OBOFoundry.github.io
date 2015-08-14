---
layout: ontology_detail
id: lipro
in_foundry: false
contact: 
  email: bakerc@unb.ca
  label: Christipher Baker
description: An ontology representation of the LIPIDMAPS nomenclature classification.
domain: lipids
products: 
  - id: lipro.owl
title: Lipid Ontology
build:
  source_url: http://www.lipidprofiles.com/LipidOntology
  method: owl2obo
---

Lipid research is increasingly integrated within systems level biology such as lipidomics where lipid classification is required before appropriate annotation of chemical functions can be applied. The ontology describes the LIPIDMAPS nomenclature classification explicitly using description logics (OWL-DL). Lipid classes are organized hierarchically with the super-classes restricted by generic necessary conditions. More specific necessary conditions are used to define membership requirements for sub classes of lipid according to appropriate functional groups.
