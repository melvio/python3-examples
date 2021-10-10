#!/usr/bin/env python3
import click


@click.group()
def main(): pass


@main.command()
@click.argument("logtype", type=click.Choice(['all', 'errors', 'no-errors', 'archive',
                                              'archive-with-errors']))
def logs(logtype): pass


@main.command()
@click.argument("process_category", type=click.Choice(['all', 'fix', 'spool', 'status', 'import']))
def process(process_category): pass


@main.command()
def check(): pass


@main.command()
@click.argument("arg")
def scan(arg): pass

if __name__ == "__main__":
    main()