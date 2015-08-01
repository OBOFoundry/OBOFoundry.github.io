---
layout: default
title: Edit metadata
---

## How do I edit the metadata for my ontology?

Previously the only way to edit the metadata for your ontology was to
log a request for an OBO administrator to make the change for you. You
are still welcome to do this, but with our github-based system you can
now do this yourself.

You will first need an account on http://github.com

Next, go to the page for your ontology. On the bottom of the metadata
panel, click the link that says "Edit"

ADD DETAILS ON FORK HERE

You will be taken to the source for the page which is managed in a
format called "Markdown" within github. You will be placed in edit
mode, where you can edit the metadata and customize your page, and
make what is known as a "Pull Request" (PR). This PR will be
automatically checked and then merged in by an OBO administrator
(provided it meets their approval).

The markdown (`.md`) page for your ontology is in two sections:

 1. The section between the `---` markers is in a format called *yaml*, and is structured metadata
 2. The section after the markers is markdown text that can be used to customize your page

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
termgenie: http://cl.termgenie.org
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

*IMPORTANT* some properties are in flux, be warned.

A few key fields to be aware of:

 * *layout* - this is not actually metadata about the ontology but controls how the page is displayed. You should not mess with this unless you are a web style guru, in which case see [this FAQ entry](how-do-i-customize-layout.html)
 * *id* - this should not be touched. Your ontology id is fixed in the system by OBO administrators at time of registration and should never be changed. Contact the OBO team if you have a valid reason for changing this. See [ID Policy](../id-policy.html)
 * *title* - a *short* name for your ontology - this is typically the spelling out of your ontology acronym.
 * *description* - a short one line description of your ontology. It should state concisely what the contents of the ontology are. Don't write this like a paper abstract. You can be more verbose in the custom section below
 * *tracker* - typically a github issues url

### Freeform Markdown

The section after the second `---` controls what goes in the main panel on your ontology page. You should include at least a one paragarph description here. You are free to put more detail, and you can use a mixture of HTML and Markdown formatting. You can even put images in here.

For example, here is the ENVO freeform markdown section

```
EnvO is a community ontology for the concise, controlled description of environments.

<img src="/logos/envo.png"/>

Envo can be cited as:

Buttigieg, P. L., Morrison, N., Smith, B., Mungall, C. J., & Lewis, S. E. (2013). <b>The environment ontology: contextualising biological and biomedical entities</b>. <i>Journal of Biomedical Semantics, 4(1), 43</i>. <a href="http://www.dx.doi.org/10.1186/2041-1480-4-43">doi:10.1186/2041-1480-4-43</a>
```

### Saving changes and making a Pull Request

Once you are done, hit save. Note that the changes will *not* be
immediately visible, a few things have to happen first. You will need
to "fork" the repo (don't worry, just click the button to do it).

After doing this you will need to click "make pull request"

This is all you need to do. What happens next:

 1. An automated Travis job will run to validate your changes
 2. An OBO administrator will evaluate your PR. If it failed the travis check, it will not be accepted
 3. If the the OBO admin rejects it they will provide feedback in the comment form which you can use to make further edits
 4. More likely, the change will be accepted by the OBO admin. They will click "merge" and the changes will be visible in a few seconds.
 5. The OBO admin will also need to run a Make script to regenerate the main metadata file, so your changes may not be visible on the front table straight away


