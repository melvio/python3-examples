#!/usr/bin/env python3
import datetime

import click

import datetime
from typing import Optional, Sequence, Any


class EnhancedDate(click.DateTime):
    name = "enhanceddate"

    def __init__(self, formats: Optional[Sequence[str]] = None):
        super().__init__(formats)
        self.formats += ["today", "tomorrow"]  # works out well here

    def convert(self, value: Any, param: Optional["Parameter"], ctx: Optional["Context"]) -> Any:
        if value == "today":
            return datetime.date.today()
        if value == "tomorrow":
            return datetime.date.today() + datetime.timedelta(days=1)

        return super().convert(value, param, ctx)


@click.command()
@click.option("--param", type=EnhancedDate())
def cli(param):
    click.echo(param)
    click.echo(type(param))

cli()
