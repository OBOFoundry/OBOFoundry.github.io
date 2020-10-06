---
layout: ontology_detail
id: so
contact:
  email: keilbeck@genetics.utah.edu
  label: Karen Eilbeck
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY 4.0
description: A structured controlled vocabulary for sequence annotation, for the exchange of annotation data and for the description of sequence objects in databases.
domain: biological sequence
homepage: https://github.com/The-Sequence-Ontology/SO-Ontologies
mailing_list: https://sourceforge.net/p/song/mailman/song-devel/
page:
  https://en.wikipedia.org/wiki/Sequence_Ontology
products:
  - id: so.owl
  - id: so.obo
title: Sequence types and features ontology
build:
  notes: SWITCH
  source_url: https://raw.githubusercontent.com/The-Sequence-Ontology/SO-Ontologies/master/so.obo
  method: obo2owl
tracker: https://github.com/The-Sequence-Ontology/SO-Ontologies/issues
publications:
  - id: http://www.ncbi.nlm.nih.gov/pubmed/15892872
    title: "The Sequence Ontology: a tool for the unification of genome annotations."
  - id: http://www.ncbi.nlm.nih.gov/pubmed/20226267
    title: Evolution of the Sequence Ontology terms and relationships.
depicted_by: http://sequenceontology.org/img/so_icon.png
activity_status: active
---

SO is a collaborative ontology project for the definition of sequence features used in biological sequence annotation. SO was initially developed by the Gene Ontology Consortium. Contributors to SO include the GMOD community, model organism database groups such as WormBase, FlyBase, Mouse Genome Informatics group, and institutes such as the Sanger Institute and the EBI. Input to SO is welcomed from the sequence annotation community. SO is also part of the Open Biomedical Ontologies library. Our aim is to develop an ontology suitable for describing the features of biological sequences. For questions, please send mail to the SO developers mailing list. For new term suggestions, please use the [Term Tracker](https://github.com/The-Sequence-Ontology/SO-Ontologies/issues).

 The Sequence Ontology is a set of terms and relationships used to describe the features and attributes of biological sequence. SO includes different kinds of features which can be located on the sequence. Biological features are those which are defined by their disposition to be involved in a biological process. Examples are binding_site and exon. Biomaterial features are those which are intended for use in an experiment such as aptamer and PCR_product. There are also experimental features which are the result of an experiment. SO also provides a rich set of attributes to describe these features such as "polycistronic" and "maternally imprinted".

The Sequence Ontologies are provided as a resource to the biological community. They have the following obvious uses:

 * To provide for a structured controlled vocabulary for the description of primary annotations of nucleic acid sequence, e.g. the annotations shared by a DAS server (BioDAS, Biosapiens DAS), or annotations encoded by GFF3.
 * To provide for a structured representation of these annotations within databases. Were genes within model organism databases to be annotated with these terms then it would be possible to query all these databases for, for example, all genes whose transcripts are edited, or trans-spliced, or are bound by a particular protein. One such genomic database is Chado.
 * To provide a structured controlled vocabulary for the description of mutations at both the sequence and more gross level in the context of genomic databases.

The Sequence Ontology is part of OBO. It has close links to other ontology projects such as the RNAO consortium, and the Biosapiens polypeptide features.



