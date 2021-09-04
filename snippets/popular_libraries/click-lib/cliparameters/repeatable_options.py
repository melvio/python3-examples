#!/usr/bin/env python3
from typing import List, Tuple

import click


@click.command()
@click.option("--header", "header_list", multiple=True, type=(str, str))
@click.argument("repeatable", nargs=-1)
def cli(header_list: List[Tuple[str, str]], repeatable: List[str]):
    for header in header_list:
        click.echo(header)

    click.echo(repeatable)


if __name__ == '__main__':
    cli()
# ./repeatable_options.py --header Accept-Language en-Us --header Connection Keep-Alive
# ('Accept-Language', 'en-Us')
# ('Connection', 'Keep-Alive')

# ./repeatable_options.py --header Accept-Language en-Us --header Connection Keep-Alive "value 1" "value 2" value3
# ('Accept-Language', 'en-Us')
# ('Connection', 'Keep-Alive')
# ('value 1', 'value 2', 'value3')

