---
layout: ontology_detail
id: gno
contact:
  email: nje5@georgetown.edu
  label: Nathan Edwards
  github: edwardsnj
  orcid: 0000-0001-5168-3196
description: GlyTouCan provides stable accessions for glycans described at varyious degrees of characterization, including compositions (no linkage) and topologies (no carbon bond positions or anomeric configurations). GNOme organizes these stable accessions for interative browsing, for text-based searching, and for automated reasoning with well-defined characterization levels.
domain: chemistry and biochemistry
tags:
  - glycan structure
homepage: https://gnome.glyomics.org/
products:
  - id: gno.owl
    description: Glycan Naming and Subsumption Ontology, OWL format (primary)
  - id: gno.obo
    description: Glycan Naming and Subsumption Ontology, OBO format (automated conversion from OWL)
  - id: gno.json
    description: Glycan Naming and Subsumption Ontology, JSON format (automated conversion from OWL)
title: Glycan Naming and Subsumption Ontology (GNOme)
build:
  checkout: git clone https://github.com/glygen-glycan-data/GNOme.git
  system: git
  path: "."
tracker: https://github.com/glygen-glycan-data/GNOme/issues
license:
  url: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
browsers:
  - label: Structure Browser
    title: GNOme Glycan Structure Browser
    url: https://gnome.glyomics.org/StructureBrowser.html?HexNAc=4&Hex=5&dHex=1&NeuAc=2
  - label: Composition Browser
    title: GNOme Glycan Composition Browser
    url: https://gnome.glyomics.org/CompositionBrowser.html?HexNAc=4&Hex=5&dHex=1&NeuAc=2
publications:
  - id: https://doi.org/10.5281/zenodo.6678278
    title: "GNOme - Glycan Naming and Subsumption Ontology"
usages:
  - user: https://www.glygen.org/
    description: GlyGen - Computational and Informatics Resources for Glycoscience
    examples:
      - url: https://www.glygen.org/glycan/G00028MO
        description: GNOme attributes and related glycans on glycan pages
  - user: https://proconsortium.org/
    description: PRO - Protein Ontology
    examples:
      - url: http://purl.obolibrary.org/obo/PR_000059585
        description: example of PRO use of GNO terms
  - user: https://www.ebi.ac.uk/chebi/init.do
    description: ChEBI - Chemical Entities of Biological Interest
    examples:
      - url: http://purl.obolibrary.org/obo/CHEBI_167503
        description: example of ChEBI use of GNO terms
activity_status: active
repository: https://github.com/glygen-glycan-data/GNOme
preferredPrefix: GNO
added: 2019-08-15
---
