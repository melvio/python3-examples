#!/usr/bin/env python3
import os

import click


def print_version(context: click.Context, parameter: click.Option, value):
    if not value or context.resilient_parsing:
        return

    click.echo(f"VERSION: {parameter.flag_value}, {value}")
    context.exit()


@click.group()
def cli():
    """some cli"""


@cli.command()
@click.option("--value", is_flag=True, callback=print_version, expose_value=True, is_eager=True)
def hello(value):
    click.echo("Hello, World!")


if __name__ == '__main__':
    cli()
