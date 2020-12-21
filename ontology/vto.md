---
layout: ontology_detail
id: vto
title: Vertebrate Taxonomy Ontology
description: Comprehensive hierarchy of extinct and extant vertebrate taxa.
products:
  - id: vto.owl
  - id: vto.obo
homepage: https://github.com/phenoscape/vertebrate-taxonomy-ontology
tracker: https://github.com/phenoscape/vertebrate-taxonomy-ontology/issues
redirects:
  - match: ""
    url: "http://vertebrate-taxonomy-ontology.s3-website-us-west-2.amazonaws.com/releases/"
contact:
  label: Jim Balhoff
  email: balhoff@renci.org
license:
  url: http://creativecommons.org/publicdomain/zero/1.0/
  label: CC-0
usages:
 - user: http://phenoscape.org
   description: Phenoscape uses VTO to annotate systematics data
activity_status: active
---

The Vertebrate Taxonomy Ontology includes both extinct and extant vertebrates, aiming to provide one comprehensive hierarchy. The hierarchy backbone for extant taxa is based on the NCBI taxonomy. Since the NCBI taxonomy only includes species associated with archived genetic data, to complement this, we also incorporate taxonomic information across the vertebrates from the Paleobiology Database (PaleoDB). The Teleost Taxonomy Ontology (TTO) and AmphibiaWeb (AWeb) are incorporated to provide a more authoritative hierarchy and a richer set of names for specific taxonomic groups.
