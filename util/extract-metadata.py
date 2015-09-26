#!/usr/bin/env python3

__author__ = 'cjm'

import argparse
import logging

#from yaml import load, dump
#from yaml import Loader, Dumper
import yaml

def main():

    parser = argparse.ArgumentParser(description='OBO'
                                                 'Helper utils for OBO',
                                     formatter_class=argparse.RawTextHelpFormatter)


    subparsers = parser.add_subparsers(dest='subcommand', help='sub-command help')
    
    # SUBCOMMAND
    parser_n = subparsers.add_parser('validate', help='validate yml inside md')
    ##parser_n.add_argument('-d', '--depth', type=int, help='number of hops')
    parser_n.set_defaults(function=validate_markdown)
    parser_n.add_argument('files',nargs='*')

    # SUBCOMMAND
    parser_n = subparsers.add_parser('concat', help='concat ontology yamls')
    parser_n.add_argument('-i', '--include', help='yml file to include for header')
    parser_n.add_argument('-o', '--output', help='output yaml')
    parser_n.set_defaults(function=concat_ont_yaml)
    parser_n.add_argument('files',nargs='*')

    # SUBCOMMAND
    parser_n = subparsers.add_parser('concat-principles', help='concat principles yamls')
    parser_n.add_argument('-i', '--include', help='yml file to include for header')
    parser_n.add_argument('-o', '--output', help='output yaml')
    parser_n.set_defaults(function=concat_principles_yaml)
    parser_n.add_argument('files',nargs='*')

    args = parser.parse_args()

    func = args.function
    func(args)


def validate_markdown(args):
    """
    Ensure the yaml encoded inside a YAML file is syntactically valid.

    First attempt to strip the yaml from the .md file, second use the standard python yaml parser
    to parse the embedded yaml. If it can't be passed then an error will be thrown and a stack
    trace shown. In future we may try and catch this error and provide a user-friendly report).
    
    In future we also perform additional structural validation on the yaml - check certain fields
    are present etc. This could be done in various ways, e.g. jsonschema, programmatic checks. We
    should also check translation -> jsonld -> rdf works as expected.
    """
    errs = []
    for fn in args.files:
        print("VALIDATING:"+fn)
        # we don't do anything with the results; an
        # error is thrown 
        (obj, md) = load_md(fn)
        print("OK:"+fn)
        errs += validate_structure(obj,md)
    if len(errs) > 0:
        print("FAILURES:")
        for e in errs:
            print("ERROR:"+e)
        exit(1)

def validate_structure(obj,md):
    errs = []
    is_obs = False
    if 'id' not in obj:
        errs.append("No id: ")
    if 'is_obsolete' in obj:
        is_obs = True
    id = obj['id']
    if 'title' not in obj:
        errs.append("No title: "+id)
    #if 'description' not in obj:
    #    errs.append("No description: "+id+" " + ("OBS" if is_obs else ""))
    if 'layout' not in obj:
        errs.append("No layout tag: "+id+" -- this is required for proper rendering")
    return errs

def concat_ont_yaml(args):
    objs = []
    cfg = {}
    if (args.include):
        f = open(args.include, 'r') 
        cfg = yaml.load(f.read())
    for fn in args.files:
        (obj, md) = load_md(fn)
        objs.append(obj)
    cfg['ontologies'] = objs
    decorate_metadata(objs)
    f = open(args.output, 'w') 
    f.write(yaml.dump(cfg))
    return cfg

def decorate_metadata(objs):
    """
    See:
    https://github.com/OBOFoundry/OBOFoundry.github.io/issues/82
    """
    for obj in objs:
        if 'license' in obj:
            # https://creativecommons.org/about/downloads
            license = obj['license']
            lurl = license['url']
            logo = ''
            if lurl.startswith('http://creativecommons.org/licenses/by/'):
                logo = 'http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png'
            if lurl.startswith('http://creativecommons.org/publicdomain/zero/'):
                logo = 'http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png'
            if not logo == '':
                license['logo'] = logo
        if 'products' in obj:
            # decorate top-level ontology; but only if it has at least one product
            decorate_entry(obj, ".owl")
            for product in obj['products']:
                decorate_entry(product)

def decorate_entry(obj, suffix=""):
    """
    Decorates EITHER an ontology metadata object OR a product object with a purl.
    
    Each object has an identifier which either identifies the ontology sensu grouping
    project (e.g. 'go') or a specific product (e.g. 'go.obo' or 'go.owl').

    By default each id is prefixed with the OBO prefix (unless is has an alternate prefix,
    in which case it is effectively ignored).
    """
    id = obj['id']
    if not('is_obsolete' in obj):
        if has_obo_prefix(obj):
            obj['ontology_purl'] = "http://purl.obolibrary.org/obo/" + id + suffix


def has_obo_prefix(obj):
    return ('uri_prefix' not in obj) or (obj['uri_prefix'] == 'http://purl.obolibrary.org/obo/')

def has_a_product(obj):
    return 'products' in obj and len(obj['products']) > 0

def concat_principles_yaml(args):
    objs = []
    cfg = {}
    if (args.include):
        f = open(args.include, 'r') 
        cfg = yaml.load(f.read())
    for fn in args.files:
        (obj, md) = load_md(fn)
        objs.append(obj)
    cfg['principles'] = objs
    f = open(args.output, 'w') 
    f.write(yaml.dump(cfg))
    return cfg


def load_md(fn):
    """
    Load a yaml text blob from a markdown file and parse the blob.

    Returns a tuple (yaml_obj, markdown_text)
    """
    f = open(fn, 'r') 
    text = f.read() 
    return extract(text)
    

def extract(mdtext):
    """
    Extract a yaml text blob from markdown text and parse the blob.

    Returns a tuple (yaml_obj, markdown_text)
    """
    lines = mdtext.split("\n")
    n = 0
    ylines = []
    mlines = []
    for line in lines:
        if (line == "---"):
            n=n+1
            hlines = []
        else:
            if (n == 1):
               ylines.append(line)
            else:
                mlines.append(line)
    yamltext = "\n".join(ylines)
    obj = yaml.load(yamltext)
    return (obj, "\n".join(mlines))

def write_legacy_metadata_objects(onts, stream):
    """
    write to the old ontologies.txt format
    """
    for ont in onts:
        write_legacy_metadata_object(ont, stream)

def write_legacy_metadata_object(ont, stream):
    """
    write to the old ontologies.txt format (single object) - TODO
    """
    write_pv('id', ont['id'], stream)
    write_pv('title', ont['title'], stream)
    write_pv('namespace', ont['id'].upper, stream)
    write_pv('foundry', ont['is_foundry'], stream)

def write_pv(k,v,s):
    s.write(p + "\t" + v)

if __name__ == "__main__":
    main()

    
    
