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
- Ontology metadata requirements [#1365](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1365)
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

- Ontology subsets  documentation [#466](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/466)
- domain metadata tag [#2779](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2779)


Follow-up on guidelines for imports: During the previous discussion, it came to light that some ontologies--when importing from a ‘third party’ ontology--filter out definitions and logical axioms in order to reduce the possibility of misalignment due to out of sync updates.
Q: The newly-accepted guideline recommends against importing terms from a third party ontology anyway, but should we add that filtering note for cases when it is done?
Q: What about when importing from the original source ontology? Principle 1 for term import says to “include any annotations for term or definition editors from the original ontology”. Should that be revisited?
James: There’s nothing special about definitions – any annotation or axiom could get out of sync, and any could be important to someone. Recommend against stripping this recommendation.
CONCLUSION: keep all information.
imports: recommend that imported terms be tagged with the ontology from which they were *directly* imported? (no issue)
Terms can be imported from the ‘source’ ontology or a third party ontology; this recommendation would provide useful tracking information should things go wrong.
P1 says  ‘imported from’ (IAO:0000412) should be used “to link back to the group (i.e. ontology) maintaining it”
Which method (annotating the direct import source vs annotating the maintaining ontology) would provide the most benefit to end users? To term re-users?
Q: Should we only recommend this tag when from a third party, or always?
If using OntoFox, it will indicate the direct import. ROBOT does it *only when asked*
James O: would not recommend using ‘imported from’ in guideline.
CONCLUSION: leave out of guidelines
ACTION (DN): make issue regarding P1 inclusion of ‘imported from’
imports: standardize how imported ontologies are noted (#424)
For individual terms there is ‘imported from’ (IAO:0000412), recommended as part of P1. (Note: the above discussion might change what is said there.)
Q: regardless of how it could be indicated (for example, using a yet-to-be-minted metadata tag such as ‘imports’ or ‘has import’--not to be confused with the directive ‘owl:imports’), do we want to make a recommendation to this effect? The context is within an already-merged ontology (which would not have any import statements).
James O: this consideration is very semweb-focused but might not be very useful
CONCLUSION: Don’t bother with this.





