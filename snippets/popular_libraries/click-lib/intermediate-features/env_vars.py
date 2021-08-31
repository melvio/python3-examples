#!/usr/bin/env python3
import click


@click.command()
@click.argument("home", envvar="HOME")
def print_cli(home):
    click.echo(f"home={home}")


if __name__ == "__main__":
    print_cli()

# ./env_vars.py hi
# home=hi

# $ ./env_vars.py
# home=/home/m
