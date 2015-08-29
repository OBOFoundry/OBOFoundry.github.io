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

    # SUBCOMMAND
    parser_n = subparsers.add_parser('concat-people', help='concat people yamls')
    parser_n.add_argument('-i', '--include', help='yml file to include for header')
    parser_n.add_argument('-o', '--output', help='output yaml')
    parser_n.set_defaults(function=concat_people_yaml)
    parser_n.add_argument('files',nargs='*')

    args = parser.parse_args()

    func = args.function
    func(args)


def validate_markdown(args):
    """
    ensure the yaml encoded inside a YAML file is syntactically valid
    """
    for fn in args.files:
        print("VALIDATING:"+fn)
        # we don't do anything with the results; an
        # error is thrown 
        load_md(fn)
        print("OK:"+fn)

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
        decorate_entry(obj, ".owl")
        if ('products' in obj):
            for product in obj['products']:
                decorate_entry(product)

def decorate_entry(obj, suffix=""):
    """
    Decorates either an ontology metadata object or a product object with a purl.
    
    Each object has an identifier which either identifies the ontology sensu grouping
    project (e.g. 'go') or a specific product (e.g. 'go.obo' or 'go.owl').

    By default each id is prefixed with the OBO prefix (unless is has an alternate prefix,
    in which case it is effectively ignored).
    """
    id = obj['id']
    if (not('uri_prefix' in obj) and not('is_obsolete' in obj)):
        obj['ontology_purl'] = "http://purl.obolibrary.org/obo/" + id + suffix

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


def concat_people_yaml(args):
    objs = []
    cfg = {}
    if (args.include):
        f = open(args.include, 'r') 
        cfg = yaml.load(f.read())
    for fn in args.files:
        (obj, md) = load_md(fn)
        objs.append(obj)
    cfg['people'] = objs
    f = open(args.output, 'w') 
    f.write(yaml.dump(cfg))
    return cfg



def load_md(fn):
    f = open(fn, 'r') 
    text = f.read() 
    return extract(text)
    

def extract(mdtext):
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

    
    
