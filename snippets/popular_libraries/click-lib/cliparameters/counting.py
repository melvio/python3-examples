#!/usr/bin/env python3
import click


@click.command()
@click.option("--count", default=1)
@click.option("--name")
def hello_cli(count, name):
    for _ in range(count):
        click.echo(f"Hello {name}!")


if __name__ == "__main__":
    hello_cli()
# $ ./counting.py
# Hello None!
# $ ./counting.py --name="melvin"
# Hello melvin!
#$ ./counting.py --count=2 --name="melvin"
# Hello melvin!
# Hello melvin!
