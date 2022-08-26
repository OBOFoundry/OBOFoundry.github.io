# Derived registry files

This directory contains combined metadata files derived from source in the [ontology directory](../ontology/).

Currently:

- `.yml` - YAML
- `.jsonld` - JSON(LD)
- `.ttl` - RDF/Turtle

See the [Makefile](../Makefile) for details how these are constructed

It is recommended you access all files in this repo through their PURLs. You can affix any filename to `http://purl.obolibrary.org/meta/`, e.g.

- http://purl.obolibrary.org/meta/context.jsonld
- http://purl.obolibrary.org/meta/ontologies.yml
- http://purl.obolibrary.org/meta/ontologies.jsonld
- http://purl.obolibrary.org/meta/obo_prefixes.ttl

https://github.com/bioregistry/bioregistry/issues/49
