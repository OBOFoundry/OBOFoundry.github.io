# OBO Foundry Registry and Website

This is the registry and website for the OBO Foundry. It is deployed with GitHub
Pages and Jekyll to https://obofoundry.github.io and is then mapped to
https://obofoundry.org.

For most questions, see the main site FAQ at https://obofoundry.org/faq/.
For details on site development, please see [README-sitedev.md](README-sitedev.md)

## Contributing

### I have some comments

You can use the [issue tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues)

### I want to contribute

Please do! Anyone can fork and make PR, or [create an issue in the tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues).

Note that most members of the community will do this via the [obofoundry.org website](http://obofoundry.org) - each ontology page has links for editing the metadata.

See [CONTRIBUTING.md](CONTRIBUTING.md)

## Repo Organization

 * [registry/](registry)   `<-- DERIVED yaml, json and RDF. DO NOT EDIT`
    * [registry/ontologies.yml](registry/ontologies.yml)  `<-- READONLY`
    * [registry/ontologies.jsonld](registry/ontologies.jsonld)  `<-- generated from yaml`
    * `registry/ontologies.rdf  <-- TODO generated from jsonld`
 * [ontology/](ontology/)  `<-- source for ontology metadata. EDIT IN HERE`
    * [ontology/obi.md](ontology/obi.md)  `<-- metadata (yml) and markdown for display. EDIT THIS`
    * [ontology/uberon.md](ontology/uberon.md)
    * ...
 * [Makefile](Makefile) `<-- For compiling derived artefacts and running tests`
 * [_posts/](_posts) `<-- Blog posts/news`
 * [_layouts/](_layouts) `<-- Jekyll layouts`
 * [_includes/](_includes) `<-- Jekyll includes`
 * [_util/](util/) `<-- scripts etc`
    * [_util/extract-metadata.py](util/extract-metadata.py) `<-- tool for working with .md files`

## Instructions for Registry Curators

See [this FAQ entry](http://obofoundry.github.io/faq/how-do-i-edit-metadata.html) for simple web-based editing of metadata

Please edit the *source* files in the [ontology/](ontology/) directory only.

For example:

 * [ontology/uberon.md](ontology/uberon.md)
 * [ontology/bfo.md](ontology/bfo.md)

Each `*.md` file consists of

 * YAML metadata
 * Markdown text to be shown on the page for that ontology

For example:

```markdown
---
layout: ontology_detail
id: aeo
title: Anatomical Entity Ontology
contact: 
  email: J.Bard@ed.ac.uk
  label: Jonathan Bard
description: AEO is an ontology of anatomical structures that expands CARO, the Common Anatomy Reference Ontology
domain: anatomy
homepage: http://www.obofoundry.org/wiki/index.php/AEO:Main_Page
products: 
  - id: aeo.owl
---

AEO is an ontology of anatomical structures that expands CARO, the Common Anatomy Reference Ontology, to about 200 classes using the is_a relationship; it thus provides a detailed type classification for tissues. The new classes were chosen for their use in categorizing the major vertebrate and invertebrate anatomy ontologies at a granularity adequate for tissues of a single cell type. The ontology should be useful in increasing the amount of knowledge in anatomy ontologies, facilitating annotation and enabling interoperability across anatomy ontologies
```

The [aeo page](http://obofoundry.github.io/ontology/aeo.html) shows the structured info on the right and the formatted text on the right. (THIS IS A BAD EXAMPLE IT HAS NO FORMATTING)

The YAML data is strictly vetted by OBO team. The Makefile takes care
of syntactic validation (the GitHub Actions runs `make test`). The OBO
team ensures the content is correct, up to date and accurate.

You can put any HTML or Markdown in the lower section - customize each ontology page!

Note that each md file is the primary source for the metadata for each
ontology. It may seem odd to mix the markdown in with the yaml, but in
practice this works well and is easy to manipulate using the python
script in the util/ directory.

The one piece of visual info in the md is the `layout` field, which is necessary for Jekyll.

#### RDF

The yaml is all "YAML-LD" and can compile down to RDF/OWL using a generic translator (eg JENA) plus our context file.

### Community Contributions

Note that general OBO users are free to edit via the GitHub web
interface and make a pull request. They can update their own entries,
but they are also welcome to suggest changes elsewhere.

On the live site, each page has links to view source and edit source. This makes use of githubs builtin editing facility

For example:

 * [view ontology/uberon.md](https://github.com/OBOFoundry/OBOFoundry.github.io/blob/master/ontology/uberon.md) 
 * [edit ontology/uberon.md](https://github.com/OBOFoundry/OBOFoundry.github.io/edit/master/ontology/uberon.md) 

Note that joe randoms cannot just come in and update things. Anyone with a GitHub account can make [pull request](https://help.github.com/articles/using-pull-requests/)
(aka PR). It is up to the OBO team whether the PR may be merged or rejected.

Note that if you make a syntax error whilst editing, then the GitHub Actions
check will fail. Your PR will have a big red X next to it, in which
case the OBO team will not merge your PR. Don't worry, all you have to
do is make further edits to fix the syntax error.

TODO: add a quick guide to yaml, and the tags we use.

## Central OBO library build

(see also the FAQ entry on this)

The central OBO build runs here:

 * http://build.berkeleybop.org/job/simple-build-obo-all/

It takes as metadata input the yml file from this repository. It makes
use of the `build` object.

The output of this job is a set of obo and owl files deposited in

 * http://berkeleybop.org/ontologies/

Depending on the build configuration, this may also make additional files. See for example:

 * http://berkeleybop.org/ontologies/uberon/

A http://berkeleybop.org/ontologies/ URL should never be handed out directly. This service exists so that:

 * Un PURL-registered ontologies will have a fall-through
 * Registered PURL ontologies that do not want to take charge of either OBO or OWL generation will have a place to 302-redirect to

This job will fail if ontologies marked as `infallible` fail. To debug, the full log of the last build can be examined:

 * https://build.berkeleybop.org/job/simple-build-obo-all/lastBuild/consoleFull

(Look for the text "should not fail")

## Instructions for Website Development

See [README-sitedev.md](README-sitedev.md)
