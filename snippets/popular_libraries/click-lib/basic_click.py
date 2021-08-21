#!/usr/bin/env python3
import click
import datetime


# ./basic_click.py
# Usage: basic_click.py [OPTIONS] COMMAND [ARGS]...
#
# Options:
#   --help  Show this message and exit.
#
# Commands:
#   now
#   today


# $ ./basic_click.py now
# 2021-08-21 11:33:57.357245

# :$ ./basic_click.py today
# 2021-08-21


@click.group()
def cli():
    pass


@cli.command()
def now():
    click.echo(datetime.datetime.now())


@cli.command()
def today():
    click.echo(datetime.date.today())


if __name__ == '__main__':
    cli()
