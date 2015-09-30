[![Build Status](https://travis-ci.org/OBOFoundry/OBOFoundry.github.io.svg?branch=master)](https://travis-ci.org/OBOFoundry/OBOFoundry.github.io)

Try it out: http://obofoundry.github.io/

## OBO Foundry website BETA

### What is this?

This is a proposed new website for the OBO Foundry. It replaces the
[previous proposal](https://github.com/OBOFoundry/omb), but uses the
same principles and YAML/RDF structures

### How does it work?

The source can be found on https://github.com/OBOFoundry/OBOFoundry.github.io

It uses GitHub Pages/[Jekyll](https://en.wikipedia.org/wiki/Jekyll_%28software%29),
a popular static site generator. I already use this for
http://uberon.org

It [integrates nicely with
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
    * [registry/ontologies.jsonld](registry/ontologies.jsonld)  `<-- generated from yaml`
    * `registry/ontologies.rdf  <-- TODO generated from jsonld`
 * [ontology/](ontology/)  `<-- source for ontology metadata. EDIT IN HERE`
    * [ontology/obi.md](ontology/obi.md)  `<-- metadata (yml) and markdown for display. EDIT THIS`
    * [ontology/uberon.md](ontology/uberon.md)
    * ...
 * [Makefile](Makefile) `<-- For compiling derived artefacts and running tests`
 * [.travis.yml](.travis.ml) `<-- continuous integration config`
 * [_posts/](_posts) `<-- Blog posts/news`
 * [_layouts/](_layouts) `<-- Jekyll layouts`
 * [_includes/](_includes) `<-- Jekyll includes`
 * [_util/](util/) `<-- scripts etc`
    * [_util/extract-metadata.py](util/extract-metadata.py) `<-- tool for working with .md files`

## Instructions for Registry Curators

**NEW!**: See [this FAQ entry](http://obofoundry.github.io/faq/how-do-i-edit-metadata.html) for simple web-based editing of metadata

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
of syntactic validation (the travis job runs `make test`). The OBO
team ensures the content is correct, up to date and accurate.

You can put any HTML or Markdown in the lower section - customize each ontology page!

Note that each md file is the primary source for the metadata for each
ontology. It may seem odd to mix the markdown in with the yaml, but in
practice this works well and is easy to mainpulate using the python
script in the util/ directory.

The one piece of visual info in the md is the `layout` field, which is necessary for Jekyll.


### Generation of downstream artefacts

OBO admins should periodically

    git pull
    make
    jekyll server
    ## open 127.0.0.1:4000 in a web browser and spot-check changes
    git commit -m 'regenerated derived files' -a
    git push origin master

See the `Makefile` for details. This will have the effect of
regenerating the main ontologies yaml (used by external consumers such
as OLS, as well as the central OBO library build), as well as the
GitHub pages `_config.yml` file. This last step is necessary to update
the front page.


#### RDF

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

Note that if you make a syntax error whilst editing, then the travis
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

A  http://berkeleybop.org/ontologies/ URL should never be handed out directly. This service exists so that:

 * Un PURL-registered ontologies will have a fall-through
 * Registered PURL ontologies that do not want to take charge of either OBO or OWL generation will have a place to 302-redirect to

This job will fail if ontologies marked as `infallible` fail. To debug, the full log of the last build can be examined:

 * https://build.berkeleybop.org/job/simple-build-obo-all/lastBuild/consoleFull

(Look for the text "should not fail")

## Adding news

Simply add a post to the [_posts/](_posts/) directory - copy an exiting one if you like

Posts can also be edited via the GH web interface, all posts are here:

https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/_posts

## Instructions for WebSite developers

Consult online Jekyll docs for details. Basically you just do

   gem install jekyll

(I am currently using Jekyll 2.5.3)

You can run a local test install from the top level directory

    jekyll serve

Then open http://127.0.0.1:4000

Every commit is visible within a few minutes on: http://obofoundry.github.io

You may want to work on a branch to avoid disrupting the live
site. Exact procedures for accepting changes back into master have yet
to be determined. See [CONTRIBUTING.md](CONTRIBUTING.md) for a draft.

The setup is fairly standard for Jekyll. We use Jekyll bootstrap
(bootstrap 3). We try and keep things minimal so that the site will
work on github. Even if you have no knowledge of Jekyll, it is fairly
easy to introspect what is going on if you have done much CMS work or
web development.

Basics:

 * source can be markdown or html
 * Different styles of pages go in _layouts
 * ...

## Site FAQ

See also the main FAQ on the website: this FAQ is for OBO internal people

### It's missing feature X from the old site

File an issue! Or better yet, make a change on a fork and make a PR!

### Shouldn't we pull project data from the ontologies themselves?

We should definitely have some mechanism for syncing these or allowing
this option. However, for the majority of ontologies for which I (cjm)
are de-facto administrating, the expertise and time to do this in OWL
is not there, and many groups prefer to have this centralized.






