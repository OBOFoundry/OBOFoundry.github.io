---
layout: ontology_detail
id: cheminf
title: Chemical Information Ontology
build:
  method: owl2obo
  source_url: https://raw.githubusercontent.com/semanticchemistry/semanticchemistry/master/ontology/cheminf.owl
contact:
  email: egon.willighagen@gmail.com
  github: egonw
  label: Egon Willighagen
  orcid: 0000-0001-7542-0286
description: Includes terms for the descriptors commonly used in cheminformatics software applications and the algorithms which generate them.
domain: chemistry and biochemistry
github_date_added: 2015-07-28
homepage: https://github.com/semanticchemistry/semanticchemistry
license:
  label: CC0 1.0
  url: http://creativecommons.org/publicdomain/zero/1.0/
mailing_list: https://groups.google.com/forum/#!forum/cheminf-ontology
preferredPrefix: CHEMINF
products:
- id: cheminf.owl
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/21991315
  title: 'The chemical information ontology: provenance and disambiguation for chemical data on the biological semantic web'
repository: https://github.com/semanticchemistry/semanticchemistry
tracker: https://github.com/semanticchemistry/semanticchemistry/issues
usages:
- description: ChEMBL uses CHEMINF in the RDF download
  examples:
  - description: The RDF is provided as SPARQL endpoint by Maastricht University.
    url: https://chemblmirror.rdf.bigcat-bioinformatics.org/
  user: https://www.ebi.ac.uk/chembl/
- description: PubChem uses CHEMINF in their RDF representation
  examples:
  - description: Physicochemical properties are represented as classes that are typed with CHEMINF classes
    url: https://pubchem.ncbi.nlm.nih.gov/rest/rdf/descriptor/CID161282_Canonical_SMILES
  user: https://pubchem.ncbi.nlm.nih.gov/
activity_status: active
---
