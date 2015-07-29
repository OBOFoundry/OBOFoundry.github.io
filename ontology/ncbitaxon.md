---
layout: ontology_detail
id: ncbitaxon
preferredPrefix: NCBITaxon
title: NCBI organismal classification
contact: 
  email: obo-taxonomy@lists.sourceforge.net
  label: obo-taxonomy-list
description: The NCBITaxon ontology is an automatic translation of the NCBI taxonomy (a taxonomic classification of living organisms and associated artifacts) database into an ontology
source: http://www.ncbi.nlm.nih.gov/taxonomy
wasDerivedFrom: ftp://ftp.ebi.ac.uk/pub/databases/taxonomy/taxonomy.dat
createdWith: http://owltools.googlecode.com/
domain: taxonomy
homepage: http://www.obofoundry.org/wiki/index.php/NCBITaxon:Main_Page
page: http://www.ncbi.nlm.nih.gov/taxonomy
jobs:
  - id: http://build.berkeleybop.org/job/build-ncbitaxon/
    type: ReleaseBuild
products: 
  - id: ncbitaxon.owl
  - id: ncbitaxon/subsets/taxslim.owl
    title: taxslim
---

The NCBITaxon ontology is an automatic translation of the NCBI taxonomy database into obo/owl.

The translation treats each taxon as an obo/owl class whose instances (for most branches of the ontology) would be individual organisms. For example:

  'Craig Venter' instance_of NCBITaxon_9606 (Homo sapiens)

The translation faithfully reproduces all of the content of the source database, even where this contravenes OBO guidelines. For example:

 * The root class is called 'root', rather than something like 'organism'
 * Plural names are used (both Linnaean and common names). E.g. "mammals"
 * The organismhood of certain classes might be contested - either biologically ("viruses") or ontologically ("environmental samples")
 * Synonyms may include quotation marks as part of the text

## PURLs

The purls for this ontology are:

 * http://purl.obolibrary.org/obo/ncbitaxon.owl (official purl)
 * http://purl.obolibrary.org/obo/ncbitaxon.obo (obo-format version)

The PURLs should be resolvable in OntoBee. E.g.

 * http://purl.obolibrary.org/obo/NCBITaxon_9606 (Homo sapiens)
 * http://purl.obolibrary.org/obo/NCBITaxon_7711 (Chordates)
 * http://purl.obolibrary.org/obo/NCBITaxon_7227 (Danio rerio)

## Extensions

The GO uses an extension of NCBITaxon for grouping purposes. See:

* http://purl.obolibrary.org/obo/go/extensions/go-taxon-groupings.owl

this ontology includes new classes in the NCBITaxon_Union namespace. These classes are all defined using unions - for example Prokaryote = Eubacteria OR Archae

## Taxon Constraints

One of the main uses for the NCBITaxon ontology is to define taxon constraints in a multi-species ontology. For details, see:

 * Waclaw Kusnierczyk (2008) [http://dx.doi.org/10.1016/j.jbi.2007.07.007 Taxonomy-based partitioning of the Gene Ontology], ''Journal of Biomedical Informatics''
 * Deegan Née Clark, J. I., Dimmer, E. C., and Mungall, C. J. (2010). [http://www.biomedcentral.com/1471-2105/11/530 Formalization of taxon-based constraints to detect inconsistencies in annotation and ontology development]. ''BMC Bioinformatics 11, 530''
 * [http://douroucouli.wordpress.com/2012/04/24/taxon-constraints-in-owl/ Taxon constraints in OWL]


## Mailing Lists

 * https://lists.sourceforge.net/lists/listinfo/obo-taxonomy
 * http://groups.google.com/group/obo-taxonomy

## Citing the NCBITaxon ontology ==

before citing, ask yourself what the artefact you wish to cite is:

 * The NCBI taxonomy ''database''
 * The OBO/OWL rendering of the NCBI taxonomy database

The latter is a fairly trivial translation of the former. If you are in any way citing the ''contents'' then '''you should cite the database'''. Currently the most up to date reference is:

Federhen, Scott. '''The NCBI taxonomy database.''' ''Nucleic acids research 40.D1 (2012): D136-D143.''
http://nar.oxfordjournals.org/content/40/D1/D136.short

If you specifically wish to cite the OBO/OWL translation, use the URL for this page

