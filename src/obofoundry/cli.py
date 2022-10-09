"""Command line interface for :mod:`obofoundry`.

Why does this file exist, and why not put this in ``__main__``? You might be tempted to import things from ``__main__``
later, but that will cause problems--the code will get executed twice:

- When you run ``python3 -m obofoundry`` python will execute``__main__.py`` as a script.
  That means there won't be any ``obofoundry.__main__`` in ``sys.modules``.
- When you import __main__ it will get executed again (as a module) because
  there's no ``obofoundry.__main__`` in ``sys.modules``.

.. seealso:: https://click.palletsprojects.com/en/8.0.x/setuptools/
"""

import click

from . import standardize_metadata, update_operations_metadata

__all__ = [
    "main",
]


@click.group()
def main():
    """CLI for the OBO Foundry."""


main.add_command(standardize_metadata.main)
main.add_command(update_operations_metadata.main)

if __name__ == "__main__":
    main()
