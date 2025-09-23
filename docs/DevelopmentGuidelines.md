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

THE FOLLOWING ARE FOR THE OTHER PAGE, KEPT HERE PENDING FINALIZATION

technical:
- Standardizing how imported ontologies are noted [#424](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/424)
- Ontology metadata requirements [#1365](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1365)
- ***MORE DISCUSSION NEEDED*** Language tags [#479](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/479)
  - For rdfs:label and IAO:0000115 annotation assertions, we discourage the use of datatype declarations such as `xsd:string`. It is important to note that `xsd:string` is essentially redundant in OWL/RDF, so "assay" and "assay"^^xsd:string should be the exact same thing. However, a lot of tooling may be confused by the difference, xsd:string datatype assertion SHOULD be omitted in general for all annotations, but MUST be omitted for rdfs:label and IAO:0000115.
  - To designate rdfs:label, and IAO:0000115 annotations in a language different from English, a [valid RDF language tag](https://www.w3.org/TR/rdf11-concepts/#section-Graph-Literal) MUST be specified, for example, "Krankheit"@de.
  - rdfs:label and IAO:0000115 annotation assertions for English content MAY be annotated with an English language tag. If the ontology chooses not to use language tags, a protege:defaultLanguage assertion MUST be added as an ontology annotation.
- Use standard synonym types [#2450](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2450)
- Modeling metaclasses [#2454](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2454)
- Ontology merging metadata [#1548](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1548)

content:
- Discourage BFO shadow classes [#1539](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1539)











