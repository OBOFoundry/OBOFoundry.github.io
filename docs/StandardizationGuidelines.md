---
layout: doc
title: Ontology Standardization Guidelines
---

### Technical

- Logical consistency of the ontology ([tracker item](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/482))
  - The ontology MUST be **logically consistent**
  - This means (a) there MUST NOT be contradictory statements revealed by reasoning; (b) there MUST NOT be any unsatisfiable classes; and (c) there MUST NOT be any circular definitions.
  - This includes when the ontology is classified together with RO, BFO, and COB
  - This also includes when the ontology is classified together with its base dependencies; that is, as part of a 'full' release (see Releases section below)
- Ontology root terms annotation ([tracker item](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2149))
  - Some ontology browsers make use of an ontology-wide annotation property, 'has ontology root term' (IAO:0000700), that governs how the hierarchy is displayed. This helps shield users from having to navigate through not-specific-enough parent terms (such as BFO:0000040 "material entity"). To enable this feature, an ontology SHOULD specify one or more appropriate root terms like so:
      ```
      OWL format:
         <obo:IAO_0000700 rdf:resource="http://purl.obolibrary.org/obo/*root term ID*"/>
      OBO format:
         property_value: IAO:0000700 *root term ID*
      ```

### Content

- NCIt term use - If an ontology developer wishes to create a term with a label that already exists in NCIt, the following apply:
  - If the NCIt term definition and hierarchical position are reasonable, that term SHOULD be used instead;
  - If either the NCIt term definition or the hierarchical position are sub-optimal, the developer MAY create a term in the ontology with an identical label but with a revised definition and subclassing; alternatively such a term MAY be requested of another ontology, if appropriate;
  - For case (b), if the definition is based on the NCIt definition, the new term MUST be linked to the original NCIt term to conform to the [NCIt license](https://evs.nci.nih.gov/license) requirements. Note: this does not apply to reuse of term labels.
- Preferred source for imported terms (no tracker item)
  - Imported terms SHOULD be drawn from the ontology that is the preferred source for the term. The preferred source is usually the ontology with the same ID space as the term, but it can instead be the ontology that currently maintains the term. Importing a term from a secondary source is not recommended because there is no guarantee that the secondary source has the most up-to-date term information, and thus drawing from the original would avoid possible conflicts due to term divergence.

### Releases

- Release types ([tracker item](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/482))
  - In addition to a set of standards pertaining to release *format* (see [Principle 2](https://obofoundry.org/principles/fp-002-format.html)), the following are the standards pertaining to release *types*, each of which differ with respect to imports, axiomization, and reasoning (see [Release Artefacts](https://oboacademy.github.io/obook/reference/release-artefacts/) for more detailed information):
  - **base** (RECOMMENDED; denoted by PURL ending with ONT.owl): Content includes only terms that are owned by the ontology, which include (a) terms using that ontology's prefix; and (b) any terms with a different prefix that are now maintained by that ontology. It does not contain any imports. It does, however, retain references to external ontologies within axioms as needed for definitions and reasoning. Such references, when displayed in Protege, will appear as identifiers only; that is, without labels. Finally, the base will have had reasoning already applied and will be stripped of redundant axioms. **QUESTION: WILL THIS APPLY TO A SPECIFIC REASONER?**
  - **full** (REQUIRED; denoted by PURL ending with ONT-full.owl ): Content is as for **base** except that all referenced external terms (that is,  are present (that is, imports are merged into the **full** release).
  - *other release artefacts* (OPTIONAL; denoted by PURL ending with ONT-<artefact_type>.owl): These include **non-classified**, **simple**, **basic**, and **simple-non-classified**. See the Release Artefacts link above for details on these.
  - Every ontology MUST provide a 'base' release and MUST provide a 'full' release.

### Social


### Communication

- Linking to issue tracker ([tracker item](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1097)) Any term (or set of terms) with an affiliated issue tracker item (term request or term discussion) SHOULD be linked to the relevant issue(s). Such linking SHOULD use the annotation property 'term tracker item' (IAO:0000233) and SHOULD NOT use a free text comment. The range for 'term tracker item' MUST consist solely of an IRI, without additional text, and the IRI MUST be for the issue tracker item.


