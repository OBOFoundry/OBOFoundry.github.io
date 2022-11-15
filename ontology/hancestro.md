---
layout: ontology_detail
id: hancestro
title: Human Ancestry Ontology
contact:
  email: danielle.welter@uni.lu
  github: daniwelter
  label: Danielle Welter
  orcid: 0000-0003-1058-2668
description: The Human Ancestry Ontology (HANCESTRO) provides a systematic description of the ancestry concepts used in the NHGRI-EBI Catalog of published genome-wide association studies.
domain: organisms
homepage: https://github.com/EBISPOT/ancestro
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: HANCESTRO
products:
- id: hancestro.owl
  title: HANCESTRO
  description: The full version of HANCESTRO in OWL format
- id: hancestro_bfo.owl
  title: HANCESTRO BFO
  description: Version of HANCESTRO with BFO upper hierarchy for easier integration with other ontologies
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/29448949
  title: A standardized framework for representation of ancestry data in genomics studies, with application to the NHGRI-EBI GWAS Catalog
repository: https://github.com/EBISPOT/ancestro
tags:
- ancestry
tracker: https://github.com/EBISPOT/ancestro/issues
usages:
- description: The Experimental Factor Ontology (EFO) provides a systematic description of many experimental variables available in EBI databases, and for external projects such as the NHGRI GWAS catalogue. It combines parts of several biological ontologies, such as anatomy, disease and chemical compounds.
  examples:
  - description: Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data
    url: https://www.ebi.ac.uk/ols/ontologies/efo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FHANCESTRO_0004&viewMode=All&siblings=false
  user: http://www.ebi.ac.uk/efo
- description: The Genomic Epidemiology Ontology (GenEpiO) covers vocabulary necessary to identify, document and research foodborne pathogens and associated outbreaks.
  examples:
  - description: Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data
    url: https://www.ebi.ac.uk/ols/ontologies/genepio/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FHANCESTRO_0004&viewMode=All&siblings=false
  user: https://genepio.org/
- description: FoodOn (http://foodon.org) is a consortium-driven project to build a comprehensive and easily accessible global farm-to-fork ontology about food, that accurately and consistently describes foods commonly known in cultures from around the world.
  examples:
  - description: Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data
    url: https://www.ebi.ac.uk/ols/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FHANCESTRO_0004&viewMode=All&siblings=false
  user: http://foodon.org
activity_status: active
---

# Summary

The Human Ancestry Ontology (HANCESTRO) provides a systematic description of the ancestry concepts used in the NHGRI-EBI Catalog of published genome-wide association studies.

* Home: [https://github.com/EBISPOT/ancestro](https://github.com/EBISPOT/ancestro)  

# Download

Use the following URI to download this ontology

* [http://purl.obolibrary.org/obo/hancestro.owl](http://purl.obolibrary.org/obo/hancestro.owl)
* This should point to: [https://raw.githubusercontent.com/EBISPOT/ancestro/master/hancestro_inferred.owl](https://raw.githubusercontent.com/EBISPOT/ancestro/master/hancestro_inferred.owl)

A non-reasoned version of the ontology is available at [https://raw.githubusercontent.com/EBISPOT/ancestro/master/hancestro.owl](https://raw.githubusercontent.com/EBISPOT/ancestro/master/hancestro.owl)

A version of HANCESTRO with BFO upper classes is available at [https://raw.githubusercontent.com/EBISPOT/ancestro/master/hancestro_bfo.owl](https://raw.githubusercontent.com/EBISPOT/ancestro/master/hancestro_bfo.owl)


# Browsing

* Default browsing in Ontobee: [http://www.ontobee.org/ontology/hancestro](http://www.ontobee.org/ontology/hancestro)
* Browsing in OLS:
[https://www.ebi.ac.uk/ols/ontologies/hancestro](https://www.ebi.ac.uk/ols/ontologies/hancestro)
* Browsing in NCBO BioPortal: [https://bioportal.bioontology.org/ontologies/HANCESTRO](https://bioportal.bioontology.org/ontologies/HANCESTRO)
