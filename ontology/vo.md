---
layout: ontology_detail
id: vo
title: Vaccine Ontology
build:
  source_url: https://raw.githubusercontent.com/vaccineontology/VO/master/src/VO_merged.owl
contact:
  email: yongqunh@med.umich.edu
  github: yongqunh
  label: Yongqunh He
  orcid: 0000-0001-9189-9661
description: VO is a biomedical ontology in the domain of vaccine and vaccination.
domain: health
homepage: https://violinet.org/vaccineontology
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
preferredPrefix: VO
products:
- id: vo.owl
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/23256535
  title: Ontology representation and analysis of vaccine formulation and administration and their effects on vaccine immune responses
- id: https://www.ncbi.nlm.nih.gov/pubmed/21624163
  title: Mining of vaccine-associated IFN-γ gene interaction networks using the Vaccine Ontology
repository: https://github.com/vaccineontology/VO
tracker: https://github.com/vaccineontology/VO/issues
usages:
- description: VIOLIN uses VO to standardize vaccine information
  examples:
  - description: VIOLIN using VO grouped all SARS-CoV-2 vaccines
    url: https://violinet.org/canvaxkb/vaccine_detail.php?c_vaccine_id=5339
  - description: A specific vaccine ‘Allogeneic Tumor Cell Vaccine’ curated in VO for VIOLIN vaccine record
    url: https://violinet.org/vaxquery/query_detail.php?c_pathogen_id=321#vaccine_5878
  user: https://violinet.org
- description: Vaccine Adjuvant Compendium (VAC) uses Vaccine Ontology to standard vaccine adjuvants developed by NIH
  examples:
  - description: A specific vaccine adjuvant, such as CaPNP (CaPtivant)(TM), in Vaccine Adjuvant Compendium, uses VO_0005295 ‘CaPNP (CaPtivant)(TM) vaccine adjuvant’
    url: https://vac.niaid.nih.gov/view?id=11
  user: https://www.niaid.nih.gov/research/vaccine-adjuvant-compendium-vac
- description: ImmPort uses Vaccine Ontology to standardize vaccine recorded collected in NIH funded ImmPort studies
  examples:
  - description: Vaccine annotated using VO terms
    url: https://www.immport.org/shared/home
  user: https://www.immport.org/
- description: Human Immunology Project Consortium (HIPC) uses VO to standardize vaccine records
  examples:
  - description: standardize vaccine records using VO
    url: https://immunespace.org/
  user: https://immunespace.org/
activity_status: active
---

The Vaccine Ontology (VO) is a biomedical ontology in the domain of vaccine and vaccination. VO aims to standardize and integrate vaccines, vaccine components, vaccine mechanisms, vaccine data types, and support computer-assisted reasoning. VO supports basic vaccine research, development, and clincal vaccine usage. VO is being developed as a community-based ontology with support and collaborations from the vaccine and bio-ontology communities.
