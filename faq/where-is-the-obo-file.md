---
layout: faq
title: Where is the OBO file for my ontology?
---

This registry makes a distinction between an _ontology_ and the
_products_ (also known as _editions_) of that ontology.

Products can be the ontology in a different format (e.g. obo vs owl),
or they can be different variants (for example, subsets or
extensions). They can also be ancilliary ontologies, e.g. bridge
files.

Note that from an OWL format, two editions that differ in format are
equivalent ontologies (they will have the same IRI), but ontology
subsets etc are considered different OWLOntologies. However, from an
OBO Foundry administrative perspective, the "parent" is considered the
ontology.

The different products are listed as objects under the `product` key, for example:

```
---
layout: ontology_detail
id: go
in_foundry_order: 1
label: GO
description: An ontology for describing the function of genes and gene products
title: Gene Ontology
products:
 - id: go.owl
 - id: go/extensions/go-plus.owl
   title: GO-Plus
   description: The core ontology plus axioms connecting to select external ontologies
 - id: go/extensions/go-taxon-groupings.owl
   title: GO Taxon Groupings
   description: Classes added to ncbitaxon for groupings such as prokaryotes
```

All ontologies MUST have at least one OWL product whose name
corresponds to the registered id. Thus the ontology whose IRI is
http://purl.obolibrary.org/obo/ro.owl (known to the obofoundry as
`ro`), must have at least the product `ro.owl`.

Developers can OPTIONALLY produce ontologies in other formats. These are conventionally the same IRI as the owl, but with .owl changed to the relevant extension (e.g., ‘.obo’, ‘.json’). Note that such products are not listed by default. If you produce an additional format product, you should register it under the ‘products’ field in the appropriate metadata file found in this [folder](https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/ontology).

It does not matter to us if you maintain the source for your ontology
in obo or owl or some hybrid. You have the option of either publishing
the alternate format yourself (using a tool like ROBOT) _or_ you can
have the OBO central build pipeline do this for you. For more
information, see the FAQ entry [What is the Build field?](what-is-the-build-field.md).
