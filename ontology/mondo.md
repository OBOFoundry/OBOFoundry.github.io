---
layout: ontology_detail
id: mondo
label: Mondo
title: Mondo Disease Ontology
description: A semi-automatically constructed ontology that merges in multiple disease resources to yield a coherent merged ontology.
homepage: https://monarch-initiative.github.io/mondo
license:
  url: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
contact:
  email: nicole@tislab.org
  label: Nicole Vasilevsky
  github: nicolevasilevsky
  orcid: 0000-0001-5208-3432
depicted_by: https://raw.githubusercontent.com/monarch-initiative/mondo/master/docs/images/mondo_logo_black-stacked-small.png
taxon:
  id: NCBITaxon:33208
  label: Metazoa
domain: health
tags:
  - disease
tracker: https://github.com/monarch-initiative/mondo/issues
mailing_list: https://groups.google.com/group/mondo-users
canonical: mondo.owl
browsers:
  - label: Monarch
    title: Monarch Initiative Disease Browser
    url: https://monarchinitiative.org/disease/MONDO:0019609
products:
  - id: mondo.owl
    title: Main OWL edition
    description: Complete ontology. Uses MONDO IDs. Imports merged. The original mondo.owl without merged imports and with equivalence axioms can now be obtained from the release pages and is called mondo-with-equivalents.
    format: owl-rdf/xml
    is_canonical: true
  - id: mondo.obo
    title: obo-format edition
    description: As OWL. xrefs can be used as proxy for equivalence. Uses Mondo IDs.
    format: obo
    derived_from: mondo.owl
  - id: mondo.json
    title: json edition
    description: Equivalent to the OWL edition.
    format: obo
    derived_from: mondo.owl
usages:
  - user: https://monarchinitiative.org/
    type: annotation
    description: Mondo is used by the Monarch Initiative for disease annotations.
    examples:
      - url: https://monarchinitiative.org/phenotype/HP:0001300#disease
        description: "Parkinsonism: Characteristic neurologic anomaly resulting form degeneration of dopamine-generating cells in the substantia nigra, a region of the midbrain, characterized clinically by shaking, rigidity, slowness of movement and difficulty with walking and gait."
    publications:
      - id: https://medrxiv.org/cgi/content/short/2022.04.13.22273750v1
        title: "Mondo: Unifying diseases for the world, by the world"
      - id: https://www.ncbi.nlm.nih.gov/pubmed/27899636
        title: "The Monarch Initiative: an integrative data and analytic platform connecting phenotypes to genotypes across species "
  - user: https://www.clinicalgenome.org/
    type: annotation
    description: Mondo is used by the ClinGen for disease curations.
    examples:
      - url: https://search.clinicalgenome.org/kb/conditions/MONDO_0011794
        description: SCN1A is an autosomal dominant mutation in Dravet syndrome.
  - user: https://portal.kidsfirstdrc.org/
    type: annotation
    description: Mondo is used by the Kids First Data Resource Portal for disease annotations. Note, a login is needed to access the portal and view the Mondo-curated data.
  - user: https://www.ancestry.com/
    type: annotation
    description: Mondo is used by the Ancestory for some disease curations.
    examples:
      - url: https://support.ancestry.com/s/article/Disease-Condition-Catalog-Powered-by-MONDO
        description: Some term names in ancestory.com are curated with Mondo, for ease of use.
  - user: https://www.humancellatlas.org/
    type: annotation
    description: Mondo is used by the Human Cell Atlas for some disease annotations.
    examples:
      - url: https://data.humancellatlas.org/explore/projects?filter=%5B%7B%22facetName%22:%22organ%22,%22terms%22:%5B%22kidney%22%5D%7D,%7B%22facetName%22:%22donorDisease%22,%22terms%22:%5B%22acoustic%20neuroma%22,%22acute%20kidney%20tubular%20necrosis%22%5D%7D%5D&catalog=dcp1
        description: Disease status specimen is normal, type 2 diabetes mellitus.
activity_status: active
repository: https://github.com/monarch-initiative/mondo
preferredPrefix: MONDO
---

The Mondo Disease Ontology (Mondo) aims to harmonize disease definitions across the world. It is a semi-automatically constructed ontology that merges in multiple disease resources to yield a coherent merged ontology. Original versions of Mondo were constructed entirely automatically and used the IDs of source databases and ontologies. Later, additional manually curated cross-ontology axioms were added, and a native Mondo ID system was used to avoid confusion with source databases.

A key feature of Mondo is that it goes beyond loose database cross-references (xrefs). It curated precise 1:1 equivalence axioms connecting to other resources, validated by OWL reasoning. This means it is safe to propagate across these from Online Mendelian Inheritance in Man (OMIM), Orphanet, Experimental Factor Ontology (EFO), Disease Ontology (DOID) and the neoplasm branch of National Cancer Institute Thesaurus (NCIt).

These precise mappings are available in three ways depending on the format:

- The [mondo-with-equivalent](http://purl.obolibrary.org/obo/mondo/mondo-with-equivalents.owl) edition uses OWL equivalence axioms directly in the ontology. Note this makes it harder to browse in some portals, but this edition may be preferable for computational use. The owl edition also includes axiomatization using CL, Uberon, GO, HP, RO, NCBITaxon.
- The primary release versions (mondo.owl, mondo.obo) are simpler, lacking owl equivalence axioms from Mondo classes to terms from other databases; instead, xrefs are used for linking these terms. If the ID is one of Orphanet, OMIM, DOID or EFO then the xref precisely shadows the equivalence axiom.
- The [mondo-with-equivalents json edition](http://purl.obolibrary.org/obo/mondo/mondo-with-equivalents.json) has all owl equivalencies as well as all xrefs to other disease sources.

Tracker

 - https://github.com/monarch-initiative/mondo/issues
