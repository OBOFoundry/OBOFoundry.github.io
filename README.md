## Test for OBO Foundry website

This uses Jekyll, which [integrates nicely with github](https://help.github.com/articles/using-jekyll-with-pages/)

Any changes made here are synced here: http://obofoundry.github.io

## Instructions for Registry Curators

Please edit the *source* files in the [ontology/](ontology/) directory only.

For example:

 * [ontology/uberon.md](ontology/uberon.md)

Each md file consists of

 * YAML metadata
 * Markdown text to be shown on the page for that ontology

Note that general OBO users are free to edit via the github web interface and make a pull request

TODO: derive [registry/ontologies.yml](registry/ontologies.yml) from ontology directory

## Instructions for WebSite developers

Consult online Jekyll docs for details

You can run a local test install:

    jekyll serve

Then open http://127.0.0.1:4000

Every commit is visible within a few minutes on: http://obofoundry.github.io

You may want to work on a branch!





