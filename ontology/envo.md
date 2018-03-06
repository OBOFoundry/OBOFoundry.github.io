---
layout: ontology_detail
id: envo
contact:
  email: p.buttigieg@googlemail.com
  label: Pier Luigi Buttigieg
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
  - id: http://doi.org/10.1186/s13326-016-0097-6
    title: "The environment ontology in 2016: bridging domains with increased scope, semantic density, and interoperation"
products:
  - id: envo.owl
  - id: envo.obo
  - id: subsets/envo-basic.obo
    title: OBO-Basic edition of ENVO
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

---

EnvO is a community ontology for the concise, controlled description of environments.

<img src="/logos/envo.png"/>

Envo can be cited as:

Buttigieg, P. L., Morrison, N., Smith, B., Mungall, C. J., & Lewis, S. E. (2013). <b>The environment ontology: contextualising biological and biomedical entities</b>. <i>Journal of Biomedical Semantics, 4(1), 43</i>. <a href="http://www.dx.doi.org/10.1186/2041-1480-4-43">doi:10.1186/2041-1480-4-43</a>

Or for latest developments:

Buttigieg, P. L., Pafilis, E., Lewis, S. E., Schildhauer, M. P., Walls, R. L., & Mungall, C. J. (2016). <b>The environment ontology in 2016: bridging domains with increased scope, semantic density, and interoperation</b>. <i>Journal of Biomedical Semantics</i>, 7(1), 57. <a href="http://doi.org/10.1186/s13326-016-0097-6">doi:10.1186/s13326-016-0097-6</a>


