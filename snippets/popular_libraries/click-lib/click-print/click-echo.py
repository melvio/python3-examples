#!/us/bin/env python3
import click





@click.command()
def cli():
    click.echo("hi there")
    click.echo("no newline to be seen over here", nl=False)
    click.echo("See!")
    click.echo("print to stderr", err=True)


cli()
# $ python3 ./click-echo.py
# hi there
# no newline to be seen over hereSee!
# print to stderr
