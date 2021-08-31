#!/usr/bin/env python3
import os
import click


@click.group()
def cli():
    pass


def host_function():
    print("inside host_function")
    return os.environ.get("HOSTNAME")


@cli.command()
@click.option("--hostname", default=host_function)
def host(hostname):
    print(hostname)


def host_function2(x):
    print(f"inside host_function2 arg={x}")
    print(os.environ.get("HOSTNAME"))
    return os.environ.get("HOSTNAME")


# * default (Optional[Union[Any, Callable[[], Any]]])
# +  This can also be a callable, in which case it's invoked when the default is needed without any arguments.
#    - so this is not really valid way of working with option's default bc it requires 1 arg here
@cli.command()
@click.option("--hostname", default=lambda x: host_function2(x))
def host2(hostname):
    print(hostname)


if __name__ == '__main__':
    cli()
