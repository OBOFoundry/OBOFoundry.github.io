---
layout: community
id: anatomy
title: Anatomy Portal
members:
  - cmungall
  - mellybelly
  - dosumis
  - balhoff
  - ANiknejad
  - fbastian
  - jaiswalp
ontologies:
  - id: uberon
    description: "covers all animals. Can bridge species-specific AOs"
  - id: po
    description: "covers all plants"
  - id: fao
    description: "covers all multicellular fungi"
  - id: ma
    description: "mouse (adult)"
  - id: emapa
    description: "mouse (embryonic)"
  - id: ddanat
    description: "dicty (slime mold)"
  - id: plana
    description: "planaria"
  - id: fma
    description: "human"
  - id: ehdaa2
    description: "human (developmental)"
  - id: zfa
    description: "zebrafish"
  - id: xao
    description: "xenopus"
  - id: fbbt
    description: "Drosophila"
  - id: wbbt
    description: "C elegans"
---

Welcome to the OBO Foundry Anatomy Portal!

This community page organizes different OBO anatomy ontologies and
describes how they relate to one another.

## Upper level

The Common Anatomy Reference Ontology (CARO) provides an upper-level
structure that should be used as superclasses in OBO anatomy ontologies.

- [caro](/ontology/caro.html)

## Subcellular

We take the term anatomy to include subcellular anatomy, which is
covered in GO.

- [go](/ontology/go.html)

Note that some ontologies (WBbt, FBbt) include their own more specific subcellular components

## Cells

- Plants: [po](/ontology/po.html)
- Animals: [cl](/ontology/cl.html)

Note that some ontologies (PO, FBbt) include their own more specific cell types

## Gross anatomy

### Plants

The Plant Ontology (PO) covers all viridiplantae, and includes cell types as well as tissues/organs

- [po](/ontology/po.html)

### Fungal

The Plant Ontology (PO) covers all multicellular fungi, and includes cell types as well as multi-cell structures

- [fao](/ontology/fao.html)

### Slime Mold

- [ddanat](/ontology/ddanat.html)

### Animals

Uberon is a multi-species anatom ontology covering metazoa
(animals). It can be used to bridge other species-specific animal
anatomy ontologies, see the documentation for details.

- [uberon](/ontology/uberon.html)

Species or taxon-specific anatomy ontologies

- Vertebrates
  - Vertebrate non-mammalian
    - [zfa](/ontology/zfa.html)
    - [xao](/ontology/xao.html)
  - Mammals
    - Mouse
      - [ma](/ontology/ma.html) (adult)
      - [emapa](/ontology/emapa.html) (all stages)
    - Human
      - [fma](/ontology/fma.html) (adult)
      - [ehdaa2](/ontology/ehdaa2.html) (embryo)
- Non-vertebrate animals
  - model organism
    - [fbbt](/ontology/fbbt.html)
    - [wbbt](/ontology/wbbt.html)
    - [plana](/ontology/plana.html)
    - coming soon - echinoderm
  - non-model organism
    - Sponges: [poro](/ontology/poro.html)
    - Ctenophores: [cteno](/ontology/cteno.html)
    - Cephalopods: [ceph](/ontology/ceph.html)

## Stage Ontologies

We have a separate github repo:

- https://github.com/obophenotype/developmental-stage-ontologies
