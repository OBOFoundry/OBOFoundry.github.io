#!/usr/bin/env python3

import ast, json, jsonschema, os, re, sys

# file paths
schema_dir = 'util/schema'

def validate(args):
	"""
	Validate registry metadata.
	"""
	data_file = args[1]
	output_file = args[2]
	data = load_data(data_file)
	schemas = get_schemas()
	# validate each object
	results = {'error': [], 'warn': [], 'info': []}
	for item in data["ontologies"]:
		if 'validate' in item and item['validate'] is False:
			continue
		if 'is_obsolete' in item and item["is_obsolete"] is True:
			continue
		if 'activity_status' in item and item['activity_status'] == 'inactive':
			continue
		add = validate_metadata(item, schemas)
		results = update_results(results, add)
	print_results(results)
	save_results(results, output_file)
	if results['error']:
		print('\nMetadata validation failed with %d errors - see %s for details'\
		      % (len(results['error']), output_file))
		sys.exit(1)
	else:
		print('\nMetadata validation passed - see %s for details' % output_file)
		sys.exit(0)

def update_results(results, add):
	""""""
	res_errors = results['error']
	res_warns = results['warn']
	res_infos = results['info']
	results['error'] = res_errors + add['error']
	results['warn'] = res_warns + add['warn']
	results['info'] = res_infos + add['info']
	return results

def print_results(results):
	""""""
	for level, messages in results.items():
		for m in messages:
			print('%s\t%s' % (level.upper(), m))

def save_results(results, output_file):
	""""""
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

def get_schemas():
	"""
	"""
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
	"""
	"""
	# these lists will be displayed on the console
	errors = []
	warnings = []
	infos = []
	ont_id = item['id']
	for s in schemas:
		title = s['title']
		if 'activity_status' in item and item['activity_status'] == 'orphaned':
			if title == 'contact' or title == 'license':
				continue
		try:
			jsonschema.validate(item, s)
		except jsonschema.exceptions.ValidationError as ve:
			level = s['level']
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

	return {'error': errors, 'warn': warnings, 'info': infos}

def format_license_msg(substr):
	"""
	Format an exception message for a license issue.
	"""
	# process to dict
	d = json.loads(substr.replace('\'', '"'))
	url = d['url']
	label = d['label']
	return '\'{0}\' <{1}> is not a recommended license'.format(label, url)

def load_data(data_file):
	"""
	Load the data to validate.
	"""
	# read the JSON-LD data
	with open(data_file) as f:
		data = json.load(f)
	return data

# run the process!
if __name__ == '__main__':
	validate(sys.argv)
