---
layout: doc
title: Ontology Project Management Guidelines
---

### Technical


### Content


### Releases

- (DISCUSS) Keep your edit file (the file you change on a regular basis) and your release files strictly separate

### Social

- (DISCUSS) Tag your GitHub repository with the obofoundry tag so that people can find it: https://github.com/topics/obofoundry

### Communication

- Publications metadata [#1671](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1671)
- ***MORE DISCUSSION NEEDED*** Short ontology descriptions [#1968](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1968)
- Documentation for license [#1840](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1840)


THE FOLLOWING ARE FOR THE OTHER PAGE, KEPT HERE PENDING FINALIZATION

technical:
- Use standard synonym types [#2450](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2450)
- Modeling metaclasses [#2454](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2454)
- Ontology merging metadata [#1548](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1548)
- ***MORE DISCUSSION NEEDED*** Ontology metadata requirements [#1365](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1365)
  - DECISION: leave Optional field off from the table. Discussion to be continued about the use of dcterms:date. Will make 2 tables: 1 with MUST and SHOULD, the other with other potential fields (including those NOT to use) with guidelines indicated (would include the list items given in the file, below the table). We should also push for recommended format for optional fields (ex. ORCID for creator/contributor). 

- ***MORE DISCUSSION NEEDED*** Language tags [#479](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/479)
  - For rdfs:label and IAO:0000115 annotation assertions, we discourage the use of datatype declarations such as `xsd:string`. It is important to note that `xsd:string` is essentially redundant in OWL/RDF, so "assay" and "assay"^^xsd:string should be the exact same thing. However, a lot of tooling may be confused by the difference, xsd:string datatype assertion SHOULD be omitted in general for all annotations, but MUST be omitted for rdfs:label and IAO:0000115.
  - To designate rdfs:label, and IAO:0000115 annotations in a language different from English, a [valid RDF language tag](https://www.w3.org/TR/rdf11-concepts/#section-Graph-Literal) MUST be specified, for example, "Krankheit"@de.
  - rdfs:label and IAO:0000115 annotation assertions for English content MAY be annotated with an English language tag. If the ontology chooses not to use language tags, a protege:defaultLanguage assertion MUST be added as an ontology annotation.

content:
- Discourage BFO shadow classes [#1539](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1539)
- Term adoption [#2330](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2330) and [#2324](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2324)
- Standardized xref prefixes in ontologies [#525](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/525)
- ***MORE DISCUSSION NEEDED*** Referring to taxa not in NCBITaxon [#434](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/434)

communication:

- Ontology subsets documentation [#466](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/466)
- domain metadata tag [#2779](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2779)


Follow-up on guidelines for imports: During the previous discussion, it came to light that some ontologies--when importing from a ‘third party’ ontology--filter out definitions and logical axioms in order to reduce the possibility of misalignment due to out of sync updates.
Q: The newly-accepted guideline recommends against importing terms from a third party ontology anyway, but should we add that filtering note for cases when it is done?
Q: What about when importing from the original source ontology? Principle 1 for term import says to “include any annotations for term or definition editors from the original ontology”. Should that be revisited?
James: There’s nothing special about definitions – any annotation or axiom could get out of sync, and any could be important to someone. Recommend against stripping this recommendation.
CONCLUSION: keep all information.

ACTION (DN): make issue regarding P1 inclusion of ‘imported from’






