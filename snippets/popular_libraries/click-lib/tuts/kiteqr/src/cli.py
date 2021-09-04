#!/usr/bin/env python3
import numpy as np
import pyqrcode as qr
import click

from subcmds import wifiqr, qr2array


@click.group()
@click.option("--ssid", help="wifi network identifier")
@click.option("--security", type=click.Choice(["WEP", "WPA", ""]))
@click.option("--password", help="wifi password")
@click.pass_context
def cli(ctx, ssid: str, security: str = "", password: str = ""):
    qrcode: qr.QRCode = wifiqr(ssid=ssid, security=security, password=password)
    ctx.obj["qrcode"] = qrcode


@cli.command()
@click.pass_context
def terminal(ctx):
    click.echo(ctx.obj["qrcode"].terminal())


@cli.command()
@click.option("--filename", help="path to png file")
@click.pass_context
def png(ctx, filename, scale: int = 10):
    ctx.obj["qrcode"].png(filename, scale)


def start():
    cli(obj={})


if __name__ == '__main__':
    start()
# ./cli.py terminal
# ./cli.py --ssid 3 --password pwd --security WEP png --filename ./here.png
