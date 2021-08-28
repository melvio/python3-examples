#!/usr/bin/env python3

import click


@click.command()
@click.option("--editor")
def cli(editor):
    comment = "# Every line below this comment represents an item on your checklist\n"
    message = click.edit(text=comment)
    if message is not None:
        checklist_str = message.split(comment, maxsplit=1)[1]
        checklist_list = checklist_str.split("\n")

        click.echo(checklist_list)


if __name__ == "__main__":
    cli()
