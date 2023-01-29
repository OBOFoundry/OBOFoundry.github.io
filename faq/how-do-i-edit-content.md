---
layout: faq
title: Edit content
---

This FAQ is about editing the narrative content of the OBO site

- To edit ontology metadata, see the FAQ <a href="{{site.baseurl}}faq/how-do-i-edit-metadata.html">How do I edit metadata</a>
- For general contributions, see the FAQ <a href="{{site.baseurl}}faq/how-do-i-modify-website.html">How do I modify the web portal</a>

## How do I edit the content of the OBO site?

The procedure for editing content of the website is similar to that
for [editing metadata files](how-do-i-edit-metadata.md):

- Click the Edit button. This takes you to the GitHub page for editing content
- Make your proposed edits
- Save and make a Pull Request

Note that even if you have permission to directly push to master,
making Pull Requests (PRs) is generally a good idea.

## Markdown

Most of the content of the website is in [markdown format](http://daringfireball.net/projects/markdown/syntax). This
is primarily:

- Principles
- The FAQ entries

Most other content is metadata driven. To modify this, edit the
metadata file itself. To change how the metadata is displayed, change
the template (advanced, see the link above). Note that there should be
a link to the jekyll template underneath the Edit button for each
page.

Markdown is generally self-explanatory, more details can be [found here](http://programminghistorian.org/new-lesson-workflow#write-in-markdown).

It is important that editors conform to the style guide for each page type

## Principles Styleguide

Jekyll template: <a href="{{site.repo_src}}_layouts/principle.html">\_layouts/principle.html</a>

The md file should have a a yaml header like the following:

```
---
layout: principle
id: fp-001-open
title: Open
---
```

The value of `layout:` **must** be `principle`

Each principle should have the following sections:

```
## Summary

...

## Purpose

...

## Recommendations

...

## Implementations

...

```

A level 2 heading (`##`) should be used for each. Level 3 headings or higher may be included.

Note that no title is necessary, as this is generated from the yaml header block by the jekyll template

## FAQ Styleguide

Jekyll template: <a href="{{site.repo_src}}_layouts/faq.html">\_layouts/faq.html</a>

The md file should have a a yaml header like the following:

```
---
layout: faq
title: Add a browser
---
```

The value of `layout:` **must** be `faq`

A level 2 heading (`##`) should be used for each section. Level 3 headings or higher may be included.

The FAQ entry should start with a title. E.g.

```
## How do I add a custom link to an ontology browser for my ontology?

Every ontology in the registry is automatically in [OntoBee](https://ontobee.org), so we
automatically provide a link to OntoBee.
...
```
