#!/usr/bin/env python3
import click
import os


# tutorial available at:
# <https://click.palletsprojects.com/en/8.0.x/complex/#building-a-git-clone>


class Repo:
    def __init__(self, home=None, debug=False):
        self.home = os.path.abspath(home or '.')
        self.debug = debug

    def __str__(self):
        return f"Repo(home={self.home}, debug={self.debug})"


# top level logic
@click.group()
@click.option("--repo-home", envvar="REPO_HOME", default=".repo")
@click.option("--debug/--no-debug", default=False, envvar="REPO_DEBUG")
@click.pass_context
def cli(ctx, repo_home, debug):
    print("in cli")
    ctx.obj = Repo(repo_home, debug)
    print(f"ctx.obj={ctx.obj}", repo_home, debug)


pass_repo = click.make_pass_decorator(Repo, ensure=True)


# git clone {src} [dst]
@cli.command()
@click.argument("src")
@click.argument("dest", required=False)
@pass_repo  # This @ will inject the ctx.obj to us as 'repo'
def clone(repo, src, dest):
    print("clone")
    print(repo, src, dest)


@click.command()
@pass_repo
def cp(repo):
    print(repo)
    click.echo(isinstance(repo, Repo))

cli()