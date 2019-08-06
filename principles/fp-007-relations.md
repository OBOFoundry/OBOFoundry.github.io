---
layout: principle
id: fp-007-relations
title: Relations (principle 7)
---

Notes
-----

The content of this page is scheduled to be reviewed. Improved wording will be posted as it becomes available.

Summary
-------

Relations should be reused from the Relations Ontology (RO).

Purpose
-------

To facilitate interoperability between multiple ontologies, especially with respect to logical inference. That is, a reasoner can only detect logical inconsistencies between ontologies and infer new axioms if the ontologies use the same object properties.

Recommendation
--------------

Each OBO ontology MUST reuse existing relations (aka object properties) that have already been declared in the Relations Ontology (RO), rather than declaring duplicative relations. In some cases it may make sense for an ontology to declare a new relation in its own ID space. In these cases, there SHOULD still be coordination with RO, for example in the form of an issue submitted to the RO tracker.

Implementation
--------------

Reuse means that the actual relations PURLs are used. Ontology developers should be aware that RO relations (in rare instances) can evolve over time and previous relations might become obsolete. This means developers should monitor the state of the RO relations they use.

Examples
--------

Counter-Examples
----------------

<Category:Principles> <Category:Accepted> <Category:Definitions>
