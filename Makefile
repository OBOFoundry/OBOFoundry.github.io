ONTS := $(wildcard ontology/*md)

all: _config.yml

t:
	echo $(ONTS)

_config.yml: _config_header.yml registry/ontologies.yml
	cat $^ > $@

# TODO: trigger
# TODO: more robust way of doing this
registry/ontologies.yml: $(ONTS)
	./util/compile-registry.pl $^ > $@.tmp && mv $@.tmp $@

validate: $(ONTS)
	./util/extract-metadata.py validate $^

