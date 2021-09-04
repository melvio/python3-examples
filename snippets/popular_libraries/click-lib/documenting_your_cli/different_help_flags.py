#!/usr/bin/env python3


import click


@click.group(context_settings=dict(help_option_names=['-h', '--help', "--huwh"]))
def group_cmd():
    pass


@group_cmd.command(name="other_name",
                   short_help="my short help")  # change the one line description
def my_cmd():
    click.echo("hi")


print(my_cmd.short_help)  # my_short help
print(my_cmd.name)  # other_name

group_cmd()
# ./different_help_flags.py --huwh
# Usage: different_help_flags.py [OPTIONS] COMMAND [ARGS]...

# Options:
# -h, --help, --huwh  Show this message and exit.

# Commands:
#   other_name  my short help
