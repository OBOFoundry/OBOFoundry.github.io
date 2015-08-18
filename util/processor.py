#!/usr/bin/env python3

__author__ = 'cjm'

import argparse
import logging
import requests
import sys
import os

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

    args = parser.parse_args()

    print("Loading "+args.input)
    f = open(args.input, 'r') 
    obj = yaml.load(f)
    ontologies = obj['ontologies']
    print(len(ontologies))

    func = args.function
    func(ontologies, args)


def check_urls(ontologies, args):
    """
    ensure PURLs resolve
    """
    print(len(ontologies))
    failed_ids = []
    for ont in ontologies:
        id = ont['id']
        print("Checking:"+id)
        # TODO: always check canonical purl?
        for p in ont['products']:
            pid = p['id']
            url = get_obo_purl(pid)
            print("Checking: "+url)
            resp = requests.get(url)
            # TODO: redirects
            ok = resp.status_code == 200
            print("IS_OK " + id + " " + pid  + " "+str(ok))
            sys.stdout.flush()
            if (not ok):
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
        for p in ont['products']:
            pid = p['id']
            url = get_obo_purl(pid)
            # we use -r to force directory structure mirroring
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

if __name__ == "__main__":
    main()

    
    
