---
layout: ontology_detail
id: vario
title: Variation Ontology
build:
  method: obo2owl
  source_url: http://variationontology.org/vario_download/vario.obo
contact:
  email: mauno.vihinen@med.lu.se
  github: maunov
  label: Mauno Vihinen
  orcid: 0000-0002-9614-7976
description: Variation Ontology, VariO, is an ontology for standardized, systematic description of effects, consequences and mechanisms of variations.
domain: biological systems
homepage: http://variationontology.org
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: VariO
products:
- id: vario.owl
  title: VariO in OWL Functional notation
- id: vario.owx
  title: VariO in OWL RDF/XML
- id: vario.obo
  title: VariO in OBO
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/24162187
  title: Variation Ontology for annotation of variation effects and mechanisms
- id: https://www.ncbi.nlm.nih.gov/pubmed/24533660
  title: 'Variation ontology: annotator guide'
- id: https://www.ncbi.nlm.nih.gov/pubmed/25616435
  title: Types and effects of protein variations
activity_status: inactive
---

## Requirements to become "active"

The following are necessary to change the `activity_status` to "active":

1. Needs public issue tracker (required by metadata schema checks). For example,
   this could be done via github even if the ontology is not maitained there, as
   ChEBI and PR do. This is part of the OBO foundry standard at https://obofoundry.org/principles/fp-020-responsiveness.html.
2. PURL configuration needs to be improved:
   - redirect http://purl.obolibrary.org/obo/vario.owl and http://purl.obolibrary.org/obo/vario.owx to latest versions
   - provide an OBO version of the latest, i.e.:
     - http://www.variationontology.org/vario_download/VariO_1.09.owl (functional format)
     - http://www.variationontology.org/vario_download/VariO_1.09.owx (RDF/XML)

## Nice to have

- Organize the various versions into OBO's standard folder structure
- Fix file extensions to match OBO standard (i.e., RDF/XML has .owl extension and functional has .ofn)

