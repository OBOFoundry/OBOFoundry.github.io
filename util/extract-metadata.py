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

    parser.add_argument('-u', '--url', type=str, required=False,
                        help='A base URL for SciGraph')
    parser.add_argument('-t', '--to', type=str, required=False,
                        help='Renderer')


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
    parser_n.set_defaults(function=concat_yaml)
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

def concat_yaml(args):
    objs = []
    cfg = {}
    if (args.include):
        f = open(args.include, 'r') 
        cfg = yaml.load(f.read())
    for fn in args.files:
        (obj, md) = load_md(fn)
        objs.append(obj)
    cfg['ontologies'] = objs
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
        if (line.startswith("---")):
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

    
    
