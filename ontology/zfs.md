---
layout: ontology_detail
id: zfs
in_foundry: false
contact:
  email: van_slyke@zfin.org
  label: Ceri Van Slyke
description: Developmental stages of the Zebrafish
domain: anatomy
homepage: https://wiki.zfin.org/display/general/Anatomy+Atlases+and+Resources
page: https://github.com/obophenotype/developmental-stage-ontologies/wiki/ZFS
tracker: https://github.com/cerivs/zebrafish-anatomical-ontology/issues
products:
  - id: zfs.owl
  - id: zfs.obo
taxon:
  id: NCBITaxon:7954
  label: Danio
title: Zebrafish developmental stages ontology
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
build:
  source_url: https://raw.githubusercontent.com/obophenotype/developmental-stage-ontologies/master/src/zfs/zfs.obo
  method: obo2owl
  infallible: 1
activity_status: active
repository: https://github.com/cerivs/zebrafish-anatomical-ontology
preferredPrefix: ZFS
---

An ontology of developmental stages of the Zebrafish (<i>Danio rerio</i>). Note that ZFA includes the leaf nodes of this ontology
