---
layout: ontology_detail
id: ms
label: MS
description: A structured controlled vocabulary for the annotation of experiments concerned with proteomics mass spectrometry.
title: Mass spectrometry ontology
createdWith: http://oboedit.org
contact:
  email: gerhard.mayer@rub.de
  label: Gerhard Mayer
integration_server: https://raw.githubusercontent.com/HUPO-PSI/psi-ms-CV/master
domain: MS experiments
mailing_list: psidev-ms-vocab@lists.sourceforge.net
homepage: http://www.psidev.info/groups/controlled-vocabularies
tracker: https://github.com/HUPO-PSI/psi-ms-CV/issues
page: http://www.psidev.info/groups/controlled-vocabularies
dependencies:
  - id: pato
  - id: uo
publications:
  - id: http://www.ncbi.nlm.nih.gov/pubmed/23482073
    title: "The HUPO proteomics standards initiative- mass spectrometry controlled vocabulary."
products:
  - id: ms.obo
  - id: ms.owl
license:
  url: https://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
build:
  source_url: https://raw.githubusercontent.com/HUPO-PSI/psi-ms-CV/master/psi-ms.obo
  method: obo2owl
activity_status: active
repository: https://github.com/HUPO-PSI/psi-ms-CV
preferredPrefix: MS
---

A structured controlled vocabulary for the annotation of experiments concerned with proteomics mass spectrometry. Developed by the HUPO Proteomics Standards Initiative (PSI).

## Mailing Lists

 * https://lists.sourceforge.net/lists/listinfo/psidev-ms-vocab
