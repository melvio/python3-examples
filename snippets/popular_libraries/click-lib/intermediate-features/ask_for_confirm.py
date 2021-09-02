#!/usr/bin/env python3

import sys
import click

# fake generated private key
PRIV_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIBOgIBAAJBAKEk9NQ9jg3mTsFN7G8Gy3wdEp23NNrznPrKp0zfspXE8P0WbaAy
92hOuUbPFvbYj5zX5cEDZv7bbe7tMd/zDl0CAwEAAQJABBvUHkE/iP0xTt50w9Px
hkWbfuf38gk6HG7kWyJtBEKJ3slIBPcB/0AD1PesindsibWbaoAHYO4smdzAPxXC
xQIhANbVBqrdYyOi2vN1Imku+HTkZPPjbx7jVZcVgfomjv+3AiEAwAYuRxbqVkJ2
hI7NFGeEVf023tokAN/+8LwadrcXeosCIEKvV2V8WQS7zYkax/asbNUj/C40X87P
tEa0l2cFxwebAiEAkUyb++LVEsxbzdYYTBZARqjBukMp9xeHWzWaeLX2KB0CIFtk
AHJ6MxmaMcR/vZdr+Ez6KbeaHWCbFEEdifjm/yh6
-----END RSA PRIVATE KEY-----"""


def exit_if_false(ctx, param, value):
    if value is False:
        sys.exit("sys.exit")


@click.group()
def cli():
    pass


PROMPT = "are you sure you want to expose your private keys?"


@cli.command()
@click.option("--uhm", is_flag=True, prompt=PROMPT,
              callback=exit_if_false, expose_value=False)
def expose_manual():
    click.echo(f"Exposed: {PRIV_KEY}")


@cli.command()
@click.confirmation_option(prompt=PROMPT)
def expose_builtin():
    click.echo(f"Exposed: {PRIV_KEY}")


if __name__ == '__main__':
    cli()
