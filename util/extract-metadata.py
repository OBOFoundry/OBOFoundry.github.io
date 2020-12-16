#!/usr/bin/env python3

import argparse
import sys
from yamllint import config, linter
import yaml
import frontmatter

__author__ = 'cjm'


def main():
  parser = argparse.ArgumentParser(description='Helper utils for OBO',
                                   formatter_class=argparse.RawTextHelpFormatter)

  subparsers = parser.add_subparsers(dest='subcommand', help='sub-command help')

  # SUBCOMMAND
  parser_n = subparsers.add_parser('validate', help='validate yaml inside md')
  # parser_n.add_argument('-d', '--depth', type=int, help='number of hops')
  parser_n.set_defaults(function=validate_markdown)
  parser_n.add_argument('files', nargs='*')
  parser_n = subparsers.add_parser('prettify', help = 'prettify YAML block in registry ontolgoy Markdown files')
  parser_n.set_defaults(function=prettify)
  parser_n.add_argument('files', nargs='*')
  # SUBCOMMAND
  parser_n = subparsers.add_parser('concat', help='concat ontology yamls')
  parser_n.add_argument('-i', '--include', help='yaml file to include for header')
  parser_n.add_argument('-o', '--output', help='output yaml file')
  parser_n.set_defaults(function=concat_ont_yaml)
  parser_n.add_argument('files', nargs='*')

  # SUBCOMMAND
  parser_n = subparsers.add_parser('concat-principles', help='concat principles yamls')
  parser_n.add_argument('-i', '--include', help='yaml file to include for header')
  parser_n.add_argument('-o', '--output', help='output yaml')
  parser_n.set_defaults(function=concat_principles_yaml)
  parser_n.add_argument('files', nargs='*')

  args = parser.parse_args()

  func = args.function
  func(args)

class MyDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)

def prettify(args):
   for file in args.files:
       text = frontmatter.load(file)
       text.content = text.content + "\n"
       file_obj = open(file, "wb")
       frontmatter.dump(text, fd = file_obj, sort_keys=False, indent=2, Dumper=MyDumper)
       file_obj.close()
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
  def validate_structure(obj):
    """
    Given an object, check to see if it has 'id', 'title', and 'layout' fields. If any are
    missing, collect them in a list of errors which is then returned.
    """
    errs = []
    id = obj.get('id') or ''
    if not id:
      errs.append("No id: ")
    if 'title' not in obj:
      errs.append("No title: " + id)
    if 'layout' not in obj:
      errs.append("No layout tag: " + id + " -- this is required for proper rendering")
    # is_obsolete = ('is_obsolete' in obj)
    # if 'description' not in obj:
    #   errs.append("No description: " + id + " " + ("OBS" if is_obsolete else ""))
    return errs

  errs = []
  for fn in args.files:
    # we don't do anything with the results; an
    # error is thrown
    (obj, md) = load_md(fn)
    errs += validate_structure(obj)
  if len(errs) > 0:
    print("FAILURES:", file=sys.stderr)
    for e in errs:
      print("ERROR:" + e, file=sys.stderr)
    sys.exit(1)


def concat_ont_yaml(args):
  """
  Given arguments with files and ouput,
  read YAML files into an array, decorate the objects, and write an output YAML file.
  Output will be Foundry ontologies first, Library ontologies second, and obsolete last.
  Assumes that args.files is already sorted alphabetically.
  """
  def has_obo_prefix(obj):
    """
    Check to see if the given object's 'uri_prefix' (if present) maps to the OBO PURL
    """
    return ('uri_prefix' not in obj) or (obj['uri_prefix'] == 'http://purl.obolibrary.org/obo/')

  def has_a_product(obj):
    """
    Check to see if the given object has at least one product.
    """
    return 'products' in obj and len(obj['products']) > 0

  def decorate_entry(obj, suffix=""):
    """
    Decorates EITHER an ontology metadata object OR a product object with a purl.

    Each object has an identifier which either identifies the ontology sensu grouping
    project (e.g. 'go') or a specific product (e.g. 'go.obo' or 'go.owl').

    By default each id is prefixed with the OBO prefix (unless is has an alternate prefix,
    in which case it is effectively ignored).
    """
    id = obj.get('id') or 'None'
    if 'is_obsolete' not in obj and has_obo_prefix(obj):
      obj['ontology_purl'] = "http://purl.obolibrary.org/obo/" + id + suffix

  def decorate_metadata(objs):
    """
    Add the logo corresponding to the given object's license (if it has one), and decorate
    it with PURLs it has any products.
    See: https://github.com/OBOFoundry/OBOFoundry.github.io/issues/82
    """
    # TODO: decide on canonical URI to use for CC licenses;
    #  ultimately this should all be specified in RDF/JSON-LD.
    #  e.g. <http://creativecommons.org/licenses/by/3.0> foaf:depictedBy < ... > .
    #  e.g. <http://creativecommons.org/licenses/by/3.0> owl:sameAs <https://creativecommons.org/licenses/by/3.0> .
    for obj in objs:
      if 'license' in obj:
        # https://creativecommons.org/about/downloads
        license = obj['license']
        lurl = license['url']
        logo = ''
        if lurl.find('creativecommons.org/licenses/by-sa') > 0:
          logo = 'https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png'
        elif lurl.find('creativecommons.org/licenses/by/') > 0:
          logo = 'http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png'
        elif lurl.find('creativecommons.org/publicdomain/zero/') > 0:
          logo = 'http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png'
        if logo:
          license['logo'] = logo
      if has_a_product(obj):
        # decorate top-level ontology; but only if it has at least one product
        decorate_entry(obj, ".owl")
        for product in obj['products']:
          decorate_entry(product)

  objs = []
  foundry = []
  library = []
  obsolete = []
  cfg = {}
  if (args.include):
    with open(args.include, 'r') as f:
      cfg = yaml.load(f.read(), Loader=yaml.SafeLoader)
  for fn in args.files:
    (obj, md) = load_md(fn)
    if obj.get('is_obsolete'):
      obsolete.append(obj)
    elif 'in_foundry_order' in obj:
      foundry.append(obj)
    else:
      library.append(obj)
  objs = foundry + library + obsolete
  cfg['ontologies'] = objs
  decorate_metadata(objs)
  with open(args.output, 'w') as f:
    f.write(yaml.dump(cfg))
  return cfg


def concat_principles_yaml(args):
  """
  Concatenate all of the principles .md files given in the command line arguments and
  add them to the 'principles' field of the YAML object that is returned. If the
  --include command line option has been specified, then the YAML will include information
  from that file.
  """
  objs = []
  cfg = {}
  if (args.include):
    with open(args.include, 'r') as f:
      cfg = yaml.load(f.read(), Loader=yaml.SafeLoader)
  for fn in args.files:
    (obj, md) = load_md(fn)
    objs.append(obj)
  objs.sort(key=lambda x: x['id'])
  cfg['principles'] = objs
  with open(args.output, 'w') as f:
    f.write(yaml.dump(cfg))
  return cfg


def load_md(fn):
  """
  Load a yaml text blob from a markdown file and parse the blob.

  Returns a tuple (yaml_obj, markdown_text)
  """
  print(fn)
  with open(fn, 'r') as f:
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
        n = n + 1
    elif n == 1:
        ylines.append(line)
    else:
        mlines.append(line)
  yamltext = "\n".join(ylines)
  yaml_config = config.YamlLintConfig(file = "util/config.yamllint")
  for p in linter.run("---\n" + yamltext, yaml_config):
       print(p)
  obj = yaml.load(yamltext, Loader=yaml.SafeLoader)
  return (obj, "\n".join(mlines))


if __name__ == "__main__":
  main()
