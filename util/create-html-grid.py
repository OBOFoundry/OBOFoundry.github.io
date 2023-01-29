#!/usr/bin/env python3

import csv
import sys
from argparse import ArgumentParser

bootstrap_css = (
    "https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"
)

headers = []


def main(args):
    parser = ArgumentParser(description="Generate an HTML output of the metadata grid")
    parser.add_argument(
        "input_grid", type=str, help="File containing the grid (CSV, TSV, or TXT)"
    )
    parser.add_argument("html_grid", type=str, help="HTML file to write the output to")
    args = parser.parse_args()

    input_grid = args.input_grid
    html_grid = args.html_grid
    lines = get_html(parse_table(input_grid))

    with open(html_grid, "w") as f:
        for line in lines:
            f.write(line + "\n")


def parse_table(input_grid):
    """Given an input grid in TSV or CSV, get the data as a dictionary. Also
    set the headers for the HTML grid.
    """
    global headers

    data = {}
    if ".tsv" in input_grid:
        delim = "\t"
    elif ".csv" in input_grid:
        delim = ","
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
    """Given the data from the grid, return an array of lines to generate an
    HTML table."""
    global headers

    lines = []
    # bootstrap CSS
    lines.append('<link rel="stylesheet" href="{0}">'.format(bootstrap_css))
    lines.append(
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css">'
    )
    # opening tags
    lines.append('<div class="container">')
    lines.append('\t<div class="row" style="padding-top: 20px;">')
    lines.append('\t\t<table class="table table-bordered">')
    lines.append("\t\t\t<tr>")

    # special columns that link to reports
    c = -1
    for h in headers:
        c += 1
        lines.append("\t\t\t\t<td><b>{0}</b></td>".format(h))
    lines.append("\t\t\t</tr>")

    for ont, fields in data.items():
        lines.append("\t\t\t<tr>")
        td_class = "active"
        lines.append('\t\t\t\t<td class="{0}">{1}</td>'.format(td_class, ont))
        c = 0
        for field in fields:
            c += 1
            if "|" in field:
                f = field.split("|")[0].strip()
                msg = field.split("|")[1]
                if ". " in msg:
                    msg = msg.replace(". ", "<br>")
                if '"' in msg:
                    msg = msg.replace('"', '\\"')
            else:
                f = field.strip()
                msg = None

            if f.lower() == "pass":
                td_class = "success"
                icon = '<i class="bi-check-circle" aria-hidden="true"></i>'

            elif f.lower() == "info":
                td_class = "info"
                icon = '<i class="bi-info-circle" aria-hidden="true"></i>'

            elif f.lower() == "warning" or f.lower() == "warn":
                td_class = "warning"
                icon = '<i class="bi bi-exclamation-circle"></i>'

            elif f.lower() == "error" or f.lower() == "fail":
                td_class = "danger"
                icon = '<i class="bi-x-circle" aria-hidden="true"></i>'

            else:
                td_class = "active"
                icon = None

            if icon:
                lines.append(
                    '\t\t\t\t<td class="{0}" style="text-align:center">{1}</td>'.format(
                        td_class, icon
                    )
                )
            else:
                lines.append(
                    '\t\t\t\t<td class="{0}" style="text-align:center">{1}</td>'.format(
                        td_class, f
                    )
                )

        lines.append("\t\t\t</tr>")

    # closing tags
    lines.append("\t\t</table>")
    lines.append("\t</div>")
    lines.append("</div>")
    return lines


if __name__ == "__main__":
    main(sys.argv)
