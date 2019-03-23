#!/usr/bin/env python3

import csv
import sys

from argparse import ArgumentParser


headers = []


def main(args):
  parser = ArgumentParser(description="Generate an HTML output of the metadata grid")
  parser.add_argument('input_grid', type=str, help='File containing the grid (CSV, TSV, or TXT)')
  parser.add_argument('html_grid', type=str, help='HTML file to write the output to')
  args = parser.parse_args()

  input_grid = args.input_grid
  html_grid = args.html_grid
  lines = get_html(parse_table(input_grid))

  with open(html_grid, 'w') as f:
    for line in lines:
      f.write(line + '\n')


def parse_table(input_grid):
  '''Given an input grid in TSV or CSV, get the data as a dictionary. Also set
  the headers for the HTML grid.'''
  global headers

  data = {}
  if '.tsv' in input_grid:
    delim = '\t'
  elif '.csv' in input_grid:
    delim = ','
  else:
    print("Invalid file format: %s" % input_grid, file=sys.stderr)
    sys.exit(1)
  reader = csv.reader(open(input_grid), delimiter=delim)
  headers = next(reader)
  for row in reader:
    ont_id = row.pop(0)
    fields = row
    data[ont_id] = fields
  return data


def get_html(data):
  '''Given the data from the grid, return an array of lines to generate an
  HTML table.'''
  global headers

  lines = []
  lines.append('<table>')
  lines.append('\t<tr>')
  for h in headers:
    lines.append('\t\t<td><b>%s</b></td>' % h)
  lines.append('\t</tr>')
  for ont, fields in data.items():
    lines.append('\t<tr>')
    bg_color = '#FFFFFF'
    lines.append('\t\t<td bgcolor="%s">%s</td>' % (bg_color, ont))
    for f in fields:
      if f == 'PASS':
        bg_color = '#97E595'
      elif f == 'info' or f == 'inactive':
        bg_color = '#DDDDDD'
      elif f == 'warning' or f == 'WARN':
        bg_color = '#F7F585'
      elif f == 'error' or f == 'FAIL':
        bg_color = '#F4A8A8'
      else:
        bg_color = '#FFFFFF'
      lines.append('\t\t<td bgcolor="%s">%s</td>' % (bg_color, f))
    lines.append('\t</tr>')
  lines.append('</table>')
  return lines


if __name__ == '__main__':
  main(sys.argv)
