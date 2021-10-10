#!/usr/bin/env python3
import click


@click.command()
@click.option('--logs', type=click.Choice(['all', 'errors', 'no-errors', 'archive',
                                           'archive-with-errors']))
@click.option('--process', type=click.Choice(['all', 'fix', 'spool', 'status', 'import']))
@click.option('--quiet', is_flag=True)
@click.option('--check', is_flag=True)
@click.option('--scan', nargs=1)
def main(logs, process, quiet, check, scan):
    pass


if __name__ == "__main__":
    main()
