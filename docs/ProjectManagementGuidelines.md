---
layout: doc
title: Ontology Project Management Guidelines
---
<!--
GO TO: [Technical Considerations](#technical-considerations) &#124; [Content Considerations](#content-considerations) &#124; [Release Considerations](#release-considerations) &#124; [Social Considerations](#social-considerations) &#124; [Communication Considerations](#communication-considerations)
-->
### Technical Considerations

- Term migration
  - <b>Definition</b>: The transfer of responsibility of term maintenance from one ontology to another.
  - <b>Purpose</b>: If a term created by ontology A would have a more suitable home in ontology B, that term can be transferred to the other ontology.
  - <b>Mechanism</b>: There are two mechanisms for doing this: (1) <i>Term adoption</i>, whereby a term originating in ontology A is maintained and managed by ontology B while retaining its original identifier; and (2) <i>Term deprecation/recreation</i>, whereby a term is obsoleted in ontology A and recreated in ontology B using the latter's ID space. An overview of the advantages and disadvantages for each of these mechanisms is given in the table below:
    
    | Mechanism | Advantages | Disadvantages |
    | --------- | -------- | -------- |
    | Term Adoption | <ul><li>Preserves the original identifier/IRI.</ul>| <ul><li>Term IRI will still resolve to original destination. If originating ontology 'A' fails to import the term from managing ontology 'B', the IRI will fail.</ul>|
    | Term Deprecation/Recreation | <ul><li>Term IRI will resolve to the managing ontology 'B'. The original IRI from ontology A will still resolve, and that version will indicate the replacement.</ul>| <ul><li>Term identifier/IRI will change, with potential downstream effects.<li>The "history" of the migrated term is not indicated by the managing ontology.</ul> |

  - <b>Implementation</b>: _Term adoption_ involves removing a term from the base (that is, before imports) ontology files (OWL or OBO) for ontology A <b>without deprecating</b> and adding it to the ontology files for ontology B <b>with no changes</b>, except that adopted terms MUST be tagged with rdfs:isDefinedBy as follows:
      ```
      OWL format (RDF/XML):
      <rdfs:isDefinedBy rdf:resource="http://purl.obolibrary.org/obo/omrse.owl"/>
      
      OWL format (Turtle serialization):
      <http://purl.obolibrary.org/obo/A_123> rdfs:isDefinedBy <http://purl.obolibrary.org/obo/b.owl>
      
      OWL format (OWL Functional Notation):
      AnnotationAssertion(rdfs:isDefinedBy obo:OOSTT_00000153 obo:omrse.owl)
      
      OBO format:
      property_value: isDefinedBy http://purl.obolibrary.org/obo/b.owl      
      ```
    _Term Deprecation/Recreation_ involves obsoleting a term in ontology A and remaking the term in ontology B. The term will therefore exist in both ontologies, active in ontology B but deprecated in ontology A. To use this mechanism, the term in ontology A MUST be marked as both obsolete and replaced according to the guidelines given in [Principle 19](https://obofoundry.org/principles/fp-019-term-stability.html) (Stability of Term Meaning).
  - <b>Examples</b>
    - <i>Term adoption</i>: http://purl.obolibrary.org/obo/OOSTT_00000153 (emergency physician role) is managed by OMRSE.
    - _Term deprecation/recreation_: http://purl.obolibrary.org/obo/COB_0000022 (organism) was formerly http://purl.obolibrary.org/obo/OBI_0100026.
  - <b>Implications</b> (licensing and other considerations)
    - Note: Regardless of the license used by the originating ontology, adopted terms will be subject to the stipulations of the license used by the adopting ontology.
<!-- 
### Content Considerations


### Release Considerations

- (DISCUSS) Keep your edit file (the file you change on a regular basis) and your release files strictly separate
- standards for GitHub ontology repositories #2840

### Social Considerations

- (DISCUSS) Tag your GitHub repository with the obofoundry tag so that people can find it: https://github.com/topics/obofoundry

### Communication Considerations

- Publications metadata [#1671](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1671)
- Short ontology descriptions [#1968](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1968)
  - No real support for the idea that this is a problem; However, going forward, no objections to this as a SHOULD. We need to add guidance for new ontologies to utilize a common format. This would appear on the YAML template https://github.com/OBOFoundry/OBOFoundry.github.io/blob/master/.github/ISSUE_TEMPLATE/new-ontology.yml 

- Documentation for license [#1840](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1840)

-->
