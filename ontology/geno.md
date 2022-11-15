---
layout: ontology_detail
id: geno
title: Genotype Ontology
build:
  checkout: git clone https://github.com/monarch-initiative/GENO-ontology.git
  path: src/ontology
  system: git
contact:
  email: mhb120@gmail.com
  github: mbrush
  label: Matthew Brush
  orcid: 0000-0002-1048-5019
description: An integrated ontology for representing the genetic variations described in genotypes, and their causal relationships to phenotype and diseases.
domain: biological systems
github_date_added: 2017-01-05
homepage: https://github.com/monarch-initiative/GENO-ontology/
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
preferredPrefix: GENO
products:
- id: geno.owl
  title: GENO
repository: https://github.com/monarch-initiative/GENO-ontology
tags:
- genotype-to-phenotype associations
tracker: https://github.com/monarch-initiative/GENO-ontology/issues
activity_status: active
---

GENO is an OWL2 ontology that represents the levels of genetic variation specified in genotypes, to support genotype-to-phenotype (G2P) data aggregation and analysis across diverse research communities and sources. The core of the ontology is a graph decomposing a genotype into smaller components of variation, from a complete genotype specifying sequence variation across an entire genome, down to specific allelic variants and sequence alterations. Structuring genotype instance data according to this model supports a primary use case of GENO to enable integrated analysis of G2P data where phenotype annotations are made at different levels of granularity in this genotype partonomy. GENO also enables description of various attributes of genotypes and genetic variants. These attributes include zygosity, genomic position, expression, dominance, and functional dependencies or consequences of a given variant.

In addition to heritable variation in genomic sequence specified by traditional genotypes, GENO also represents transient variation in gene expression, as seen in experiments where genes are targeted by knockdown reagents or overexpressed by DNA constructs at the time a phenotype is assessed. This variation in gene expression is represented in terms of the targeted genes themselves, to parallel representation of sequence variation and facilitate integrated description and analysis of data about any genetic contribution to a measured phenotype.

Finally, GENO also supports modelling of G2P associations, focusing on the interplay between genotype, phenotype, and environment. GENO describes provenance and experimental evidence for these associations using the Scientific Evidence and Provenance Information Ontology (SEPIO) model.
