#!/usr/bin/env python3
import click
from pathlib import Path

@click.command()
def cli():
    click.edit(filename=Path.home() / ".bashrc")


if __name__ == '__main__':
    cli()
