[![Build Status](https://travis-ci.org/OBOFoundry/OBOFoundry.github.io.svg?branch=master)](https://travis-ci.org/OBOFoundry/OBOFoundry.github.io)

## OBO Foundry website ALPHA

### What is this?

This is a proposed new website for the OBO Foundry. It replaces the
[previous proposal](https://github.com/OBOFoundry/omb), but uses the
same principles and YAML/RDF structures

### How does it work?

The source can be found on https://github.com/OBOFoundry/OBOFoundry.github.io

It uses [Jekyll](https://en.wikipedia.org/wiki/Jekyll_%28software%29),
a very nice static site generator. I already use this for
http://uberon.org

It also [integrates nicely with
github](https://help.github.com/articles/using-jekyll-with-pages/)
which means that the entire site can be seen on
http://obofoundry.github.io (no need to run a dedicated webserver)

At the same time, we are not dependent on github - we could do our own
static generation, e.g. with a Jenkins job

### I have some comments

You can use the [issue
tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues)
but you may want to hold off til things are more stable

### I want to contribute

Please do! Fork and make PR, but beware things are not yet stable

## Organization

 * [registry/](registry)   `<-- DERIVED yaml, json and RDF. DO NOT EDIT`
    * [registry/ontologies.yaml](registry/ontologies.yaml)  `<-- READONLY`
 * [ontology/](ontology/)  `<-- source for ontology metadata. EDIT THIS`
    * [ontology/obi.md](ontology/obi.md)
    * [ontology/uberon.md](ontology/uberon.md)
    * ...
 * [Makefile](Makefile) `<-- For compiling derived artefacts`
 * [_layouts/](_layouts) `<-- Jekyll layouts`
 * [_includes/](_includes) `<-- Jekyll includes`
 * [_util/](util/) `<-- useful python`

## Instructions for Registry Curators

Please edit the *source* files in the [ontology/](ontology/) directory only.

For example:

 * [ontology/uberon.md](ontology/uberon.md)
 * [ontology/bfo.md](ontology/bfo.md)

Each md file consists of

 * YAML metadata
 * Markdown text to be shown on the page for that ontology

For example:

```
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
of syntactic validation. The OBO team ensures the content is correct,
up to date and accurate.

You can put any HTML or Markdown in the lower section - customize each ontology page!

Note that each md file is the primary source for the metadata for each
ontology. It may seem odd to mix the markdown in with the yaml, but in
practice this works well and is easy to mainpulate using the python
script in the util/ directory.

The one piece of visual info in the md is the `layout` field, which is necessary for Jekyll.

The yaml is all "YAML-LD" and can compile down to RDF/OWL using a generic translator (eg JENA) plus our context file.

### Community Contributions

Note that general OBO users are free to edit via the github web
interface and make a pull request. They can update their own entries,
but they are also welcome to suggest changes elsewhere.

On the live site, each page has links to view source and edit source. This makes use of githubs builtin editing facility

For example:

 * [view ontology/uberon.md](https://github.com/OBOFoundry/OBOFoundry.github.io/blob/master/ontology/uberon.md) 
 * [edit ontology/uberon.md](https://github.com/OBOFoundry/OBOFoundry.github.io/edit/master/ontology/uberon.md) 

Note that joe randoms cannot just come in and update things. Anyone with a github ID can make [pull request](https://help.github.com/articles/using-pull-requests/)
(aka PR). It is up to the OBO team whether the PR may be merged or rejected.

## Adding news

Simply add a post to the [_posts/](_posts/) directory - copy an exiting one if you like

TODO

## Instructions for WebSite developers

Consult online Jekyll docs for details. Basically you just do

   gem install jekyll

You can run a local test install from the top level directory

    jekyll serve

Then open http://127.0.0.1:4000

Every commit is visible within a few minutes on: http://obofoundry.github.io

You may want to work on a branch to avoid disrupting the live
site. Exact procedures for accepting changes back into master have yet
to be determined. For example, we may have a voting mechanism. As an
example of how this might work see
https://github.com/ga4gh/schemas/blob/master/CONTRIBUTING.md

The setup is fairly standard for Jekyll. We use Jekyll bootstrap
(bootstrap 3). We try and keep things minimal so that the site will
work on github. Even if you have no knowledge of Jekyll, it is fairly
easy to introspect what is going on if you have done much CMS work or
web development.

Basics:

 * source can be markdown or html
 * Different styles of pages go in _layouts
 * ...

## FAQ

### It's missing feature X from the old site

File an issue! Or better yet, make a change on a fork and make a PR!

### Shouldn't we pull project data from the ontologies themselves?

We should definitely have some mechanism for syncing these or allowing
this option. However, for the majority of ontologies for which I (cjm)
are de-facto administrating, the expertise and time to do this in OWL
is not there, and many groups prefer to have this centralized.






