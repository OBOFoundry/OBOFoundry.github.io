---
layout: ontology_detail
id: envo
contact:
  email: p.buttigieg@gmail.com
  label: Pier Luigi Buttigieg
  github: pbuttigieg
  orcid: 0000-0002-4366-3088
description: Ontology of environmental features and habitats
domain: environment
homepage: http://environmentontology.org/
page: https://github.com/EnvironmentOntology/envo
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC BY 3.0
publications:
  - id: http://www.dx.doi.org/10.1186/2041-1480-4-43
    title: "The environment ontology: contextualising biological and biomedical entities"
  - id: https://doi.org/10.1186/s13326-016-0097-6
    title: "The environment ontology in 2016: bridging domains with increased scope, semantic density, and interoperation"
products:
  - id: envo.owl
    title: "main ENVO OWL release"
  - id: envo.json
    title: "ENVO in obographs JSON format"
  - id: envo.obo
    title: "ENVO in OBO Format. May be lossy"
  - id: envo/subsets/envo-basic.obo
    title: OBO-Basic edition of ENVO
  - id: envo/subsets/envoEmpo.owl
    title: Earth Microbiome Project subset
  - id: envo/subsets/EnvO-Lite-GSC.obo
    title: GSC Lite subset of ENVO
    homepage: http://environmentontology.org/downloads
title: Environment Ontology
dependencies:
  - id: uberon
  - id: pco
  - id: ro
  - id: chebi
  - id: ncbitaxon
  - id: foodon
  - id: po
  - id: go
usages:
  - user: http://eol.org
    type: data-annotation
    description: "describing species habitats"
    examples:
      - url: http://eol.org/pages/211700/data
        description: "Pseudobarbus burchelli (Tradou Redfin) is a species of bony fishes in the family Cyprinidae. They are associated with freshwater habitat. Individuals can grow to 13.5 cm. They have sexual reproduction."
  - user: http://globalbioticinteractions.org
    type: data-annotation
    description: "describing stomach contents"
  - user: http://www.nature.com/sdata/
    type: dataset-description
    description: "annotating datasets in data repositories"
    seeAlso: http://blogs.nature.com/scientificdata/2015/12/17/isa-explorer/
  - user: http://oceans.taraexpeditions.org/en/
    description: Samples collected during Tara Oceans expedition are annotated with ENVO
    examples:
      - url: https://www.ebi.ac.uk/metagenomics/projects/ERP001736/samples/ERS487899
        description: "Sample collected during the Tara Oceans expedition (2009-2013) at station TARA_004 (latitudeN=36.5533, longitudeE=-6.5669)"
  - user: https://www.ncbi.nlm.nih.gov/
    description: Annotation of habitats of microbes
    examples:
      - url: https://www.ncbi.nlm.nih.gov/nuccore/NC_016642
        description: "Annotation of habitat of Pseudovibrio sp. FO-BEG1 to marine environment"
  - user: https://www.planetmicrobe.org/project/
    description: Annotation and semantic search over microbial data sets
    examples:
      - url: https://www.planetmicrobe.org/project/#/samples/200
        description: "Example metadata of a sample of marine water near Lisboa, taken as part of the Ocean Sampling Day Project (https://www.microb3.eu/osd.html). ENVO is used for the fields environmental feature, material, and biome."
jobs:
  - id: https://travis-ci.org/EnvironmentOntology/envo
    type: travis-ci
build:
  checkout: git clone https://github.com/EnvironmentOntology/envo.git
  email_cc: cjmungall@lbl.gov
  system: git
  path: .
  method: vcs
  infallible: 1
tracker: https://github.com/EnvironmentOntology/envo/issues/
activity_status: active
repository: https://github.com/EnvironmentOntology/envo
preferredPrefix: ENVO
depicted_by: /logos/envo.png
---

EnvO is a community ontology for the concise, controlled description of environments.

Envo can be cited as:

Buttigieg, P. L., Morrison, N., Smith, B., Mungall, C. J., & Lewis, S. E. (2013). <b>The environment ontology: contextualising biological and biomedical entities</b>. <i>Journal of Biomedical Semantics, 4(1), 43</i>. <a href="http://www.dx.doi.org/10.1186/2041-1480-4-43">doi:10.1186/2041-1480-4-43</a>

Or for latest developments:

Buttigieg, P. L., Pafilis, E., Lewis, S. E., Schildhauer, M. P., Walls, R. L., & Mungall, C. J. (2016). <b>The environment ontology in 2016: bridging domains with increased scope, semantic density, and interoperation</b>. <i>Journal of Biomedical Semantics</i>, 7(1), 57. <a href="https://doi.org/10.1186/s13326-016-0097-6">doi:10.1186/s13326-016-0097-6</a>
