#!/usr/bin/env python3
import click


@click.command()
@click.option("--value1", type=int, prompt=True)
@click.option("--value2", type=int)
@click.option("--value3", type=int, prompt="Please type in value 3:")
@click.option("--value4", type=click.Choice(["42", "69"]),
              prompt="please type in the correct number")
def multiply(value1, value2, value3, value4):
    if value2 is None:
        value2 = click.prompt("Please type in value 2")

    click.echo(f"value1 * value2 * value 3 = {value1 * value2 * value3}")
    click.echo(f"value4 {value4}")


if __name__ == "__main__":
    multiply()
