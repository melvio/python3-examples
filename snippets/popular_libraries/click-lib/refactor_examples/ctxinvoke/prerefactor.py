#!/usr/bin/env python3
import click


def get_funds(user): return 100  # assume the funds comes from some API
def get_price(item): return 50  # assume the price comes from some API


@click.group()
@click.pass_context
def our_cli(ctx: click.Context):
    ctx.obj = {"user": "Cindy"}  # Assume the cli knows the invoking user


@our_cli.command()
@click.argument("user")
def get_user_funds(user):
    funds = get_funds(user)
    click.echo(f"{funds=}")
    return funds


@our_cli.command()
@click.argument("item")
@click.pass_context
def buy_item(ctx: click.Context, item: str):
    funds = ctx.invoke(get_user_funds)
    if funds >= get_price(item):
        print(f"bought {item}")
    else:
        print("f{funds}")


if __name__ == "__main__":
    our_cli()
