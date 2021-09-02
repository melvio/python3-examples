#!/usr/bin/env python3
import click

PREFIX = "myapp"

context_settings = dict(help_option_names=['-h', '--help', "--huwh"],
                        auto_envvar_prefix=PREFIX)


@click.command(context_settings=context_settings)
@click.option("--auth-file", type=click.File())
def showfile(auth_file):
    click.echo(f"Auth file is over here: {auth_file}")


showfile()
# ./moreenv_vars.py --auth-file=/etc/passwd
# Auth file is over here: <_io.TextIOWrapper name='/etc/passwd' mode='r' encoding='UTF-8'>

# MYAPP_AUTH_FILE="${HOME}/auth.txt" ./moreenv_vars.py
# Auth file is over here: <_io.TextIOWrapper name='/home/m/auth.txt' mode='r' encoding='UTF-8'>

