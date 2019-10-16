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
# but sometimes it helps to delete the target files first by running `make clean`
#
# WARNING: Makefiles contain significant tab characters!
# Before editing this file, ensure that your editor is not set up to convert tabs
# to spaces, and then use tabs to indent recipe lines.


### Configuration

# All ontology .md files
ONTS := $(wildcard ontology/*.md)

# All principles .md files
PRINCIPLES := $(wildcard principles/*.md)


### Main Tasks
.PHONY: all pull_and_build test pull clean

all: _config.yml registry/ontologies.ttl registry/publications.md registry/obo_context.jsonld

pull:
	git pull

pull_and_build: pull all

test: reports/metadata-grid.html _config.yml

integration-test: test valid-purl-report.txt

# Remove and/or revert all targets to their repository versions:
clean:
	rm -Rf registry/ontologies.nt registry/ontologies.ttl registry/ontologies.yml registry/publications.md sparql-consistency-report.txt jenkins-output.txt valid-purl-report.txt valid-purl-report.txt.tmp _site/ tmp/ reports/
	git checkout _config.yml registry/ontologies.jsonld registry/ontologies.ttl registry/ontologies.yml registry/publications.md


### Directories:

tmp:
	mkdir -p $@

reports:
	mkdir -p $@


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

# Sort ontologies based on the validation (metadata-grid)
registry/ontologies.yml: reports/metadata-grid.csv
	./util/sort-ontologies.py tmp/unsorted-ontologies.yml $< $@ && rm -rf tmp

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
registry/publications.md: registry/ontologies.yml
	util/extract-publications.py $< $@

### Validate Configuration Files

# generate both a report of the violations and a grid of all results
# the grid is later used to sort the ontologies on the home page
RESULTS = reports/metadata-violations.tsv reports/metadata-grid.csv
reports/metadata-grid.csv: tmp/unsorted-ontologies.yml | extract-metadata reports
	./util/validate-metadata.py $< $(RESULTS)

# generate an HTML output of the metadata grid
# TODO: determine where this output belongs
reports/metadata-grid.html: reports/metadata-grid.csv
	./util/create-html-grid.py $< $@

# Extract metadata from each ontology .md file and combine into single yaml
tmp/unsorted-ontologies.yml: $(ONTS) | tmp
	./util/extract-metadata.py concat -o $@.tmp $^  && mv $@.tmp $@

extract-metadata: $(ONTS)
	./util/extract-metadata.py validate $^


### OBO Dashboard

# This is the Jenkins job
# The reports will be archived

dashboard: reports/dashboard.html

RUN_ROBOT = java -jar build/robot.jar python &

build:
	mkdir -p $@

#.PHONY: build/robot.jar
build/robot.jar: build
	curl -o $@ -Lk https://build.obolibrary.io/job/ontodev/job/robot/job/py4j/lastSuccessfulBuild/artifact/bin/robot.jar

#.PHONY: build/robot-foreign.jar
build/robot-foreign.jar: build
	curl -o $@ -Lk  https://build.obolibrary.io/job/ontodev/job/robot/job/562-feature/lastSuccessfulBuild/artifact/bin/robot.jar

reports/dashboard.csv: registry/ontologies.yml | reports build/robot.jar build/robot-foreign.jar
	kill $$(lsof -t -i:25333) || true
	$(RUN_ROBOT)
	./util/principles/dashboard.py $< $@

reports/dashboard.html: reports/dashboard.csv
	./util/create-html-grid.py $< $@
	mkdir -p reports/assets
	cp -r assets/svg reports/assets


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
