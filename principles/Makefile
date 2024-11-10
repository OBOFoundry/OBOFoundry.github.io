# Collect the list of query files for report.
SCRIPTS := build/fp_001.py build/fp_002.py build/fp_003.py build/fp_004.py \
build/fp_005.py build/fp_006.py build/fp_007.py build/fp_008.py build/fp_009.py \
build/fp_011.py build/fp_012.py build/fp_016.py build/fp_020.py
DOCS := $(foreach x, $(SCRIPTS), checks/$(notdir $(basename $(x))).md)

# FP ID to the principle name
1 = Open
2 = 'Common Format'
3 = URI
4 = Versioning
5 = Scope
6 = 'Textual Definitions'
7 = Relations
8 = Documentation
9 = 'Documented Plurality of Users'
11 = 'Locus of Authority'
12 = 'Naming Conventions'
16 = Maintenance

# Generate all check docs
all: clean
scripts: $(SCRIPTS)

# Make the directories
checks build:
	mkdir -p $@

# Download the scripts from the OBO-Dashboard repo
.PHONY: build/fp_%.py
build/fp_%.py: | build
	curl -Lk -o $@ https://raw.githubusercontent.com/OBOFoundry/OBO-Dashboard/master/util/dashboard/$(notdir $@)

# Build the MD page from the check script
checks/fp_%.md: build/fp_%.py | $(SCRIPTS) checks
	$(eval ID := $(subst 0,,$(subst fp_,,$(notdir $(basename $@)))))
	if [ $(ID) == 1 ]; then export TITLE=$(1); \
	elif [ $(ID) == 2 ]; then export TITLE=$(2); \
	elif [ $(ID) == 3 ]; then export TITLE=$(3); \
	elif [ $(ID) == 4 ]; then export TITLE=$(4); \
	elif [ $(ID) == 5 ]; then export TITLE=$(5); \
	elif [ $(ID) == 6 ]; then export TITLE=$(6); \
	elif [ $(ID) == 7 ]; then export TITLE=$(7); \
	elif [ $(ID) == 8 ]; then export TITLE=$(8); \
	elif [ $(ID) == 9 ]; then export TITLE=$(9); \
	elif [ $(ID) == 11 ]; then export TITLE=$(11); \
	elif [ $(ID) == 12 ]; then export TITLE=$(12); \
	elif [ $(ID) == 16 ]; then export TITLE=$(16); \
	fi; \
	echo "---\nlayout: check\nid: $(ID)\ntitle: $$TITLE Automated Check\n---\n" > $@
	tail -n+3 $< \
	| sed 's/^##//' \
	| sed 's/^ //' \
	| awk '!found && /import/ { print "```python"; found=1 } 1' \
	>> $@
	echo '```' >> $@
	

clean: $(DOCS)
	rm -rf build