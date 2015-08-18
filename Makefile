ONTS := $(wildcard ontology/*md)
PRINCIPLES := $(wildcard principles/*md)

all: _config.yml registry/ontologies.yml

test: validate all

integration-test: test valid-purl-report.txt

t:
	echo $(ONTS)

#_config.yml: _config_header.yml $(ONTS)
#	./util/extract-metadata.py concat -i $< $(ONTS) -o $@.tmp && mv $@.tmp $@
_config.yml: _config_header.yml registry/ontologies.yml principles/all.yml
	cat $^ > $@.tmp && mv $@.tmp $@

registry/ontologies.yml: $(ONTS)
	./util/extract-metadata.py concat -o $@.tmp $^  && mv $@.tmp $@

principles/all.yml: $(PRINCIPLES)
	./util/extract-metadata.py concat-principles -o $@.tmp $^  && mv $@.tmp $@

# TODO: add @context
registry/ontologies.jsonld: registry/ontologies.yml
	./util/yaml2json.py $< > $@.tmp && mv $@.tmp $@

# TODO
registry/ontologies.ttl: registry/ontologies.jsonld
	riot registry/context.jsonld $< > $@.tmp && mv $@.tmp $@


validate: $(ONTS)
	./util/extract-metadata.py validate $^

# Note this should *not* be run as part of general travis jobs, it is expensive
# and may be prone to false positives as it is inherently network-based
#
# See: https://github.com/OBOFoundry/OBOFoundry.github.io/issues/18
valid-purl-report.txt: registry/ontologies.yml
	./util/processor.py -i $< check-urls > $@.tmp && mv $@.tmp $@
