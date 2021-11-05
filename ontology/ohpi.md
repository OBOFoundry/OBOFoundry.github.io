---
layout: ontology_detail
id: ohpi
title: Ontology of Host Pathogen Interactions
description: OHPI is a community-driven ontology of host-pathogen interactions (OHPI) and represents the virulence factors (VFs) and how the mutants of VFs in the Victors database become less virulence inside a host organism or host cells. It is developed to represent manually curated HPI knowledge available in the PHIDIAS resource.
homepage: https://github.com/OHPI/ohpi
mailing_list: http://groups.google.com/group/ohpi-discuss
tracker: https://github.com/OHPI/ohpi/issues
contact:
  email: edong@umich.edu
  label: Edison Ong
products:
  - id: ohpi.owl
license:
  url: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
activity_status: active
repository: https://github.com/OHPI/ohpi
preferredPrefix: OHPI
---

# OHPI: Ontology of Host-Pathogen Interactions

OHPI is a community-driven ontology of host-pathogen interactions (OHPI) and represents the virulence factors (VFs) and how the mutants of VFs in the [Victors](http://www.phidias.us/victors/index.php) database become less virulence inside a host organism or host cells. It is developed to represent manually curated HPI knowledge available in the [PHIDIAS](http://www.phidias.us) resource.

**Example:** The OHPI object property ‘gene mutant attenuated in host cell’ represents a relation between a gene and a host cell where the microbial mutant lacking the gene is attenuated in the host cell compared to the wild type microbe. Such an object property can be used to represent a virulence factor and its interaction in a host cell, e.g., the ugpB gene of *Brucella spp.* and human epithelial cell line HeLa cell line where the ugpB mutant of *Brucella spp.* is attenuated in HeLa cells.

## Reference

Sayers S, Li L, Ong E, Deng S, Fu G, Lin Y, Yang B, Zhang S, Fa Z, Zhao B, Xiang Z, Li Y, Zhao Z, Olszewski MA, Chen L, He Y. Victors: a web-based knowledge base of virulence factors in human and animal pathogens. Nucleic Acid Research. 2019 Jan 8;47(D1):D693-D700. doi: 10.1093/nar/gky999. [PMID: 30365026](https://www.ncbi.nlm.nih.gov/pubmed/30365026). PMCID: [PMC6324020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6324020/).

More detail about OHPI can be found in the supplemental data from the paper: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6324020/bin/gky999_supplemental_files.pdf


More information can be found at http://obofoundry.org/ontology/ohpi
