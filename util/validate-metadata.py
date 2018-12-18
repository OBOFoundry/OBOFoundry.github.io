#!/usr/bin/env python3

import ast
import sys
import json
import jsonschema
import re

# file paths
data_file = "registry/ontologies.jsonld"
schema_file = "util/metadata-schema.json"
schema_lite_file = "util/metadata-schema-lite.json"
report_file = "reports/metadata-violations.csv"

# ultra-escaped regex strings
email_sub = 'does not match \'\\^\\[\\^@\\]\\+\\$\''
fmt_sub = ('does not match \'\\^\\[0\\-9A\\-Za\\-z\\-_\\\\\\\\/\\]\\+'
          '\\\\\\\\.\\(owl\\|obo\\|json\\|omn\\|ofn\\|owx\\|ttl\\|owl'
          '\\\\\\\\.gz\\)\\$\'')

def validate():
	"""
	Validate registry metadata.
	"""
	print("--- validating metadata against {0} ---".format(schema_file))
	data = load_data()
	schema = load_schema()
	# validate each object
	errors = {}
	for item in data["ontologies"]:
		if 'is_obsolete' in item and item["is_obsolete"] is True:
			continue
		# skip any 'validate: false' ontologies
		if 'validate' in item and item["validate"] is False:
			continue
		ont_id = item["id"]
		try:
			jsonschema.validate(item, schema)
		except jsonschema.exceptions.ValidationError as ve:
			print("ERROR in {0}".format(ont_id))
			errors[ont_id] = format_msg(ve)
	if errors:
		write_errors(errors)
	else:
		print("SUCCESS - no errors found in metadata")
		sys.exit(0)

def format_msg(ve):
	"""
	Format exception message from jsonchema.validate(...).
	"""
	# replace u characters
	replace_u = re.sub('u\'', '\'', ve.message)
	# replace scary regex strings
	replace_email = re.sub(
		email_sub, 'is not valid for \'contact.label\'', replace_u)
	msg = re.sub(fmt_sub, 'is not valid for \'products.id\'', replace_email)

	# check if output is for license error
	is_license = re.search('({\'url\'.+?\'label\'.+?})', msg)
	if is_license:
		return format_license_msg(is_license.group(1))

	# check if output is for list error
	is_list = re.search('(\\[.+?\\]) is not of type \'string\'', msg)
	if is_list:
		return format_list_msg(is_list.group(1), ve)

	# otherwise return the message
	return msg

def format_license_msg(substr):
	"""
	Format an exception message for a license issue.
	"""
	# process to dict
	d = json.loads(substr.replace('\'', '"'))
	url = d['url']
	label = d['label']
	return '\'{0}\' <{1}> is not valid for \'license\''.format(label, url)

def format_list_msg(substr, ve):
	"""
	Format an exception for an unexpected list.
	"""
	l = json.loads(substr.replace('\'', '"'))
	# use the full message to find the violating property
	prop_find = re.search('On instance\\[(\'.+?\')\\]', str(ve))
	if prop_find:
		prop = prop_find.group(1)
		return '{0} expects one value, got {1}'.format(prop, len(l))
	else:
		return substr

def load_schema():
	"""
	Load the schema to validate against.
	"""
	# read the schema
	with open(schema_file) as f:
		schema = json.load(f)
	return schema

def load_data():
	"""
	Load the data to validate.
	"""
	# read the JSON-LD data
	with open(data_file) as f:
		data = json.load(f)
	return data

def write_errors(errors):
	"""
	Write validation errors to a user-friendly report.
	"""
	with open(report_file, 'w+') as f:
		f.write("ID,ERROR\n")
		for ont_id, msg in errors.items():
			f.write('"' + ont_id + '","' + msg + '"\n')
	print(
		"VALIDATION FAILED: {0} errors - see {1} for details".format(
			len(errors), report_file))
	sys.exit(1)

# run the process!
if __name__ == '__main__':
	validate()
