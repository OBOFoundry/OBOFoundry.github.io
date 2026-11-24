---
layout: ontology_detail
id: idpo
title: Intrinsically Disordered Proteins Ontology
contact:
  email: ximena.castro@unipd.it
  github: XimeAixa
  label: Ximena Aixa Castro
  orcid: 0000-0002-9211-1255
dependencies:
- id: bfo
- id: cob
- id: go
- id: iao
- id: omo
- id: ro
description: An ontology of the structural states, transitions, functions and roles of intrinsically disordered proteins and regions, including biomolecular condensates.
domain: chemistry and biochemistry
homepage: https://github.com/BioComputingUP/idpo
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: IDPO
products:
- id: idpo.owl
  description: The main release of IDPO in OWL format.
  name: IDPO (OWL)
- id: idpo.obo
  description: The main release of IDPO in OBO format.
  name: IDPO (OBO)
- id: idpo.json
  description: The main release of IDPO in OBO Graphs JSON format.
  name: IDPO (OBO Graphs JSON)
- id: idpo/idpo-base.owl
  description: IDPO's own axioms only, without imported terms.
  name: IDPO base module (OWL)
- id: idpo/idpo-base.obo
  description: The IDPO base module in OBO format.
  name: IDPO base module (OBO)
- id: idpo/idpo-base.json
  description: The IDPO base module in OBO Graphs JSON format.
  name: IDPO base module (OBO Graphs JSON)
- id: idpo/idpo-full.owl
  description: IDPO with all imports merged and the full reasoned class hierarchy.
  name: IDPO full (OWL)
- id: idpo/idpo-full.obo
  description: The IDPO full release in OBO format.
  name: IDPO full (OBO)
- id: idpo/idpo-full.json
  description: The IDPO full release in OBO Graphs JSON format.
  name: IDPO full (OBO Graphs JSON)
- id: idpo/idpo-simple.owl
  description: A simplified version of IDPO with only subclass and existential restriction axioms.
  name: IDPO simple (OWL)
- id: idpo/idpo-simple.obo
  description: The IDPO simple release in OBO format.
  name: IDPO simple (OBO)
- id: idpo/idpo-simple.json
  description: The IDPO simple release in OBO Graphs JSON format.
  name: IDPO simple (OBO Graphs JSON)
repository: https://github.com/BioComputingUP/idpo
tracker: https://github.com/BioComputingUP/idpo/issues
usages:
- description: DisProt uses IDPO terms for the standardized annotation of intrinsically disordered proteins and regions.
  examples:
  - description: IDPO ontology page in DisProt
    url: https://disprot.org/ontology
  user: https://disprot.org
activity_status: active
---

The Intrinsically Disordered Proteins Ontology (IDPO) defines concepts and relationships that describe the structural states, dynamic transitions, and functional roles of intrinsically disordered proteins (IDPs) and intrinsically disordered regions (IDRs). Its terms and definitions are grounded in the terminology used by the IDP research community and derived from scientific literature in the field.

IDPO’s primary goal is to harmonize vocabulary across experimental and computational studies, enabling consistent annotation of IDP-related data and supporting integration and interoperability across biomedical and structural biology resources. By standardizing terms, IDPO facilitates data sharing, knowledge discovery, and collaboration within the protein disorder research community. IDPO is used by the [DisProt database](https://disprot.org/) to provide ontology-driven, standardized annotation of intrinsically disordered proteins and regions, improving data consistency and enabling richer cross-database integration.

IDPO is maintained by the [IDP Community](https://elixir-europe.org/communities/intrinsically-disordered-proteins) and supported by the [ELIXIR Infrastructure](https://elixir-europe.org/) (project: [Advancing structural and functional ontologies of disordered proteins](https://elixir-europe.org/how-we-work/scientific-programme/commissioned-services/science/cmr/ontologies)). It has also received funding from the European Union (HORIZON-MSCA-SE project IDPfun2) [no. 101182949].

More information can be found at the [DisProt Ontology Page](https://disprot.org/ontology).
