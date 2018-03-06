#!/usr/bin/env python3

__author__ = 'cjm'

import argparse
import logging
import requests
import sys
import os
from contextlib import closing
from SPARQLWrapper import SPARQLWrapper, JSON
from json import dumps

#from yaml import load, dump
#from yaml import Loader, Dumper
import yaml



def main():

    parser = argparse.ArgumentParser(description='OBO'
                                                 'Helper utils for OBO',
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-i', '--input', type=str, required=False,
                        help='Input metadata file')


    subparsers = parser.add_subparsers(dest='subcommand', help='sub-command help')
    
    # SUBCOMMAND
    parser_n = subparsers.add_parser('check-urls', help='Checks URLs')
    parser_n.set_defaults(function=check_urls)
    #parser_n.add_argument('files',nargs='*')

    parser_n = subparsers.add_parser('sparql-compare', help='Checks URLs')
    parser_n.set_defaults(function=sparql_compare_all)

    parser_n = subparsers.add_parser('extract-context', help='Extracts JSON-LD context')
    parser_n.set_defaults(function=extract_context)

    args = parser.parse_args()

    #print("Loading "+args.input)
    f = open(args.input, 'r') 
    obj = yaml.load(f)
    ontologies = obj['ontologies']
    #print(len(ontologies))
    
    func = args.function
    func(ontologies, args)

def test_url(url):
    print("Checking: "+url)
    if (url.startswith("ftp:")):
        # TODO: requests lib doesn't handle ftp
        return True
    with closing(requests.get(url, stream=False)) as resp:
        print("  Got response for: "+url)
        # TODO: redirects
        ok = resp.status_code == 200
        print("IS_OK " + url  + " "+str(ok))
    sys.stdout.flush()
    return ok

def check_urls(ontologies, args):
    """
    ensure PURLs resolve
    """
    print(len(ontologies))
    failed_ids = []
    for ont in ontologies:
        id = ont['id']
        print("Checking:"+id)
        if 'products' in ont:
            for p in ont['products']:
                pid = p['id']
                if 'ontology_purl' in p:
                    if not test_url(p['ontology_purl']):
                        failed_ids.append(pid)
    if (len(failed_ids) > 0):
        print("FAILURES:")
        for pid in failed_ids:
            print(pid)
        exit(1)
    else:
        print("SUCCESS")


def mirror(ontologies, args):
    """
    Mirror all PURLs locally
    """
    for ont in ontologies:
        id = ont['id']
        if 'is_obsolete' in ont:
            print("SKIPPING OBSOLETE: "+id)
            continue
        for p in ont['products']:
            pid = p['id']
            url = get_obo_purl(pid)
            # we use -r to force directory structure mirroring
            if url.startswith("ftp"):
                print("Cannot check FTP: "+url)
                continue
            status = os.system("wget -r "+url)
            if (status):
                print("FAILED: "+url)


def get_obo_purl(fragment):
    """
    Add the magic prefix
    """
    return "http://purl.obolibrary.org/obo/"+fragment

def build_from_source(obj):
    """
    NOT IMPLEMENTED - use perl for now

    Given a metadata object describing a build/clone process,
    build the ontology.
    Replaces build-obo-ontologies.pl in owltools
    """
    if (obj.method == 'robot'):
        print("TODO: build obo and owl")
    elif (obj.method == 'jenkins-archive'):
        print("TODO: download and unzip")
    elif (obj.method == 'github-archive'):
        print("TODO: download and unzip")
    elif (obj.method == 'svn-co'):
        print("TODO: run svn")
    else:
        print("UNKNOWN METHOD:"+obj.method)

def extract_context(ontologies, args):
    prefix_map = {}
    for obj in ontologies:
        id = obj['id']
        if not('is_obsolete' in obj):
            if has_obo_prefix(obj):
                prefix = id.upper()
                if 'preferredPrefix' in obj:
                    prefix = obj['preferredPrefix']
                #if prefix in prefix_map:
                #    print("ERROR: prefix present twice:"+prefix)
                #    exit(1)
                prefix_map[prefix] = "http://purl.obolibrary.org/obo/" + prefix + "_"
    ctxt = {}
    ctxt['@context'] = prefix_map
    print(dumps(ctxt, sort_keys=True, indent=4, separators=(',', ': ')))

            

# TODO: put this in common lib        
def has_obo_prefix(obj):
    return ('uri_prefix' not in obj) or (obj['uri_prefix'] == 'http://purl.obolibrary.org/obo/')

def sparql_compare_all(ontologies, args):
    for obj in ontologies:
        sparql_compare_ont(obj)

def sparql_compare_ont(obj):
    """
    Some ontologies will directly declare some subset of the OBO metadata
    directly in the ontology header. In the majority of cases we should
    yield to the provider. However, we reserve the right to override. For
    example, OBO may have particular guidelines about the length of the title,
    required for coherency within the registry. All differences should be
    discussed with the provider and an accomodation reached
    """
    if not 'ontology_purl' in obj:
        return
    purl = obj['ontology_purl']
    id = obj['id']
    # this could be made more declarative, or driven by the context.jsonld mapping;
    # however, for now this is relatively simple and easy to understand:
    license = obj['license']['url'] if 'license' in obj else ''
    run_sparql(obj, 'license', license, "SELECT DISTINCT ?license WHERE {<"+purl+"> <http://purl.org/dc/elements/1.1/license> ?license}")
    run_sparql(obj, 'title', obj['title'] if 'title' in obj else '', "SELECT DISTINCT ?title WHERE {<"+purl+"> <http://purl.org/dc/elements/1.1/title> ?title}")
    run_sparql(obj, 'description', obj['description'] if 'description' in obj else '', "SELECT DISTINCT ?description WHERE {<"+purl+"> <http://purl.org/dc/elements/1.1/description> ?description}")
    run_sparql(obj, 'homepage', obj['homepage'] if 'homepage' in obj else '', "SELECT DISTINCT ?homepage WHERE {<"+purl+"> <http://xmlns.com/foaf/0.1/homepage> ?homepage}")

def run_sparql(obj, p, expected_value, q):
    sparql = SPARQLWrapper("http://sparql.hegroup.org/sparql")
    sparql.setQuery(q)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    id = obj['id']
    got_value = False
    is_match = False
    vs = []

    for result in results["results"]["bindings"]:
        got_value = True
        v = result[p]["value"]
        vs.append(str(v))
        if v == expected_value:
            is_match = True
    msg = ''
    if got_value and is_match:
        msg = 'CONSISTENT'
    elif got_value and not is_match:
        if expected_value == '':
            msg = 'UNDECLARED_LOCAL: REMOTE:' + ",".join(vs)
        else:
            msg = 'INCONSISTENT: REMOTE:' + ",".join(vs)+" != LOCAL:"+expected_value
    else:
        msg = 'UNDECLARED_REMOTE'
    print(id + " " + p + " " + msg)

            

        

if __name__ == "__main__":
    main()

    
    
