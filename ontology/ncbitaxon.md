---
layout: ontology_detail
id: ncbitaxon
title: NCBI organismal classification
browsers:
- title: NCBI Taxonomy Browser
  label: NCBI
  url: http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi
build:
  infallible: 1
  method: archive
  path: archive
  source_url: http://build.berkeleybop.org/job/build-ncbitaxon/lastSuccessfulBuild/artifact/*zip*/archive.zip
contact:
  email: frederic.bastian@unil.ch
  github: fbastian
  label: Frederic Bastian
  orcid: 0000-0002-9415-5104
description: An ontology representation of the NCBI organismal taxonomy
domain: organisms
homepage: https://github.com/obophenotype/ncbitaxon
jobs:
- id: http://build.berkeleybop.org/job/build-ncbitaxon/
  type: ReleaseBuild
license:
  label: CC0 1.0
  url: https://creativecommons.org/publicdomain/zero/1.0/
page: http://www.ncbi.nlm.nih.gov/taxonomy
preferredPrefix: NCBITaxon
products:
- id: ncbitaxon.owl
  title: Main release
- id: ncbitaxon.obo
  title: OBO Format version of Main release
- id: ncbitaxon.json
  title: OBOGraphs JSON version of Main release
- id: ncbitaxon/subsets/taxslim.owl
  title: taxslim
  page: https://github.com/obophenotype/ncbitaxon/blob/master/subsets/README.md
- id: ncbitaxon/subsets/taxslim-disjoint-over-in-taxon.owl
  title: taxslim disjointness axioms
  page: https://github.com/obophenotype/ncbitaxon/blob/master/subsets/README.md
repository: https://github.com/obophenotype/ncbitaxon
tags:
- taxonomy
tracker: https://github.com/obophenotype/ncbitaxon/issues
wasDerivedFrom: ftp://ftp.ebi.ac.uk/pub/databases/taxonomy/taxonomy.dat
usages:
- description: The Immune Epitope Database (IEDB) is funded by NIAID that catalogs experimental data on antibody and T cell epitopes studied in humans, non-human primates, and other animal species in the context of infectious disease, allergy, autoimmunity and transplantation.
  examples:
  - description: A specific assay curated in the IEDB using the NCBITaxon:520 Bordetella pertussis as the source organism.
    url: http://www.iedb.org/assay/1505273
  user: https://www.iedb.org
activity_status: active
---

The NCBITaxon ontology is an automatic translation of the [NCBI taxonomy database](http://www.ncbi.nlm.nih.gov/taxonomy) into obo/owl.

The translation treats each taxon as an obo/owl class whose instances (for most branches of the ontology) would be individual organisms. For example:

    'Craig Venter' instance_of NCBITaxon_9606 (Homo sapiens)

The translation faithfully reproduces all of the content of the source database, even where this contravenes OBO guidelines. For example:

 * The root class is called 'root', rather than something like 'organism'
 * Plural names are used (both Linnaean and common names). E.g. "mammals"
 * The organismhood of certain classes might be contested - either biologically ("viruses") or ontologically ("environmental samples")
 * Synonyms may include quotation marks as part of the text

## PURLs

The purls for this ontology are:

 * http://purl.obolibrary.org/obo/ncbitaxon.owl (official purl for *ontology*)
 * http://purl.obolibrary.org/obo/ncbitaxon.obo (obo-format version)

The PURLs should be resolvable in OntoBee. E.g.

 * [http://purl.obolibrary.org/obo/NCBITaxon_9606](http://purl.obolibrary.org/obo/NCBITaxon_9606) (Homo sapiens)
 * http://purl.obolibrary.org/obo/NCBITaxon_7711 (Chordates)
 * http://purl.obolibrary.org/obo/NCBITaxon_7955 (Danio rerio)

## Releases

Releases of the obo/owl happen when the [Continuous Integration
Job](http://build.berkeleybop.org/job/build-ncbitaxon/) is manually
triggered. Currently this must be done by an OBO administrator. There
is currently no fixed cycle, and this is generally done on demand. The
team that informally handles this are:

 * James Overton, IEBD/OBO
 * Frederic Bastian, BgeeDb/Uberon
 * Chris Mungall, LBNL/GO/Monarch/Uberon/OBO
 * Peter Midford, Phenoscape

Contact the mail list (see below) for comments on this.

## Extensions

The GO uses an extension of NCBITaxon for grouping purposes. See:

* http://purl.obolibrary.org/obo/go/extensions/go-taxon-groupings.owl

this ontology includes new classes in the NCBITaxon_Union namespace. These classes are all defined using unions - for example Prokaryote = Eubacteria OR Archae

## Taxon Constraints

One of the main uses for the NCBITaxon ontology is to define taxon constraints in a multi-species ontology. For details, see:

 * Waclaw Kusnierczyk (2008) [Taxonomy-based partitioning of the Gene Ontology](https://doi.org/10.1016/j.jbi.2007.07.007), *Journal of Biomedical Informatics*
 * Deegan Née Clark, J. I., Dimmer, E. C., and Mungall, C. J. (2010). [Formalization of taxon-based constraints to detect inconsistencies in annotation and ontology development](http://www.biomedcentral.com/1471-2105/11/530). *BMC Bioinformatics 11, 530**
 * [Taxon constraints in OWL](http://douroucouli.wordpress.com/2012/04/24/taxon-constraints-in-owl) (blog post)
 * [Taxon constraints in Uberon](https://github.com/obophenotype/uberon/wiki/Taxon-constraints)
 * [A Taxonomy for Immunologists](http://ceur-ws.org/Vol-1060/icbo2013_submission_76.pdf) **ICBO 2013**

## Mailing Lists

 * https://lists.sourceforge.net/lists/listinfo/obo-taxonomy
 * http://groups.google.com/group/obo-taxonomy

## Tracker

Note that this differs from other OBO ontologies in that it is a
translation of a database produced external to OBO. If you wish to
suggest actual taxonomy changes to the database, contact NCBI.

The NCBI staff are very responsive and helpful, [as this post from the Bgee team shows](https://bgeedb.wordpress.com/2013/05/29/new-taxon-dipnotetrapodomorpha-in-ncbi-taxonomy/)

If you wish to suggest changes to the *translation* then contact the
maintainer or the mail list above.

## Citing the NCBITaxon ontology

before citing, ask yourself what the artefact you wish to cite is:

 * The NCBI taxonomy **database**
 * The OBO/OWL rendering of the NCBI taxonomy database

The latter is a fairly trivial translation of the former. If you are in any way citing the *contents* then **you should cite the database**. Currently the most up to date reference is:

 * Federhen, Scott. **The NCBI taxonomy database.** *Nucleic acids research 40.D1 (2012): D136-D143.* [http://nar.oxfordjournals.org/content/40/D1/D136.short](http://nar.oxfordjournals.org/content/40/D1/D136.short)

If you specifically wish to cite the OBO/OWL translation, use the URL for this page
