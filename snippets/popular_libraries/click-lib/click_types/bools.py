#!/usr/bin/env python3
import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("--bool1", type=bool, required=True)
@click.option("--bool2", type=click.BOOL, required=True)
@click.option("--bool3", type=click.BOOL, required=True)
def boolios(bool1, bool2, bool3):
    click.echo(f"--bool1={bool1}, --bool2={bool2}, --bool3={bool3}")
# ./bools.py boolios --bool1 yes --bool2 true --bool3 0
# --bool1=True, --bool2=True, --bool3=False


if __name__ == '__main__':
    cli()
