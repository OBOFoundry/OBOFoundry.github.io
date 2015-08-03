This documentation is for developers of this prototype OBO Foundry site.

Note this document is in markdown and is best view on the github.

## Getting Started

You will first need jekyll, which can be installed by the ruby [gem](https://rubygems.org/):

    gem install jekyll

After checking out the code from github, you can start a local server:

    jekyll serve

(this must always be done from the top level)

Then view http://127.0.0.1:4000

You can make changes locally (you will need to start jekyll again - no
hot fixes).

If you commit and push, your change will be visible within a few
minutes on: http://obofoundry.github.io

If this site becomes official we may want to institute policies for
the site: e.g. major new changes happen on forks/branches, with a
voting policy for merging these in.

## Details

The setup is fairly standard for Jekyll. We use Jekyll bootstrap
(bootstrap 3). We try and keep things minimal so that the site will
work on github. Even if you have no knowledge of Jekyll, it is fairly
easy to introspect what is going on if you have done much CMS work or
web development.

Basically, every `.md` or `.html` file in the directory is visible on
the site, the same path. `.md` files are automatically translated to
`.html` (this happens in the [_site](_site) directory, which you
should never touch).

Jekyll uses a templating system called liquid. The basic idea is
simple, templating commands are contained within braces '{ }'.

Pages can have different layouts - see the [_layout/](_layout/)
directory. They can also include templates from the
[_includes/](_includes/) directory.

See [_assets](_assets) for bootstrap styling - don't touch this unless
you know what you're doing.

## Compilation of metadata

For the most part no compilation is necessary. Ontology pages are
served directly from the source `.md` file.

However, for some purposes it may be necessary to recompile the [_config.yml](_config.yml) file (**never edit this directly**)

To do this, type:

    make

In the top level. Note you will need python3 and the yaml library:

    pip3 install yaml

The dependencies should be visible in the [Makefile](Makefile). The basic idea is:

 * [ontology/](ontology/)*.md  --[extract yaml]--> [registry/ontologies.yaml](registry/ontologies.yaml) --> [_config.yml](_config.yml)

[registry/ontologies.yaml](registry/ontologies.yaml) is also used to
create [registry/ontologies.rdf](registry/ontologies.rdf) via a
JSON-LD file (JENA required).

## Pages

### Ontology Table

The front page [index.html](index.html) is the ontology table. It is
driven by the
[_includes/ontology_table.html](_includes/ontology_table.html)
template.

It iterates through all ontologies (these are stored in the variable
`pages.ontologies` which is set via `_config.yml` - see above for how
this is built). For each ontology it writes a table row.

### Ontology Pages

These are displayed directly via jekyll. Each ontology has it's own
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

### Bootstrap Conventions

We use bootstrap 3, so far no themes.

