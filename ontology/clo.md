---
layout: ontology_detail
id: clo
title: Cell Line Ontology
contact:
  email: zhengj2007@gmail.com
  github: zhengj2007
  label: Jie Zheng
  orcid: 0000-0002-2999-0103
dependencies:
- id: cl
- id: doid
- id: ncbitaxon
- id: uberon
description: An ontology to standardize and integrate cell line information and to support computer-assisted reasoning.
domain: anatomy and development
homepage: https://github.com/CLO-Ontology/CLO
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: CLO
products:
- id: clo.owl
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/25852852
  title: 'CLO: The Cell Line Ontology'
repository: https://github.com/CLO-Ontology/CLO
tracker: https://github.com/CLO-Ontology/CLO/issues
usages:
- description: Cellosaurus, a knowledge resource for cell lines, provides cross-references to CLO IDs.
  examples:
  - description: Mouse 10B9 cell
    url: https://www.cellosaurus.org/CVCL_B379
  user: https://www.cellosaurus.org/
- description: NIH PubChem records include cross-references to CLO IDs.
  examples:
  - description: NCI-H226 (Cell)
    url: https://pubchem.ncbi.nlm.nih.gov/cell/4004#section=Cell-Line-Ontology-ID
  user: https://pubchem.ncbi.nlm.nih.gov
- description: NIH LINCS project uses CLO for cell line annotation.
  examples:
  - description: In LINCS cell line metadata, the field "CL_Alternative_ID" specifies the CLO.
    url: https://lincsproject.org/LINCS/files/Cell_Line_Metadata_2017.pdf
  user: https://lincsproject.org
- description: Immune Epitope Database uses CLO for annotation
  examples:
  - description: We continue to expand our use of ontologies for more fields, and have recently incorporated the MRO, Uberon, cell type and cell line ontologies.
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6324067/
  user: https://www.iedb.org
activity_status: active
---

# Summary

The Cell Line Ontology (CLO) is a community-driven ontology that is developed to standardize and integrate cell line information and support computer-assisted reasoning.

# Download

Use the following URI to download this ontology

* [http://purl.obolibrary.org/obo/clo.owl](http://purl.obolibrary.org/obo/clo.owl)
* This should point to: [https://raw.githubusercontent.com/CLO-ontology/CLO/master/src/ontology/clo_merged.owl](https://raw.githubusercontent.com/CLO-ontology/CLO/master/clo.owl)


# Browsing

* Default browsing in Ontobee: [https://www.ontobee.org/ontology/clo](https://www.ontobee.org/ontology/clo)
* Browsing in NCBO BioPortal: [https://bioportal.bioontology.org/ontologies/CLO](https://bioportal.bioontology.org/ontologies/CLO)
