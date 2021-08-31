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


def my_string(ctx: click.Context, param: click.Parameter, mystring_exposed_value: str):
    click.echo(f"in my_string {mystring_exposed_value}")


def my_int(ctx: click.Context, param: click.Parameter, myint_exposed_value: int):
    click.echo(f"in my_int {myint_exposed_value}")


@cli.command()
@click.option("--string", "mystring", type=str, callback=my_string)
@click.option("--int", "myint", type=int, callback=my_int)
def cb(mystring, myint):
    pass
# $ ./self_version_impl.py cb --int 32 --string "hi there"
# in my_int 32
# in my_string hi there
# $ ./self_version_impl.py cb --string "hi there" --int 32
# in my_string hi there
# in my_int 32


if __name__ == '__main__':
    cli()
