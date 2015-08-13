ONTS := $(wildcard ontology/*md)
PRINCIPLES := $(wildcard principles/*md)

all: _config.yml registry/ontologies.yml

test: validate all

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

