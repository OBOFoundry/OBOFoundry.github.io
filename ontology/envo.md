---
layout: ontology_detail
id: envo
title: Environment Ontology
build:
  checkout: git clone https://github.com/EnvironmentOntology/envo.git
  email_cc: cjmungall@lbl.gov
  infallible: 1
  method: vcs
  path: .
  system: git
contact:
  email: p.buttigieg@gmail.com
  github: pbuttigieg
  label: Pier Luigi Buttigieg
  orcid: 0000-0002-4366-3088
dependencies:
- id: chebi
- id: foodon
- id: go
- id: ncbitaxon
- id: pco
- id: po
- id: ro
- id: uberon
depicted_by: /logos/envo.png
description: Ontology of environmental features and habitats
domain: environment
homepage: http://environmentontology.org/
jobs:
- id: https://travis-ci.org/EnvironmentOntology/envo
  type: travis-ci
license:
  label: CC BY 3.0
  url: http://creativecommons.org/licenses/by/3.0/
page: https://github.com/EnvironmentOntology/envo
preferredPrefix: ENVO
products:
- id: envo.owl
  title: main ENVO OWL release
- id: envo.json
  title: ENVO in obographs JSON format
- id: envo.obo
  title: ENVO in OBO Format. May be lossy
- id: envo/subsets/envo-basic.obo
  title: OBO-Basic edition of ENVO
- id: envo/subsets/envoEmpo.owl
  title: Earth Microbiome Project subset
- id: envo/subsets/EnvO-Lite-GSC.obo
  title: GSC Lite subset of ENVO
  homepage: http://environmentontology.org/downloads
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/24330602
  title: 'The environment ontology: contextualising biological and biomedical entities'
- id: https://www.ncbi.nlm.nih.gov/pubmed/27664130
  title: 'The environment ontology in 2016: bridging domains with increased scope, semantic density, and interoperation'
repository: https://github.com/EnvironmentOntology/envo
tracker: https://github.com/EnvironmentOntology/envo/issues/
usages:
- description: describing species habitats
  examples:
  - description: Pseudobarbus burchelli (Tradou Redfin) is a species of bony fishes in the family Cyprinidae. They are associated with freshwater habitat. Individuals can grow to 13.5 cm. They have sexual reproduction.
    url: http://eol.org/pages/211700/data
  type: data-annotation
  user: http://eol.org
- description: describing stomach contents
  type: data-annotation
  user: http://globalbioticinteractions.org
- description: annotating datasets in data repositories
  seeAlso: http://blogs.nature.com/scientificdata/2015/12/17/isa-explorer/
  type: dataset-description
  user: http://www.nature.com/sdata/
- description: Samples collected during Tara Oceans expedition are annotated with ENVO
  examples:
  - description: Sample collected during the Tara Oceans expedition (2009-2013) at station TARA_004 (latitudeN=36.5533, longitudeE=-6.5669)
    url: https://www.ebi.ac.uk/metagenomics/projects/ERP001736/samples/ERS487899
  user: http://oceans.taraexpeditions.org/en/
- description: Annotation of habitats of microbes
  examples:
  - description: Annotation of habitat of Pseudovibrio sp. FO-BEG1 to marine environment
    url: https://www.ncbi.nlm.nih.gov/nuccore/NC_016642
  user: https://www.ncbi.nlm.nih.gov/
- description: Annotation and semantic search over microbial data sets
  examples:
  - description: Example metadata of a sample of marine water near Lisboa, taken as part of the Ocean Sampling Day Project (https://www.microb3.eu/osd.html). ENVO is used for the fields environmental feature, material, and biome.
    url: https://www.planetmicrobe.org/project/#/samples/200
  user: https://www.planetmicrobe.org/project/
activity_status: active
---

EnvO is a community ontology for the concise, controlled description of environments.

Envo can be cited as:

Buttigieg, P. L., Morrison, N., Smith, B., Mungall, C. J., & Lewis, S. E. (2013). <b>The environment ontology: contextualising biological and biomedical entities</b>. <i>Journal of Biomedical Semantics, 4(1), 43</i>. <a href="http://www.dx.doi.org/10.1186/2041-1480-4-43">doi:10.1186/2041-1480-4-43</a>

Or for latest developments:

Buttigieg, P. L., Pafilis, E., Lewis, S. E., Schildhauer, M. P., Walls, R. L., & Mungall, C. J. (2016). <b>The environment ontology in 2016: bridging domains with increased scope, semantic density, and interoperation</b>. <i>Journal of Biomedical Semantics</i>, 7(1), 57. <a href="https://doi.org/10.1186/s13326-016-0097-6">doi:10.1186/s13326-016-0097-6</a>
