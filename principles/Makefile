# Collect the list of query files for report.
SCRIPTS := $(wildcard ../util/principles/fp_*.py)
DOCS := $(foreach x, $(SCRIPTS), checks/$(notdir $(basename $(x))).md)

all: $(DOCS)

checks:
	mkdir -p $@

checks/fp_%.md: ../util/principles/fp_%.py | checks
	tail -n+3 $< \
	| sed 's/^##//' \
	| sed 's/^ //' \
	| awk '!found && /import/ { print "```"; found=1 } 1' \
	> $@
	echo '```' >> $@
	echo "---\nlayout: check\nid: $(notdir $(basename $@))\ntitle: $(subst 0,,$(subst fp_,,$(notdir $(basename $@))))\n---\n$$(cat $@)" > $@