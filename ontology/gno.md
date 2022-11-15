---
layout: ontology_detail
id: gno
title: Glycan Naming and Subsumption Ontology (GNOme)
browsers:
- title: GNOme Glycan Structure Browser
  label: Structure Browser
  url: https://gnome.glyomics.org/StructureBrowser.html?HexNAc=4&Hex=5&dHex=1&NeuAc=2
- title: GNOme Glycan Composition Browser
  label: Composition Browser
  url: https://gnome.glyomics.org/CompositionBrowser.html?HexNAc=4&Hex=5&dHex=1&NeuAc=2
build:
  checkout: git clone https://github.com/glygen-glycan-data/GNOme.git
  path: .
  system: git
contact:
  email: nje5@georgetown.edu
  github: edwardsnj
  label: Nathan Edwards
  orcid: 0000-0001-5168-3196
description: GlyTouCan provides stable accessions for glycans described at varyious degrees of characterization, including compositions (no linkage) and topologies (no carbon bond positions or anomeric configurations). GNOme organizes these stable accessions for interative browsing, for text-based searching, and for automated reasoning with well-defined characterization levels.
domain: chemistry and biochemistry
github_date_added: 2019-08-15
homepage: https://gnome.glyomics.org/
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: GNO
products:
- id: gno.owl
  description: Glycan Naming and Subsumption Ontology, OWL format (primary)
- id: gno.obo
  description: Glycan Naming and Subsumption Ontology, OBO format (automated conversion from OWL)
- id: gno.json
  description: Glycan Naming and Subsumption Ontology, JSON format (automated conversion from OWL)
publications:
- id: https://doi.org/10.5281/zenodo.6678278
  title: GNOme - Glycan Naming and Subsumption Ontology
repository: https://github.com/glygen-glycan-data/GNOme
tags:
- glycan structure
tracker: https://github.com/glygen-glycan-data/GNOme/issues
usages:
- description: GlyGen - Computational and Informatics Resources for Glycoscience
  examples:
  - description: GNOme attributes and related glycans on glycan pages
    url: https://www.glygen.org/glycan/G00028MO
  user: https://www.glygen.org/
- description: PRO - Protein Ontology
  examples:
  - description: example of PRO use of GNO terms
    url: http://purl.obolibrary.org/obo/PR_000059585
  user: https://proconsortium.org/
- description: ChEBI - Chemical Entities of Biological Interest
  examples:
  - description: example of ChEBI use of GNO terms
    url: http://purl.obolibrary.org/obo/CHEBI_167503
  user: https://www.ebi.ac.uk/chebi/init.do
activity_status: active
---
