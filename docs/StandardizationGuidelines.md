---
layout: doc
title: Ontology Standardization Guidelines
---

### Technical

- (ACCEPTED?) The ontology MUST be **logically consistent** (from [#482](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/482))
  - This means (a) there MUST NOT be contradictory statements revealed by reasoning; (b) there MUST NOT be any unsatisfiable classes; and (c) there MUST NOT be any circular definitions.
  - This includes when the ontology is classified together with RO, BFO, and COB (from [#482](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/482))
- (ACCEPTED? Need clarification on what exactly 'base dependency' is) Every ontology SHOULD be coherent when classified together with all its base-dependencies (from [#482](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/482))
- Standardizing how imported ontologies are noted [#424](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/424)
- Ontology metadata requirements [#1365](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1365)
- Ontology root terms annotation [#2149](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2149)
- Language tags [#479](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/479)
- Use standard synonym types [#2450](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2450)
- Modeling metaclasses [#2454](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2454)
- The target for 'term tracker item' ([IAO:0000233](http://purl.obolibrary.org/obo/IAO_0000233)) should solely be an IRI, without additional text or comment  [#175](https://github.com/information-artifact-ontology/ontology-metadata/issues/175)

### Content

- Discourage BFO shadow classes [#1539](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1539)
- (ACCEPTED?) Ignoring NCIT (no issue, but has come up that NCIT is not well-formed enough to be a concern re: things like overlap)
- Term adoption [#2330](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2330) and [#2324](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2324)
- Standardized xref prefixes in ontologies [#525](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/525)
- Referring to taxa not in NCBITaxon [#434](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/434)

### Releases

- In addition to a set of release standards in terms of format (see [Principle 2](https://obofoundry.org/principles/fp-002-format.html)), the following are the standards regarding imports, axiomization, and reasoning (see [Release Artefacts](https://oboacademy.github.io/obook/reference/release-artefacts/) for more detailed information):
  - **base** (REQUIRED; denoted by PURL ending with ONT.owl): Content includes only terms that are owned by the ontology, which include (a) terms using that ontology's prefix; and (b) any terms with a different prefix that are now maintained by that ontology. It does not contain any imports. It does, however, retain references to external ontologies within axioms as needed for definitions and reasoning. Such references, when displayed in Protege, will appear as identifiers only; that is, without labels. Finally, the base will have had reasoning already applied and will be stripped of redundant axioms. QUESTION: WILL THIS APPLY TO A SPECIFIC REASONER?
  - **full** (REQUIRED; denoted by PURL ending with ONT-full.owl ): Content is as for **base** except that all referenced external terms (that is,  are present (that is, imports are merged into the **full** release).
  - *other release artefacts* (OPTIONAL; denoted by PURL ending with ONT-<artefact_type>.owl): These include **non-classified**, **simple**, **basic**, and **simple-non-classified**. See the Release Artefacts link above for details on these.
- (ACCEPTED?) Every ontology SHOULD provide a 'base' release (from [#482](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/482))

### Social


### Communication

- Ontology subsets documentation [#466](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/446)
- Document how to add logo [#72](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/72)
- Short ontology descriptions [#1968](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1968)
- Documentation for license [#1840](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1840)
- Exemplar classes [#899](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/899)
- Linking term to discussion on tracker [#1097](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1097)
