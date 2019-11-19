#!/usr/bin/env python3

import csv
import sys
import yaml

from argparse import ArgumentParser


def main(args):
    """Usage: ./sort_tables.py <dashboard_csv>
                               <big_dashboard_csv>
                               <ontologies_yml>
                               <output_csv>

    Combine the regular and "big" dashboard result CSVs in registry order.
    """
    global headers

    # parse input args
    parser = ArgumentParser(description='Create a dashboard file')
    parser.add_argument('dashboard',
                        type=str,
                        help='Dashboard CSV')
    parser.add_argument('big_dashboard',
                        type=str,
                        help='Big dashboard CSV')
    parser.add_argument('ontologies_yml',
                        type=str,
                        help='YAML file with registry data')
    parser.add_argument('output',
                        type=str,
                        help='Sorted output CSV')
    args = parser.parse_args()

    dashboard_csv = args.dashboard
    big_dashboard_csv = args.big_dashboard
    ontologies_yml = args.ontologies_yml
    output_csv = args.output

    registry_order = get_registry_order(ontologies_yml)
    dashboard_map = get_csv_map(dashboard_csv, big_dashboard_csv)

    with open(output_csv, 'w') as f:
        writer = csv.writer(f,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        writer.writerow(headers)
        for ns in registry_order:
            if ns not in dashboard_map:
                continue
            writer.writerow(dashboard_map[ns])


def get_registry_order(ontologies_yml):
    """Get an ordered list of ontology namespaces from the registry data.

    Args:
        ontologies_yml: path to YAML file containing registry data

    Return:
        registry-orderd list of ontology namespaces
    """
    with open(ontologies_yml, 'r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    ordered = []
    for item in data['ontologies']:
        ordered.append(item['id'])
    return ordered


def get_csv_map(csv_file, big_csv_file):
    """Create a CSV map of ontology NS to dashboard results row from both the
    regular and the "big" dashboard.

    Args:
        csv_file: path to dashboard CSV
        big_csv_file: path to big dashboard CSV

    Return:
        map of ontology NS to results row
    """
    global headers

    csv_map = {}
    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        # skip headers
        headers = next(reader)
        for row in reader:
            ns = row[0]
            csv_map[ns] = row
    with open(big_csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        # skip headers
        next(reader)
        for row in reader:
            ns = row[0]
            csv_map[ns] = row
    return csv_map


if __name__ == '__main__':
    main(sys.argv)
