---
layout: ontology_detail
id: hp
title: Human Phenotype Ontology (HPO)
browsers:
- title: JAX HPO Browser
  label: HPO
  url: https://hpo.jax.org/app/
- title: Monarch Phenotype Page
  label: Monarch
  url: http://monarchinitiative.org/phenotype/HP:0000118
contact:
  email: dr.sebastian.koehler@gmail.com
  github: drseb
  label: Sebastian Koehler
  orcid: 0000-0002-5316-1399
depicted_by: https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/logo/HPO-logo-black_small.png
description: The Human Phenotype Ontology (HPO) is a structured and controlled vocabulary for the phenotypic features encountered in human hereditary and other disease.
domain: phenotype
homepage: http://www.human-phenotype-ontology.org/
license:
  label: hpo
  url: https://hpo.jax.org/app/license
mailing_list: https://groups.io/g/human-phenotype-ontology
preferredPrefix: HP
products:
- id: hp.json
  title: Official HPO release in obographs JSON format
  derived_from: hp/hp-simple-non-classified.owl
  description: Simple, manually curated version of the ontology without the use of a reasoner, and without any imported terms, in obographs JSON format.
  format: json
- id: hp.obo
  title: Official HPO release in OBO format
  derived_from: hp/hp-simple-non-classified.owl
  description: Simple, manually curated version of the ontology without the use of a reasoner, and without any imported terms, in OBO file format.
  format: obo
- id: hp.owl
  title: Official HPO release in OWL
  description: Manually classified version of the ontology without the use of a reasoner, with imported terms, in OWL format (RDF/XML).
  format: owl
- id: hp/hp-base.json
  title: HPO base release in obographs JSON format
  derived_from: hp/hp-base.owl
  description: Manually curated version of the ontology without the use of a reasoner, with references to imported terms, in obographs JSON file format.
  format: obo
- id: hp/hp-base.obo
  title: HPO base release in OBO format
  derived_from: hp/hp-base.owl
  description: Manually curated version of the ontology without the use of a reasoner, with references to imported terms, in OBO file format.
  format: obo
- id: hp/hp-base.owl
  title: HPO base release in OWL format
  description: Manually curated version of the ontology without the use of a reasoner, with references to imported terms, in OWL (RDF/XML) file format.
  format: owl
- id: hp/hp-full.json
  title: HPO full release in obographs JSON format
  derived_from: hp/hp-full.owl
  description: Version of the ontology automatically classified with the use of a reasoner, including all imported terms, in obographs JSON file format.
  format: json
- id: hp/hp-full.obo
  title: HPO full release in OBO format
  derived_from: hp/hp-full.owl
  description: Version of the ontology automatically classified with the use of a reasoner, including all imported terms, in OBO file format.
  format: obo
- id: hp/hp-full.owl
  title: HPO full release in OWL format
  description: Version of the ontology automatically classified with the use of a reasoner, including all imported terms, in OWL (RDF/XML) file format.
  format: owl
- id: hp/hp-international.json
  title: HPO International Edition in obographs JSON format
  derived_from: hp/hp-international.owl
  description: Version of the ontology corresponding to the primary release (hp.owl), with translated labels, synonyms, and definitions, in obographs JSON file format.
  format: json
- id: hp/hp-international.obo
  title: HPO International Edition in OBO format
  derived_from: hp/hp-international.owl
  description: Version of the ontology corresponding to the primary release (hp.owl), with translated labels, synonyms, and definitions, in OBO file format.
  format: obo
- id: hp/hp-international.owl
  title: HPO International Edition in OWL format
  description: Version of the ontology corresponding to the primary release (hp.owl), with translated labels, synonyms, and definitions, in OWL (RDF/XML) file format.
  format: owl
- id: hp/hp-simple-non-classified.json
  title: HPO simple, manually classified, without imports in obographs JSON format
  derived_from: hp/hp-simple-non-classified.owl
  description: Simple, manually curated version of the ontology without the use of a reasoner, and without any imported terms, in obographs JSON file format.
  format: json
- id: hp/hp-simple-non-classified.obo
  title: HPO simple, manually classified, without imports in OBO format
  derived_from: hp/hp-simple-non-classified.owl
  description: Simple, manually curated version of the ontology without the use of a reasoner, and without any imported terms, in OBO file format.
  format: obo
- id: hp/hp-simple-non-classified.owl
  title: HPO simple, manually classified, without imports in OWL format
  description: Simple, manually curated version of the ontology without the use of a reasoner, and without any imported terms, in OWL (RDF/XML) file format.
  format: owl
- id: hp/phenotype.hpoa
  title: HPO Annotations (Phenotype to Disease)
  description: https://hpo.jax.org/app/data/annotations
  format: tsv
- id: hp/phenotype_to_genes.txt
  title: HPO phenotype to gene annotations
  description: https://hpo.jax.org/app/data/annotations
  format: tsv
- id: hp/genes_to_phenotype.txt
  title: HPO gene to phenotype annotations
  description: https://hpo.jax.org/app/data/annotations
  format: tsv
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/18950739
  title: 'The Human Phenotype Ontology: a tool for annotating and analyzing human hereditary disease.'
- id: https://www.ncbi.nlm.nih.gov/pubmed/26119816
  title: 'The Human Phenotype Ontology: Semantic Unification of Common and Rare Disease.'
- id: https://www.ncbi.nlm.nih.gov/pubmed/24217912
  title: 'The Human Phenotype Ontology project: linking molecular biology and disease through phenotype data.'
- id: https://www.ncbi.nlm.nih.gov/pubmed/30476213
  title: Expansion of the Human Phenotype Ontology (HPO) knowledge base and resources.
repository: https://github.com/obophenotype/human-phenotype-ontology
taxon:
  id: NCBITaxon:9606
  label: Homo sapiens
tracker: https://github.com/obophenotype/human-phenotype-ontology/issues/
twitter: hp_ontology
usages:
- description: HPO is used by the Monarch Initiative for phenotype annotations.
  examples:
  - url: https://monarchinitiative.org/phenotype/HP:0001300
  reference: https://academic.oup.com/nar/article/45/D1/D712/2605791
  type: annotation
  user: https://monarchinitiative.org/
activity_status: active
---

An ontology is a computational representation of a domain of knowledge based upon a controlled, standardized vocabulary for describing entities and the semantic relationships between them.

The Human Phenotype Ontology (HPO) aims to provide a standardized vocabulary of phenotypic abnormalities encountered in human disease. Each term in the HPO describes a phenotypic abnormality, such as atrial septal defect. The HPO is currently being developed using the medical literature, Orphanet, DECIPHER, and OMIM.

The HPO can be browsed using:

 * [Main Browser](https://hpo.jax.org/)
 * [Monarch Browser](https://monarchinitiative.org/phenotype/HP:0000118)
