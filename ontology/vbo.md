---
layout: ontology_detail
id: vbo
title: Vertebrate Breed Ontology
contact:
  email: Sabrina@tislab.org
  github: sabrinatoro
  label: Sabrina Toro
  orcid: 0000-0002-4142-7153
dependencies:
- id: ncbitaxon
depicted_by: https://github.com/tis-lab/closed-illustrations/blob/15058315cba1018e09572b28ebeee262a458b1c6/logos/vbo-logo/VBO-black-logo-stackedv2.png
description: Vertebrate Breed Ontology is an ontology created to serve as a single computable resource for vertebrate breed names.
domain: organisms
homepage: https://github.com/monarch-initiative/vertebrate-breed-ontology
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
mailing_list: https://groups.google.com/group/VBO-users
preferredPrefix: VBO
products:
- id: vbo.owl
  name: Vertebrate Breed Ontology main release in OWL format
- id: vbo.obo
  name: Vertebrate Breed Ontology additional release in OBO format
- id: vbo.json
  name: Vertebrate Breed Ontology additional release in OBOJSon format
- id: vbo/vbo-base.owl
  name: Vertebrate Breed Ontology main release in OWL format
- id: vbo/vbo-base.obo
  name: Vertebrate Breed Ontology additional release in OBO format
- id: vbo/vbo-base.json
  name: Vertebrate Breed Ontology additional release in OBOJSon format
publications:
- id: https://doi.org/10.1111/jvim.70133
  title: 'The Vertebrate Breed Ontology: Toward Effective Breed Data Standardization'
repository: https://github.com/monarch-initiative/vertebrate-breed-ontology
tracker: https://github.com/monarch-initiative/vertebrate-breed-ontology/issues
usages:
- description: VBO is used in the Online Mendelian Inheritance in Animals (OMIA) for breed annotations.
  examples:
  - description: Urticaria pigmentosa affects the Sphynx (Cat) (VBO:0100230) breed.
    url: https://www.omia.org/OMIA001289/9685/
  type: annotation
  user: https://omia.org/home/
- description: VBO is used in Cellosaurus for breed/subspecies of origin of cell lines.
  examples:
  - description: The cell line AG07906 derived from the Thoroughbred (VBO:0001083) breed of Equuus caballus (Horse).
    url: https://www.cellosaurus.org/CVCL_2L83
  type: annotation
  user: https://www.cellosaurus.org/index.html
activity_status: active
---
