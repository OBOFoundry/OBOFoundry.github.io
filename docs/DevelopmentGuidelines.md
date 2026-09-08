---
layout: doc
title: Ontology Project Management Guidelines
---

### Technical

- Term migration
  - <b>Definition</b>: The transfer of responsibility of term maintenance from one ontology to another.
  - <b>Purpose</b>: If a term created by ontology A would have a more suitable home in ontology B, that term can be transferred to the other ontology.
  - <b>Mechanism</b>: There are two mechanisms for doing this: (1) <i>Term adoption</i>, whereby the term from ontology A is managed by ontology B while retaining its original identifier; and (2) <i>Term deprecation/recreation</i>, whereby the term is obsoleted in ontology A and recreated in ontology B using the latter's namespace. An overview of the advantages and disadvantages for each of these mechanisms is given in the table below:
    
    | Mechanism | Advantages | Disadvantages |
    | --------- | -------- | -------- |
    | Term Adoption | <ul><li>is good <li>is also good </ul>| <ul><li>is bad </ul>|
    | Term Deprecation/Recreation | <ul><li>is good </ul>| <ul><li>is bad</ul> |

  - <b>Implementation</b>: _Term adoption_ involves removing a term from the ontology files (OWL or OBO) for ontology A <b>without deprecating</b> and adding it to the ontology files for ontology B <b>with no changes</b>, except that adopted terms MUST be tagged with rdfs:isDefinedBy as follows:
      ```
      OWL format (Turtle serialization):
      <http://purl.obolibrary.org/obo/A_123> rdfs:isDefinedBy <http://purl.obolibrary.org/obo/b.owl>
      OBO format:
      property_value: isDefinedBy http://purl.obolibrary.org/obo/b.owl
      ```
    _Term Deprecation/Recreation_ involves obsoleting a term in ontology A and remaking the term in ontology B. The term will therefore exist in both ontologies, active in ontology B but deprecated in ontology A. To use this mechanism, the term in ontology A MUST be marked as both obsolete and replaced according to the guidelines given in [Principle 19](https://obofoundry.org/principles/fp-019-term-stability.html) (Stability of Term Meaning).
  - <b>Examples</b> 
  - <b>Implications</b> (licensing and other considerations)
    - Note: Regardless of the license used by the originating ontology, adopted terms will be subject to the stipulations of the license used by the adopting ontology.

### Content


### Releases

- (DISCUSS) Keep your edit file (the file you change on a regular basis) and your release files strictly separate
- standards for GitHub ontology repositories #2840

### Social

- (DISCUSS) Tag your GitHub repository with the obofoundry tag so that people can find it: https://github.com/topics/obofoundry

### Communication

- Publications metadata [#1671](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1671)
- Short ontology descriptions [#1968](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1968)
  - No real support for the idea that this is a problem; However, going forward, no objections to this as a SHOULD. We need to add guidance for new ontologies to utilize a common format. This would appear on the YAML template https://github.com/OBOFoundry/OBOFoundry.github.io/blob/master/.github/ISSUE_TEMPLATE/new-ontology.yml 

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
- ***MORE DISCUSSION NEEDED*** Standardized xref prefixes in ontologies [#525](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/525)
- ***MORE DISCUSSION NEEDED*** Referring to taxa not in NCBITaxon [#434](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/434)
 

communication:

- domain metadata tag [#2779](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2779)



