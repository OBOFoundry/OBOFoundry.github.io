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
  email: nicole@tislab.org
  github: nicolevasilevsky
  label: Nicole Vasilevsky
  orcid: 0000-0001-5208-3432
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
  title: Main OWL edition
  description: Complete ontology. Uses MONDO IDs. Imports merged. The original mondo.owl without merged imports and with equivalence axioms can now be obtained from the release pages and is called mondo-with-equivalents.
  format: owl-rdf/xml
  is_canonical: true
- id: mondo.obo
  title: obo-format edition
  derived_from: mondo.owl
  description: As OWL. xrefs can be used as proxy for equivalence. Uses Mondo IDs.
  format: obo
- id: mondo.json
  title: json edition
  derived_from: mondo.owl
  description: Equivalent to the OWL edition.
  format: obo
- id: mondo/mondo-base.owl
  title: Mondo Base Module
  description: The main ontology plus axioms connecting to select external ontologies, excluding the external ontologies themselves
  format: owl
publications:
- id: https://www.medrxiv.org/content/10.1101/2022.04.13.22273750
  title: 'Mondo: Unifying diseases for the world, by the world'
repository: https://github.com/monarch-initiative/mondo
tags:
- disease
taxon:
  id: NCBITaxon:33208
  label: Metazoa
tracker: https://github.com/monarch-initiative/mondo/issues
twitter: MonarchInit
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

The Mondo Disease Ontology (Mondo) aims to harmonize disease definitions across the world. It is a global community effort to reconcile and curate the very many disease resources within a coherent merged ontology. Original versions of Mondo were constructed entirely automatically and used the IDs of source databases and ontologies. Later, additional manually curated cross-ontology axioms were added, and a native Mondo ID system was used to avoid confusion with source databases.

A key feature of Mondo is that it goes beyond loose database cross-references (xrefs). It curated precise 1:1 equivalence axioms connecting to other resources, validated by OWL reasoning. This means it is safe to propagate across these from Online Mendelian Inheritance in Man (OMIM), Orphanet, Experimental Factor Ontology (EFO), Disease Ontology (DOID) and the neoplasm branch of National Cancer Institute Thesaurus (NCIt). All provenance and attribution is tracked, ensuring interoperability across resources.

These precise mappings are available in three ways depending on the format:

- The [mondo-with-equivalent](http://purl.obolibrary.org/obo/mondo/mondo-with-equivalents.owl) edition uses OWL equivalence axioms directly in the ontology. Note this makes it harder to browse in some portals, but this edition may be preferable for computational use. The owl edition also includes axiomatization using CL, Uberon, GO, HP, RO, NCBITaxon.
- The primary release versions (mondo.owl, mondo.obo) are simpler, lacking owl equivalence axioms from Mondo classes to terms from other databases; instead, xrefs are used for linking these terms. If the ID is one of Orphanet, OMIM, DOID or EFO then the xref precisely shadows the equivalence axiom.
- The [mondo-with-equivalents json edition](http://purl.obolibrary.org/obo/mondo/mondo-with-equivalents.json) has all owl equivalencies as well as all xrefs to other disease sources.
