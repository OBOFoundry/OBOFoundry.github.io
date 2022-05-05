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
publications:
  - id: https://doi.org/10.1186/2041-1480-4-34
    title: The vertebrate taxonomy ontology: a framework for reasoning across model organism and species phenotypes
contact:
  label: Jim Balhoff
  email: balhoff@renci.org
  github: balhoff
  orcid: 0000-0002-8688-6599
license:
  url: http://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
usages:
  - user: http://phenoscape.org
    description: Phenoscape uses VTO to annotate systematics data
activity_status: active
repository: https://github.com/phenoscape/vertebrate-taxonomy-ontology
preferredPrefix: VTO
---

The Vertebrate Taxonomy Ontology includes both extinct and extant vertebrates, aiming to provide one comprehensive hierarchy. The hierarchy backbone for extant taxa is based on the NCBI taxonomy. Since the NCBI taxonomy only includes species associated with archived genetic data, to complement this, we also incorporate taxonomic information across the vertebrates from the Paleobiology Database (PaleoDB). The Teleost Taxonomy Ontology (TTO) and AmphibiaWeb (AWeb) are incorporated to provide a more authoritative hierarchy and a richer set of names for specific taxonomic groups.
