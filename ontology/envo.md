---
layout: ontology_detail
id: envo
contact:
  email: p.buttigieg@gmail.com
  label: Pier Luigi Buttigieg
  github: pbuttigieg
description: Ontology of environmental features and habitats
domain: environment
homepage: http://environmentontology.org/
page: https://github.com/EnvironmentOntology/envo
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
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
  - id: subsets/envo-basic.obo
    title: OBO-Basic edition of ENVO
  - id: subsets/envoEmpo.owl
    title: Earth Microbiome Project subset
  - id: subsets/EnvO-Lite-GSC.obo
    title: GSC Lite subset of ENVO
    homepage: http://environmentontology.org/downloads
title: Environment Ontology
dependencies:
 - id: uberon
 - id: pco
 - id: ro
 - id: chebi
 - id: ncbitaxon
usages:
 - type: data-annotation
   description: "describing species habitats"
   examples:
     url: http://eol.org/pages/211700/data
   resources:
     url: http://eol.org
     label: EOL
 - type: data-annotation
   description: "describing stomach contents"
   datasets:
     url: https://s3.amazonaws.com/globi/snapshot/target/data/taxa/interactions.csv.gz
   resources:
     url: http://globalbioticinteractions.org
     label: GloBI
 - type: dataset-description
   description: "annotating datasets in data repositories"
   seeAlso: http://blogs.nature.com/scientificdata/2015/12/17/isa-explorer/
   search: http://scientificdata.isa-explorer.org/
   resources:
     url: http://www.nature.com/sdata/
     label: Nature Scientific Data
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
usages:
  - user: http://oceans.taraexpeditions.org/en/
    description: Samples collected during Tara Oceans expedition are annotated with ENVO
    example:
      - url: https://www.ebi.ac.uk/metagenomics/projects/ERP001736/samples/ERS487899
        description: "Sample collected during the Tara Oceans expedition (2009-2013) at station TARA_004 (latitudeN=36.5533, longitudeE=-6.5669)"
  - user: https://www.ncbi.nlm.nih.gov/
    description: Annotation of habitats of microbes
    example:
      - url: https://www.ncbi.nlm.nih.gov/nuccore/NC_016642
        description: "Annotation of habitat of Pseudovibrio sp. FO-BEG1 to marine environment"
activity_status: active
---

EnvO is a community ontology for the concise, controlled description of environments.

<img src="/logos/envo.png"/>

Envo can be cited as:

Buttigieg, P. L., Morrison, N., Smith, B., Mungall, C. J., & Lewis, S. E. (2013). <b>The environment ontology: contextualising biological and biomedical entities</b>. <i>Journal of Biomedical Semantics, 4(1), 43</i>. <a href="http://www.dx.doi.org/10.1186/2041-1480-4-43">doi:10.1186/2041-1480-4-43</a>

Or for latest developments:

Buttigieg, P. L., Pafilis, E., Lewis, S. E., Schildhauer, M. P., Walls, R. L., & Mungall, C. J. (2016). <b>The environment ontology in 2016: bridging domains with increased scope, semantic density, and interoperation</b>. <i>Journal of Biomedical Semantics</i>, 7(1), 57. <a href="https://doi.org/10.1186/s13326-016-0097-6">doi:10.1186/s13326-016-0097-6</a>


