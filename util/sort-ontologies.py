#!/usr/bin/env python3

import csv, sys, yaml

def main(args):
	'''Usage: sort-ontologies.py <unsorted-yaml> <metdata-grid> <output-yaml>'''
	data_file = args[1]
	grid = args[2]
	output = args[3]

	sort_order = get_sort_order(grid)
	data = load_data(data_file)
	data = sort_ontologies(data, sort_order)
	write_data(data, output)

def get_sort_order(grid):
	'''Given the path to the metadata grid (CSV or TSV), extract the order of 
	ontologies from the grid. Return the list of ontology IDs in that order.'''
	sort_order = []
	if '.csv' in grid:
		separator = ','
	elif '.tsv' or '.txt' in grid:
		separator = '\t'
	else:
		print('%s must be tab- or comma-separated.')
		sys.exit(1)
	with open(grid, 'r') as f:
		reader = csv.reader(f, delimiter=separator)
		next(reader)
		for row in reader:
			sort_order.append(row[0])
	return sort_order

def load_data(data_file):
	'''Given a YAML file, load the data into a dictionary.'''
	stream = open(data_file, 'r')
	data = yaml.load(stream)
	return data

def sort_ontologies(data, sort_order):
	'''Given the ontologies data as a dictionary and the list of ontologies in 
	proper sort order, return the sorted data.'''
	mapped = {}
	for item in data['ontologies']:
		ont_id = item['id']
		mapped[ont_id] = item
	ontologies = []
	for ont_id in sort_order:
		ontologies.append(mapped[ont_id])
	data['ontologies'] = ontologies
	return data

def write_data(data, output):
	'''Given the ontologies data as a dictionary and an output YAML file to 
	write to, write the data to the file. '''
	yaml_str = yaml.dump(data)
	with open(output, 'w') as f:
		f.write(yaml_str)

if __name__ == '__main__':
	main(sys.argv)
