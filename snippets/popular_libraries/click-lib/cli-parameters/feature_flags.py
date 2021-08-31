#!/usr/bin/env python3
import click


@click.group()
def groupy():
    pass


@groupy.command()
@click.option("--high", "score", flag_value=2.0)
@click.option("--medium", "score", flag_value=1.0, default=True)
@click.option("--grokked")
@click.option("--low", "score", flag_value=0.5)
def score_cmd(score, grokked):
    click.echo(f"score={score}")
    click.echo(f"score={type(score)}")


@groupy.command()
@click.option("--hard", "difficulty", flag_value="hard")
@click.option("--medium", "difficulty", flag_value="medium")
@click.option("--easy", "difficulty", flag_value="easy")
def diff(difficulty):
    click.echo(f"difficulty={difficulty}")


if __name__ == '__main__':
    groupy()
