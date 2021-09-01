#!/usr/bin/env python3
import click, os


@click.group()
def cli():
    """group cmd"""


@cli.command()
@click.option("--username", "-u", prompt=True, show_default="$USER",
              default=lambda: os.environ.get("USER", "BASH_VERSION"))
def user(username):
    click.echo("hi " f"{username}")


if __name__ == '__main__':
    cli()
