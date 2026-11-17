---
layout: ontology_detail
id: idpo
title: Intrinsically Disordered Proteins Ontology
description: An ontology of the structural states, transitions, functions and roles of intrinsically disordered proteins and regions, including biomolecular condensates.
domain: biochemistry
contact:
  email: ximena.castro@unipd.it
  label: Ximena Aixa Castro
  github: XimeAixa
  orcid: 0000-0002-9211-1255
homepage: https://github.com/BioComputingUP/idpo
repository: https://github.com/BioComputingUP/idpo
tracker: https://github.com/BioComputingUP/idpo/issues
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC-BY 4.0
preferredPrefix: IDPO
products:
  - id: idpo.owl
    name: IDPO (OWL)
    description: The main release of IDPO in OWL format.
  - id: idpo.obo
    name: IDPO (OBO)
    description: The main release of IDPO in OBO format.
  - id: idpo.json
    name: IDPO (OBO Graphs JSON)
    description: The main release of IDPO in OBO Graphs JSON format.
  - id: idpo/idpo-base.owl
    name: IDPO base module (OWL)
    description: IDPO's own axioms only, without imported terms.
  - id: idpo/idpo-base.obo
    name: IDPO base module (OBO)
    description: The IDPO base module in OBO format.
  - id: idpo/idpo-base.json
    name: IDPO base module (OBO Graphs JSON)
    description: The IDPO base module in OBO Graphs JSON format.
  - id: idpo/idpo-full.owl
    name: IDPO full (OWL)
    description: IDPO with all imports merged and the full reasoned class hierarchy.
  - id: idpo/idpo-full.obo
    name: IDPO full (OBO)
    description: The IDPO full release in OBO format.
  - id: idpo/idpo-full.json
    name: IDPO full (OBO Graphs JSON)
    description: The IDPO full release in OBO Graphs JSON format.
  - id: idpo/idpo-simple.owl
    name: IDPO simple (OWL)
    description: A simplified version of IDPO with only subclass and existential restriction axioms.
  - id: idpo/idpo-simple.obo
    name: IDPO simple (OBO)
    description: The IDPO simple release in OBO format.
  - id: idpo/idpo-simple.json
    name: IDPO simple (OBO Graphs JSON)
    description: The IDPO simple release in OBO Graphs JSON format.
dependencies:
- id: ro
- id: go
- id: omo
- id: bfo
- id: cob
- id: iao
usages:
  - user: https://disprot.org
    description: DisProt uses IDPO terms for the standardized annotation of intrinsically disordered proteins and regions.
    examples:
      - url: https://disprot.org/ontology
        description: IDPO ontology page in DisProt
activity_status: active
---

The Intrinsically Disordered Proteins Ontology (IDPO) defines concepts and relationships that describe the structural states, dynamic transitions, and functional roles of intrinsically disordered proteins (IDPs) and intrinsically disordered regions (IDRs). Its terms and definitions are grounded in the terminology used by the IDP research community and derived from scientific literature in the field.

IDPO’s primary goal is to harmonize vocabulary across experimental and computational studies, enabling consistent annotation of IDP-related data and supporting integration and interoperability across biomedical and structural biology resources. By standardizing terms, IDPO facilitates data sharing, knowledge discovery, and collaboration within the protein disorder research community. IDPO is used by the [DisProt database](https://disprot.org/) to provide ontology-driven, standardized annotation of intrinsically disordered proteins and regions, improving data consistency and enabling richer cross-database integration.

IDPO is maintained by the [IDP Community](https://elixir-europe.org/communities/intrinsically-disordered-proteins) and supported by the [ELIXIR Infrastructure](https://elixir-europe.org/) (project: [Advancing structural and functional ontologies of disordered proteins](https://elixir-europe.org/how-we-work/scientific-programme/commissioned-services/science/cmr/ontologies)). It has also received funding from the European Union (HORIZON-MSCA-SE project IDPfun2) [no. 101182949].

More information can be found at the [DisProt Ontology Page](https://disprot.org/ontology).
