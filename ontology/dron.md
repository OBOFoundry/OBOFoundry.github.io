---
layout: ontology_detail
id: dron
contact:
  email: hoganwr@gmail.com
  label: William Hogan
  github: hoganwr
  orcid: 0000-0002-9881-1017
description: An ontology to support comparative effectiveness researchers studying claims data.
domain: health
homepage: https://github.com/ufbmi/dron
products:
  - id: dron.owl
title: The Drug Ontology
build:
  source_url: http://purl.obolibrary.org/obo/dron.owl
  method: owl2obo
tracker: https://github.com/ufbmi/dron/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
activity_status: active
repository: https://github.com/ufbmi/dron
preferredPrefix: DRON
publications:
  - id: https://doi.org/10.1186/s13326-017-0121-5
    title: "Therapeutic indications and other use-case-driven updates in the drug ontology: anti-malarials, anti-hypertensives, opioid analgesics, and a large term request"
added: 2015-07-28
---

We built this ontology primarily to support comparative effectiveness researchers studying claims data. They need to be able to query U.S. National Drug Codes (NDCs) by ingredient, mechanism of action (beta-adrenergic blockade), physiological effect (diuresis), and therapeutic intent (anti-hypertensive).
