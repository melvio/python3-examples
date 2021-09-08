#!/usr/bin/env python3
import click


@click.group()
@click.option("--debug/--nodebug", help="Toggle for verbose logging output")
@click.pass_context
def how_to_access_parent(ctx, debug):
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug


@how_to_access_parent.command()
@click.option("--childopt", type=click.INT, help="something")
@click.pass_context
def childcmd(ctx: click.Context, childopt):
    parent_cmd: click.Command = ctx.parent.command
    for param in parent_cmd.params:
        click.echo(param.get_help_record(ctx))
        # ('--debug / --nodebug', 'Toggle for verbose logging output')


how_to_access_parent(obj={})
