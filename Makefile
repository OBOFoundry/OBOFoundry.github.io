ONTS := $(wildcard ontology/*md)

all: _config.yml

test: validate all

t:
	echo $(ONTS)

#_config.yml: _config_header.yml registry/ontologies.yml
#	cat $^ > $@

_config.yml: _config_header.yml $(ONTS)
	./util/extract-metadata.py concat -i $< $(ONTS) -o $@.tmp && mv $@.tmp $@

# TODO: trigger
# TODO: more robust way of doing this
#registry/ontologies.yml: $(ONTS)
#	./util/compile-registry.pl $^ > $@.tmp && mv $@.tmp $@

registry/ontologies.yml: $(ONTS)
	./util/extract-metadata.py concat $^ > $@.tmp && mv $@.tmp $@

validate: $(ONTS)
	./util/extract-metadata.py validate $^

