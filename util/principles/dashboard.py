#!/usr/bin/env python3

import gc
import json
import os
import sys
import yaml

import dash_utils
import fp_001
import fp_002
import fp_003
import fp_004
import fp_005
import fp_006
import fp_007
import fp_008
import fp_009
import fp_011
import fp_012
import fp_016
import report_utils

from argparse import ArgumentParser
from py4j.java_gateway import JavaGateway

big_onts = ['chebi', 'bto', 'uberon', 'ncbitaxon', 'pr', 'ncit', 'gaz']
foundry = ['bfo', 'doid', 'go', 'obi', 'pato', 'po', 'xao', 'zfa']


def main(args):
    global domain_map, \
           gateway, \
           io_helper, \
           robot_gateway, \
           ro_props

    # parse input args
    parser = ArgumentParser(description='Create a dashboard file')
    parser.add_argument('yaml_infile',
                        type=str,
                        help='YAML file with registry data')
    parser.add_argument('outfile',
                        type=str,
                        help='CSV output file to write dashboard data')
    args = parser.parse_args()

    # globals
    gateway = JavaGateway()
    robot_gateway = gateway.jvm.org.obolibrary.robot
    io_helper = robot_gateway.IOHelper()

    # IO files
    yaml_infile = args.yaml_infile
    outfile = args.outfile
    ont_data = load_data(yaml_infile)
    data_map = sort_data(ont_data)

    # domains for scope check
    domain_map = get_domains(ont_data)

    # RO properties for relations check
    print('Retrieving RO properties')
    ro = load_ontology_from_iri('http://purl.obolibrary.org/obo/ro.owl')
    ro_merged = robot_gateway.MergeOperation.merge(ro)
    ro_props = fp_007.get_properties('ro', ro)

    del ro
    del ro_merged

    # Run checks and save to file
    dashboard_map = {}
    for ns, data in data_map.items():
        if ns in big_onts:
            continue
            if 'is_obsolete' in data and data['is_obsolete'] is 'true':
                continue
            try:
                dashboard_map[ns] = big_check_principles(ns, data)
            except Exception as e:
                # delete any partial entry if it exists
                if ns in dashboard_map:
                    del dashboard_map[ns]
                print(
                    'ERROR - Unable to run principle check on {0}\
\nCAUSE:\n'.format(ns, str(e)))
        else:
            if 'is_obsolete' in data and data['is_obsolete'] is 'true':
                continue
            try:
                dashboard_map[ns] = check_principles(ns, data)
            except Exception as e:
                # delete any partial entry if it exists
                if ns in dashboard_map:
                    del dashboard_map[ns]
                print(
                    'ERROR - Unable to run principle check on {0}\
\nCAUSE:\n'.format(ns, str(e)))
    save_dashboard(dashboard_map, outfile)

    # clean up
    gc.collect()


def check_principles(ns, data):
    '''Given an ontology ID and the corresponding data from the YAML,
    run the automated principle validation. Return a map of results.'''
    print('Checking ' + ns)
    ont_file = fetch_base_ontology(ns)
    ont = load_ontology_from_file(ont_file)

    print('Running ROBOT report on %s...' % ns)
    report = report_utils.run_report(robot_gateway, io_helper, ns, ont)

    file = 'build/%s.owl' % ns

    check_map = {}
    check_map[1] = fp_001.is_open(ont, data)
    check_map[2] = fp_002.is_common_format(ont)
    check_map[3] = fp_003.has_valid_uris(robot_gateway, ns, ont)
    check_map[4] = fp_004.has_versioning(ont)
    check_map[5] = fp_005.has_scope(data, domain_map)
    check_map[6] = fp_006.has_valid_definitions(report)
    check_map[7] = fp_007.has_valid_relations(ns, ont, ro_props)
    check_map[8] = fp_008.has_documentation(data)
    check_map[9] = fp_009.has_users(data)
    # FP 10 cannot be automatically validated
    check_map[11] = fp_011.has_contact(data)
    check_map[12] = fp_012.has_valid_labels(report)
    check_map[16] = fp_016.is_maintained(ont)

    # add the report results to the dashboard
    check_map['report'] = report_utils.process_report(
        robot_gateway, ns, report)

    # remove from memory
    del report
    del ont

    return check_map


def big_check_principles(ns, data):
    '''Given an ontology ID and the corresponding data from the YAML,
    run the automated principle validation. Return a map of results.'''
    print('Checking ' + ns)
    file = download_ontology(ns)

    print('Running ROBOT report on {0}...'.format(ns))
    report_obj = report_utils.BigReport(robot_gateway, ns, file)
    report = report_obj.get_report()
    good_format = report_obj.get_good_format()

    check_map = {}
    check_map[1] = fp_001.big_is_open(file, data)
    check_map[2] = fp_002.big_is_common_format(True)  # good_format
    check_map[3] = fp_003.big_has_valid_uris(ns, file)
    check_map[4] = fp_004.big_has_versioning(file)
    check_map[5] = fp_005.has_scope(data, domain_map)
    check_map[6] = fp_006.has_valid_definitions(report)
    check_map[7] = fp_007.big_has_valid_relations(ns, file, ro_props)
    check_map[8] = fp_008.has_documentation(data)
    check_map[9] = fp_009.has_users(data)
    # FP 10 cannot be automatically validated
    check_map[11] = fp_011.has_contact(data)
    check_map[12] = fp_012.has_valid_labels(report)
    check_map[16] = fp_016.big_is_maintained(file)

    # add the report results to the dashboard
    check_map['report'] = report_utils.process_report(
        robot_gateway, ns, report)

    # remove from memory
    del report
    # os.remove(file)

    return check_map


def save_dashboard(dashboard_map, outfile):
    '''Given a map of results and a CSV file to write to,
    format and write the validation results.'''
    with open(outfile, 'w') as f:
        # Headers
        f.write('ID,Open,Format,URIs,Versioning,')
        f.write('Scope,Definitions,Relations,Documentation,Users,')
        f.write('Authority,Naming,Maintenance,Report,Summary\n')
        for ns, check_map in dashboard_map.items():
            f.write(ns + ',')
            err = 0
            warn = 0
            info = 0
            for k, val in check_map.items():
                if val is None:
                    print('Missing value for check {0} on {1}'.format(k, ns))
                    continue
                if val.startswith('ERROR'):
                    err += 1
                elif val.startswith('WARN'):
                    warn += 1
                elif val.startswith('INFO'):
                    info += 1
                f.write(str(val) + ',')
            # Summary status
            if err > 0:
                f.write('ERROR|%d errors' % err)
            elif warn > 0:
                f.write('WARN|%d warnings' % warn)
            elif info > 0:
                f.write('INFO|%d info messages' % info)
            else:
                f.write('PASS')
            f.write('\n')


def load_data(yaml_infile):
    '''Given the registry YAML file, load the data.
    Return a map of ontology ID to data item.'''
    with open(yaml_infile, 'r') as s:
        data = yaml.load(s, Loader=yaml.SafeLoader)
    return data['ontologies']


def sort_data(ont_data):
    '''Given the ontology data from the registry YAML file,
    sort by ontology ID. Return a map of ont ID to data item.'''
    data_map = {}
    for item in ont_data:
        ont_id = item['id']
        data_map[ont_id] = item
    return data_map


def get_domains(ont_data):
    '''Given the ontology data fro the registry YAML file,
    map the ontology ID to the scope (domain).'''
    domain_map = {}
    for item in ont_data:
        ont_id = item['id']
        if 'domain' in item:
            domain_map[ont_id] = item['domain']
    return domain_map


def fetch_base_ontology(ns):
    """
    """
    # circumstances where NS isn't totally upper
    # we probably won't try to get base for large ontologies right now
    if ns == 'ncbitaxon':
        ns = 'NCBITaxon'
    elif ns == 'fbdv':
        ns = 'FBdv'
    elif ns == 'mirnao':
        ns = 'miRNAO'
    elif ns == 'vario':
        ns = 'VariO'
    elif ns == 'wbbt':
        ns = 'WBbt'
    elif ns == 'wbphenotype':
        ns = 'WBPhenotype'
    else:
        ns = ns.upper()

    # option args
    purl = 'http://purl.obolibrary.org/obo/{0}.owl'.format(ns.lower())
    base = 'http://purl.obolibrary.org/obo/{0}_'.format(ns)
    output = 'build/ontologies/{0}.owl'.format(ns.lower())

    if os.path.exists(output):
        return output

    # easier to do this via command line
    cmd = '''java -jar build/robot-foreign.jar merge --input-iri {0} \
             remove --base-iri {1} --axioms external \
             -p false --output {2}'''.format(purl, base, output)
    print(cmd)
    os.system(cmd)

    if not os.path.isfile(output):
        print('Unable to retrieve {0}'.format(ns))
        return None
    return output


def load_ontology_from_file(path):
    """
    """
    ont = None
    try:
        ont = io_helper.loadOntology(path)
    except Exception as e:
        print('Unable to load \'{0}\''.format(path))
        return None
    print('Loaded \'{0}\''.format(path))
    return ont


def load_ontology_from_iri(purl):
    '''Given a PURL, return an OWLOntology object.'''
    print('Retrieving <{0}>'.format(purl))
    iri = gateway.jvm.org.semanticweb.owlapi.model.IRI.create(purl)
    ont = None
    try:
        ont = io_helper.loadOntology(iri)
    except Exception as e:
        print('ERROR - Unable to load <{0}>'.format(purl))
        return None
    print('Loaded <{0}>'.format(purl))
    return ont


def download_ontology(ns):
    '''Given a PURL, download the ontology to a file in the build directory.'''

    purl = 'http://purl.obolibrary.org/obo/%s.owl' % ns.lower()
    file = 'build/%s.owl' % ns
    if not os.path.isfile(file):
        print('Downloading <{0}>'.format(purl))
        curl = 'curl -Lk {0} > {1}'.format(purl, file)
        os.system(curl)
    if not os.path.isfile(file):
        print('ERROR - Unable to download {0}'.format(ns))
        return None
    return file


if __name__ == '__main__':
    main(sys.argv)
