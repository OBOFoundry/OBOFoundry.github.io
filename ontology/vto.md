---
layout: ontology_detail
id: vto
title: Vertebrate Taxonomy Ontology
contact:
  email: balhoff@renci.org
  github: balhoff
  label: Jim Balhoff
  orcid: 0000-0002-8688-6599
description: Comprehensive hierarchy of extinct and extant vertebrate taxa.
domain: organisms
github_date_added: 2015-07-28
homepage: https://github.com/phenoscape/vertebrate-taxonomy-ontology
license:
  label: CC0 1.0
  url: http://creativecommons.org/publicdomain/zero/1.0/
preferredPrefix: VTO
products:
- id: vto.owl
- id: vto.obo
publications:
- id: https://doi.org/10.1186/2041-1480-4-34
  title: 'The vertebrate taxonomy ontology: a framework for reasoning across model organism and species phenotypes'
repository: https://github.com/phenoscape/vertebrate-taxonomy-ontology
tracker: https://github.com/phenoscape/vertebrate-taxonomy-ontology/issues
usages:
- description: Phenoscape uses VTO to annotate systematics data
  user: http://phenoscape.org
activity_status: active
---

The Vertebrate Taxonomy Ontology includes both extinct and extant vertebrates, aiming to provide one comprehensive hierarchy. The hierarchy backbone for extant taxa is based on the NCBI taxonomy. Since the NCBI taxonomy only includes species associated with archived genetic data, to complement this, we also incorporate taxonomic information across the vertebrates from the Paleobiology Database (PaleoDB). The Teleost Taxonomy Ontology (TTO) and AmphibiaWeb (AWeb) are incorporated to provide a more authoritative hierarchy and a richer set of names for specific taxonomic groups.
