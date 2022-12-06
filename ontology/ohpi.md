---
layout: ontology_detail
id: ohpi
title: Ontology of Host Pathogen Interactions
contact:
  email: edong@umich.edu
  github: e4ong1031
  label: Edison Ong
  orcid: 0000-0002-5159-414X
description: OHPI is a community-driven ontology of host-pathogen interactions (OHPI) and represents the virulence factors (VFs) and how the mutants of VFs in the Victors database become less virulence inside a host organism or host cells. It is developed to represent manually curated HPI knowledge available in the PHIDIAS resource.
domain: biological systems
homepage: https://github.com/OHPI/ohpi
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
mailing_list: http://groups.google.com/group/ohpi-discuss
preferredPrefix: OHPI
products:
- id: ohpi.owl
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/30365026
  title: 'Victors: a web-based knowledge base of virulence factors in human and animal pathogens'
repository: https://github.com/OHPI/ohpi
tracker: https://github.com/OHPI/ohpi/issues
activity_status: active
---

# OHPI: Ontology of Host-Pathogen Interactions

OHPI is a community-driven ontology of host-pathogen interactions (OHPI) and represents the virulence factors (VFs) and how the mutants of VFs in the [Victors](http://www.phidias.us/victors/index.php) database become less virulence inside a host organism or host cells. It is developed to represent manually curated HPI knowledge available in the [PHIDIAS](http://www.phidias.us) resource.

**Example:** The OHPI object property ‘gene mutant attenuated in host cell’ represents a relation between a gene and a host cell where the microbial mutant lacking the gene is attenuated in the host cell compared to the wild type microbe. Such an object property can be used to represent a virulence factor and its interaction in a host cell, e.g., the ugpB gene of *Brucella spp.* and human epithelial cell line HeLa cell line where the ugpB mutant of *Brucella spp.* is attenuated in HeLa cells.

More detail about OHPI can be found in the supplemental data from the paper: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6324020/bin/gky999_supplemental_files.pdf
