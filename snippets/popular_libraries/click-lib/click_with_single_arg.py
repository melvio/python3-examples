#!/usr/bin/env python3

# <https://click.palletsprojects.com/en/8.0.x/arguments/>
import click


@click.command()
@click.argument('filename')
def create(filename):
    click.echo(filename)


create()
# ./click_with_args.py hi.txt
# hi.txt

# ./click_with_args.py
# Usage: click_with_args.py [OPTIONS] FILENAME
# Try 'click_with_args.py --help' for help.
#
# Error: Missing argument 'FILENAME'.
