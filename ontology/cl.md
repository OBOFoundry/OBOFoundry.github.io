---
layout: ontology_detail
id: cl
title: Cell Ontology
canonical: cl.owl
contact:
  email: addiehl@buffalo.edu
  github: addiehl
  label: Alexander Diehl
  orcid: 0000-0001-9990-8331
dependencies:
- id: go
- id: ncbitaxon
- id: omo
- id: pato
- id: pr
- id: ro
- id: uberon
depicted_by: /images/CL-logo.jpg
description: The Cell Ontology is a structured controlled vocabulary for cell types in animals.
domain: anatomy and development
homepage: https://obophenotype.github.io/cell-ontology/
label: Cell Ontology
license:
  label: CC BY 4.0
  url: http://creativecommons.org/licenses/by/4.0/
mailing_list: https://groups.google.com/g/cl_edit
preferredPrefix: CL
products:
- id: cl.owl
  title: Main CL OWL edition
  description: Complete ontology, plus inter-ontology axioms, and imports modules
  format: owl-rdf/xml
  is_canonical: true
  uses:
  - go
  - ncbitaxon
  - omo
  - pato
  - pr
  - ro
  - uberon
- id: cl.obo
  title: CL obo format edition
  derived_from: cl.owl
  description: Complete ontology, plus inter-ontology axioms, and imports modules merged in
  format: obo
- id: cl/cl.json
  title: CL OBOGraph-JSON format edition
  derived_from: cl.owl
  description: Complete ontology, plus inter-ontology axioms, and imports modules merged in
  format: json
- id: cl/cl-basic.owl
  title: Basic CL
  description: Basic version, no inter-ontology axioms
  format: owl-rdf/xml
- id: cl/cl-basic.obo
  title: Basic CL (OBO version)
  description: Basic version, no inter-ontology axioms
  format: obo
- id: cl/cl-basic.json
  title: Basic CL (OBOGraph-JSON version)
  description: Basic version, no inter-ontology axioms
  format: json
- id: cl/cl-base.owl
  title: CL base module
  description: complete CL but with no imports or external axioms
  format: owl-rdf/xml
- id: cl/cl-base.obo
  title: CL base module (OBO version)
  description: complete CL but with no imports or external axioms
  format: obo
- id: cl/cl-base.json
  title: CL base module (OBOGraph-JSON version)
  description: complete CL but with no imports or external axioms
  format: json
publications:
- id: https://www.ncbi.nlm.nih.gov/pubmed/27377652
  title: 'The Cell Ontology 2016: enhanced content, modularization, and ontology interoperability.'
repository: https://github.com/obophenotype/cell-ontology
tags:
- cells
taxon:
  id: NCBITaxon:33208
  label: Metazoa
tracker: https://github.com/obophenotype/cell-ontology/issues
twitter: CellOntology
usages:
- description: The BICCN created a high-resolution atlas of cell types in the primary motor based on single cell transcriptomics. These cell types are represented in the brain data standards ontology which anchors to cell types in the cell ontology.
  examples:
  - description: cell type card of a cell type linked to a PCL cell type (L2/3 IT primary motor cortex glutamatergic neuron) which is a subclass of cell types in CL (CL:4023041)
    url: https://knowledge.brain-map.org/celltypes/CCN202002013/CS202002013_193
  - description: PCL cell type used in cell type cards linked directly to CL cell types
    url: https://www.ebi.ac.uk/ols/ontologies/pcl/terms?iri=http://purl.obolibrary.org/obo/PCL_0011193
  publications:
  - id: https://doi.org/10.1101/2021.10.10.463703
    title: 'Brain Data Standards Ontology: A data-driven ontology of transcriptomically defined cell types in the primary motor cortex'
  type: annotation
  user: https://biccn.org/
- description: HuBMAP develops tools to create an open, global atlas of the human body at the cellular level. The Cell Ontology is used in annotating cell types in the tools developed.
  examples:
  - description: ASCT+B reporter showing CL being used to annotate cell types in the heart
    url: https://hubmapconsortium.github.io/ccf-asct-reporter/vis?selectedOrgans=heart-v1.1&playground=false
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/31597973
    title: 'The human body at cellular resolution: the NIH Human Biomolecular Atlas Program.'
  type: annotation
  user: https://hubmapconsortium.org/
- description: The single-cell transcriptomics platform CZ CELLxGENE uses CL to annotate all cell types. All datasets on CellXGene are annotated according to a standard schema that specifies the use of CL to record Cell Type.
  examples:
  - description: A CELLxGENE Cell Guide entry for 'luminal adaptive secretory precursor cell of mammary gland', which includes the CL ID (CL:4033057), CL definition and a visualizer of CL hierarchy
    url: https://cellxgene.cziscience.com/cellguide/CL:4033057
  publications:
  - id: https://doi.org/10.1101/2021.04.05.438318
    title: 'CELLxGENE: a performant, scalable exploration platform for high dimensional sparse matrices'
  type: annotation
  user: https://cellxgene.cziscience.com/
- description: The Human Cell Atlas (HCA) is an international group of researchers using a combination of these new technologies to create cellular reference maps. The HCA use CL to annotate cells in their reference maps.
  examples:
  - description: HCA collection studies that are related B cell (CL:0000236) that is filtered through CL annotation
    url: https://singlecell.broadinstitute.org/single_cell?type=study&page=1&facets=cell_type%3ACL_0000236&scpbr=human-cell-atlas-main-collection
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/29206104
    title: The Human Cell Atlas
  type: annotation
  user: https://www.humancellatlas.org/
- description: The EBI single cell expression atlas is an extension to EBI expression atlas that displays gene expression in single cells. Cell types in the single cell expression atlas linked with terms from the Cell Ontology.
  examples:
  - description: RNA-Seq CAGE (Cap Analysis of Gene Expression) analysis of mice cells in RIKEN FANTOM5 project annotated using cell types from CL
    url: https://www.ebi.ac.uk/gxa/experiments/E-MTAB-3578/Results
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/31665515
    title: 'Expression Atlas update: from tissues to single cells'
  type: annotation
  user: https://www.ebi.ac.uk/gxa/home
- description: The National Human Genome Research Institute (NHGRI) launched a public research consortium named ENCODE, the Encyclopedia Of DNA Elements, in September 2003, to carry out a project to identify all functional elements in the human genome sequence. The ENCODE DCC uses Uberon to annotate samples
  publications:
  - id: https://www.ncbi.nlm.nih.gov/pubmed/25776021
    title: Ontology application and use at the ENCODE DCC
  seeAlso: https://doi.org/10.25504/FAIRsharing.v0hbjs
  type: annotation
  user: https://www.encodeproject.org/
- description: FANTOM5 is using Uberon and CL to annotate samples allowing for transcriptome analyses with cell-type and tissue-level specificity.
  examples:
  - description: FANTOM5 samples annotated to neuron
    url: http://fantom.gsc.riken.jp/5/sstar/CL:0000540
  type: annotation
  user: http://fantom5-collaboration.gsc.riken.jp/
activity_status: active
---

Cell Ontology (CL) is an ontology designed to classify and describe cell types across different organisms. 
It serves as a resource for model organism and bioinformatics databases. 
The ontology covers a broad range of cell types in animal cells, with over 2700 cell type classes, 
and provides high-level cell type classes as mapping points for cell type classes in ontologies 
representing other species, such as the Plant Ontology or Drosophila Anatomy Ontology. 
Integration with other ontologies such as Uberon, GO, CHEBI, PR, and PATO enables linking cell types to anatomical structures, biological processes, and other relevant concepts. 

The Cell Ontology was created in 2004 and has been a core OBO Foundry ontology since the start of the Foundry. 
Since then, CL has been adopted by various efforts,  including the HuBMAP project, Human Cell Atlas (HCA), 
cellxgene platform, Single Cell Expression Atlas, BRAIN Initiative Cell Census Network (BICCN), 
ArrayExpress, The Cell Image Library, ENCODE, and FANTOM5, for annotating cell types and 
facilitating cellular reference mapping, as documented through various publications and examples.

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

**CZ CELLxGENE**

CZI Single-Cell Biology Program, Shibla Abdulla, Brian Aevermann, Pedro Assis, Seve Badajoz, Sidney M. Bell, Emanuele Bezzi, et al. 2023. “CZ CELL×GENE Discover: A Single-Cell Data Platform for Scalable Exploration, Analysis and Modeling of Aggregated Data.” bioRxiv. [doi:10.1101/2023.10.30.563174](https://doi.org/10.1101/2023.10.30.563174).

**HuBMAP**

HuBMAP Consortium (2019) The human body at cellular resolution: the NIH Human Biomolecular Atlas Program. Nature, 574, 187–192

**Human Cell Atlas (HCA)**

Regev,A., Teichmann,S.A., Lander,E.S., Amit,I., Benoist,C., Birney,E., Bodenmiller,B., Campbell,P., Carninci,P., Clatworthy,M., et al. (2017) The Human Cell Atlas. Elife, 6.

**Kidney Precision Medicine Project (KPMP)**

Ong E, Wang LL, Schaub J, O'Toole JF, Steck B, Rosenberg AZ, Dowd F, Hansen J, Barisoni L, Jain S, de Boer IH, Valerius MT, Waikar SS, Park C, Crawford DC, Alexandrov T, Anderton CR, Stoeckert C, Weng C, Diehl AD, Mungall CJ, Haendel M, Robinson PN, Himmelfarb J, Iyengar R, Kretzler M, Mooney S, and He Y, Kidney Precision Medicine Project. Modeling Kidney Disease Using Ontology: insights from the Kidney Precision Medicine Project. Nature Review Nephrology. 2020 Nov;16(11):686-696. doi: 10.1038/s41581-020-00335-w. PMID: 32939051. PMCID: PMC8012202.

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
