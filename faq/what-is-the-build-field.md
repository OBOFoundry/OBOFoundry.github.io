---
layout: faq
title: OBO central builds
---

## What does the build object do in my YAML configuration?

Most ontology metadata files contain a `build` field (see other FAQ
entries for how to view and edit metadata files).

For example, the [mouse anatomy](/ontology/ma.html) yaml file `ma.md` has the following:

```
...
build:
  source_url: ftp://ftp.informatics.jax.org/pub/reports/adult_mouse_anatomy.obo
  method: obo2owl
...
```

This is instructions for the central OBO library build pipeline which
runs nightly. This ensures creation of correct obo and owl files for
each ontology.

The output goes here:

- http://ontologies.berkeleybop.org/

You can choose to entirely ignore the output of this pipeline for your
ontology. However, it provides a convenient fall-through for groups
who are not running their own release pipelines. Historically many
groups in OBO have just produced a single obo file, e.g. on their ftp
site, and the central build has ensured owl and roundtripped obo (as
well as additional services such as validation).

## Where does the job run?

The continuous integration job runs here:

- http://build.berkeleybop.org/job/simple-build-obo-all/

It takes as metadata input the yml file from this repository. It makes
use of the `build` object.

This job will fail if ontologies marked as `infallible` fail. To debug, the full log of the last build can be examined:

- https://build.berkeleybop.org/job/simple-build-obo-all/lastBuild/consoleFull

(Look for the text "should not fail")

## Warning

A http://ontologies.berkeleybop.org/ URL should never be handed out directly. This service exists so that:

- Un PURL-registered ontologies will have a fall-through
- Registered PURL ontologies that do not want to take charge of either OBO or OWL generation will have a place to 302-redirect to

## What are some of the methods?

The build object takes a number of different methods:

- obo2owl: creates a release folder using an obo file as source
- owl2obo: creates a release folder using an owl file as source
- archive: copies a release folder (e.g. from an existing CI job) to the bbop ontology repository
- vcs: does a git or svn checkout and copies the resulting folder

For more details, ask a question on the tracker or see the script:

- https://github.com/owlcollab/owltools/blob/master/OWLTools-Oort/bin/build-obo-ontologies.pl

## Assumptions

### Ontology URI

If you are using the obo2owl or owl2obo method, you should make sure
that the ontology URI is set correctly. This should be set to whatever
is intended as the final URI for the ontology.

Assume we have an ontology with ID space `FOO`. For the owl2obo method, the file will contain:

```
   <owl:Ontology rdf:about="http://purl.obolibrary.org/obo/foo.owl">
```

For obo2owl, the file should contain:

```
ontology: foo
```

(the obo2owl method builds in assumptions about the ID policy for ontology URIs).

Note that some legacy `.obo` files do not include an ontology
header. For those, we add an extra line in the `build` object in the
metadata file:

```
build:
  source_url: http://some.old.url.org/my/foo.obo
  method: obo2owl
  insert_ontology_id: true
```

This will use the `id` field to set the ontology ID/URI correctly.

This currently only works for owl2obo. If you are going from OWL, you
should use the final URI for your ontology - this assumption is built in.

Note that if the id/uri is not set correctly and you don't auto-insert
the id using the directive above, then the build for your ontology will fail!

## How do I tell if the build for my ontology failed?

Note that the jenkins job will still succeed even if your ontology
build fails (unless the `is_infallible` field is set). Currently the
only way around this is to download the jenkins report and examine it.

If that does not sound ideal, remember the central build is a fallback
system, and includes many legacy/grandfathered ontologies.

## How do I take control of my own builds

You do not need to rely on the OBO central builds!

You can use an existing tool like
[robot](https://github.com/ontodev/robot/) and a Makefile. See some
existing github repositories for examples.

You would make your own releases (I recommend using the github release mechanism)

You can then configure your ontology entries in OCLC to point to the
location in your repository (or to where you choose to release them, e.g. S3)

Another option is to use a CI system to build your ontology.
