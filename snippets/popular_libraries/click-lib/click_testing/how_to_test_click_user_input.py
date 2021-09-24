#!/usr/bin/env python3
import sys

import click
from click.testing import CliRunner, Result


@click.command()
def are_you_sure():
    user_confirmed: bool = click.confirm("Do you want to proceed?")
    if user_confirmed:
        print("You seem very sure about this!")
        sys.exit(0)
    else:
        print("Want to try again?")
        sys.exit(1)


def test_are_you_sure_user_confirmed():
    runner = CliRunner()
    result: Result = runner.invoke(are_you_sure, input="yes")

    assert result.exit_code == 0
    assert result.stdout.endswith("You seem very sure about this!\n")


def test_are_you_sure_user_declined():
    runner = CliRunner()
    result: Result = runner.invoke(are_you_sure, input="no")

    assert result.exit_code == 1
    assert result.stdout.endswith("Want to try again?\n")

if __name__ == "__main__":
    are_you_sure()