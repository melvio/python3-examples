#!/usr/bin/env python3
import click


@click.command()
@click.argument('postfixes', nargs=-1)  # narg=number of args
@click.argument('base', nargs=1)
def append_cli(postfixes, base):
    print(*[base + postfix for postfix in postfixes])


if __name__ == "__main__":
    append_cli()
# $ ./click_with_variable_args.py .txt README
#   README.txt

# $ ./click_with_variable_args.py .txt .md .rst README
#   README.txt README.md README.rst

# $ ./click_with_variable_args.py .{txt,md,rst} README
#   README.txt README.md README.rst


# $ ./click_with_variable_args.py .txt
#

# $ ./click_with_variable_args
# Usage: click_with_variable_args.py [OPTIONS] [POSTFIXES]... BASE
# Try 'click_with_variable_args.py --help' for help.
#
# Error: Missing argument 'BASE'.
