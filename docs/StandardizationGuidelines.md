---
layout: doc
title: Ontology Standardization Guidelines
---

### Technical

- ***DONE*** The ontology MUST be **logically consistent**
  - This means (a) there MUST NOT be contradictory statements revealed by reasoning; (b) there MUST NOT be any unsatisfiable classes; and (c) there MUST NOT be any circular definitions.
  - This includes when the ontology is classified together with RO, BFO, and COB
  - This also includes when the ontology is classified together with its base dependencies; that is, as part of a 'full' release (see Releases section below)
  - ***CLOSE THIS*** https://github.com/OBOFoundry/OBOFoundry.github.io/issues/482
- Standardizing how imported ontologies are noted [#424](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/424)
- Ontology metadata requirements [#1365](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1365)
- Ontology root terms annotation [#2149](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2149)
- Language tags [#479](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/479)
  - For rdfs:label and IAO:0000115 annotation assertions, we discourage the use of datatype declarations such as `xsd:string`. It is important to note that `xsd:string` is essentially redundant in OWL/RDF, so "assay" and "assay"^^xsd:string should be the exact same thing. However, a lot of tooling may be confused by the difference, xsd:string datatype assertion SHOULD be omitted in general for all annotations, but MUST be omitted for rdfs:label and IAO:0000115.
  - To designate rdfs:label, and IAO:0000115 annotations in a language different from English, a [valid RDF language tag](https://www.w3.org/TR/rdf11-concepts/#section-Graph-Literal) MUST be specified, for example, "Krankheit"@de.
  - rdfs:label and IAO:0000115 annotation assertions for English content MAY be annotated with an English language tag. If the ontology chooses not to use language tags, a protege:defaultLanguage assertion MUST be added as an ontology annotation.



- Use standard synonym types [#2450](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2450)
- Modeling metaclasses [#2454](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2454)

### Content

- Discourage BFO shadow classes [#1539](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1539)
- ***DONE*** NCIt term use - If an ontology developer wishes to create a term with a label that already exists in NCIt, the following apply:
  - If the NCIt term definition and hierarchical position are reasonable, that term SHOULD be used instead;
  - If either the NCIt term definition or the hierarchical position are sub-optimal, the developer MAY create a term in the ontology with an identical label but with a revised definition and subclassing; alternatively such a term MAY be requested of another ontology, if appropriate;
  - For case (b), if the definition is based on the NCIt definition, the new term MUST be linked to the original NCIt term to conform to the [NCIt license](https://evs.nci.nih.gov/license) requirements. Note: this does not apply to reuse of term labels.
- Term adoption [#2330](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2330) and [#2324](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2324)
- Standardized xref prefixes in ontologies [#525](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/525)
- Referring to taxa not in NCBITaxon [#434](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/434)

### Releases

- ***DONE*** In addition to a set of standards pertaining to release *format* (see [Principle 2](https://obofoundry.org/principles/fp-002-format.html)), the following are the standards pertaining to release *types*, each of which differ with respect to imports, axiomization, and reasoning (see [Release Artefacts](https://oboacademy.github.io/obook/reference/release-artefacts/) for more detailed information):
  - **base** (REQUIRED; denoted by PURL ending with ONT.owl): Content includes only terms that are owned by the ontology, which include (a) terms using that ontology's prefix; and (b) any terms with a different prefix that are now maintained by that ontology. It does not contain any imports. It does, however, retain references to external ontologies within axioms as needed for definitions and reasoning. Such references, when displayed in Protege, will appear as identifiers only; that is, without labels. Finally, the base will have had reasoning already applied and will be stripped of redundant axioms. QUESTION: WILL THIS APPLY TO A SPECIFIC REASONER?
  - **full** (REQUIRED; denoted by PURL ending with ONT-full.owl ): Content is as for **base** except that all referenced external terms (that is,  are present (that is, imports are merged into the **full** release).
  - *other release artefacts* (OPTIONAL; denoted by PURL ending with ONT-<artefact_type>.owl): These include **non-classified**, **simple**, **basic**, and **simple-non-classified**. See the Release Artefacts link above for details on these.
  - Every ontology MUST provide a 'base' release and MUST provide a 'full' release.

### Social


### Communication

- Ontology subsets documentation [#466](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/446)
- Documentation for license [#1840](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1840)
- Exemplar classes [#899](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/899)
- ***DONE*** Any term (or set of terms) with an affiliated issue tracker item (term request or term discussion) SHOULD be linked to the relevant issue(s). Such linking SHOULD use the annotation property 'term tracker item' (IAO:0000233) and SHOULD NOT use a free text comment. The range for 'term tracker item' MUST consist solely of an IRI, without additional text, and the IRI MUST be for the issue tracker item.
  - ***CLOSE THIS*** [#1097](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1097)


