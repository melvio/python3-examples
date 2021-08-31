#!/usr/bin/env python3
import click
from collections import namedtuple


@click.group()
@click.option("--debug/--no-debug", default=False)
@click.pass_context
def cli(context, debug):
    click.echo(f"Debug mode is {'on' if debug else 'off'}")

    click.echo(context.args)  # []
    click.echo(context.invoked_subcommand)  # child
    click.echo(context.command.name)  # cli

    TypeThing = namedtuple(typename="MyType", field_names=["car", "crypt", "specialism"])
    passed_thing = TypeThing(car="ford", crypt="colonic", specialism="GI")
    context.obj = passed_thing


@cli.command()
@click.pass_context
def child(context):
    click.echo(f"context.args={context.args}")  # []
    click.echo(context.command.name)  # child
    click.echo(context.obj)  # MyType(car='ford', crypt='colonic', specialism='GI')


if __name__ == '__main__':
    cli()
