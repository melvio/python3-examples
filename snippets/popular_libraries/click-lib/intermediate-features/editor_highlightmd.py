#!/usr/bin/env python3

import click


@click.command()
def cli():
    example_md = "# this is a header\n* **some boldface item** "
    click.edit(text=example_md, extension=".md")


if __name__ == '__main__':
    cli()
