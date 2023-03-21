---
layout: ontology_detail
id: obi
title: Ontology for Biomedical Investigations
browsers:
- title: BioPortal Browser
  label: BioPortal
  url: http://bioportal.bioontology.org/ontologies/OBI?p=classes
build:
  source_url: http://purl.obofoundry.org/obo/obi/repository/trunk/src/ontology/branches/
contact:
  email: bpeters@lji.org
  github: bpeters42
  label: Bjoern Peters
  orcid: 0000-0002-8457-6693
depicted_by: https://svn.code.sf.net/p/obi/code/trunk/web/htdocs/images/obi-lotext.png
description: An integrated ontology for the description of life-science and clinical investigations
domain: investigations
homepage: http://obi-ontology.org
in_foundry_order: 1
integration_server: http://build.berkeleybop.org/job/build-obi/
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
mailing_list: http://groups.google.com/group/obi-users
preferredPrefix: OBI
products:
- id: obi.owl
  title: OBI
  description: The full version of OBI in OWL format
- id: obi.obo
  title: OBI in OBO
  description: The OBO-format version of OBI
- id: obi/obi_core.owl
  title: OBI Core
  description: A collection of important high-level terms and their relations from OBI and other ontologies
- id: obi/obi-base.owl
  title: OBI Base module
  description: Base module for OBI
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/27128319
  title: The Ontology for Biomedical Investigations
repository: https://github.com/obi-ontology/obi
review:
  date: 2013
  document:
    label: PDF
    link: https://drive.google.com/open?id=0B8vqEgF1N0NIMFlSM3RvdUxGTnc
tracker: http://purl.obolibrary.org/obo/obi/tracker
usages:
- description: The Immune Epitope Database (IEDB) is funded by NIAID that catalogs experimental data on antibody and T cell epitopes studied in humans, non-human primates, and other animal species in the context of infectious disease, allergy, autoimmunity and transplantation.
  examples:
  - description: A specific assay curated in the IEDB using the OBI:1110180 '3H-thymidine assay measuring epitope specific proliferation of T cells' ('3H-thymidine')
    url: http://www.iedb.org/assay/1505273
  user: https://www.iedb.org
- description: ENCODE is a comprehensive parts list of functional elements in the human genome, including elements that act at the protein and RNA levels, and regulatory elements that control cells and circumstances in which a gene is active.
  examples:
  - description: A specific assay annotated in ENCODE using OBI:0000716 'ChiP-seq'
    url: https://www.encodeproject.org/report/?type=Experiment&accession=ENCSR012KGU&accession=ENCSR560MXA&accession=ENCSR803FKU&accession=ENCSR216YPQ&accession=ENCSR115BCB&field=%40id&field=assay_term_name&field=assay_term_id
  user: https://www.encodeproject.org/
- description: The NASA GeneLab data repository hosts space biology and space-related datasets funded by multiple space agencies around the world.
  examples:
  - description: A specific assay annotated in NASA GeneLab using OBI:0001271 'RNA-seq assay'
    url: https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-464/
  user: https://genelab-data.ndc.nasa.gov/genelab/projects
- description: The CFDE is providing a centralized metadata resource to allow search across data coordination centers from multiple Common Fund programs.
  examples:
  - description: OBI is used in CFDE to captures types of experiments with assay terms such as OBI:0003094 'fluorescence in-situ hybridization assay'
    url: https://app.nih-cfde.org/chaise/recordset/#1/CFDE:assay_type@sort(nid)
  user: https://app.nih-cfde.org/
- description: NIF is a dynamic inventory of Web-based neuroscience resources, data, and tools accessible via any computer connected to the Internet.
  examples:
  - description: A specific OBI term used to autocomplete in NIF search OBI:0100026 'organism'
    url: https://neuinfo.org/data/search?q=organism&l=organism#all
  user: http://www.neuinfo.org
activity_status: active
---

The Ontology for Biomedical Investigations (OBI) project is developing an integrated ontology for the description of life-science and clinical investigations.

- [Browse OBI on Ontobee](http://www.ontobee.org/browser/index.php?o=obi)
- Download OBI: [http://purl.obolibrary.org/obo/obi.owl](http://purl.obolibrary.org/obo/obi.owl)
- [OBI homepage](http://obi-ontology.org)
- [OBI mailing list](http://groups.google.com/group/obi-users)
- To cite a journal article for OBI please use [Bandrowski et al, PLOS ONE, 2016](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0154556)
- To refer to the most current information on the OBI project, please use the following: The OBI Consortium [http://purl.obolibrary.org/obo/obi](http://purl.obolibrary.org/obo/obi)
