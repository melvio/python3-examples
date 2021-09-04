#!/usr/bin/env python3

import click


@click.option("-s", default=1)  # type is is INT
@click.option("-p")  # type is assumed to be STRING
@click.option("-f", type=click.STRING)  # type is always string
@click.option("-x", type=click.STRING, default=2)  # type is always string
@click.command()
def opt_example(s, p, f, x):
    print(type(s))
    print(type(p))
    print(type(f))
    print(type(x))


opt_example()
