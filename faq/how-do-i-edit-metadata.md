---
layout: faq
title: Edit metadata
---

## How do I edit the metadata for my ontology?

Previously the only way to edit the metadata for your ontology was to
log a request for an OBO administrator to make the change for you. You
are still welcome to do this, but with our github-based system you can
now do this yourself.

You will first need an account on [github](http://github.com).

See below for a tutorial. If you are already familiar with github and
forks and pull requests, here is how the OBO site works.

Each ontology has its own file in github called `ONT.md`, where ONT is
the idspace for your ontology.

The markdown (`.md`) page for your ontology is in two sections:

1.  The section between the `---` markers is in a format called _yaml_, and is structured metadata
2.  The section after the markers is markdown text that can be used to customize your page

### YAML Metadata

The YAML section may look something like this:

```
layout: ontology_detail
id: cl
label: Cell Ontology
title: Cell Ontology
description: The Cell Ontology is a structured controlled vocabulary for cell types in animals.
integration_server: http://build.berkeleybop.org/job/build-cl/
taxon:
  id: NCBITaxon:33208
  label: Metazoa
domain: cells
tracker: https://code.google.com/p/cell-ontology/issues/list
mailing_list: https://lists.sourceforge.net/lists/listinfo/obo-cell-type
dependencies:
 - id: uberon
 - id: go
canonical: cl.owl
products:
 - id: cl.owl
 - id: cl.obo
 - id: cl/cl-basic.obo
```

_IMPORTANT_ some properties are in flux, be warned.

_TODO_ link to doc for properties

A few key properties to be aware of:

- _layout_ - this is not actually metadata about the ontology but controls how the page is displayed. You should not mess with this unless you are a web style guru.
- _id_ - this should not be touched. Your ontology id is fixed in the system by OBO administrators at time of registration and should never be changed. Contact the OBO team if you have a valid reason for changing this. See [ID Policy](../id-policy.html)
- _title_ - a _short_ name for your ontology - this is typically the spelling out of your ontology acronym.
- _description_ - a short one line description of your ontology. It should state concisely what the contents of the ontology are. Don't write this like a paper abstract. You can be more verbose in the custom section below
- _tracker_ - typically a github issues url

### Freeform Markdown

The section after the second `---` controls what goes in the main panel on your ontology page. You should include at least a one paragraph description here. You are free to put more detail, and you can use a mixture of HTML and Markdown formatting. You can even put images in here. You should not put citations, funding statements, or other information that is possible to include in the structured data.

For example, here is the AMPHX freeform markdown section

```markdown
The Amphioxus Development and Anatomy Ontology (AMPHX) is to describe the anatomy and development of Amphioxus, also known as lancelet, member of the invertebrate subphylum Cephalochordata and the phylum Chordata. This ontology is intended to be used for description of gene expression in amphioxus (e.g. Insitus, RNA-seq). The ontology was created in the context of the European project [CORBEL](https://www.corbel-project.eu/home.html), and used in the database [MARIMBA](http://marimba.obs-vlfr.fr/home).
```

### Pull Request Pipeline

Any user can make proposed changes to any `*.md` file. These remain on
their fork until approved by OBO admins. The workflow is:

1. An automated GitHub Actions job will run to validate your changes
2. An OBO administrator will evaluate your PR. If it failed the checks, it will not be accepted
3. If the the OBO admin rejects it they will provide feedback in the comment form which you can use to make further edits
4. More likely, the change will be accepted by the OBO admin. They will click "squash and merge".
5. An automated GitHub Actions workflow will update the build artifacts and issue a new PR. An OBO admin can review and accept.

## Pull Request Tutorial

This is a walk through of how a pull request works, featuring the
github user @planteome-user (who maintains various OBO ontologies such
as po and eo) and the OBO administrator @cmungall

### Getting Started

@planteome-user navigates to the [page with their ontology](http://obofoundry.github.io/ontology/eo.html), in this case eo.

<img style="border: 2px solid black" alt="s1" width="50%" src="/images/eo-example-s1.png"/>

The exact layout may differ in future versions of the site, this demo
is being prepared from an alpha version. The thing to notice here is
that the link for "Trackers" says sourceforge. This is out of date, as
planteome-user has recently migrated eo from SF to GitHub.

The user clicks on the link that says "View" taking them to the HTML view in github...

### Viewing metadata

This page shows the github view of their structured metadata (with the
text that goes in the main panel underneath)

<img style="border: 2px solid black" alt="s2" width="50%" height="50%" src="/images/eo-example-s2.png"/>

Note that github chooses to render the yaml in a different way from
the OBO site, don't be perturbed by this.

### Editing metadata: first create a fork

The user can either click on the "Edit" button from the github page,
or on the "Edit" button on the OBO page. This will take them to a
web-based editor for their metadata.

As a first step, the user will be asked to "Fork this
repository". This is to prevent any random github user for making
unwanted changes. The changes will exist only on the user's fork until
approved by OBO admins:

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s3.png"/>

You don't need to worry about details here. Just click the big green button to fork!

You will only ever need to do this step once.

### Editing metadata: web based editing

You will now be placed into a web-based editor. Your metadata is in
two sections: YAML formatted structured data, and freeform
descriptions in markdown format.

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s4.png"/>

At this time eo has a relatively minimal freeform
description. For now we will focus on the yaml.

The tracker entry in the yaml above is for sourceforge. The
@planteome-user has migrated their tracker from sourceforge to github,
so they now want to change this:

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s5.png"/>

Don't worry too much about making mistakes at this stage - as we'll
see later the system will prevent syntax errors from making it into
the system, and a friendly OBO admin will double-check what you've
done.

If you're still nervous, you can click "preview":

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s6.png"/>

Once you're happy you can propose the change:

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s7.png"/>

Filling in a message is optional, but we recommend doing it. After this, click the big green button, and you will be taken to a page for comparing changes:

### Comparing changes

Here you can see your changes once again (this time on the raw source):

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s8.png"/>

If it all looks good, click the big green button to make a PR!

### Open a PR

Almost there! You can make any additional comments on this page:

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s9.png"/>

But most of the time you can just click the big green button to
proceed, where your proposed changes will be automatically vetted:

### Automated validation by Travis

We can see that our edits have passed the automated checks run by Travis. Phew!

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s10.png"/>

You may see a message that the check is in progress - it should only
take a few seconds for it to finish.

See later for more on what happens when this step fails.

## Merging of PRs by OBO admins

@planteome-user now has to wait a bit for changes to become live.

Some time later OBO admin @cmungall (that's me) comes along and examines the PR. This is what my view looks like:

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s11.png"/>

Now I vet your changes, and most likely these should be fine, in which case I will merge:

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s12.png"/>

The change is reflected within seconds on the main site:

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s13.png"/>

(note that changes will not be immediately visible in the front
table. The OBO admin will need to regenrate metadata for this)

## What happens with mistakes?

Now let's work through an example of what happens when a user makes a
syntax error when editing their metadata.

From [the eo page](http://obofoundry.github.io/ontology/eo.html), the
user clicks the edit button, and enters some garbage on lines 5 and 6:

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s14.png"/>

They go through the same steps as before, except now when they get to
the automatic validation page they get a big red mark next to their change:

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s15.png"/>

You can click on "details" to see the report. This takes you to the Travis website. Scroll down to see the error message:

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s16.png"/>

Sometimes these may be a bit cryptic, but you should get the
idea. Note the line number is within the yaml section, not the whole
md file. If this is too geeky, the OBO tech will help you if you get stuck.

The OBO admins will be able to see the failed PRs and may contact you
with friendly advice. This is what it looks like from @cmungall's end:

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s17.png"/>

An OBO admin will in general not merge a PR that fails the Travis
check (although it if it's obvious how to fix the mistake, they may
elect to merge then fix).

There are a few things to do here. You can just sit back and wait for
advice. Or, you can proactively go back and make further changes to
fix your error.

Alternatively, if you want to abort and start again you can easily do
this. You may want to close your PR. You can optionally leave a
message:

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s18.png"/>

Then click "Close and comment"

Finally delete your branch:

<img style="border: 2px solid black" alt="s" width="50%" height="50%" src="/images/eo-example-s19.png"/>

## Happy? Confused?

If this seems bewildering, don't worry. The PR mechanism is optional
you can always ask OBO administrators to make any changes for you, via
email or the tracker.
