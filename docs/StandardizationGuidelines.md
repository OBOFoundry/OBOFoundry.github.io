---
layout: doc
title: Ontology Standardization Guidelines
---

## Social

SOCIAL External axioms #1443 & #1991 | possible new "what to do with terms" principle (can be p14)

## Communication

   ### Documentation
    - Documentation for license #1840 = github repository SHOULD have a LICENSE file (named 'LICENSE' with no extension, LICENSE.md, or LICENSE.txt; the latter will be plain text)
    - Fully document ontology subsets #466
    - Link terms to relevant discussion on issue tracker #1097

## Content

   ### Terms
    Discourage BFO shadow classes #1539
    Ignoring NCIT (no issue, but has come up that NCIT is not well-formed enough to be a concern re: things like overlap)
    Referring to taxa not in NCBITaxon #434
    Term adoption #2330 (also #2324)
    Versioning term identifiers #1347
   ### Products
    Every ontology SHOULD provide a base
    Imports should be merged into the main release file

   ### Coherency
    Every ontology primary release MUST be consistent and coherent
    Every ontology MUST be coherent when classified together with RO, BFO, and COB
    Every ontology SHOULD be coherent when classified together with all its base-dependencies

## Technical

METADATA Language tags #479 (also #325)

Not yet classified:


METADATA Synonym types #2450 = Use standardized SynonymTypes (OBO) 
METADATA Ontology root terms annotation #2149
METADATA Publications metadata #1671
METADATA Ontology merging #1548
METADATA Exemplar classes #899
METADATA Ontology metadata requirements #1365
STANDARDIZATION? Standardized xref prefixes in ontologies #525
Proposals here: #482 (comment)
METADATA Modeling metaclasses #2454 (thanks @cthoyt, that's a good addition)
METADATA Standardizing how imported ontologies are noted #424
