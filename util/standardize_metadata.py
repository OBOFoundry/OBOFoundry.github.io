# -*- coding: utf-8 -*-

"""This script sorts the ordering of the metadata in each ontology markdown file.

Run with: ``python standardize_metadata.py``.

Author: `Charles Tapley Hoyt <https://cthoyt.com>`_.
"""

import pathlib
from io import StringIO

import yaml
from yaml import MappingNode, SafeDumper, ScalarNode

HERE = pathlib.Path(__file__).parent.resolve()
ONTOLOGY_DIRECTORY = HERE.parent.joinpath("ontology").resolve()


def sort_key(kv):
    k, v = kv
    if k == "layout":
        return 1, k
    elif k == "id":
        return 2, k
    elif k == "title":
        return 3, k
    elif k == "activity_status":
        return 5, k
    else:
        return 4, k


class ModifiedDumper(SafeDumper):
    def represent_mapping(self, tag, mapping, flow_style=None):
        value = []
        node = MappingNode(tag, value, flow_style=flow_style)
        if self.alias_key is not None:
            self.represented_objects[self.alias_key] = node
        best_style = True
        if hasattr(mapping, "items"):
            mapping = list(mapping.items())
            if self.sort_keys:
                try:
                    # all code is directly from the base class except this sorted
                    mapping = sorted(mapping, key=sort_key)
                except TypeError:
                    pass
        for item_key, item_value in mapping:
            node_key = self.represent_data(item_key)
            node_value = self.represent_data(item_value)
            if not (isinstance(node_key, ScalarNode) and not node_key.style):
                best_style = False
            if not (isinstance(node_value, ScalarNode) and not node_value.style):
                best_style = False
            value.append((node_key, node_value))
        if flow_style is None:
            if self.default_flow_style is not None:
                node.flow_style = self.default_flow_style
            else:
                node.flow_style = best_style
        return node


def update_markdown(path: pathlib.Path) -> None:
    """Update the given markdown file."""
    with path.open() as file:
        lines = [line.rstrip("\n") for line in file]

    assert lines[0] == "---"
    idx = min(i for i, line in enumerate(lines[1:], start=1) if line == "---")

    # Load the data like it is YAML
    data = yaml.safe_load(StringIO("\n".join(lines[1:idx])))
    dumped = yaml.dump(
        data,
        Dumper=ModifiedDumper,
        sort_keys=True,
        explicit_end=False,
        width=float("inf"),
    ).rstrip()

    with path.open("w") as file:
        print("---", file=file)
        print(dumped, file=file)
        print("---", file=file)
        for line in lines[idx + 1:]:
            print(line, file=file)


def main():
    for path in ONTOLOGY_DIRECTORY.glob("*.md"):
        update_markdown(path)


if __name__ == "__main__":
    main()
