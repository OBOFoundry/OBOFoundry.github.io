#!/usr/bin/env python3

import ast, json, jsonschema, os, re, sys

# file paths
schema_dir = 'util/schema'

def validate(args):
	"""
	Validate registry metadata.
	Usage: ./validate-metadata.py <data file> <output file> <grid file>
	"""
	global metadata_grid

	data_file = args[1]
	output_file = args[2]
	grid_file = args[3]

	data = load_data(data_file)
	schemas = get_schemas()
	
	results = {'error': [], 'warn': [], 'info': []}
	metadata_grid = {}

	# validate each object
	for item in data["ontologies"]:
		add = validate_metadata(item, schemas)
		results = update_results(results, add)
	print_results(results)
	save_results(results, output_file)
	save_grid(metadata_grid, grid_file)
	if results['error']:
		print('Metadata validation failed with %d errors - see %s for details'\
		      % (len(results['error']), output_file))
		sys.exit(1)
	else:
		print('Metadata validation passed - see %s for details' % output_file)
		sys.exit(0)

def update_results(results, add):
	"""Given a map of results for all ontologies and a map of results to add, 
	append the results to the lists in the map."""
	res_errors = results['error']
	res_warns = results['warn']
	res_infos = results['info']
	results['error'] = res_errors + add['error']
	results['warn'] = res_warns + add['warn']
	results['info'] = res_infos + add['info']
	return results

def print_results(results):
	"""Given a map of results, log results on the console."""
	for level, messages in results.items():
		for m in messages:
			print('%s\t%s' % (level.upper(), m))

def save_results(results, output_file):
	"""Given a map of results and an output file to write to, write each result 
	on a line."""
	if '.csv' in output_file:
		separator = ','
	elif '.tsv' or '.txt' in output_file:
		separator = '\t'
	else:
		print('Output file must be CSV, TSV, or TXT')
		return
	with open(output_file, 'w') as f:
		f.write('Level%sMessage\n' % separator)
		for level, messages in results.items():
			for m in messages:
				f.write('%s%s%s\n' % (level.upper(), separator, m))

def save_grid(metadata_grid, grid_file):
	"""Given a metadata grid of all results and a grid file to write to, create 
	a sorted table of the full results."""
	if '.csv' in grid_file:
		separator = ','
	elif '.tsv' or '.txt' in grid_file:
		separator = '\t'
	else:
		print('Grid file must be CSV, TSV, or TXT')
		return

	sort = sort_grid(metadata_grid)
	header = 'Ontology{0}Activity Status{0}Validation Status{0}activity_status{0}contact{0}description{0}homepage{0}id{0}license{0}products{0}title\n'.format(separator)

	with open(grid_file, 'w') as f:
		f.write(header)
		for ont_id in sort:
			results = metadata_grid[ont_id]
			s = '{1}{0}{2}{0}{3}{0}{4}{0}{5}{0}{6}{0}{7}{0}{8}{0}{9}{0}{10}{0}{11}\n'\
				.format(separator,
					    ont_id, 
					    results['ontology_status'], 
					    results['validation_status'], 
					    results['activity_status'],
					    results['contact'],
					    results['description'],
					    results['homepage'],
					    results['id'],
					    results['license'],
					    results['products'],
					    results['title'])
			f.write(s)
	print('Full validation results written to %s' % grid_file)

def sort_grid(metadata_grid):
	"""Given a metadata grid as a map, sort the grid based on:
	   1. Foundry status
	   2. Ontology activity status
	   3. Validation status
	   4. Alphabetical
	Return a sorted list of IDs."""
	pass_foundry = []
	info_foundry = []
	warn_foundry = []
	fail_foundry = []
	pass_active = []
	info_active = []
	warn_active = []
	fail_active = []
	pass_orphaned = []
	info_orphaned = []
	warn_orphaned = []
	fail_orphaned = []
	pass_inactive = []
	info_inactive = []
	warn_inactive = []
	fail_inactive = []

	for ont_id, results in metadata_grid.items():
		# get the info about the ontology to sort on
		foundry = results['foundry']
		ontology_status = results['ontology_status']
		validation_status = results['validation_status']

		if foundry:
			if validation_status == 'PASS':
				pass_foundry.append(ont_id)
			elif validation_status == 'INFO':
				info_foundry.append(ont_id)
			elif validation_status == 'WARN':
				warn_foundry.append(ont_id)
			elif validation_status == 'FAIL':
				fail_foundry.append(ont_id)
			continue

		if ontology_status == 'active':
			if validation_status == 'PASS':
				pass_active.append(ont_id)
			elif validation_status == 'INFO':
				info_active.append(ont_id)
			elif validation_status == 'WARN':
				warn_active.append(ont_id)
			elif validation_status == 'FAIL':
				fail_active.append(ont_id)

		elif ontology_status == 'orphaned':
			if validation_status == 'PASS':
				pass_orphaned.append(ont_id)
			elif validation_status == 'INFO':
				info_orphaned.append(ont_id)
			elif validation_status == 'WARN':
				warn_orphaned.append(ont_id)
			elif validation_status == 'FAIL':
				fail_orphaned.append(ont_id)

		elif ontology_status == 'inactive':
			if validation_status == 'PASS':
				pass_inactive.append(ont_id)
			elif validation_status == 'INFO':
				info_inactive.append(ont_id)
			elif validation_status == 'WARN':
				warn_inactive.append(ont_id)
			elif validation_status == 'FAIL':
				fail_inactive.append(ont_id)

	sort = sort_list(pass_foundry) + sort_list(info_foundry) \
	       + sort_list(warn_foundry) + sort_list(fail_foundry) \
	       + sort_list(pass_active) + sort_list(info_active) \
	       + sort_list(warn_active) + sort_list(fail_active) \
	       + sort_list(pass_orphaned) + sort_list(info_orphaned) \
	       + sort_list(warn_orphaned) + sort_list(fail_orphaned) \
	       + sort_list(pass_inactive) + sort_list(info_inactive) \
	       + sort_list(warn_inactive) + sort_list(fail_inactive)

	return sort

def sort_list(arr):
	"""Given an array, sort the list. If the list is empty, return an empty list 
	(instead of None)."""
	arr.sort(key=str.lower)
	if not arr:
		return []
	return arr

def get_schemas():
	"""Return a set of schemas from the master schema directory."""
	schemas = []
	for f in os.listdir(schema_dir):
		if '.json' not in f:
			continue
		try:
			file = '%s/%s' % (schema_dir, f)
			with open(file, 'r') as s:
				schema = json.load(s)
				schemas.append(schema)
		except Exception as e:
			print('Unable to load %s: %s' % (f, str(e)))
	return schemas

def validate_metadata(item, schemas):
	"""Given an item and a set of schemas, validate the item against the 
	schemas. Add the full results to the metadata_grid and return a map of 
	errors, warnings, and infos for any active ontologies."""
	global metadata_grid

	ont_id = item['id']

	# these lists will be displayed on the console
	errors = []
	warnings = []
	infos = []
	
	# results are put into the metadata grid
	results = {}

	# determine how to sort this item in the grid
	if 'in_foundry_order' in item and item['in_foundry_order'] == 1:
		results['foundry'] = True
	else:
		results['foundry'] = False

	if 'activity_status' in item:
		results['ontology_status'] = item['activity_status']
	else:
		# if there is no status, put them at the bottom with inactive
		results['ontology_status'] = 'inactive'

	has_error = False
	has_warn = False
	has_info = False
	for s in schemas:
		title = s['title']
		try:
			jsonschema.validate(item, s)
			results[title] = 'pass'
		except jsonschema.exceptions.ValidationError as ve:
			level = s['level']

			# add to the results map
			results[title] = level

			# flag for errors, warnings, and infos
			# without adding results to the lists that are logged
			if level == 'error':
				has_error = True
			elif level == 'warning':
				has_warn = True
			elif level == 'info':
				has_info = True

			# these cases will not cause test failure and will not be logged
			# the results are just added to the metadata grid:
			# - orphaned ontology on contact or license chekck
			# - inactive ontology
			# - obsolete ontology
			# - ontology annotated with `validate: false`
			if (('activity_status' in item \
			    and item['activity_status'] == 'orphaned') \
			and (title == 'contact' or title == 'license')) \
			and ('is_obsolete' in item and item['is_obsolete'] is True) \
			or ('activity_status' in item \
				and item['activity_status'] == 'inactive') \
			or ('validate' in item and item['validate'] is False):
				continue

			# get a message for displaying on terminal
			msg = ve.message
			if title == 'license':
				# license error message can show up in a few different ways
				search = re.search('\'(.+?)\' is not one of', msg)
				if search:
					msg = '\'%s\' is not a recommended license' % search.group(1)
				search = re.search('({\'label\'.+?\'url\'.+?}) is not valid', msg)
				if search:
					format_license_msg(search.group(1))
				search = re.search('({\'url\'.+?\'label\'.+?}) is not valid', msg)
				if search:
					format_license_msg(search.group(1))

			# format the message with the ontology ID
			msg = '%s %s: %s' % (ont_id.upper(), title, msg)

			# append to correct set of warnings
			if level == 'error':
				errors.append(msg)
			elif level == 'warning':
				# warnings are recommended fixes, not required
				if 'required' in msg:
					msg = msg.replace('required', 'recommended')
				warnings.append(msg)
			elif level == 'info':
				infos.append(msg)

	# add an overall validation status to the grid entry
	if has_error:
		results['validation_status'] = 'FAIL'
	elif has_warn:
		results['validation_status'] = 'WARN'
	elif has_info:
		results['validation_status'] = 'INFO'
	else:
		results['validation_status'] = 'PASS'
	metadata_grid[ont_id] = results

	return {'error': errors, 'warn': warnings, 'info': infos}

def format_license_msg(substr):
	"""Format an exception message for a license issue."""
	# process to dict
	d = json.loads(substr.replace('\'', '"'))
	url = d['url']
	label = d['label']
	return '\'{0}\' <{1}> is not a recommended license'.format(label, url)

def load_data(data_file):
	"""Load the data to validate."""
	# read the JSON-LD data
	with open(data_file) as f:
		data = json.load(f)
	return data

# run the process!
if __name__ == '__main__':
	validate(sys.argv)
