#!/usr/bin/env python3

import json
import re
import sys
from argparse import ArgumentParser

import jsonschema
import yaml

# Path to JSON schema file:
SCHEMA_FILE = "util/schema/registry_schema.json"

# The metadata grid to be generated:
metadata_grid = {}


#: These ontologies have invalid licenses, but they're grandfathered in
LEGACY_LICENSE_PREFIXES = {
    "gsso",
    "hp",
    "kisao",
    "mamo",
    "sbo",
    "scdo",
    "txpo",
}


def main():
    global metadata_grid
    parser = ArgumentParser(
        description="""
  Validate registry metadata in the given YAML file yaml_infile and produce two output files:
  1) violations_outfile: a CSV, TSV, or TXT file which contain all metadata violations, and
  2) grid_outfile: a CSV, TSV, or TXT file which will contain a custom sorted metadata grid"""
    )
    parser.add_argument(
        "yaml_infile", type=str, help="YAML file containing registry data"
    )
    parser.add_argument(
        "violations_outfile",
        type=str,
        help="Output file (CSV, TSV, or TXT) to contain metadata violations",
    )
    parser.add_argument(
        "grid_outfile",
        type=str,
        help="Output file (CSV, TSV, or TXT) to contain custom sorted metadata grid",
    )
    args = parser.parse_args()

    yaml_infile = args.yaml_infile
    violations_outfile = args.violations_outfile
    grid_outfile = args.grid_outfile

    # Load in the YAML and the JSON schemas that we will need:
    data = load_data(yaml_infile)
    schema = get_schema()

    results = {"error": [], "warn": [], "info": []}

    # Validate each object
    for item in data["ontologies"]:
        add = validate_metadata(item, schema)
        results = update_results(results, add)

    # save the metadata-grid with ALL results
    headers = []
    for s in schema["properties"]:
        if "level" in s:
            headers.append(s)
    save_grid(metadata_grid, headers, grid_outfile)

    # print and save the results that did not pass
    print_results(results)
    save_results(results, violations_outfile)
    if results["error"]:
        print(
            "Metadata validation failed with %d errors - see %s for details"
            % (len(results["error"]), violations_outfile)
        )
        sys.exit(1)
    else:
        print("Metadata validation passed - see %s for warnings" % violations_outfile)
        sys.exit(0)


def load_data(yaml_infile):
    """Given a YAML data file, load the data to validate."""
    with open(yaml_infile, "r") as stream:
        data = yaml.load(stream, Loader=yaml.SafeLoader)
    return data


def get_schema():
    """Return a schema from the master schema directory."""
    schema = None
    file = SCHEMA_FILE
    try:
        with open(file, "r") as s:
            schema = json.load(s)
    except Exception as e:
        print("Unable to load %s: %s" % (file, str(e)))
    return schema


def validate_metadata(item, schema):
    """Given an item and a schema, validate the item against the
    schema. Add the full results to the metadata_grid and return a map of
    errors, warnings, and infos for any active ontologies."""
    global metadata_grid

    ont_id = item["id"]
    # these lists will be displayed on the console:
    errors = []
    warnings = []
    infos = []
    # these results are put into the metadata grid:
    results = {}

    # determine how to sort this item in the grid:
    results["foundry"] = False  # True if item.get("in_foundry_order") == 1 else False
    results["obsolete"] = True if item.get("is_obsolete") is True else False
    # if there is no status, put them at the bottom with inactive:
    results["ontology_status"] = (
        item["activity_status"] if "activity_status" in item else "inactive"
    )

    has_error = False
    has_warn = False
    has_info = False
    try:
        jsonschema.validate(item, schema)
    except jsonschema.exceptions.ValidationError as ve:
        title = list(ve.absolute_schema_path)[
            0
        ]  # Find the named section within the schema
        if title == "required":
            field_names = re.findall(r"\'(.*?)\'", ve.message)  # Rather get which field
            if len(field_names) > 0:
                title = field_names[0]
        if title == "properties":
            title = list(ve.absolute_schema_path)[1]  # Get which field
        # Get the schema "level" for this field dynamically, if we can
        if title in list(ve.absolute_schema_path) or title in schema["properties"]:
            if title in list(ve.absolute_schema_path):
                title_index = list(ve.absolute_schema_path).index(title)
                path = list(ve.absolute_schema_path)[0 : (title_index + 1)]
            else:
                path = ["properties", title]
            abs_schema = schema
            level = None
            for schema_item in path:
                if schema_item in abs_schema:
                    if "level" in abs_schema[schema_item]:
                        level = abs_schema[schema_item]["level"]
                    abs_schema = abs_schema[schema_item]
            if level is None:
                raise ValueError
        else:
            raise ValueError

        # add to the results map
        results[title] = level

        # flag for errors, warnings, and infos
        # without adding results to the lists that are logged
        if level == "error":
            has_error = True
        elif level == "warning":
            has_warn = True
        elif level == "info":
            has_info = True

        # these cases will not cause test failure and will not be logged
        # the results are just added to the metadata grid:
        # - orphaned ontology on contact or license or repository check
        # - inactive ontology
        # - obsolete ontology
        # - ontology annotated with `validate: false`
        # - ontology in legacy license exception list
        if not (
            (
                item.get("activity_status") == "orphaned"
                and title in ["contact", "license", "repository"]
            )
            or (
                item.get("is_obsolete") is True
                or item.get("activity_status") == "inactive"
                or item.get("validate") is False
            )
            or (title == "license" and ont_id in LEGACY_LICENSE_PREFIXES)
        ):
            # get a message for displaying on terminal
            msg = ve.message
            if title in ["license"]:
                # license error message can show up in a few different ways
                search = re.search("'(.+?)' is not one of", msg)
                if search:
                    msg = "'%s' is not a recommended license" % search.group(1)
                else:
                    search = re.search("({'label'.+?'url'.+?}) is not valid", msg)
                    if search:
                        msg = format_license_msg(search.group(1))
                    else:
                        search = re.search("({'url'.+?'label'.+?}) is not valid", msg)
                        if search:
                            msg = format_license_msg(search.group(1))

            # format the message with the ontology ID
            msg = "%s %s: %s" % (ont_id.upper(), title, msg)

            # append to correct set of warnings
            if level == "error":
                errors.append(msg)
            elif level == "warning":
                # warnings are recommended fixes, not required
                if "required" in msg:
                    msg = msg.replace("required", "recommended")
                warnings.append(msg)
            elif level == "info":
                infos.append(msg)

    # add an overall validation status to the grid entry
    if has_error:
        results["validation_status"] = "FAIL"
    elif has_warn:
        results["validation_status"] = "WARN"
    elif has_info:
        results["validation_status"] = "INFO"
    else:
        results["validation_status"] = "PASS"
    metadata_grid[ont_id] = results

    return {"error": errors, "warn": warnings, "info": infos}


def format_license_msg(substr):
    """Format an exception message for a license issue."""
    # process to dict
    d = json.loads(substr.replace("'", '"'))
    url = d["url"]
    label = d["label"]
    return "'{0}' <{1}> is not a recommended license".format(label, url)


def update_results(results, add):
    """Given a map of results for all ontologies and a map of results to add,
    append the results to the lists in the map."""
    results["error"] = results["error"] + add["error"]
    results["warn"] = results["warn"] + add["warn"]
    results["info"] = results["info"] + add["info"]
    return results


def sort_grid(metadata_grid):
    """
    Given a metadata grid as a map, sort the grid based on:
    1. Foundry status
    2. Ontology activity status
    3. Validation status
    4. Alphabetical
    Return a sorted list of IDs.
    """
    foundry = {"PASS": [], "INFO": [], "WARN": [], "FAIL": []}
    active = {"PASS": [], "INFO": [], "WARN": [], "FAIL": []}
    orphaned = {"PASS": [], "INFO": [], "WARN": [], "FAIL": []}
    inactive = {"PASS": [], "INFO": [], "WARN": [], "FAIL": []}
    obsolete = {"PASS": [], "INFO": [], "WARN": [], "FAIL": []}

    for ont_id, results in metadata_grid.items():
        # get the info about the ontology to sort on
        ontology_status = results["ontology_status"]
        validation_status = results["validation_status"]

        # foundry ontologies are displayed first
        # they must be active
        if results["foundry"]:
            foundry[validation_status].append(ont_id)
            continue

        # obsolete ontologies are displayed last
        # they are always inactive
        # (inactive does not mean obsolete)
        if results["obsolete"]:
            obsolete[validation_status].append(ont_id)
            continue

        # finally, sort by: active, orphaned, inactive
        if ontology_status == "active":
            active[validation_status].append(ont_id)
        elif ontology_status == "orphaned":
            orphaned[validation_status].append(ont_id)
        elif ontology_status == "inactive":
            inactive[validation_status].append(ont_id)

    # concatenate everything to a sorted list:
    def sort_list(arr):
        arr.sort(key=str.lower)
        if not arr:
            return []
        return arr

    sort = []
    for ont_type in [foundry, active, orphaned, inactive, obsolete]:
        for v_status in ["PASS", "INFO", "WARN", "FAIL"]:
            sort = sort + sort_list(ont_type[v_status])

    return sort


def save_grid(metadata_grid, headers, grid_outfile):
    """Given a metadata grid of all results and a grid file to write to, create
    a sorted table of the full results."""
    if ".csv" in grid_outfile:
        separator = ","
    elif ".tsv" or ".txt" in grid_outfile:
        separator = "\t"
    else:
        print("Grid file must be CSV, TSV, or TXT", file=sys.stderr)
        return

    # Determine order of ontologies based on statuses
    sort_order = sort_grid(metadata_grid)

    # First three help to see overall details
    header = "Ontology{0}Activity Status{0}Validation Status".format(separator)
    # After that, we show the results of each check
    for h in headers:
        header += separator + h
    header += "\n"

    with open(grid_outfile, "w") as f:
        f.write(header)
        for ont_id in sort_order:
            results = metadata_grid[ont_id]
            s = "{1}{0}{2}{0}{3}".format(
                separator,
                ont_id,
                results["ontology_status"],
                results["validation_status"],
            )
            for h in headers:
                if h == "license":
                    # license has two checks
                    # so the license entry will be the more severe violation
                    all_res = [results["license"], results["license-lite"]]
                    if "error" in all_res:
                        s += separator + "error"
                    elif "warning" in all_res:
                        s += separator + "warning"
                    elif "info" in all_res:
                        s += separator + "info"
                    else:
                        s += separator + "pass"
                    continue
                s += separator + results[h]
            s += "\n"
            f.write(s)

    print("Full validation results written to %s" % grid_outfile)


def print_results(results):
    """Given a map of results, log results on the console."""
    for level, messages in results.items():
        for m in messages:
            print("%s\t%s" % (level.upper(), m))


def save_results(results, violations_outfile):
    """Given a map of results and an output file to write to, write each result
    on a line."""
    if ".csv" in violations_outfile:
        separator = ","
    elif ".tsv" or ".txt" in violations_outfile:
        separator = "\t"
    else:
        print("Output file must be CSV, TSV, or TXT", file=sys.stderr)
        return
    with open(violations_outfile, "w") as f:
        f.write("Level%sMessage\n" % separator)
        for level, messages in results.items():
            for m in messages:
                f.write("%s%s%s\n" % (level.upper(), separator, m))


if __name__ == "__main__":
    main()
