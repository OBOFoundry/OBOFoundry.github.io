---
layout: ontology_detail
id: cl
label: Cell Ontology
title: Cell Ontology
homepage: https://obophenotype.github.io/cell-ontology/
jobs:
  - id: https://travis-ci.org/obophenotype/cell-ontology
    type: travis-ci
build:
  checkout: git clone https://github.com/obophenotype/cell-ontology.git
  email_cc: cl_edit@googlegroups.com
  system: git
  method: vcs
  infallible: 1
description: The Cell Ontology is a structured controlled vocabulary for cell types in animals.
integration_server: http://build.berkeleybop.org/job/build-cl/
contact:
  label: Alexander Diehl
  email: addiehl@buffalo.edu
  github: addiehl
  orcid: 0000-0001-9990-8331
license:
  url: http://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
taxon:
  id: NCBITaxon:33208
  label: Metazoa
domain: anatomy and development
tags:
  - cells
tracker: https://github.com/obophenotype/cell-ontology/issues
mailing_list: https://groups.google.com/g/cl_edit
publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/27377652
    title: "The Cell Ontology 2016: enhanced content, modularization, and ontology interoperability."
dependencies:
  - id: uberon
  - id: go
  - id: ro
  - id: chebi
  - id: pato
  - id: pr
  - id: ncbitaxon
canonical: cl.owl
products:
  - id: cl.owl
    title: Main CL OWL edition
    description: Complete ontology, plus inter-ontology axioms, and imports modules
    format: owl-rdf/xml
    is_canonical: true
    uses: [uberon, chebi, go, pr, pato, ncbitaxon, ro]
  - id: cl.obo
    title: CL obo format edition
    description: Complete ontology, plus inter-ontology axioms, and imports modules merged in
    format: obo
    derived_from: cl.owl
  - id: cl/cl-basic.obo
    title: Basic CL
    description: Basic version, no inter-ontology axioms
    format: obo
  - id: cl/cl-base.owl
    title: CL base module
    description: complete CL but with no imports or external axioms
usages:
  - user: https://biccn.org/
    type: annotation
    description: The BICCN created a high-resolution atlas of cell types in the primary motor based on single cell transcriptomics. These cell types are represented in the brain data standards ontology which anchors to cell types in the cell ontology.
    publications:
    - id: https://doi.org/10.1101/2021.10.10.463703
      title: "Brain Data Standards Ontology: A data-driven ontology of transcriptomically defined cell types in the primary motor cortex"
  - user: https://hubmapconsortium.org/
    type: annotation
    description: HuBMAP develops tools to create an open, global atlas of the human body at the cellular level. The Cell Ontology is used in annotating cell types in the tools developed.
    publications:
    - id: https://pubmed.ncbi.nlm.nih.gov/31597973/
      title: "The human body at cellular resolution: the NIH Human Biomolecular Atlas Program."
  - user: https://www.humancellatlas.org/
    type: annotation
    description: The Human Cell Atlas (HCA) is an international group of researchers using a combination of these new technologies to create cellular reference maps. The HCA use CL to annotated cells in their reference maps. 
    publications:
    - id: https://pubmed.ncbi.nlm.nih.gov/29206104/
      title: "The Human Cell Atlas"
  - user: https://www.ebi.ac.uk/gxa/home
    type: annotation
    description: The EBI single cell expression atlas is an extension to EBI expression atlas that displays gene expression in single cells. Cell types in the single cell expression atlas linked with terms from the Cell Ontology.
    publications:
    - id: https://pubmed.ncbi.nlm.nih.gov/31665515/
      title: "Expression Atlas update: from tissues to single cells"
  - user: https://www.encodeproject.org/
    seeAlso: https://www.biosharing.org/biodbcore-000034
    type: annotation
    description: The National Human Genome Research Institute (NHGRI) launched a public research consortium named ENCODE, the Encyclopedia Of DNA Elements, in September 2003, to carry out a project to identify all functional elements in the human genome sequence. The ENCODE DCC uses Uberon to annotate samples
    publications:
      - id: https://www.ncbi.nlm.nih.gov/pubmed/25776021
        title: "Ontology application and use at the ENCODE DCC"
  - user: http://fantom5-collaboration.gsc.riken.jp/
    type: annotation
    description: FANTOM5 is using Uberon and CL to annotate samples allowing for transcriptome analyses with cell-type and tissue-level specificity.
    examples:
      - url: http://fantom.gsc.riken.jp/5/sstar/CL:0000540
        description: FANTOM5 samples annotated to neuron
activity_status: active
repository: https://github.com/obophenotype/cell-ontology
preferredPrefix: CL
---

![logo](/images/CL-logo.jpg)

The Cell Ontology is designed as a structured controlled vocabulary for cell types. This ontology was constructed for use by the model organism and other bioinformatics databases, where there is a need for a controlled vocabulary of cell types. This ontology is not organism specific. It covers cell types from prokaryotes to mammals. However, it excludes plant cell types, which are covered by PO.

## Integration with other ontologies

Cell types in CL are linked to [uberon](uberon.html) via part-of
relationships. The cl.owl product imports a subset of the entire
uberon ontology. To see all cell types in the context of all
anatomical structures, use the uberon ext release.

Cell types are linked to [GO](go.html) biological processes via the
capable-of relationship type. CL also links to other ontologies such
as [chebi](chebi.html), [pr](pr.html) and [pato](pato.html).

In turn, CL is linked to from a variety of ontologies such as GO,
Uberon and various phenotype ontologies.

## Applications

The following are some applications of the cell ontology along with their publications: 

**HuBMAP**

HuBMAP Consortium (2019) The human body at cellular resolution: the NIH Human Biomolecular Atlas Program. Nature, 574, 187–192

**Human Cell Atlas (HCA)**

Regev,A., Teichmann,S.A., Lander,E.S., Amit,I., Benoist,C., Birney,E., Bodenmiller,B., Campbell,P., Carninci,P., Clatworthy,M., et al. (2017) The Human Cell Atlas. Elife, 6.

**Single Cell Expression Atlas**

Papatheodorou,I., Moreno,P., Manning,J., Fuentes,A.M.-P., George,N., Fexova,S., Fonseca,N.A., Füllgrabe,A., Green,M., Huang,N., et al. (2020) Expression Atlas update: from tissues to single cells. Nucleic Acids Res., 48, D77–D83.

**BRAIN Initiative Cell Census Network (BICCN)/Brain Data Standards Ontology**

Tan,S.Z.K., Kir,H., Aevermann,B., Gillespie,T., Hawrylycz,M., Lein,E., Matentzoglu,N., Miller,J., Mollenkopf,T.S., Mungall,C.J., et al. (2021) Brain Data Standards Ontology: A data-driven ontology of transcriptomically defined cell types in the primary motor cortex. bioRxiv, 10.1101/2021.10.10.463703.

**ENCODE**

Malladi, V. S., Erickson, D. T., Podduturi, N. R., Rowe, L. D., Chan,
E. T., Davidson, J. M., … Hong, E. L. (2015). Ontology application and
use at the ENCODE DCC. Database : The Journal of Biological Databases
and Curation, 2015, bav010–. [doi:10.1093/database/bav010](https://doi.org/doi:10.1093/database/bav010)

**FANTOMS**

Lizio, M., Harshbarger, J., Shimoji, H., Severin, J., Kasukawa, T.,
Sahin, S., … Kawaji, H. (2015). Gateways to the FANTOM5 promoter level
mammalian expression atlas. Genome Biology, 16(1),
22. [doi:10.1186/s13059-014-0560-6](https://doi.org/doi:10.1186/s13059-014-0560-6)

**LINCS**

[Metadata Standard and Data Exchange Specifications
to Describe, Model, and Integrate Complex and Diverse High-Throughput
Screening Data from the Library of Integrated Network-based Cellular
Signatures
(LINCS)](http://jbx.sagepub.com/content/early/2014/02/11/1087057114522514.full)
