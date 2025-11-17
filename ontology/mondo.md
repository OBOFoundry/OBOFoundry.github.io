---
layout: ontology_detail
id: mondo
title: Mondo Disease Ontology
browsers:
- title: Monarch Initiative Disease Browser
  label: Monarch
  url: https://monarchinitiative.org/disease/MONDO:0019609
canonical: mondo.owl
contact:
  email: Sabrina@tislab.org
  github: sabrinatoro
  label: Sabrina Toro
  orcid: 0000-0002-4142-7153
depicted_by: https://raw.githubusercontent.com/monarch-initiative/mondo/master/docs/images/mondo_logo_black-stacked-small.png
description: A global community effort to harmonize multiple disease resources to yield a coherent merged ontology.
domain: health
homepage: https://monarch-initiative.github.io/mondo
label: Mondo
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
mailing_list: https://groups.google.com/group/mondo-users
preferredPrefix: MONDO
products:
- id: mondo.owl
  title: Mondo OWL edition
  description: Complete ontology with merged imports.
  format: owl-rdf/xml
  is_canonical: true
- id: mondo.obo
  title: Mondo OBO Format edition
  derived_from: mondo.owl
  description: OBO serialization of mondo.owl.
  format: obo
- id: mondo.json
  title: Mondo JSON edition
  derived_from: mondo.owl
  description: Obographs serialization of mondo.owl.
  format: obo
- id: mondo/mondo-base.owl
  title: Mondo Base Release
  description: The main ontology plus axioms connecting to select external ontologies, excluding the external ontologies themselves
  format: owl
- id: mondo/mondo-simple.owl
  title: Mondo Simple Release
  description: The main ontology classes and their hierarchies, without references to external terms.
  format: owl
publications:
- id: https://doi.org/10.1093/genetics/iyaf215
  title: 'Mondo: Integrating Disease Terminology Across Communities'
- id: https://www.medrxiv.org/content/10.1101/2022.04.13.22273750
  title: 'Mondo: Unifying diseases for the world, by the world'
repository: https://github.com/monarch-initiative/mondo
tags:
- disease
taxon:
  id: NCBITaxon:33208
  label: Metazoa
tracker: https://github.com/monarch-initiative/mondo/issues
usages:
- description: Mondo is used by the Monarch Initiative for disease annotations.
  examples:
  - description: 'Parkinsonism: Characteristic neurologic anomaly resulting form degeneration of dopamine-generating cells in the substantia nigra, a region of the midbrain, characterized clinically by shaking, rigidity, slowness of movement and difficulty with walking and gait.'
    url: https://monarchinitiative.org/phenotype/HP:0001300#disease
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/27899636
    title: 'The Monarch Initiative: an integrative data and analytic platform connecting phenotypes to genotypes across species '
  type: annotation
  user: https://monarchinitiative.org/
- description: Mondo is used by the ClinGen for disease curations.
  examples:
  - description: FBN1 is an autosomal dominant mutation in Marfan syndrome.
    url: https://search.clinicalgenome.org/kb/conditions/MONDO:0007947
  type: annotation
  user: https://www.clinicalgenome.org/
- description: Mondo is used by the Kids First Data Resource Portal for disease annotations. Note, a login is needed to access the portal and view the Mondo-curated data.
  type: annotation
  user: https://portal.kidsfirstdrc.org/
- description: Mondo is used by the Ancestory for some disease curations.
  examples:
  - description: Some term names in ancestory.com are curated with Mondo, for ease of use.
    url: https://support.ancestry.com/s/article/Disease-Condition-Catalog-Powered-by-MONDO
  type: annotation
  user: https://www.ancestry.com/
- description: Mondo is used by the Human Cell Atlas for some disease annotations.
  examples:
  - description: Disease status specimen is normal, type 2 diabetes mellitus.
    url: https://data.humancellatlas.org/explore/projects?filter=%5B%7B%22facetName%22:%22organ%22,%22terms%22:%5B%22kidney%22%5D%7D,%7B%22facetName%22:%22donorDisease%22,%22terms%22:%5B%22acoustic%20neuroma%22,%22acute%20kidney%20tubular%20necrosis%22%5D%7D%5D&catalog=dcp1
  type: annotation
  user: https://www.humancellatlas.org/
activity_status: active
---

The Mondo Disease Ontology (Mondo) aims to harmonize existing disease terminologies into a coherent ontological representation of diseases.
Mondo integrates widely used terminologies such as Online Mendelian Inheritance in Man (OMIM), Orphanet, Experimental Factor Ontology (EFO), Disease Ontology (DOID), ICD 11 (Foundation) and the neoplasm branch of National Cancer Institute Thesaurus (NCIt).
Mondo aims to track provenance and attribution for every integrated part of the disease definition to serve a wide range of data integration and cross-terminology analysis use cases.

A key part of Mondo is the curation of precise mappings across resources. These mappings are available in two ways:

- The official Mondo disease mappings in [SSSOM](https://mapping-commons.github.io/sssom/) format: [https://github.com/monarch-initiative/mondo/tree/master/src/ontology/mappings](https://github.com/monarch-initiative/mondo/tree/master/src/ontology/mappings)
- As part of the various Mondo release products (both as SKOS mappings and oboInOwl:hasDbXref cross-references).
