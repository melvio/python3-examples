#!/usr/bin/env python3


import click


@click.command()
@click.option("-s", "--string-to-echo")
@click.option("-p", "--string-to-print", "printable")
@click.option("--SpecialCase")
@click.option("---dashtown")
def echo(string_to_echo, printable, specialcase, _dashtown):
    click.echo(string_to_echo)
    click.echo(printable)
    click.echo(specialcase)
    click.echo(_dashtown)


if __name__ == '__main__':
    echo()
