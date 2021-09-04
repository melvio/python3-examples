#!/usr/bin/env python3
import json
import click


@click.group()
@click.argument("document", type=click.Path(file_okay=True, exists=True))
@click.pass_context
def cli(ctx, document):
    with open(document) as file:
        contents: dict = json.load(file)
    ctx.obj = contents


@cli.command("check_context_object")
@click.pass_context
def check_context(ctx):
    click.echo(type(ctx.obj))


pass_dict = click.make_pass_decorator(dict)


@cli.command()
@pass_dict
def get_keys(dict_passed: dict):
    keys = list(dict_passed.keys())
    click.secho("The keys in our dictionary are ", fg="green", nl=False)
    click.echo(click.style(keys, fg="blue"))


@cli.command()
@click.argument("key")
@click.pass_context
def get_key(ctx, key):
    click.echo(ctx.obj[key])


def main():
    cli()


# ./main.py ./hopla.json check_context_object
# ./main.py  ./hopla.json get-keys
# ./main.py  ./hopla.json get-key quest.progress.hp

if __name__ == '__main__':
    main()
