#!/usr/bin/env python3
import click
from click.testing import CliRunner


@click.group()
def cmd():
    pass


@cmd.command()
def ask_abort() -> str:
    # abort will exit directly
    user_confirmed = click.confirm("Please confirm.", abort=True)
    click.echo(f"{user_confirmed=}")
    return "not aborted"


@cmd.command()
def ask_confirmation() -> str:
    user_confirmed = click.confirm("Please confirm.", abort=True)
    click.echo(f"{user_confirmed=}")
    return "hi"


@cmd.command()
def suite():
    test_ask_abort_no()
    test_ask_abort_yes()


def test_ask_abort_no():
    runner = CliRunner()
    result = runner.invoke(ask_abort, input="No")

    assert result.return_value is None
    assert result.exit_code == 1
    assert "Please confirm." in result.stdout


def test_ask_abort_yes():
    runner = CliRunner()
    result = runner.invoke(ask_abort, input="No")

    assert result.return_value is None
    assert result.exit_code == 1
    assert result.stdout == "Please confirm. [y/N]: No\nAborted!\n"


if __name__ == '__main__':
    cmd()
    # suite()
