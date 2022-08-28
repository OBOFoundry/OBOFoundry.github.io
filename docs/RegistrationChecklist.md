---
layout: doc
id: registration-checklist
title: Minimum Ontology Registration Request Checklist
---

The _Minimum Ontology Registration Request Checklist_ (MORRC) is intended to provide a first pass to fairly evaluate ontology registration requests to the OBO foundry.
The goal is to formalize what is currently an ad-hoc process, to filter out ontologies that are clearly out of scope for OBO. It is intentionally weaker than full
conformance, because (a) we want to allow registration of imperfect ontologies (b) partial conformance is easier to quickly and objectively check.

Note this does not change the existing process in any way. Anyone from the OBO community is free to object to the ontology on the basis of any of these checks.
However, if no objections are raised during the review period as specified by the guidelines (typically two weeks from the next OBO foundry operations committee meeting), then the ontology becomes registered. Once registered an ontology is never unregistered.

We use ISO language here for SHOULD/MUST. Anyone is free to raise an objection based on a SHOULD but this is informative and non-blocking.
If a MUST is clearly violated then this is basis for exclusion/delaying registration.

The checklist is intended for

1. OBO Operations Committee members to evaluate the requests
2. Ontology maintainers to ensure their ontology is eligible for admission prior to making a request

The checklist is expected to evolve over time; anyone can contribute to the discussion [here](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1116).

A Google sheets version of the checklist is available [here](https://docs.google.com/spreadsheets/d/1aH8ivqS1pE5IchJtkWYOfebmtkd-s2Zsdq4b5PK8hgQ/edit#gid=0). Feel free to make a copy and use it to assess an ontology!

## Checklist

- Principle 1: [Open](http://obofoundry.org/principles/fp-001-open.html)
  - The ontology MUST be conformant with this principle
- Principle 2: [Common Format](http://obofoundry.org/principles/fp-002-format.html)
  - The ontology MUST be conformant with this principle
  - The ontology MUST be parseable in Protégé, ROBOT or OWLAPI and be logically consistent and coherent with a standard OWL reasoner such as ELK or HermiT (i.e. there should be no unintended unsatisfiable classes)
- Principle 3: [URI/Identifier Space](http://obofoundry.org/principles/fp-003-uris.html)
  - The ontology MUST be conformant with this principle, with the caveat the prefix is not yet registered
  - The requested namespace MUST be available (not already used by another ontology)
- Principle 4: [Versioning](http://obofoundry.org/principles/fp-004-versioning.html)
  - The ontology MUST have a versionIRI
- Principle 5: [Scope](http://obofoundry.org/principles/fp-005-delineated-content.html)
  - IF there is significant conceptual overlap to ontologies already registered by the OBO foundry or matching labels THEN there MUST be computable linkages (one of: skos, obo:xref, owl) which are reasonably comprehensive
  - There SHOULD be a written plan (e.g ticket) for coordinating with overlapping ontologies
- Principle 6: [Textual Definitions](http://obofoundry.org/principles/fp-006-textual-definitions.html)
  - The ontology SHOULD be conformant with this principle
  - All ontology root terms MUST have definitions
  - All ontology terms SHOULD have a definition
  - Coverage:
    - Alt 1: At least 20% of terms in the ontology MUST have definitions OR
    - Alt 2: There should be a very good (explicit reason) for not having definitions on at least 20% of the terms
  - There SHOULD be a plan for defining all terms
  - classes SHOULD have defining logical axioms where appropriate
- Principle 7: [Relations](http://obofoundry.org/principles/fp-007-relations.html)
  - The ontology SHOULD be conformant with this principle
- Principle 8: [Documentation](http://obofoundry.org/principles/fp-008-documented.html)
  - The ontology SHOULD be conformant with this principle
- Principle 9: [Documented Plurality of Users](http://obofoundry.org/principles/fp-009-users.html)
  - The submitter SHOULD state existing users and assumed users
- Principle 10: [Commitment To Collaboration](http://obofoundry.org/principles/fp-010-collaboration.html)
  - The submitter SHOULD be committed to collaboration
- Principle 11: [Locus of Authority](http://obofoundry.org/principles/fp-011-locus-of-authority.html)
  - The ontology MUST be conformant with this principle
- Principle 12: [Naming Conventions](http://obofoundry.org/principles/fp-012-naming-conventions.html)
  - All non-obsolete classes MUST have labels
- Principle 16: [Maintenance](http://obofoundry.org/principles/fp-016-maintenance.html)
  - The ontology MUST have an open tracker where anyone from the community can submit
  - The maintainers SHOULD be responsive to issues in this tracker
