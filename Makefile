# Makefile for OBOFoundry.github.io
#
# This file contains commands for validating and generating
# configuration files for the OBO Foundry website.
# The `util/` directory contains additional scripts
# called from this Makefile.
# It is intended to be run on a Unix system (Linux, Mac OS X)
# **before** the site is built using
# [Jekyll](http://jekyllrb.com).
#
# Software requirements:
#
# - [GNU Make](http://www.gnu.org/software/make/)
# - [Apache Jena](https://jena.apache.org/download/)
# - [Python 3](https://www.python.org/downloads/)
# - [PyYAML](http://pyyaml.org/wiki/PyYAML)
# - [SPARQLWrapper](https://pypi.python.org/pypi/SPARQLWrapper)
#
# Run `make` in this directory to update all generated files
# (i.e. the default `all` task).
# Make does its best to detect changes and run only the required tasks,
# but sometimes it helps to delete the target files first.
#
# WARNING: Makefiles contain significant tab characters!
# Ensure that your editor shows tab characters before editing this file.


### Configuration

# All ontology .md files
ONTS := $(wildcard ontology/*md)

# All principles .md file
PRINCIPLES := $(wildcard principles/*md)


### Main Tasks

all: yml registry/ontologies.ttl registry/publications.md registry/obo_context.jsonld

pull_and_build: pull all

yml: _config.yml registry/ontologies.yml

test: validate yml

integration-test: test valid-purl-report.txt

pull:
	git pull


### Build Configuration Files

# Create the site-wide config file by combining all metadata on ontologies + principles
#  and combining with site-wide metadata.
#
# Note that anything in _config.yml is accessible to any liquid template via the
# `sites` object - think of it like the global database
#
# (this is somewhat hacky, but concatenating these yamls is safe)
_config.yml: _config_header.yml registry/ontologies.yml principles/all.yml
	cat $^ > $@.tmp && mv $@.tmp $@

# Extract metadata from each ontology .md file and combine into single yaml
registry/ontologies.yml: $(ONTS)
	./util/extract-metadata.py concat -o $@.tmp $^  && mv $@.tmp $@

# Extract the metadata from each principle in the principles/ directory, and concatenate
# into a single yaml file in that directory
principles/all.yml: $(PRINCIPLES)
	./util/extract-metadata.py concat-principles -o $@.tmp $^  && mv $@.tmp $@

# Use a generic yaml->json conversion, but adding a @content
registry/ontologies.jsonld: registry/ontologies.yml
	./util/yaml2json.py $< > $@.tmp && mv $@.tmp $@

registry/obo_context.jsonld: registry/ontologies.yml
	./util/processor.py -i $< extract-context  > $@.tmp && mv $@.tmp $@

# Use Apache-Jena RIOT to convert jsonld to n-triples
# NOTE: UGLY HACK. If there is a problem then Jena will write WARN message (to stdout!!!), there appears to
#  be no way to get it to flag this even with strict and check options, so we do a check with grep, ugh.
# see: http://stackoverflow.com/questions/20860222/why-do-i-have-these-warnings-with-jena-2-11-0
registry/ontologies.nt: registry/ontologies.jsonld
	riot --base=http://purl.obolibrary.org/obo/ --strict --check -q registry/context.jsonld $< > $@.tmp && mv $@.tmp $@ && egrep '(WARN|ERROR)' $@ && exit 1 || echo ok

registry/ontologies.ttl: registry/ontologies.nt
	riot --base=http://purl.obolibrary.org/obo/ --out=ttl $< > $@.tmp && mv $@.tmp $@

# Generate a list of primary publications
registry/publications.md: util/extract-publications.py registry/ontologies.yml
	$^ $@

### Validate Configuration Files

validate: $(ONTS)
	./util/extract-metadata.py validate $^ && \
	cd util && \
	./validate-metadata.py

# Note this should *not* be run as part of general travis jobs, it is expensive
# and may be prone to false positives as it is inherently network-based
#
# TODO: Other non-travis CI job. Nightly?
# TODO: Integrate this with some kind of OCLC query check
#
# See: https://github.com/OBOFoundry/OBOFoundry.github.io/issues/18
valid-purl-report.txt: registry/ontologies.yml
	./util/processor.py -i $< check-urls > $@.tmp && mv $@.tmp $@

sparql-consistency-report.txt: registry/ontologies.yml
	./util/processor.py -i $< sparql-compare > $@.tmp && mv $@.tmp $@


# output of central OBO build
# See FAQ for more details, and also README.md
jenkins-output.txt:
	wget http://build.berkeleybop.org/job/simple-build-obo-all/lastBuild/consoleFull -O $@

reports/%.csv: registry/ontologies.ttl sparql/%.sparql
	arq --data $< --query sparql/$*.sparql --results csv > $@.tmp && mv $@.tmp $@
