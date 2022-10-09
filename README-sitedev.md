# Site Development

This documentation is for developers of this prototype OBO Foundry site.

## Getting Started

Because Jekyll can be difficult to install, Docker provides an
alternative for running the `serve` command, then open http://localhost:4000:

```shell
$ docker run --rm --volume="$PWD:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll:3.5 jekyll serve
```

You can make changes locally and the Docker image will automatically update.
When you're ready, you can commit to a new branch and send a pull request.
After it's accepted, it will be automatically built and deployed to
http://obofoundry.github.io in a few minutes.

## Details

The setup is fairly standard for Jekyll. We use Jekyll bootstrap
(bootstrap 3). We try and keep things minimal so that the site will
work on github. Even if you have no knowledge of Jekyll, it is fairly
easy to introspect what is going on if you have done much CMS work or
web development.

Basically, every `.md` or `.html` file in the directory is visible on
the site, the same path. `.md` files are automatically translated to
`.html`.

Jekyll uses a templating system called liquid. The basic idea is
simple, templating commands are contained within braces '{ }'.

Pages can have different layouts - see the [_layouts/](_layouts/)
directory. They can also include templates from the
[_includes/](_includes/) directory.

See [assets/themes](assets/themes) for bootstrap styling - don't touch this unless
you know what you're doing.

## Compilation of metadata

For the most part no compilation is necessary. Ontology pages are
served directly from the source `.md` file.

However, for some purposes it may be necessary to recompile the [_config.yml](_config.yml) file (**never edit this directly**)

To do this, type:

    make

In the top level. Note you will need python3 and the yaml library, as well as jena's rdfcat

    pip3 install yaml
    
jena is at https://archive.apache.org/dist/jena/binaries/apache-jena-3.10.0.tar.gz. Uncompress and then add the bin directory to your PATH

The dependencies should be visible in the [Makefile](Makefile). The basic idea is:

 * [ontology/](ontology/)*.md  --[extract yaml]--> [registry/ontologies.yml](registry/ontologies.yml) --> [_config.yml](_config.yml)

[registry/ontologies.yml](registry/ontologies.yml) is also used to
create RDF files via a JSON-LD file (JENA required):
- [registry/ontologies.nt](registry/ontologies.nt) (in the N-tuples format)
- [registry/ontologies.ttl](registry/ontologies.ttl) (in the turtle format)
- [registry/ontologies.jsonld](registry/ontologies.jsonld) (in the JSON-LD format)

## Pages

### Ontology Table

The front page [index.html](index.html) is the ontology table. It is
driven by the
[_includes/ontology_table.html](_includes/table_widget.html)
template.

It iterates through all ontologies (these are stored in the variable
`pages.ontologies` which is set via `_config.yml` - see above for how
this is built). For each ontology it writes a table row.

### Ontology Pages

These are displayed directly via jekyll. Each ontology has its own
`.md` page, which consists of the main page content (free form
markdown) preceded by a structured yaml block. The structured yaml is
the ontology metadata (with a direct mapping to RDF), arbitrarily
nested. See the FAQ for how users should edit this.

The system is fairly simple with no additional compilation outside the
normal jekyll system. Whenever jekyll displays a markdown file, it
examines the yaml block and looks for a tag called `layout` (users
should not mess with this field unless they know what they are
doing). This determines the template in the `_layout` directory that
is used to render the markdown.

Currently all pages use the `ontology_detail` layout, which is found
in
[_layouts/ontology_detail.html](_layouts/ontology_detail.html). What
this currently does (and devs more web-savvy than me are welcome to
contribute different ways of doing this) is display the structured
yaml metadata in the left of the page, and the freeform (compiled)
markdown and html in the center.

### Navbar

The navigation bar / menu on the top of the page is controlled by
[_includes/navbar.html](_includes/navbar.html). It should be easy for
site admins to add new items, rearrange etc as they see fit

### Organization

This site provides a convenient way to organize OBO Foundry docs, if
this is deemed appropriate. So far I have copied some docs from the
original website (much of which is embarassingly stale, rotten or out
of date). Many things at the top level could be moved down into
directories to provide better organization.

I have already started a [faq/](faq/) directory (one md file per FAQ entry).

We could in theory easily manage our principles here. E.g. one .md
file per principle. I personally think this much better than the
current wiki, but other opinions welcome.

### Code quality

1. Install the Node Package Manager (NPM) following [these instructions](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
2. Install the [node package exector (`npx`)](https://www.npmjs.com/package/npx) with NPM using `npm install npx`
3. Install [`prettier`](https://prettier.io) with NPM using `npm install prettier`
4. Run `prettier` from the root of the repository with `npx prettier --write .`
