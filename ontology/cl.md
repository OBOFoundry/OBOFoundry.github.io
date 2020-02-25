---
layout: ontology_detail
id: cl
label: Cell Ontology
title: Cell Ontology
homepage: https://github.com/obophenotype/cell-ontology
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
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
taxon:
  id: NCBITaxon:33208
  label: Metazoa
domain: cells
tracker: https://github.com/obophenotype/cell-ontology/issues
mailing_list: https://lists.sourceforge.net/lists/listinfo/obo-cell-type
dependencies:
 - id: uberon
 - id: go
 - id: ro
 - id: chebi
 - id: pato
canonical: cl.owl
products:
 - id: cl.owl
   title: Main CL OWL edition
   description: Complete ontology, plus inter-ontology axioms, and imports modules
   format: owl-rdf/xml
   is_canonical: true
   uses: [uberon, chebi, go, pr, pato]
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
 - user: https://www.encodeproject.org/
   seeAlso: https://www.biosharing.org/biodbcore-000034
   type: annotation
   description: The National Human Genome Research Institute (NHGRI) launched a public research consortium named ENCODE, the Encyclopedia Of DNA Elements, in September 2003, to carry out a project to identify all functional elements in the human genome sequence. The ENCODE DCC users Uberon to annotate samples
   reference: https://doi.org/10.1093/database/bav010
 - user: http://fantom5-collaboration.gsc.riken.jp/
   type: annotation
   description: FANTOM5 is using Uberon and CL to annotate samples allowing for transcriptome analyses with cell-type and tissue-level specificity.
   examples:
    - url: http://fantom.gsc.riken.jp/5/sstar/CL:0000540
      description: FANTOM5 samples annotated to neuron
activity_status: active
---

![neuron](https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Derived_Neuron_schema_with_no_labels.svg/320px-Derived_Neuron_schema_with_no_labels.svg.png)
![lymphocyte](https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Blausen_0625_Lymphocyte_T_cell.png/128px-Blausen_0625_Lymphocyte_T_cell.png)
![epithelial](https://upload.wikimedia.org/wikipedia/commons/5/5d/Epithelial_shedding.png)

The Cell Ontology is designed as a structured controlled vocabulary for cell types. This ontology was constructed for use by the model organism and other bioinformatics databases, where there is a need for a controlled vocabulary of cell types. This ontology is not organism specific it covers cell types from prokaryotes to mammals. However, it excludes plant cell types, which are covered by PO.

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

One of the main uses of the CL is to describe samples used in
transcriptomic and functional genomics studies, such as FANTOM5,
ENCODE and LINCS.

This is described in the following publications:

Malladi, V. S., Erickson, D. T., Podduturi, N. R., Rowe, L. D., Chan,
E. T., Davidson, J. M., … Hong, E. L. (2015). Ontology application and
use at the ENCODE DCC. Database : The Journal of Biological Databases
and Curation, 2015, bav010–. [doi:10.1093/database/bav010](https://doi.org/doi:10.1093/database/bav010)

Lizio, M., Harshbarger, J., Shimoji, H., Severin, J., Kasukawa, T.,
Sahin, S., … Kawaji, H. (2015). Gateways to the FANTOM5 promoter level
mammalian expression atlas. Genome Biology, 16(1),
22. [doi:10.1186/s13059-014-0560-6](https://doi.org/doi:10.1186/s13059-014-0560-6)

[Metadata Standard and Data Exchange Specifications
to Describe, Model, and Integrate Complex and Diverse High-Throughput
Screening Data from the Library of Integrated Network-based Cellular
Signatures
(LINCS)](http://jbx.sagepub.com/content/early/2014/02/11/1087057114522514.full)


