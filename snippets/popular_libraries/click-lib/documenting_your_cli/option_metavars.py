#!/usr/bin/env python3
from pathlib import Path

import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("--string", type=str, expose_value=False)
@click.option("--flag/--no-flag", type=click.BOOL, expose_value=False)
@click.option("--int", type=click.INT, expose_value=False)
@click.option("--float", type=click.FLOAT, expose_value=False)
@click.option("--tuple", type=click.Tuple([int, float, str, object, bool]), expose_value=False)
@click.option("--datetime", type=click.DateTime(formats=["%Y-%m-%d"]), expose_value=False)
@click.option("--file", type=click.File(), expose_value=False)
@click.option("--path-noargs", type=click.Path(), expose_value=False)
@click.option("--path-dir",
              type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
              expose_value=False)
@click.option("--choices", type=click.Choice(["one", "two", "three"]), default="one",
              show_default=True, expose_value=False)
@click.option("--choices2", type=click.Choice(["one", "two", "three"]), expose_value=False)
@click.option("--floatrange",
              type=click.FloatRange(min=-1.0, max=1.0, min_open=False, max_open=True),
              expose_value=False)
@click.option("--uuid", type=click.UUID, expose_value=False)
@click.option("--uuid", type=click.UUID, metavar="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
              expose_value=False)
def options():
    """options command"""
    pass
# Options:
# --string TEXT
# --flag / --no-flag
# --int INTEGER
# --float FLOAT
# --tuple <INTEGER FLOAT TEXT OBJECT BOOLEAN>...
# --datetime [%Y-%m-%d]
# --file FILENAME
# --path-noargs PATH
# --path-dir DIRECTORY
# --choices [one|two|three]       [default: one]
# --choices2 [one|two|three]
# --floatrange FLOAT RANGE        [-1.0<=x<1.0]
# --uuid UUID
# --uuid xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
# --help                          Show this message and exit.


@cli.command(options_metavar="<OPTS_HERE>...")
def changemetavar():
    """changed metavar"""
    pass
# Usage: option_metavars.py changemetavar <OPTS_HERE>...


if __name__ == '__main__':
    cli()
