#!/usr/bin/env python3
import click


@click.command()
@click.argument("user_name", default="World")
def say_hello(user_name: str):
    click.echo(f"Hello, {user_name}!")


say_hello()