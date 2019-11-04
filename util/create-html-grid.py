#!/usr/bin/env python3

import csv
import sys

from argparse import ArgumentParser

jquery = 'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.js'
bootstrap_css = 'https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css'
bootstrap_js = 'https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js'

headers = []
# Map of principle names to links for Dashboard
host = 'http://obofoundry.org/'
principle_map = {"Open":
                 "{0}/principles/fp-001-open.html".format(host),
                 "Format":
                 "{0}/principles/fp-002-format.html".format(host),
                 "URIs":
                 "{0}/principles/fp-003-uris.html".format(host),
                 "Versioning":
                 "{0}/principles/fp-004-versioning.html".format(host),
                 "Scope":
                 "{0}/principles/fp-005-delineated-content.html".format(host),
                 "Definitions":
                 "{0}/principles/fp-006-textual-definitions.html".format(host),
                 "Relations":
                 "{0}/principles/fp-007-relations.html".format(host),
                 "Documentation":
                 "{0}/principles/fp-008-documented.html".format(host),
                 "Users":
                 "{0}/principles/fp-009-users.html".format(host),
                 "Collaboration":
                 "{0}/principles/fp-010-collaboration.html".format(host),
                 "Authority":
                 "{0}/principles/fp-011-locus-of-authority.html".format(host),
                 "Naming":
                 "{0}/principles/fp-012-naming-conventions.html".format(host),
                 "Maintenance":
                 "{0}/principles/fp-016-maintenance.html".format(host)}


def main(args):
    parser = ArgumentParser(
        description="Generate an HTML output of the metadata grid")
    parser.add_argument('input_grid',
                        type=str,
                        help='File containing the grid (CSV, TSV, or TXT)')
    parser.add_argument('html_grid',
                        type=str,
                        help='HTML file to write the output to')
    args = parser.parse_args()

    input_grid = args.input_grid
    html_grid = args.html_grid
    lines = get_html(parse_table(input_grid))

    with open(html_grid, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def parse_table(input_grid):
    '''Given an input grid in TSV or CSV, get the data as a dictionary. Also
    set the headers for the HTML grid.
    '''
    global headers

    data = {}
    if '.tsv' in input_grid:
        delim = '\t'
    elif '.csv' in input_grid:
        delim = ','
    else:
        print("Invalid file extension: %s" % input_grid, file=sys.stderr)
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
    # bootstrap CSS
    lines.append('<link rel="stylesheet" href="{0}">'.format(bootstrap_css))
    lines.append('<style>')
    lines.append('.tooltip-inner {')
    lines.append('\tmax-width: 280px;')
    lines.append('}')
    lines.append('</style>')
    lines.append('<script src="{0}"></script>'.format(jquery))
    lines.append('<script src="{0}"></script>'.format(bootstrap_js))
    # opening tags
    lines.append('<div class="container">')
    lines.append('\t<div class="row" style="padding-top: 20px;">')
    lines.append('\t\t<table class="table table-bordered">')
    lines.append('\t\t\t<tr>')

    # special columns that link to reports
    c = -1
    report_col = -1
    uri_col = -1
    relations_col = -1
    for h in headers:
        c += 1
        if h == 'Report':
            report_col = c
        elif h == 'URIs':
            uri_col = c
        elif h == 'Relations':
            relations_col = c

        if h in principle_map:
            lines.append(
                '\t\t\t\t<td><b><a href="{0}" target="_blank">{1}</a></b></td>'.format(principle_map[h], h))
        else:
            lines.append('\t\t\t\t<td><b>{0}</b></td>'.format(h))
    lines.append('\t\t\t</tr>')

    for ont, fields in data.items():
        lines.append('\t\t\t<tr>')
        td_class = 'active'
        lines.append('\t\t\t\t<td class="{0}">{1}</td>'.format(td_class, ont))
        c = 0
        for field in fields:
            c += 1
            if '|' in field:
                f = field.split('|')[0].strip()
                msg = field.split('|')[1]
                if '. ' in msg:
                    msg = msg.replace('. ', '<br>')
                if '"' in msg:
                    msg = msg.replace('"', '\\"')
            else:
                f = field.strip()
                msg = None

            if f == 'PASS':
                td_class = 'success'
                icon = '<img src="assets/svg/check.svg" height="15px">'

            elif f == 'info' or f == 'INFO' or f == 'inactive':
                td_class = 'info'
                if msg:
                    icon = '<img src="assets/svg/info.svg"\
 height="15px"\
 data-toggle="tooltip"\
 data-html="true"\
 data-placement="right"\
 title="{0}">'.format(msg)
                else:
                    icon = '<img src="assets/svg/info.svg" height="15px">'

            elif f == 'warning' or f == 'WARN':
                td_class = 'warning'
                if msg:
                    icon = '<img src="assets/svg/warning.svg"\
 height="15px"\
 data-toggle="tooltip"\
 data-html="true"\
 data-placement="right"\
 title="{0}">'.format(msg)
                else:
                    icon = '<img src="assets/svg/warning.svg" height="15px">'

            elif f == 'error' or f == 'FAIL' or f == 'ERROR':
                td_class = 'danger'
                if msg:
                    icon = '<img src="assets/svg/x.svg"\
 height="15px"\
 data-toggle="tooltip"\
 data-html="true"\
 data-placement="right"\
 title="{0}">'.format(msg)
                else:
                    icon = '<img src="assets/svg/x.svg" height="15px">'

            else:
                td_class = 'active'
                icon = None

            if c == report_col and msg != 'report failed':
                lines.append('\t\t\t\t<td class="{1}" style="text-align:center">\
<a href="reports/robot/{0}.tsv">{2}</a></td>'.format(ont, td_class, icon))
            elif c == uri_col and f != 'PASS':
                lines.append('\t\t\t\t<td class="{1}" style="text-align:center">\
<a href="reports/principles/fp3-{0}.tsv">{2}</a></td>'.format(ont, td_class, icon))
            elif c == relations_col and f != 'PASS':
                lines.append('\t\t\t\t<td class="{1}" style="text-align:center">\
<a href="reports/principles/fp7-{0}.tsv">{2}</a></td>'.format(ont, td_class, icon))
            else:
                if icon:
                    lines.append(
                        '\t\t\t\t<td class="{0}" style="text-align:center">{1}</td>'.format(td_class, icon))
                else:
                    lines.append(
                        '\t\t\t\t<td class="{0}" style="text-align:center">{1}</td>'.format(td_class, f))

        lines.append('\t\t\t</tr>')

    # closing tags
    lines.append('\t\t</table>')
    lines.append('\t</div>')
    lines.append('</div>')
    lines.append('<script>')
    lines.append('\t$(function () {')
    lines.append('\t\t$(\'[data-toggle="tooltip"]\').tooltip()')
    lines.append('\t});')
    lines.append('</script>')
    return lines


if __name__ == '__main__':
    main(sys.argv)
