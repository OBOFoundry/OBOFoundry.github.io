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
    parser_n.set_defaults(function=validate)
    parser_n.add_argument('files',nargs='*')


    args = parser.parse_args()

    func = args.function
    func(args)


    ##data = load(stream, Loader=Loader)


def validate(args):
    for fn in args.files:
        load_md(fn)

def load_md(fn):
    print("VALIDATING:"+fn)
    f = open(fn, 'r') 
    text = f.read() 
    (obj, md) = extract(text)
    ##print(str(obj))
    print("OK:"+fn)

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

if __name__ == "__main__":
    main()

    
    
