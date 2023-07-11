---
layout: ontology_detail
id: dron
title: The Drug Ontology
build:
  method: owl2obo
  source_url: http://purl.obolibrary.org/obo/dron.owl
contact:
  email: hoganwr@gmail.com
  github: hoganwr
  label: William Hogan
  orcid: 0000-0002-9881-1017
description: An ontology to support comparative effectiveness researchers studying claims data.
domain: health
homepage: https://github.com/ufbmi/dron
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
preferredPrefix: DRON
products:
- id: dron.owl
publications:
- id: https://doi.org/10.1186/s13326-017-0121-5
  title: 'Therapeutic indications and other use-case-driven updates in the drug ontology: anti-malarials, anti-hypertensives, opioid analgesics, and a large term request'
repository: https://github.com/ufbmi/dron
tracker: https://github.com/ufbmi/dron/issues
usages:
- description: DrOn is used for the classification of Drugs, in particular, based on RxNorm codes, in the PennTURBO project.
  examples:
  - description: 'From the documentation: For example, the text `500 mg Tylenol po tabs` might be mapped to http://purl.obolibrary.org/obo/DRON_00073395, with the label `Acetaminophen 500 MG Oral Tablet [Tylenol]`. DrOn knows that this is a subclass of `Acetaminophen 500 MG Oral Tablet` (through its logical axiomatisation).'
    url: https://pennturbo.github.io/Turbo-Documentation/medication_text_to_terms_to_roles.html
  type: annotation
  user: https://github.com/PennTURBO
activity_status: active
---

We built this ontology primarily to support comparative effectiveness researchers studying claims data. They need to be able to query U.S. National Drug Codes (NDCs) by ingredient, mechanism of action (beta-adrenergic blockade), physiological effect (diuresis), and therapeutic intent (anti-hypertensive).
