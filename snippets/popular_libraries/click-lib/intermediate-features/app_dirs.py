#!/usr/bin/env python3
import click

app_name = "myappname"
config_file_name = "myconf.ini"
app_dir_name = click.get_app_dir(app_name)

click.echo(app_dir_name)



# ./app_dirs.py
# /home/melv/.config/myappname

# XDG_CONFIG_HOME=/home/melv/ ./app_dirs.py
# /home/melv/myappname
