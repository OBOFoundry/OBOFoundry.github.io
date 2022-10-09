---
layout: faq
title: Adding Custom Browsers
---
## How do I add a custom link to an ontology browser for my ontology?

Every ontology in the registry is automatically in OntoBee, so we
automatically provide a link to OntoBee.

You can provide links to additional browsers under a `browsers`
key. For example, see the metadata for the [/ontology/hp.html](HP
ontology) (click on "View" in the left panel to see the metadata).

It will contain an entry something like this:

```
browsers:
  - label: HPO
    title: Charite HPO Browser
    url: http://www.human-phenotype-ontology.org/hpoweb/showterm?id=HP:0000118
  - label: Monarch
    title: Monarch Phenotype Page
    url: http://monarchinitiative.org/phenotype/HP:0000118
```

`browsers` is a multifield key. In YAML, each element in an array is
indicated by the `-`s. Each such element must have `label` (this is
used to render the button), `title` and `url` (the actual link).

### Future expansions

In future we hope to enhance this:

- embeddable browsers
- embeddable search
- automatic links to OLS and BioPortal
