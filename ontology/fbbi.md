---
layout: ontology_detail
id: fbbi
title: Biological Imaging Methods Ontology
browsers:
- title: BioPortal Browser
  label: BioPortal
  url: https://bioportal.bioontology.org/ontologies/FBbi
build:
  checkout: git clone https://github.com/foundingGIDE/fbbi.git
  path: .
  system: git
contact:
  email: damien@gerbi-gmb.de
  github: gouttegd
  label: Damien Goutte-Gattat
  orcid: 0000-0002-6095-8718
dependencies:
- id: iao
- id: omo
- id: ro
description: An ontology for the description of sample preparation, visualization, and imaging methods used in biomedical research.
domain: investigations
homepage: https://github.com/foundingGIDE/fbbi
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: FBbi
products:
- id: fbbi.owl
- id: fbbi.obo
- id: fbbi/fbbi-base.owl
- id: fbbi/fbbi-base.obo
repository: https://github.com/foundingGIDE/fbbi
tags:
- imaging experiments
tracker: https://github.com/foundingGIDE/fbbi/issues
usages:
- description: FlyBase uses FBbi to annotate its image collection.
  examples:
  - description: images annotated to "scanning electron micrograph"
    url: https://flybase.org/cgi-bin/fbcvquery.pl?mode=subtreehits&cvterm=FBbi:00000257%3EFBim
  user: https://flybase.org
- description: Virtual Fly Brain uses FBbi to annotate images.
  user: https://virtualflybrain.org
- description: The Cell Image Library uses FBbi to annotate images.
  examples:
  - description: An image annotate with several terms from FBbi.
    url: https://www.cellimagelibrary.org/images/13654
  user: https://www.cellimagelibrary.org
activity_status: active
---
