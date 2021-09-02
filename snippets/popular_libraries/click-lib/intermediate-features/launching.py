#!/usr/bin/env python3

import click


@click.group()
def grp():
    pass


@grp.command()
@click.argument("url", default="https://click.palletsprojects.com/")
def launch(url):
    click.launch(url)


# open file explorer app
@grp.command()
@click.argument("file", default="/etc/")
def openfilemanager(file):
    click.launch(file, locate=True)


@grp.command()
@click.argument("file", default="/etc/hosts")
def openfile(file):
    click.launch(file)


@grp.command()
@click.argument("img", default="/home/m/Documents/xdg/pictures/sample-images/urothelium.png" )
def openimg(img):
    click.launch(img)


if __name__ == '__main__':
    grp()
